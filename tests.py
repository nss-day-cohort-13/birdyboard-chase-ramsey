import unittest
from main import *

class TestChirpLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.chirp_data = ChirpData('test_chirps.txt')
    self.user_data = UserData('test_users.txt')
    self.user_data.set_current_user('test_acct', 'test_password')

  def test_create_public_chirp(self):
    chirp_text = 'This is the text of a public chirp'
    self.chirp_data.new_chirp(text, self.user_data.current_user.username)
    chirp = dict()
    chirp.text = chirp_text,
    chirp.username = self.user_data.current_user.username,
    chirp.chirp_id = str(len(self.chirp_data.chirps))
    chirp.private = False

    self.assertTrue(chirp in self.chirp_data.chirps)

    # Clean up
    self.chirp_data.chirps = self.chirp_data.chirps[:-1]

  def test_create_private_chirp(self):
    chirp_text = 'This is the text of a public chirp'
    self.chirp_data.new_chirp(text, self.user_data.current_user.username, private=True)
    chirp = dict()
    chirp.text = chirp_text,
    chirp.username = self.user_data.current_user.username,
    chirp.chirp_id = str(len(self.chirp_data.chirps))
    chirp.private = True

    self.assertTrue(chirp in self.chirp_data.chirps)

    # Clean up
    self.chirp_data.chirps = self.chirp_data.chirps[:-1]

class TestUserLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.user_data = UserData()

  def test_find_user_returns_true_false(self):
    self.assertTrue(self.user_data.find_user('test_acct'))
    self.assertFalse(self.user_data.find_user('chase'))

    self.assertTrue(self.user_data.find_user('test_acct', 'test_password'))
    self.assertFalse(self.user_data.find_user('test_acct', 'wrong_password'))
    self.assertFalse(self.user_data.find_user('test_acct', ''))

  def test_login_sets_correct_current_user(self):
    self.user_data = UserData('test_users.txt')

    self.assertEqual(self.user_data.current_user, None)
    self.user_data.set_current_user('test_acct', 'test_password')

    self.assertEqual(self.user_data.current_user.username, 'test_acct')
    self.assertEqual(self.user_data.current_user.password, 'test_password')
    self.assertEqual(self.user_data.current_user.user_id, '00000001')

    # Clean up
    self.user_data.current_user = None

  def test_create_new_user(self):
    self.user_data = UserData('test_users.txt')

    self.assertEqual(self.user_data.current_user, None)
    self.user_data.new_user('new_test', 'new_password')
    new = dict()
    new.username = 'new_test',
    new.password = 'new_password',
    new.user_id = '00000002'
    self.assertTrue(new in self.user_data.users)

    self.assertEqual(self.user_data.current_user.username, 'new_test')
    self.assertEqual(self.user_data.current_user.password, 'new_password')
    self.assertEqual(self.user_data.current_user.user_id, '00000002')

    # Clean up
    self.user_data.current_user = None
    self.user_data.users = self.user_data.users[:-1]

  class TestUserInterface:

    @classmethod
    def setUpClass(self):
      self.chirp_data = ChirpData('test_chirps.txt')
      self.user_data = UserData('test_users.txt')
      self.user_interface = UserInterface()

    def test_user_must_be_logged_in_to_chirp(self):
      self.assertEqual(self.user_data.current_user, None)
      self.assertRaises(Exception, self.user_interface.submit_new_chirp())
