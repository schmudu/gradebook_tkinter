import tkinter as Tk

class DialogController:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      if(('parent_window' in kwargs) and (type(kwargs['parent_window'] == Tk.Tk))):
        cls._instance = super().__new__(cls)
        cls._instance.parent_window = kwargs['parent_window']
        return cls._instance
      else:
        raise ValueError("DialogController must be passed a reference to tkinter.Tk() for initialization")
    else:
      if(bool(kwargs) == False):
        return cls._instance
      else:
        raise ValueError("DialogController does not need to be passed arguments after initialization.")

  def add_class(self):
    print("need to show class view")
