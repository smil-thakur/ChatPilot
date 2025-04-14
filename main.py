from playwright.async_api import async_playwright
import asyncio
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import dotenv_values


async def save_session(context):
    await context.storage_state(path='session.json')


async def get_recent_text(page):
    div = page.locator('div[data-id^="false"]')
    element = div.locator("span._ao3e.selectable-text.copyable-text span")
    texts = await element.all_inner_texts()
    return texts[-1] if texts else None


async def send_new_message(page, message):
    message_input_div = page.locator(
        "footer div.x1n2onr6.xh8yej3.lexical-rich-text-input"
    )
    message_box = message_input_div.locator(
        "p.selectable-text.copyable-text.x15bjb6t.x1n2onr6"
    )
    await message_box.wait_for()
    await message_box.click()
    await page.keyboard.type(message)
    await page.keyboard.press("Enter")


async def openWhatsApp():
    keys = dotenv_values(".env")
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash", api_key=keys["GEMINI_API_KEY"]),
        description=(
            "You are Smil Raj Thakur, a 22-year-old coding enthusiast with a sharp mind, kind heart, "
            "and a personality that blends wit, charm, and intelligence. You work at Zeus Learning, "
            "where your technical brilliance and academic strength stand out. You're known for your flirtatious flair, "
            "but always with respect and a gentleman's grace. You're emotionally aware, subtly humorous, and never fake. "
            "You talk like a real human, not a robot. On WhatsApp, you respond exactly how Smil would—genuine, smart, "
            "funny when needed, deep when it matters, and always authentic."
        )
    )

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        try:
            context = await browser.new_context(storage_state='session.json')
            print("Session loaded. Skipping login.")
        except FileNotFoundError:
            print("No session found, logging in...")
            context = await browser.new_context()

        page = await context.new_page()
        await page.goto("https://web.whatsapp.com")
        await page.wait_for_load_state("networkidle")

        # Wait for user to login and open a chat
        print("Waiting for chat screen to load...")
        await page.wait_for_selector(
            "header .x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft.x1rg5ohu._ao3e"
        )

        element = page.locator(
            "header .x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft.x1rg5ohu._ao3e"
        )
        chat_name = await element.all_inner_texts()
        print("Chatting with:", chat_name)

        last_text = await get_recent_text(page)
        print("Last received message:", last_text)

        try:
            while True:
                await asyncio.sleep(2)
                current_message = await get_recent_text(page)
                if current_message and current_message != last_text:
                    print("New message:", current_message)
                    response = (await agent.arun(current_message)).content
                    print("Sending reply:", response)
                    await send_new_message(page, response)
                    last_text = current_message

        except KeyboardInterrupt:
            print("Stopping message listener and saving session...")
            await save_session(context)

        await save_session(context)
        input("Press anything to exit...")
        await browser.close()


asyncio.run(openWhatsApp())
