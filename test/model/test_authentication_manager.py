import unittest
from src.model.authentication_manager import AuthenticationManager

class TestAuthenticationManager(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_singleton(self):
    self.assertEqual(AuthenticationManager(), AuthenticationManager())