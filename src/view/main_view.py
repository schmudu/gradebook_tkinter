import tkinter as Tk
from src.view.custom_dialog import CustomDialog
from src.view.navigation_bar.navigation_bar import NavigationBar

from src.model.application_model import ApplicationModel

class MainView(Tk.Frame):
  def __init__(self, parent_window):
    super().__init__(parent_window)

    self.parent_window = parent_window

    application_model = ApplicationModel()
    application_model.add_observer(self.add_class, ApplicationModel.EVENT_ADD_CLASS)
    NavigationBar(parent_window=self).grid(row=0)

    #parent_window.grid_rowconfigure(0, weight=0)

  def add_class(self):
    CustomDialog(self.parent_window)
