import unittest
import tkinter as Tk
from src.controller.menu_controller import MenuController

class TestApplicationModel(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    #if('controller' in locals()):
    # destroy instance variable if exists
    if(hasattr(MenuController, '_instance')):
      MenuController._instance = None

  def test_success(self):
    self.controller = MenuController(Tk.Tk())
    self.assertNotEquals(self.controller, None, "MenuController should be defined if" + \
      "tkinter.Tk() instance is passed in")

  def test_singleton(self):
    try:
      self.controller = MenuController()
      self.fail("MenuController needs to be passed reference " + \
        "to tkinter.Tk() upon first instantiation")
    except ValueError as e:
      pass
  '''

  def test_wrong_argument_passed_in(self):
    try:
      self.controller = MenuController(5)
      self.fail("MenuController needs to be passed reference " + \
        "to tkinter.Tk() upon first instantiation")
    except ValueError as e:
      pass

  def test_argument_passed_on_subsequent_calls(self):
    try:
      self.controller = MenuController(Tk.Tk())
      self.controller = MenuController(5)
      self.fail("MenuController needs to be passed reference " + \
        "to tkinter.Tk() upon first instantiation")
    except ValueError as e:
      pass
  '''
