from src.model.application_model import ApplicationModel

class MenuController:
  def __init__(self):
    self.application_model = ApplicationModel()

  def add_class(self):
    self.application_model.add_class()
