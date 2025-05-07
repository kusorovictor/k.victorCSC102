import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice

# Speak Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Process User Input (You can replace this with actual AI logic later)
def process_input():
    user_text = entry.get()
    if not user_text.strip():
        response = "Please type something."
    else:
        response = f"You said: {user_text}"  # Dummy AI response
    response_label.config(text=response)
    speak(response)

# Main GUI Window
root = tk.Tk()
root.title("Nova: AI Assistant")
root.geometry("600x400")
root.configure(bg="#0f0f0f")

# Title
title = tk.Label(root, text="💠 Nova: Your AI Assistant", font=("Orbitron", 20), bg="#0f0f0f", fg="#00f0ff")
title.pack(pady=20)

# Entry Box
entry = tk.Entry(root, font=("Consolas", 16), bg="#1e1e1e", fg="#00ffcc", insertbackground="#00ffcc", width=40)
entry.pack(pady=10)
entry.focus()

# Button
speak_button = tk.Button(root, text="Speak 🔊", command=process_input,
                         font=("Orbitron", 14), bg="#222", fg="#00ffcc",
                         activebackground="#333", activeforeground="#00ffcc", borderwidth=0)
speak_button.pack(pady=10)

# Response Display
response_label = tk.Label(root, text="", font=("Consolas", 14), bg="#0f0f0f", fg="#ffffff", wraplength=500)
response_label.pack(pady=20)

# Run
root.mainloop()
