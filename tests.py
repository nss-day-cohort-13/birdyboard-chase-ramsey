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

  def test_login_sets_correct_current_user(self):
    user_data = UserData('test_users.txt')

    self.assertEqual(user_data.current_user, None)
    self.user_data.set_current_user('test_acct', 'test_password')

    self.assertEqual(user_data.current_user.username, 'test_acct')
    self.assertEqual(user_data.current_user.password, 'test_password')
    self.assertEqual(user_data.current_user.id, '00000001')

  def test_create_new_user(self):
    self.user_data = UserData('test_users.txt')

    self.assertEqual(user_data.current_user, None)
    user_data.new_user('new_test', 'new_password')
    new = {
      'username': 'new_test',
      'password': 'new_password',
      'id': '00000002'
    }
    self.assertTrue(new in user_data.users)

    self.assertEqual(user_data.current_user.username, 'new_test')
    self.assertEqual(user_data.current_user.password, 'new_password')
    self.assertEqual(user_data.current_user.id, '00000002')
