from src.lib.dispatcher import Dispatcher

class ApplicationModel(Dispatcher):
  _instance = None

  EVENT_ADD_CLASS = "event.application_model.add_class"

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(ApplicationModel, cls).__new__(
                          cls, *args, **kwargs)
      cls._instance.init()
    return cls._instance

  def init(self):
    # call dispatcher init
    super().init()

  def add_class(self):
    self.notify_observers(ApplicationModel.EVENT_ADD_CLASS)
