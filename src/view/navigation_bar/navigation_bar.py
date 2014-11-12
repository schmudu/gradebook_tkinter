import tkinter as Tk
from src.view.custom_dialog import CustomDialog

from src.model.application_model import ApplicationModel

class NavigationBar(Tk.Frame):
  def __init__(self, parent_window):
    super().__init__(parent_window)

    self.parent_window = parent_window

    application_model = ApplicationModel()
    #application_model.add_observer(self.add_class, ApplicationModel.EVENT_ADD_CLASS)

    label = Tk.Label(self, text="Navigation Bar").grid()
    #label.pack()


