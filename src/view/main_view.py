import tkinter as tk

from src.model.application_model import ApplicationModel

class MainView(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    application_model = ApplicationModel()
    application_model.add_observer(self.add_class, ApplicationModel.EVENT_ADD_CLASS)

  def add_class(self):
    print("adding class in main view")
