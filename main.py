import subprocess

import customtkinter as ctk
from customtkinter import CTkButton

from CTkPDFViewer import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Asyk")
        self.geometry("800x700")

        self.current_page = 1
        self.min_page = 1
        self.max_page = 40

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text="Курсаев А.Г., Кулмуханбет Д.А., Байдрахманова Г.А., Мухтаров С.М., Култанов Д.Т.")

        self.pdf_frame = CTkPDFViewer(self, file=f"_internal/asyk-split/page_{self.current_page}.pdf")
        self.pdf_frame.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.prev_page_button = CTkButton(self, text="Prev Page", command=self.view_prev_page)
        self.prev_page_button.grid(row=1, sticky="sw")

        self.start_game_button = CTkButton(self, text="Start Game", command=self.start_game)
        self.start_game_button.grid(row=1, sticky="s")

        self.next_page_button = CTkButton(self, text="Next Page", command=self.view_next_page)
        self.next_page_button.grid(row=1, sticky="se")

        self.label.grid(row=2, sticky="s")

    def view_next_page(self):
        if self.current_page < self.max_page:
            self.current_page += 1
            self.pdf_frame.configure(file=f"_internal/asyk-split/page_{self.current_page}.pdf")

    def view_prev_page(self):
        if self.current_page > self.min_page:
            self.current_page -= 1
            self.pdf_frame.configure(file=f"_internal/asyk-split/page_{self.current_page}.pdf")

    def start_game(self):
        subprocess.call(["_internal/Game/Asyk.exe"])


if __name__ == '__main__':
    app = App()
    app.mainloop()
