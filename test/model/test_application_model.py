import unittest
from src.model.application_model import ApplicationModel

class TestApplicationModel(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_singleton(self):
    self.assertEqual(ApplicationModel(), ApplicationModel())