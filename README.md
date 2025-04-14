# 🤖 ChatPilot — AI WhatsApp Auto Responder

ChatPilot is an AI-powered WhatsApp agent that reads your incoming messages and auto-replies like it's _you_. Whether you're busy coding or taking a break, ChatPilot ensures you're always present on WhatsApp — smart, witty, and charming.

---

## 🚀 Features

- 🔁 Automatically responds to WhatsApp messages in real time
- 🧠 Powered by Google Gemini via the `agno` library
- 💾 Session storage (no QR scan every time)
- 🧑‍🎤 Customizable personality for realistic human-like replies
- 🦾 Headless browser support using Playwright

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ChatPilot.git
cd ChatPilot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright Browsers

```bash
playwright install
```

### 4. Set Up Environment Variables

Create a `.env` file from the sample:

```bash
cp .env.sample .env
```

Then, open `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 📄 Sample `.env.sample`

```env
# Copy this to .env and replace with your actual API key
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 📦 requirements.txt

This project uses the following Python packages:

```txt
playwright
python-dotenv
agno
```

---

## ▶️ Run the Bot

```bash
python main.py
```

- On first run, scan the QR code on WhatsApp Web.
- The bot will monitor the most recent chat and reply accordingly.

---

## 🤖 Agent Personality

The AI agent is described as:

> “You are Smil Raj Thakur, 22 years old, into coding, witty, flirt king, gentleman, good in academics. You work at Zeus Learning and respond like yourself on WhatsApp.”

Customize the behavior in your script:

```python
agent = Agent(
    model=Gemini(id="gemini-2.0-flash", api_key=keys["GEMINI_API_KEY"]),
    description="Your custom behavior description here..."
)
```

---

## 🧠 How It Works

1. Logs into WhatsApp Web using Playwright
2. Checks for new messages in the most recent chat
3. Sends the text to Gemini for a reply
4. Types and sends the reply as if it's you
5. Repeats the cycle every few seconds

---

## 📂 Project Structure

```
chatpilot/
│
├── .env.sample        # Sample environment file
├── requirements.txt   # Python dependencies
├── main.py     # Main bot script
└── README.md          # You're reading this
```

---

## ⚠️ Disclaimer

- This tool interacts with WhatsApp Web using automation and is meant for educational or personal use.
- Please respect WhatsApp's terms of service when deploying it.

---

## ✨ Credits

- [Playwright](https://playwright.dev/python/) for browser automation
- [agno](https://github.com/agno-agi/agno) for Google Gemini integration
- [Python](https://www.python.org/) for being awesome

---

## 📬 Contribute

Pull requests, issues, and stars are always welcome!

---

## 🛡 License

MIT License. Use responsibly.

---

## 🔮 Final Words

**Let your AI alter ego handle WhatsApp while you rule the real world.**
