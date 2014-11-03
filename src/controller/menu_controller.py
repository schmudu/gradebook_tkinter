from src.model.application_model import ApplicationModel

class MenuController:
  _instance = None

  def __new__(cls, *args, **kwargs):
    #print("hitting new")
    if not cls._instance:
      cls._instance = super(MenuController, cls).__new__(cls)
      #print("setting instance to :{0} cls:{1}".format(cls._instance, cls))
    return cls._instance

  def __init__(self, *args, **kwargs):
    super().__init__()
    #self.application_model = ApplicationModel()
    pass

  def add_class(self):
    print("need to add a class")
