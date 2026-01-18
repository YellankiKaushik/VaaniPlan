# 🎙️ VaaniPlan — Voice-First AI Daily Planning Assistant

VaaniPlan is a **voice-first AI daily planning assistant** that converts natural spoken thoughts into a **clear, structured, time-based daily timetable**.

This project was developed as a **prototype submission** for the **Unleash LLM Innovation Challenge** under the **YuvAI Initiative**, demonstrating how **Large Language Models (LLMs)** can be used as a core intelligence layer to solve real-world productivity problems through natural voice interaction.

---

## 🔗 Prototype Links (Live)

- **Frontend (GitHub Pages):**  
  https://yellankikaushik.github.io/VaaniPlan/

- **Backend (FastAPI API):**  
  https://vaaniplan-backend.onrender.com/

> ⚠️ Note: This is a demo prototype. API usage is limited and intended for evaluation purposes only.

---

## 🚩 Problem Statement

Many people struggle to plan their day effectively due to the **friction of typing**, **manual structuring**, and **prioritizing tasks**, especially when they are already tired or cognitively overloaded.

Students, professionals, and lifelong learners often abandon planning tools not because they lack value — but because **using them feels like extra work**.

---

## 💡 Solution Overview

**VaaniPlan removes planning friction** by allowing users to simply **speak their day in natural language**.

An AI language model then:
- Understands the intent behind the speech
- Organizes tasks chronologically
- Generates a **structured daily timetable**

No prompt crafting.  
No manual formatting.  
Just **voice → structure**.

---

## 🧭 What is VaaniPlan?

VaaniPlan is a prototype **voice-first AI system** designed to:
- Capture daily plans through natural speech
- Use an LLM as a reasoning engine
- Output a concise, time-based schedule optimized for daily execution

It is built for **simplicity, speed, and minimal user effort**.

---

## ❓ Why VaaniPlan?

Most planning tools fail not due to poor features, but due to **high interaction cost**.

VaaniPlan stands out because it focuses on:
- Voice-first interaction
- Zero data storage
- No personal history tracking
- Structured outputs optimized for daily planning

It is about **reducing friction**, not replacing chatbots.

---

## 🧑‍💻 How to Use VaaniPlan

1. Click **Start Speaking**
2. Describe your day naturally in your own words
3. Review or edit the transcribed text if needed
4. Click **Generate Plan**
5. View your structured, time-based daily schedule

---

## ⚙️ How It Works (High-Level)

1. User speaks their daily plan
2. Browser captures audio and converts it to text
3. Text is sent to the backend API
4. An LLM processes the input
5. A structured daily timetable is returned and displayed

---

## 🧱 System Architecture

### Frontend
- HTML, CSS, JavaScript
- Browser-based Speech Recognition (Web Speech API)
- Hosted on **GitHub Pages**

### Backend
- FastAPI (Python)
- REST API for plan generation
- Hosted on **Render**

### AI Layer
- Large Language Model (LLM)
- Converts unstructured natural language into structured schedules

---

## 🧠 LLM Usage (Core Innovation)

**Role of the LLM:**
- Understands unstructured speech-derived text
- Infers intent, priorities, and ordering
- Converts human thought into a usable daily plan

> ⚠️ The LLM is **not optional** — it is the **core intelligence layer** of the system, not a cosmetic add-on.

---

## 🔁 Model-Agnostic Design

While this prototype is demonstrated using **OpenAI-based models**, the architecture is **model-agnostic** and can be adapted to:
- Open-source LLMs (e.g., LLaMA-based models, Mistral)
- Self-hosted inference setups

This aligns with the **open innovation goals** of the challenge.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **AI:** Large Language Models (LLMs)
- **Hosting:** GitHub Pages (Frontend), Render (Backend)

---

## 🧪 Prototype Status

- Working end-to-end prototype
- No authentication
- No database
- No user data storage
- Designed for demonstration and evaluation

---

## 🌱 Future Scope

- Replace API-based LLMs with fully open-source models
- Add multilingual voice input support
- Improve plan refinement and regeneration
- Extend use cases to education and workforce planning

---

## 👤 Team & Author

**Team Lead:**  
Kaushik Yellanki  

**Team ID:**  
TEAM-MJEEYWAO-01DCCB  

**Email:**  
kaushikyellanki@gmail.com  

---

## 🏁 Closing Note

VaaniPlan contributes to the **YuvAI mission** by making AI more accessible through **voice-first interaction** and demonstrating a **responsible, practical application of LLMs** for everyday productivity.

This project reflects how a simple human-centered idea can evolve into a complete, deployable AI prototype.
