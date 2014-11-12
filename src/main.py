from src.controller.dialog_controller import DialogController
from src.view.main_view import MainView
from src.view.menu.main_menu import MainMenu
from src.model.application_model import ApplicationModel
import tkinter as Tk

if __name__ == "__main__":
  root = Tk.Tk()

  # init model
  app_model = ApplicationModel()
  app_model.init()

  # init controllers
  DialogController(parent_window=root)

  # init views
  MainMenu(parent_window=root)
  MainView(parent_window=root).grid()
  Tk.mainloop()

  # post init

  # start
