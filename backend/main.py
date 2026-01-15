from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
import tempfile

# -------------------------
# Initialize FastAPI app
# -------------------------
app = FastAPI()

# -------------------------
# ENABLE CORS (FRONTEND ↔ BACKEND)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yellankikaushik.github.io",
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# OpenAI client (API key from env)
# -------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------
# Health check endpoint
# -------------------------
@app.get("/")
def root():
    return {"message": "VaaniPlan backend is running"}

# -------------------------
# Text → AI plan endpoint
# -------------------------
@app.get("/plan")
def generate_plan(text: str):
    prompt = f"""
You are a daily planning assistant.

Convert the following input into a structured daily timetable.

Rules:
- Use time ranges
- Order tasks chronologically
- Be concise
- Output ONLY the timetable

Input:
{text}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return {
        "input": text,
        "plan": response.output_text
    }

# -------------------------
# Voice → AI plan endpoint
# -------------------------
@app.post("/voice-plan")
async def voice_plan(audio: UploadFile = File(...)):
    # Save uploaded audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await audio.read())
        audio_path = tmp.name

    # Speech → Text (Whisper)
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )

    spoken_text = transcript.text

    # Text → Plan
    prompt = f"""
You are a daily planning assistant.

Convert the following input into a structured daily timetable.

Rules:
- Use time ranges
- Order tasks chronologically
- Output ONLY the timetable

Input:
{spoken_text}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return {
        "spoken_text": spoken_text,
        "plan": response.output_text
    }
