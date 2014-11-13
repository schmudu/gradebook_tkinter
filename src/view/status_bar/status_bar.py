import tkinter as Tk
from src.view.custom_dialog import CustomDialog

from src.model.application_model import ApplicationModel

class StatusBar(Tk.Frame):
  def __init__(self, parent_window):
    super().__init__(parent_window)

    self.parent_window = parent_window

    application_model = ApplicationModel()
    #application_model.add_observer(self.add_class, ApplicationModel.EVENT_ADD_CLASS)

    self.primary_status = Tk.StringVar()
    self.primary_status.set("Primary Status")
    self.primary_status_label = Tk.Label(self, textvariable=self.primary_status).grid(sticky="nsew")
    #label.pack()


