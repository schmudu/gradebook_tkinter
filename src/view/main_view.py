import tkinter as tk
from src.view.custom_dialog import CustomDialog

from src.model.application_model import ApplicationModel

class MainView(tk.Frame):
  def __init__(self, parent_window):
    super().__init__(parent_window)

    self.parent_window = parent_window

    application_model = ApplicationModel()
    application_model.add_observer(self.add_class, ApplicationModel.EVENT_ADD_CLASS)

  def add_class(self):
    CustomDialog(self.parent_window)
    print("adding class in main view")
