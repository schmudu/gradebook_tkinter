import tkinter as tk
from src.controller.dialog_controller import DialogController

class MainMenu(tk.Menu):
  def __init__(self, parent_window):
    super().__init__(parent_window)

    menu_bar = tk.Menu(parent_window)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Add Class", command=self.add_class)
    menu_bar.add_cascade(label="Class", menu=file_menu)
    parent_window.config(menu=menu_bar)


  def add_class(self):
    DialogController().add_class()