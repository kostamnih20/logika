import threading
import socket
from customkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat")
        self.geometry("700x420")

        self.username = "User"


        self.main_frame = CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)


        self.menu_closed = 40
        self.menu_opened = 220
        self.menu_open = False

        self.menu_frame = CTkFrame(self.main_frame, widht=self.menu_closed)
        self.menu_frame.pack(side="left", fill="y")
        self.menu_frame.pack_propagate(False)

        self.menu_btn = CTkButton(self.menu_frame, text="menu", width=30, command=self.toggle_menu)
        self.menu_btn.pack(pady=5)

        self.name_label = CTkLabel(self.menu_frame, text="Ваше ім'я:")
        self.name_entery = CTkEntry(self.menu_frame)
        self.save_btn = CTkButton(self.menu_frame, text="Зберегти",command=self.save_username)


        self.chat_frame = CTkFrame(self.main_frame)
        self.chat_frame.pack(side="left", fill="both", expand=True)

        self.chat = CTkTextbox(self.chat_frame, state="disabled", font=("Arial", 14))
        self.chat.pack(fill="both", expand=True, padx=10, pady=10)

        bottom = CTkFrame(self.chat_frame)
        bottom.pack(fill="x")

        self.entry = CTkEntry(bottom, placeholder_text="Ведіть повідомлення...")
        self.entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.send_btn = CTkButton(bottom,text="Надіслати", width=50, command=self.send_message)
        self.send_btn.pack(side="right", padx=5)
