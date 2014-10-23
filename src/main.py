from src.view.main_view import MainView
from src.view.menu.main_menu import MainMenu
import tkinter as tk

def hello():
  print("hello!")

if __name__ == "__main__":
  root = tk.Tk()
  MainMenu(master=root)
  #menubar.add_command(label="Hello", command=hello)
  #root.config(menu=menubar)
  #MainMenu(master=root)
  #main_view = MainView(master=root).mainloop()
  main_view = MainView(master=root).mainloop()
