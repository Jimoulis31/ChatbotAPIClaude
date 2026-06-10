# Claude Chatbot (Tkinter)

A simple desktop chatbot built with **Python**, **Tkinter**, and the **Anthropic Claude API**.

The application provides a clean graphical interface and supports real-time streaming responses from Claude while keeping the UI responsive through multithreading.

---

## Features

- ⚡ Real-time streaming responses
- 🖥️ Clean and easy-to-use GUI
- 🔄 Multi-threaded architecture (prevents UI freezing)
- 🔐 Secure API key handling through environment variables
- 🚀 Lightweight and easy to set up

---

## Screenshot

Add a screenshot of the application below:

![Claude Chatbot Screenshot](APIChatBot.png)


---

## Requirements

- Python 3.10+
- Anthropic API Key
- Internet Connection

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/claude-chatbot.git
cd claude-chatbot
```

### 2. Install Dependencies

```bash
pip install anthropic
```

### 3. Set Your API Key

#### Windows (PowerShell)

```powershell
setx ANTHROPIC_API_KEY "your_api_key_here"
```

Restart your terminal after setting the variable.

#### Linux / macOS

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

---

## Running the Application

```bash
python ChatbotReadyAPIClaude.py
```

---

## Project Structure

```text
.
├── ChatbotReadyAPIClaude.py
├── README.md
├── .gitignore
└── images/
    └── screenshot.png
```

---

## Notes

- Uses the Anthropic Claude Streaming API.
- Requires an active internet connection.
- Do not upload API keys to GitHub.
- Make sure your `.gitignore` excludes sensitive files.

---

## License

This project is open-source and available under the MIT License.
