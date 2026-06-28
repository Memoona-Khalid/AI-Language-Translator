import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Language Dictionary
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese": "zh-CN"
}

# Translation Function
def translate_text():
    try:
        text = input_box.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning(
                "Input Required",
                "Please enter text to translate."
            )
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)

        status_label.config(
            text="✓ Translation Successful",
            fg="#16a34a"
        )

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


# Swap Languages Function
def swap_languages():
    source = source_lang.get()
    target = target_lang.get()

    source_lang.set(target)
    target_lang.set(source)


# Main Window
root = tk.Tk()
root.title("AI Language Translator")
root.geometry("400x600")
root.configure(bg="#f5f9ff")

# Header
title = tk.Label(
    root,
    text="🌐 AI Language Translator",
    font=("Arial", 12, "bold"),
    bg="#f5f9ff",
    fg="#1e3a8a"
)
title.pack(pady=(15,5))

subtitle = tk.Label(
    root,
    text="Translate between multiple languages",
    font=("Arial", 10),
    bg="#f5f9ff",
    fg="gray"
)
subtitle.pack()

# Input Label
input_label = tk.Label(
    root,
    text="Enter Text",
    font=("Arial", 11, "bold"),
    bg="#f5f9ff"
)
input_label.pack(pady=(15,5))

# Input Box
input_box = tk.Text(
    root,
    height=5,
    width=40,
    font=("Arial", 11),
    relief="solid",
    bd=1
)
input_box.pack()

# Language Selection Frame
lang_frame = tk.Frame(root, bg="#f5f9ff")
lang_frame.pack(pady=15)

source_lang = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    state="readonly",
    width=12
)
source_lang.set("English")
source_lang.grid(row=0, column=0, padx=5)

swap_btn = tk.Button(
    lang_frame,
    text="⇄",
    font=("Arial", 12, "bold"),
    bg="#dbeafe",
    width=3,
    command=swap_languages
)
swap_btn.grid(row=0, column=1, padx=5)

target_lang = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    state="readonly",
    width=12
)
target_lang.set("Urdu")
target_lang.grid(row=0, column=2, padx=5)

# Translate Button
translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    height=1,
    relief="flat"
)
translate_btn.pack(pady=10)

# Status Label
status_label = tk.Label(
    root,
    text="",
    bg="#f5f9ff",
    font=("Arial", 9)
)
status_label.pack()

# Output Label
output_label = tk.Label(
    root,
    text="Translated Text",
    font=("Arial", 11, "bold"),
    bg="#f5f9ff"
)
output_label.pack(pady=(15,5))

# Output Box
output_box = tk.Text(
    root,
    height=5,
    width=40,
    font=("Arial", 11),
    relief="solid",
    bd=1
)
output_box.pack()

# Footer
footer = tk.Label(
    root,
    text="Powered by Google Translator",
    font=("Arial", 8),
    bg="#f5f9ff",
    fg="gray"
)
footer.pack(pady=15)

root.mainloop()