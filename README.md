# 🎨 Chainlit + Gemini Image Generator

A conversational AI application that transforms text prompts into images using **Chainlit**, **Google Gemini**, and **Pollinations.ai**.

Built to explore Chainlit's decorator-driven architecture while creating a simple, interactive image generation experience.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Chainlit](https://img.shields.io/badge/UI-Chainlit-orange.svg)](https://docs.chainlit.io/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%20API-4285F4.svg)](https://ai.google.dev/)

---

## What This Does

Describe an image in natural language, and the application generates it for you.

Your prompt is first enhanced using Gemini's free `gemini-3.1-flash-lite` model, making it more detailed and visually descriptive while matching your selected artistic style. The enhanced prompt is then sent to Pollinations.ai, which renders the final image without requiring an API key.

The entire process is shown live in the chat using collapsible reasoning steps, so you can follow each stage before the image appears.

Every generated image also includes:

- **Regenerate** – create another version using the same prompt and style.
- **Try Another Style** – render the same prompt using the next available style.

### Example

```text
You:
A fox reading a book in a cozy old library

Assistant:
Writing a cinematic prompt...

Rendering image...

[Generated Image]
Style: Cinematic
```

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/s-zaid-13/chainlit-image-generation.git
cd chainlit-image-generation
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Paste your free Gemini API key into `.env`.

Get your API key from:

https://aistudio.google.com/apikey

### 5. Run the Application

```bash
chainlit run app.py -w
```

Open:

```
http://localhost:8000
```

You'll be greeted with a welcome screen containing a few starter prompts (Fox in a library, Floating city, Neon street, Cozy cabin), or you can simply enter your own prompt.

---

## How It Works

| Stage | Description |
|------|-------------|
| **1. User Prompt** | Your prompt is received by `@cl.on_message`. |
| **2. Prompt Enhancement** | Gemini (`gemini-3.1-flash-lite`) rewrites it into a richer, more descriptive prompt based on the selected style. |
| **3. Image Generation** | The enhanced prompt is sent to `image.pollinations.ai` for rendering. |
| **4. Result** | The generated image is displayed with **Regenerate** and **Try Another Style** actions. |

Each stage is displayed as a live, collapsible reasoning trace using `cl.Step`, making the generation process transparent.

**Available styles**

- Cinematic
- Anime
- Watercolor
- Cyberpunk
- Photorealistic

Styles can be changed at any time from the settings panel, or by clicking **Try Another Style** on a generated image.

---

## Project Structure

```text
chainlit-image-generation/
├── app.py                 # Core application logic
├── chainlit.md            # Welcome screen shown in Chainlit
├── requirements.txt       # Project dependencies
├── .env.example           # Environment variable template
└── generated_images/      # Generated images (gitignored)
```

---

## Why Chainlit?

This project was also an opportunity to explore **Python decorators** through Chainlit's event-driven architecture.

Decorators such as `@cl.on_chat_start`, `@cl.on_message`, `@cl.on_settings_update`, and `@cl.action_callback` allow Chainlit to automatically trigger different parts of the application in response to user interactions. Unlike Streamlit, there is no need to manage reruns or manually maintain chat state.

As a result, chat history, streaming responses, settings, and reasoning traces work out of the box, allowing the application logic to stay focused on prompt enhancement and image generation.

**In short:** Streamlit is a general-purpose framework for Python applications, while Chainlit is designed specifically for conversational AI experiences.

| | Streamlit | Chainlit |
|---|---|---|
| Best for | Dashboards, data apps | Chatbots, AI agents |
| Chat history | Manual | Built-in |
| Reasoning traces | Manual | Built-in (`cl.Step`) |
| Layout | Highly customizable | Chat-focused |

---

**Built as part of a hands-on exploration of Chainlit and Python decorators.**