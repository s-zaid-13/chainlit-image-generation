import os
import uuid
import asyncio
import urllib.parse

import httpx
from dotenv import load_dotenv
import chainlit as cl
from google import genai

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
TEXT_MODEL = "gemini-3.1-flash-lite"
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

STYLES = {
    "Cinematic": "cinematic lighting, dramatic composition, film grain, 35mm",
    "Anime": "anime style, vibrant colors, cel shading, studio ghibli inspired",
    "Watercolor": "soft watercolor painting, delicate brush strokes, pastel palette",
    "Cyberpunk": "neon-lit cyberpunk, high contrast, futuristic, rain-soaked streets",
    "Photorealistic": "photorealistic, sharp focus, natural lighting, 8k detail",
}


def get_client() -> genai.Client:
    if not GEMINI_API_KEY:
        raise RuntimeError("Missing GEMINI_API_KEY — add it to your .env file.")
    return genai.Client(api_key=GEMINI_API_KEY)


def enhance_prompt_sync(prompt: str, style: str) -> str:
    client = get_client()
    instruction = (
        f"Turn this into one vivid, detailed image-generation prompt. "
        f"Lean into this style: {STYLES.get(style, '')}. "
        f"Return only the prompt, nothing else.\n\n{prompt}"
    )
    response = client.models.generate_content(model=TEXT_MODEL, contents=instruction)
    return (response.text or "").strip() or prompt


async def render_image(prompt: str) -> str:
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}"
    params = {"width": 1024, "height": 1024, "nologo": "true"}

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.get(url, params=params)
        resp.raise_for_status()

    path = f"{OUTPUT_DIR}/{uuid.uuid4().hex}.png"
    with open(path, "wb") as f:
        f.write(resp.content)
    return path


@cl.set_starters
async def starters():
    return [
        cl.Starter(
            label="Fox in a library",
            message="a fox reading a book in a cozy old library",
        ),
        cl.Starter(
            label="Floating city", message="a floating city above the clouds at sunset"
        ),
        cl.Starter(
            label="Neon street", message="a rain-soaked neon-lit street at night"
        ),
        cl.Starter(
            label="Cozy cabin", message="a snow-covered cabin with warm window light"
        ),
    ]


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("style", "Cinematic")
    cl.user_session.set("last_prompt", None)

    await cl.ChatSettings(
        [
            cl.input_widget.Select(
                id="style",
                label="Art style",
                values=list(STYLES.keys()),
                initial_index=0,
            )
        ]
    ).send()

    await cl.Message(
        content=(
            "**Welcome to the Image Studio** 🎨\n\n"
            "Describe anything and I'll generate it — pick a style from the "
            "settings panel (⚙️) or just start typing."
        )
    ).send()


@cl.on_settings_update
async def on_settings_update(settings):
    cl.user_session.set("style", settings["style"])
    await cl.Message(content=f"Style set to **{settings['style']}** ✨").send()


@cl.on_message
async def on_message(message: cl.Message):
    prompt = message.content.strip()
    if not prompt:
        await cl.Message(
            content="Give me something to picture — a scene, a mood, a character."
        ).send()
        return

    cl.user_session.set("last_prompt", prompt)
    await _create_image(prompt)


@cl.action_callback("regenerate")
async def regenerate(action: cl.Action):
    prompt = action.payload.get("prompt") or cl.user_session.get("last_prompt")
    if prompt:
        await _create_image(prompt)


@cl.action_callback("change_style")
async def change_style(action: cl.Action):
    prompt = action.payload.get("prompt")
    styles = list(STYLES.keys())
    current = cl.user_session.get("style", styles[0])
    next_style = styles[(styles.index(current) + 1) % len(styles)]
    cl.user_session.set("style", next_style)
    await cl.Message(content=f"Switched to **{next_style}** — regenerating...").send()
    await _create_image(prompt)


async def _create_image(prompt: str):
    style = cl.user_session.get("style", "Cinematic")

    async with cl.Step(name=f"Writing a {style.lower()} prompt", type="tool") as step:
        step.input = prompt
        enhanced = await asyncio.to_thread(enhance_prompt_sync, prompt, style)
        step.output = enhanced

    async with cl.Step(name="Rendering", type="tool") as step:
        step.input = enhanced
        try:
            path = await render_image(enhanced)
        except Exception as exc:
            await cl.Message(content=f"⚠️ Rendering failed: {exc}").send()
            return
        step.output = "done"

    await cl.Message(
        content=f"**{prompt}** — *{style} style*",
        elements=[cl.Image(path=path, name="result", display="inline")],
        actions=[
            cl.Action(
                name="regenerate", payload={"prompt": prompt}, label="🔄 Regenerate"
            ),
            cl.Action(
                name="change_style",
                payload={"prompt": prompt},
                label="🎨 Try another style",
            ),
        ],
    ).send()
