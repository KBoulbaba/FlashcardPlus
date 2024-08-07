import tkinter as tk
from tkinter import ttk
from typing import Self

from src.application.db_service import DbService
from src.application.flashcard_service import FlashcardService


class TkinterUI:
    """
    A class representing a Tkinter-based user interface for a flashcard application.

    Methods:
    - load_certifications: Loads certifications into a Combobox.
    - load_categories: Loads categories based on the selected certification.
    - load_flashcards: Loads flashcards based on the selected category and certification.
    - run: Starts the Tkinter main event loop to run the UI.
    """

    def __init__(self: Self, flashcard_service: FlashcardService, db_service: DbService):
        """
        Initializes the TkinterUI with FlashcardService and DbService instances, setting up the UI components.

        """
        self.flashcard_service = flashcard_service
        self.db_service = db_service
        self.root = tk.Tk()
        self.root.title("Flashcards Application")

        self.cert_combo = ttk.Combobox(self.root, state="readonly")
        self.cert_combo.pack(padx=10, pady=5)
        self.cert_combo.bind("<<ComboboxSelected>>", self.load_categories)

        self.cat_combo = ttk.Combobox(self.root, state="readonly")
        self.cat_combo.pack(padx=10, pady=5)
        self.cat_combo.bind("<<ComboboxSelected>>", self.load_flashcards)

        self.flashcard_frame = tk.Frame(self.root)
        self.flashcard_frame.pack(padx=10, pady=5)

        self.load_certifications()

    def load_certifications(self: Self):
        """
        Loads certifications into the Combobox UI component based on data retrieved from the database service.

        """
        certs = self.db_service.get_certifications()
        self.cert_combo["values"] = [cert.name for cert in certs]

    def load_categories(self: Self, _):
        """
        Loads categories into the Combobox UI component based on the selected certification name and data retrieved from the database service.

        """
        cert_name = self.cert_combo.get()
        if cert := self.db_service.get_certification_by_name(cert_name):
            service = self.db_service.get_categories(cert.id)
            self.cat_combo["values"] = [cat.name for cat in service.categories]

    def load_flashcards(self: Self, _):
        """
        Loads flashcards into the UI based on the selected category and certification names, retrieved from the database service and displayed in the UI frame.

        """
        cat_name = self.cat_combo.get()
        cert_name = self.cert_combo.get()
        if cert := self.db_service.get_certification_by_name(cert_name):
            if cat := self.db_service.get_categories(cert.id).get_by_name_category(cat_name):
                flashcards = self.flashcard_service.get_flashcards(cat.id)
                for widget in self.flashcard_frame.winfo_children():
                    widget.destroy()
                for flashcard in flashcards:
                    tk.Label(self.flashcard_frame, text=f"Question: {flashcard.question}", wraplength=400).pack(
                        anchor="w"
                    )
                    tk.Label(self.flashcard_frame, text=f"Answer: {flashcard.answer}", wraplength=400).pack(anchor="w")

    def run(self: Self):
        """
        Starts the Tkinter main event loop to run the UI.

        """
        self.root.mainloop()
