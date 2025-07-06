import tkinter as tk
from tkinter import messagebox
import random
import os
from datetime import datetime

# Folder to save journal entries
if not os.path.exists("journal_entries"):
    os.makedirs("journal_entries")

# Mood to quote mapping
quotes = {
    "Happy": [
        "Happiness is not by chance, but by choice.",
        "Smile more, worry less.",
        "Joy is a net of love by which you can catch souls."
    ],
    "Sad": [
        "It’s okay to not be okay.",
        "Tears come from the heart, not the brain.",
        "Every storm runs out of rain."
    ],
    "Angry": [
        "For every minute you remain angry, you give up sixty seconds of peace of mind.",
        "Speak when you are angry and you will make the best speech you will ever regret.",
        "Anger is one letter short of danger."
    ],
    "Anxious": [
        "You don’t have to control your thoughts. You just have to stop letting them control you.",
        "Feelings are just visitors. Let them come and go.",
        "This too shall pass."
    ]
}

current_mood = None

# Save the journal entry
def save_journal():
    global current_mood
    entry = journal_entry.get("1.0", tk.END).strip()
    if not entry:
        messagebox.showwarning("Empty Entry", "Please write something before saving.")
        return
    if not current_mood:
        messagebox.showwarning("No Mood Selected", "Please select a mood first.")
        return

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"journal_entries/{current_mood}_{now}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Mood: {current_mood}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(entry)
    messagebox.showinfo("Saved", f"Your journal entry has been saved as {filename}.")
    journal_entry.delete("1.0", tk.END)
    quote_label.config(text="")
    journal_label.config(text="")

# Show quote for selected mood
def select_mood(mood):
    global current_mood
    current_mood = mood
    quote = random.choice(quotes[mood])
    quote_label.config(text=quote)
    journal_entry.delete("1.0", tk.END)
    journal_label.config(text=f"Your {mood} Journal:")

# GUI Setup
root = tk.Tk()
root.title("Inner Child: Mood Journal")
root.geometry("600x500")
root.configure(bg="#f0f4f8")

# Heading
heading = tk.Label(root, text="Inner Child ✨", font=("Helvetica", 24, "bold"), bg="#f0f4f8", fg="#333")
heading.pack(pady=10)

# Mood Buttons
moods = ["Happy", "Sad", "Angry", "Anxious"]
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=10)

for mood in moods:
    btn = tk.Button(button_frame, text=mood, width=10, height=2, bg="#d0e8ff", fg="#333",
                    command=lambda m=mood: select_mood(m))
    btn.pack(side=tk.LEFT, padx=10)

# Quote Label
quote_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), wraplength=500, bg="#f0f4f8", fg="#444")
quote_label.pack(pady=10)

# Journal Heading Label
journal_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f0f4f8", fg="#222")
journal_label.pack(pady=5)

# Journal Text Box
journal_entry = tk.Text(root, height=10, width=60, wrap=tk.WORD, font=("Helvetica", 12))
journal_entry.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Save Entry", command=save_journal, bg="#a5d6a7", font=("Helvetica", 12))
save_button.pack(pady=10)

root.mainloop()
