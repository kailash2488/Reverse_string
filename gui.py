"""Lightweight desktop interface for the string-reversal examples."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from reverse import METHODS, is_palindrome, reverse_each_word, reverse_words


APP_BACKGROUND = "#f4f7fb"
CARD_BACKGROUND = "#ffffff"
ACCENT = "#6558d3"
TEXT_COLOR = "#172033"
MUTED_COLOR = "#667085"


class ReverseStringApp(tk.Tk):
    """A small desktop app that exposes the project's reversal functions."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Reverse String")
        self.geometry("760x600")
        self.minsize(600, 500)
        self.configure(background=APP_BACKGROUND)

        self.mode = tk.StringVar(value="Characters")
        self.method = tk.StringVar(value="slice")
        self.status = tk.StringVar(value="Ready")

        self._configure_styles()
        self._build_interface()
        self.bind("<Control-Return>", lambda _event: self.transform())
        self.bind("<Escape>", lambda _event: self.clear())
        self.input_text.focus_set()

    def _configure_styles(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("App.TFrame", background=APP_BACKGROUND)
        style.configure("Card.TFrame", background=CARD_BACKGROUND)
        style.configure(
            "Title.TLabel", background=APP_BACKGROUND, foreground=TEXT_COLOR,
            font=("TkDefaultFont", 22, "bold"),
        )
        style.configure(
            "Subtitle.TLabel", background=APP_BACKGROUND, foreground=MUTED_COLOR,
            font=("TkDefaultFont", 10),
        )
        style.configure(
            "Card.TLabel", background=CARD_BACKGROUND, foreground=TEXT_COLOR,
            font=("TkDefaultFont", 10, "bold"),
        )
        style.configure("Status.TLabel", background=APP_BACKGROUND, foreground=MUTED_COLOR)
        style.configure(
            "Accent.TButton", background=ACCENT, foreground="white",
            borderwidth=0, padding=(18, 10), font=("TkDefaultFont", 10, "bold"),
        )
        style.map("Accent.TButton", background=[("active", "#5145b8")])

    def _build_interface(self) -> None:
        outer = ttk.Frame(self, style="App.TFrame", padding=28)
        outer.pack(fill="both", expand=True)

        ttk.Label(outer, text="Reverse String", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            outer,
            text="Explore five Python techniques and useful text transformations.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(3, 20))

        card = ttk.Frame(outer, style="Card.TFrame", padding=20)
        card.pack(fill="both", expand=True)
        card.columnconfigure(0, weight=1)
        card.rowconfigure(2, weight=1)
        card.rowconfigure(7, weight=1)

        ttk.Label(card, text="Input text", style="Card.TLabel").grid(sticky="w")
        ttk.Label(
            card, text="Type or paste anything below", style="Card.TLabel"
        ).grid(sticky="e", row=0, column=0)
        self.input_text = tk.Text(
            card, height=6, wrap="word", relief="solid", borderwidth=1,
            font=("TkDefaultFont", 11), padx=10, pady=10, undo=True,
        )
        self.input_text.grid(row=2, column=0, sticky="nsew", pady=(8, 16))

        controls = ttk.Frame(card, style="Card.TFrame")
        controls.grid(row=3, column=0, sticky="ew", pady=(0, 16))
        controls.columnconfigure(1, weight=1)

        ttk.Label(controls, text="Action", style="Card.TLabel").grid(row=0, column=0, sticky="w")
        mode_box = ttk.Combobox(
            controls,
            textvariable=self.mode,
            values=("Characters", "Word order", "Each word", "Palindrome check"),
            state="readonly",
            width=20,
        )
        mode_box.grid(row=1, column=0, sticky="w", pady=(5, 0), padx=(0, 18))
        mode_box.bind("<<ComboboxSelected>>", self._mode_changed)

        ttk.Label(controls, text="Technique", style="Card.TLabel").grid(row=0, column=1, sticky="w")
        self.method_box = ttk.Combobox(
            controls, textvariable=self.method, values=tuple(METHODS),
            state="readonly", width=18,
        )
        self.method_box.grid(row=1, column=1, sticky="w", pady=(5, 0))

        ttk.Button(
            controls, text="Transform  ⌃↵", style="Accent.TButton", command=self.transform
        ).grid(row=0, column=2, rowspan=2, sticky="e", padx=(18, 0))

        ttk.Label(card, text="Result", style="Card.TLabel").grid(row=5, column=0, sticky="w")
        self.output_text = tk.Text(
            card, height=6, wrap="word", relief="solid", borderwidth=1,
            font=("TkDefaultFont", 11), padx=10, pady=10, state="disabled",
            background="#f8fafc",
        )
        self.output_text.grid(row=7, column=0, sticky="nsew", pady=(8, 14))

        actions = ttk.Frame(card, style="Card.TFrame")
        actions.grid(row=8, column=0, sticky="ew")
        ttk.Button(actions, text="Copy result", command=self.copy_result).pack(side="left")
        ttk.Button(actions, text="Clear", command=self.clear).pack(side="left", padx=8)
        ttk.Label(outer, textvariable=self.status, style="Status.TLabel").pack(
            anchor="w", pady=(10, 0)
        )

    def _mode_changed(self, _event: tk.Event[tk.Misc] | None = None) -> None:
        is_character_mode = self.mode.get() == "Characters"
        self.method_box.configure(state="readonly" if is_character_mode else "disabled")

    def _set_output(self, value: str) -> None:
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", value)
        self.output_text.configure(state="disabled")

    def transform(self) -> None:
        text = self.input_text.get("1.0", "end-1c")
        mode = self.mode.get()
        try:
            if mode == "Word order":
                result = reverse_words(text)
            elif mode == "Each word":
                result = reverse_each_word(text)
            elif mode == "Palindrome check":
                result = "Yes — this is a palindrome." if is_palindrome(text) else "No — this is not a palindrome."
            else:
                result = METHODS[self.method.get()](text)
        except RecursionError:
            messagebox.showerror(
                "Text too long",
                "The recursive technique cannot process text this long. Choose slice instead.",
            )
            return
        self._set_output(result)
        self.status.set(f"Done · {len(text)} input characters")

    def copy_result(self) -> None:
        result = self.output_text.get("1.0", "end-1c")
        if not result:
            self.status.set("Nothing to copy yet")
            return
        self.clipboard_clear()
        self.clipboard_append(result)
        self.status.set("Result copied to clipboard")

    def clear(self) -> None:
        self.input_text.delete("1.0", "end")
        self._set_output("")
        self.status.set("Cleared")
        self.input_text.focus_set()


def main() -> None:
    """Launch the desktop application."""
    app = ReverseStringApp()
    app.mainloop()


if __name__ == "__main__":
    main()
