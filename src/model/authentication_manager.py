class AuthenticationManager:
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(AuthenticationManager, cls).__new__(
                          cls, *args, **kwargs)
    return cls._instance

  def __init__(self):
    pass