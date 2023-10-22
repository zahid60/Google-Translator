import tkinter as tk
from tkinter import ttk
from translate import Translator

# Define language codes for common languages
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
    "Bengali": "bn",
    "Hindi": "hi",
    "Portuguese": "pt",
    "Dutch": "nl",
}

def translate():
    src_lang = LANGUAGES.get(src_lang_var.get())
    target_lang = LANGUAGES.get(target_lang_var.get())
    text = src_text.get(1.0, tk.END)

    if src_lang and target_lang:
        try:
            translator = Translator(to_lang=target_lang, from_lang=src_lang)
            translated = translator.translate(text)

            target_text.delete(1.0, tk.END)
            target_text.insert(tk.END, translated)
        except Exception as e:
            target_text.delete(1.0, tk.END)
            target_text.insert(tk.END, f"Translation Error: {e}")
    else:
        target_text.delete(1.0, tk.END)
        target_text.insert(tk.END, "Select valid source and target languages.")

root = tk.Tk()
root.title("Google Translator")
root.geometry("610x400")
root.configure(bg="#E5E4E2")

frame = ttk.LabelFrame(root, text="Translation")
frame.place(x=20, y=20, width=580, height=350)

src_label = tk.Label(frame, text="Enter Text", bg="#E5E5E5")
src_label.grid(row=0, column=0, padx=10, pady=10)

src_text = tk.Text(frame, height=5, width=40)
src_text.grid(row=1, column=0, padx=10, pady=10)

src_lang_label = tk.Label(frame, text="Source Language", bg="#E5E5E5")
src_lang_label.grid(row=0, column=1, padx=10, pady=10)

src_lang_var = tk.StringVar()
src_lang_combobox = ttk.Combobox(frame, textvariable=src_lang_var, values=list(LANGUAGES.keys()))
src_lang_combobox.grid(row=1, column=1, padx=10, pady=10)
src_lang_combobox.set("English")

target_label = tk.Label(frame, text="Translation", bg="#E5E5E5")
target_label.grid(row=2, column=0, padx=10, pady=10)

target_text = tk.Text(frame, height=5, width=40)
target_text.grid(row=3, column=0, padx=10, pady=10)

target_lang_label = tk.Label(frame, text="Target Language", bg="#E5E5E5")
target_lang_label.grid(row=2, column=1, padx=10, pady=10)

target_lang_var = tk.StringVar()
target_lang_combobox = ttk.Combobox(frame, textvariable=target_lang_var, values=list(LANGUAGES.keys()))
target_lang_combobox.grid(row=3, column=1, padx=10, pady=10)
target_lang_combobox.set("English")

translate_button = tk.Button(frame, text="Translate", command=translate, bg="#4CAF50", fg="white")
translate_button.grid(row=4, column=0, padx=10, pady=10)

clear_button = tk.Button(frame, text="Clear", command=lambda: src_text.delete(1.0, tk.END), bg="#FF5733", fg="white")
clear_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
