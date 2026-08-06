# Chainlit + Gemini Image Generator 🎨

> A conversational AI app that turns your words into images — built with Chainlit's decorator-driven architecture, Gemini for prompt enhancement, and Pollinations.ai for free image rendering.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Chainlit](https://img.shields.io/badge/UI-Chainlit-orange.svg)](https://docs.chainlit.io/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%20API-4285F4.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## ✨ What This Does

Type a description, watch it come to life. Gemini's free `gemini-3.1-flash-lite` text model rewrites your prompt into something richer and more vivid, styled to whichever aesthetic you pick — then **Pollinations.ai** (free, no API key required) renders the actual image. The whole pipeline is shown live in the chat as collapsible reasoning steps, with buttons to regenerate or cycle through styles without retyping anything.

You: a fox reading a book in a cozy old library
Bot: ⚙️ Writing a cinematic prompt...
Bot: ⚙️ Rendering...
Bot: [image] — a fox reading a book in a cozy old library — Cinematic style


---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/s-zaid-13/chainlit-image-generation.git
cd chainlit-image-generation

# 2. Set up your environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Add your free Gemini API key
cp .env.example .env
# → paste your key from https://aistudio.google.com/apikey

# 4. Launch
chainlit run app.py -w
```

Open **http://localhost:8000** — you'll land on a welcome screen with clickable starter prompts (Fox in a library, Floating city, Neon street, Cozy cabin), or just type your own idea.

---

## 🧠 How It Works

| Stage | What happens |
|---|---|
| **1. You type a prompt** | Caught by `@cl.on_message` |
| **2. Gemini enhances it** | `gemini-3.1-flash-lite` rewrites your prompt into a vivid, detailed version, leaning into your selected style |
| **3. Pollinations renders it** | The enhanced prompt is sent to `image.pollinations.ai` — no API key needed, fully free |
| **4. Result appears inline** | Shown with a **🔄 Regenerate** button and a **🎨 Try another style** button |

Every step is visible in the chat as a live, collapsible trace (`cl.Step`) — you can literally watch the app think before the image appears.

🎨 Art styles available: Cinematic · Anime · Watercolor · Cyberpunk · Photorealistic


Change styles anytime from the ⚙️ settings panel, or hit **🎨 Try another style** on any result to cycle through the list and re-render the same prompt instantly.

---

## 📂 Project Structure

chainlit-gemini-imagegen/
├── app.py # All the logic — decorators, prompt enhancement, rendering
├── chainlit.md # Welcome text shown in the Chainlit UI
├── requirements.txt # Dependencies
├── .env.example # Template for your API key
└── generated_images/ # Output folder (gitignored)


---

## 🎓 Why Chainlit?

This project doubled as a hands-on exploration of **Python decorators** — `@cl.on_chat_start`, `@cl.on_message`, `@cl.on_settings_update`, and `@cl.action_callback` let Chainlit manage *when* code runs, instead of hand-rolling a rerun loop the way Streamlit requires. Chat history, streaming, style settings, and reasoning traces came essentially for free, leaving the actual generation logic as the only real work.

**Streamlit vs Chainlit, in one line:**
> Streamlit is a canvas for any Python app. Chainlit is a stage built specifically for conversation.

| | Streamlit | Chainlit |
|---|---|---|
| Best for | Dashboards, data apps | Chatbots, agents |
| Chat history | Manual | Built-in |
| Reasoning traces | Manual | Built-in (`cl.Step`) |
| Layout freedom | High | Chat-shaped |

---


**Built as part of a hands-on exploration of Chainlit and Python decorators.** 