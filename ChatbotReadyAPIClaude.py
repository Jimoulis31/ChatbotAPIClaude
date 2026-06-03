import anthropic
import threading
import tkinter as tk
from tkinter import scrolledtext

client = anthropic.Anthropic()

SYSTEM_PROMPT = "You are a helpful assistant. Be precise and and keep you answers concise."

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Bot")
        self.root.geometry("800x700")
        self.root.configure(bg="#2E2E2E")

        self.messages = []

        # Title
        tk.Label(
            root, text="Chat Bot", font=("Helvetica", 16, "bold"),
            fg="#FFFFFF", bg="#2E2E2E"
        ).pack(pady=10)

        # Chat area (scrollable)
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, height=30, width=100, font=("Arial", 11),
            bg="#3C3C3C", fg="#E0E0E0", insertbackground="white"
        )
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END,
                              "Welcome to Chat Bot!\n\n"
                              "Not sure what to ask? Here are some ideas:\n"
                              "  • 'What are the best new games in 2026?'\n"
                              "  • 'What are some good recipes?'\n"
                              "  • 'Tell me the highest rated movies.'\n"
                              "  • 'What are all the European countries?'\n\n"
                              "Go ahead and ask anything!\n")
        self.chat_area.config(state='disabled')

        input_frame = tk.Frame(self.root, bg="#2E2E2E")
        input_frame.pack(pady=5)

        self.input_field = tk.Entry(
            input_frame, width=40, font=("Arial", 12, "bold"), bg="#4A4A4A", fg="#FFFFFF",
            insertbackground="white"

        )
        self.input_field.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="#FFFFFF",
            activebackground="#45A094"
        )

        self.send_button.pack(side=tk.LEFT, padx=5)

        tk.Button(
            root, text="Clear Chat",command=self.clear_chat, font=("Arial", 12),
            bg="#F44336", fg="#FFFFFF", activebackground="#D32F2F"
        ).pack(pady=5)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, "Bot: ")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)

        self.messages.append({"role": "user", "content": user_input})

        self.input_field.config(state='disabled')
        self.send_button.config(state='disabled')

        thread = threading.Thread(target=self.stream_response, daemon=True)
        thread.start()

    def stream_response(self):
        full_response = ""

        with client.messages.stream(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=self.messages,
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                self.root.after(0, self.append_text, text)

        self.messages.append({"role": "user", "content": full_response})
        self.root.after(0, self.finish_response)

    def append_text(self, text):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, text)
        #self.chat_area.config(state='disabled')
        #self.chat_area.see(tk.END)
    def finish_response(self):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "\n")
        self.chat_area.config(state='disabled')
        self.input_field.config(state='normal')
        self.send_button.config(state='normal')
        #self.input_field.focus()
    def clear_chat(self):
        self.messages.clear()
        self.chat_area.config(state='normal')
        self.chat_area.delete('1.0', tk.END)
        self.chat_area.insert(tk.END, "Welcome to Chat Bot!\n")
        self.chat_area.config(state='disabled')



def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()