# 🎙️ VaaniPlan — Voice-First AI Daily Planning Assistant

VaaniPlan is a **voice-first AI daily planning assistant** that converts natural spoken thoughts into a clear, structured daily timetable.

This project is built as a **prototype submission for the Unleash LLM Innovation Challenge** under the **YuvAI Initiative**, demonstrating how Large Language Models (LLMs) can improve everyday productivity through natural voice interaction.

---

## 🔗 Live Demo

👉 **Frontend (GitHub Pages)**  
https://yellankikaushik.github.io/VaaniPlan/

👉 **Backend (FastAPI API)**  
https://vaaniplan-backend.onrender.com/

---

## 🚩 Problem Statement

Many people struggle to plan their day effectively due to the friction of typing, structuring tasks, and prioritizing activities.  
This problem is especially common among students, professionals, and learners managing dynamic daily schedules.

---

## 💡 Solution Overview

VaaniPlan removes planning friction by allowing users to simply **speak their day** in natural language.  
An AI language model understands the intent, organizes tasks chronologically, and generates a time-based daily plan.

---

## ⚙️ How It Works

1. User clicks **Start Speaking** and describes their day naturally
2. Browser captures voice and converts it to text
3. Text is sent to the backend API
4. An LLM processes the input and generates a structured timetable
5. The plan is displayed instantly to the user

---

## 🧱 System Architecture

**Frontend**
- HTML, CSS, JavaScript
- Browser-based Speech Recognition (Web Speech API)
- Hosted via GitHub Pages

**Backend**
- FastAPI (Python)
- REST API for plan generation
- Hosted on Render

**AI Layer**
- LLM processes natural language input
- Generates structured daily schedules

---

## 🧠 LLM Usage (Core Innovation)

- **Current Model:** OpenAI GPT-based model
- **Role of LLM:**  
  - Understands unstructured natural language  
  - Infers intent and priorities  
  - Converts speech-based input into a structured timetable  

> ⚠️ The LLM is **not optional** in this system — it is the core intelligence layer.

### Model-Agnostic Design
While demonstrated with OpenAI for prototyping, the architecture is **model-agnostic** and can be adapted to open-source LLMs such as LLaMA or Mistral to align with open innovation requirements.

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI (Python)
- AI: Large Language Models (LLMs)
- Hosting: GitHub Pages (Frontend), Render (Backend)

---

## 🧪 Prototype Status

- This is a **working prototype**
- No authentication or database
- Designed for demonstration and evaluation
- API usage is limited and intended for demo purposes

---

## 🚀 Future Scope

- Replace API-based LLM with fully open-source models
- Add multilingual voice support
- Improve plan customization and refinement
- Scale for educational and workforce planning use cases

---

## 👤 Author & Team

**Kaushik Yellanki**  
Team ID: TEAM-MJEEYWAO-01DCCB  
Email: kaushikyellanki@gmail.com

---

## 🏁 Closing Note

VaaniPlan contributes to the **YuvAI mission** by making AI more accessible through voice-first interaction and demonstrating responsible, practical use of LLMs for real-world productivity.
