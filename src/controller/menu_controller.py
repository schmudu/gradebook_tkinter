from src.model.application_model import ApplicationModel
import tkinter as Tk

class MenuController:
  _instance = None

  def __new__(cls, *args, **kwargs):
    # TODO: verify that kwargs has tkinter.Tkinter() as an argument
    if not cls._instance:
      if(('parent_window' in kwargs) and (type(kwargs['parent_window'] == Tk.Tk))):
        cls._instance = super().__new__(cls)
        cls._instance.parent_window = kwargs['parent_window']
        return cls._instance
      else:
        raise ValueError("MenuController must be passed a reference to tkinter.Tk() for initialization")
    else:
      if(bool(kwargs) == False):
        return cls._instance
      else:
        raise ValueError("MenuController does not need to be passed arguments after initialization.")

  '''
  def __init__(self, *args, **kwargs):
    super().__init__()
    #self.application_model = ApplicationModel()
    pass
  '''

  def add_class(self):
    print("need to add a class")
