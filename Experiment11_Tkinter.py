"""A small Tkinter GUI that greets the user."""

import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Greeting App")
    window.geometry("300x160")

    tk.Label(window, text="Enter your name:").pack(pady=(15, 5))
    name_entry = tk.Entry(window)
    name_entry.pack()
    message_label = tk.Label(window, text="")
    message_label.pack(pady=10)

    def show_greeting():
        name = name_entry.get().strip() or "Guest"
        message_label.config(text=f"Hello, {name}!")

    tk.Button(window, text="Greet", command=show_greeting).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
