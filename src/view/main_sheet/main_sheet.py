import tkinter as Tk
from src.view.custom_dialog import CustomDialog

from src.model.application_model import ApplicationModel

class MainSheet(Tk.Frame):
  def __init__(self, parent_window):
    super().__init__(parent_window)

    self.parent_window = parent_window

    #application_model.add_observer(self.add_class, ApplicationModel.EVENT_ADD_CLASS)

    self.primary_status_label = Tk.Label(self, text="Main Sheet")
    self.primary_status_label.grid(sticky="nsew")
    self.primary_status_label.config(bg="red")
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)
    #label.pack()


