# Claude Chatbot (Tkinter)

A simple desktop chatbot built with Python, Tkinter, and the Anthropic Claude API.

## Features
- Real-time streaming responses
- GUI chat interface
- Multi-threaded (no freezing UI)

## Setup

### 1. Install dependencies
pip install anthropic

### 2. Set API key (IMPORTANT)

Windows (PowerShell):
setx ANTHROPIC_API_KEY "your_api_key_here"

Restart terminal after setting it.

### 3. Run the app
python ChatbotReadyAPIClaude.py

## Notes
- Uses Claude streaming API
- Requires internet connection
- Make sure .gitignore is set to avoid uploading sensitive files
EOF
