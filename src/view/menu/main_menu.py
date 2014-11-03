import tkinter as tk

from src.controller.menu_controller import MenuController

class MainMenu(tk.Menu):
  def __init__(self, parent_window):
    super().__init__(parent_window)

    menu_bar = tk.Menu(parent_window)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Add Class", command=self.add_class)
    menu_bar.add_cascade(label="Class", menu=file_menu)
    parent_window.config(menu=menu_bar)

    self.menu_controller = MenuController()

  def add_class(self):
    self.menu_controller.add_class()