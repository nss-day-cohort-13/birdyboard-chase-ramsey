import unittest
from main import *

class TestChirpLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.chirp_data = ChirpData('test_chirps.txt')
    sel.user_data = UserData('test_users.txt')

  def test_create_public_chirp(self):
    pass

  def test_create_private_chirp(self):
    pass

class TestUserLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.chirp_data = ChirpData('test_chirps.txt')
    sel.user_data = UserData('test_users.txt')

  def test_login_sets_correct_current_user(self):
    self.user_data.set_current_user('test_acct', 'test_password')
    self.assertEqual(self.user_data.current_user.username, 'test_acct')
    self.assertEqual(self.user_data.current_user.password, 'test_password')
    self.assertEqual(self.user_data.current_user.id, '00000001')

  def test_create_new_user(self):
    pass
