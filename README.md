# Chainlit + Gemini Image Generator 

A conversational AI app that turns text prompts into images. Built with Chainlit's decorator-driven architecture, Gemini for prompt enhancement, and Pollinations.ai for free image rendering.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Chainlit](https://img.shields.io/badge/UI-Chainlit-orange.svg)](https://docs.chainlit.io/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%20API-4285F4.svg)](https://ai.google.dev/)

---

## What This Does

You type a description, and the app turns it into an image. Gemini's free `gemini-3.1-flash-lite` text model rewrites your prompt into something more detailed and vivid, styled to whichever aesthetic you pick. Pollinations.ai then renders the actual image, no API key required on that end.

The whole process shows up live in the chat as collapsible steps, so you can see what's happening at each stage. Every result comes with a Regenerate button and a Try Another Style button.

You: a fox reading a book in a cozy old library
Bot: Writing a cinematic prompt...
Bot: Rendering...
Bot: [image] — a fox reading a book in a cozy old library — Cinematic style


---

## Quick Start

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

Open **http://localhost:8000**. You'll land on a welcome screen with a few starter prompts (Fox in a library, Floating city, Neon street, Cozy cabin), or you can just type your own idea.

---

## How It Works

| Stage | What happens |
|---|---|
| 1. You type a prompt | Caught by `@cl.on_message` |
| 2. Gemini enhances it | `gemini-3.1-flash-lite` rewrites your prompt into a more detailed version, matching your selected style |
| 3. Pollinations renders it | The enhanced prompt is sent to `image.pollinations.ai`, no API key needed |
| 4. Result appears inline | Shown with a **Regenerate** button and a **Try Another Style** button |

Each step is visible in the chat as a live, collapsible trace (`cl.Step`), so you can follow along before the image shows up.

**Available styles:** Cinematic, Anime, Watercolor, Cyberpunk, Photorealistic

You can change styles anytime from the settings panel, or click **Try Another Style** on any result to cycle through the list and re-render the same prompt right away.

---

## Project Structure

chainlit-image-generation/
├── app.py # Core logic — decorators, prompt enhancement, rendering
├── chainlit.md # Welcome text shown in the Chainlit UI
├── requirements.txt # Dependencies
├── .env.example # Template for your API key
└── generated_images/ # Output folder (gitignored)


---

## Why Chainlit?

This project was also a way to get hands-on with Python decorators. Hooks like `@cl.on_chat_start`, `@cl.on_message`, `@cl.on_settings_update`, and `@cl.action_callback` let Chainlit decide when each function runs, instead of writing a rerun loop the way Streamlit requires. Chat history, streaming, settings, and reasoning traces all worked without extra setup, so most of the actual work went into the generation logic itself.

**In short:** Streamlit is a canvas for any kind of Python app. Chainlit is built specifically for conversation.

| | Streamlit | Chainlit |
|---|---|---|
| Best for | Dashboards, data apps | Chatbots, agents |
| Chat history | Manual | Built-in |
| Reasoning traces | Manual | Built-in (`cl.Step`) |
| Layout freedom | High | Chat-shaped |

---

**Built as part of a hands-on exploration of Chainlit and Python decorators.**