from src.view.main_view import MainView
from src.view.menu.main_menu import MainMenu
import tkinter as tk

if __name__ == "__main__":
  root = tk.Tk()
  MainMenu(parent_window=root)
  main_view = MainView(parent_window=root).mainloop()
