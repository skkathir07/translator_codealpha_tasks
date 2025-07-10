import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json
import pyperclip
import pyttsx3
import threading
from deep_translator import GoogleTranslator
from typing import Dict, Optional

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to translate text
def translate_text():
    input_text = input_box.get("1.0", tk.END).strip()
    target_lang = target_lang_combo.get()

    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(input_text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function to copy translated text
def copy_text():
    translated_text = output_box.get("1.0", tk.END).strip()
    pyperclip.copy(translated_text)
    messagebox.showinfo("Copied", "Translated text copied to clipboard.")

# Function to speak translated text
def speak_text():
    translated_text = output_box.get("1.0", tk.END).strip()
    engine.say(translated_text)
    engine.runAndWait()

# GUI setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")

# Input box
ttk.Label(root, text="Enter Text").pack()
input_box = scrolledtext.ScrolledText(root, height=5)
input_box.pack(fill="x", padx=10)

# Target language selection
ttk.Label(root, text="Select Target Language (eg: en, ta, hi)").pack()
target_lang_combo = ttk.Entry(root)
target_lang_combo.pack(fill="x", padx=10)
target_lang_combo.insert(0, "en")  # default to English

# Translate button
translate_btn = ttk.Button(root, text="Translate", command=lambda: threading.Thread(target=translate_text).start())
translate_btn.pack(pady=10)

# Output box
ttk.Label(root, text="Translated Text").pack()
output_box = scrolledtext.ScrolledText(root, height=5)
output_box.pack(fill="x", padx=10)

# Copy & Speak buttons
copy_btn = ttk.Button(root, text="Copy", command=copy_text)
copy_btn.pack(pady=5)

speak_btn = ttk.Button(root, text="Speak", command=speak_text)
speak_btn.pack(pady=5)

root.mainloop()
