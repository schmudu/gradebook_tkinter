import tkinter as tk

from src.controller.menu_controller import MenuController

class MainMenu(tk.Menu):
  def __init__(self, master):
    super().__init__(master)

    menu_bar = tk.Menu(master)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=self.hello)
    menu_bar.add_cascade(label="Test", menu=file_menu)
    master.config(menu=menu_bar)

    self.menu_controller = MenuController()

  def hello(self):
    self.menu_controller.add_class()