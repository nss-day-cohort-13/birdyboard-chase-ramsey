import unittest
from main import *

class TestChirpLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.chirp_data = ChirpData('test_chirps.txt')
    self.user_data = UserData('test_users.txt')
    self.user_data.set_current_user('test_acct', 'test_password')

  def test_public_chirp_creation(self):
    chirp_text = 'This is the text of a public chirp'
    chirp = Chirp(chirp_text, self.user_data.current_user)

    self.assertEqual(chirp.text, chirp_text)
    self.assertEqual(chirp.sender_id, 00000001)
    self.assertFalse(chirp.private)

  def test_private_chirp_creation(self):
    chirp_text = 'This is the text of a private chirp'
    chirp = PrivateChirp(chirp_text, self.user_data.current_user, 00000002)

    self.assertEqual(chirp.text, chirp_text)
    self.assertEqual(chirp.sender_id, 00000001)
    self.assertTrue(chirp.private)
    self.assertEqual(chirp.receiver_id, 00000002)

  def test_create_public_chirp_appears_in_all_chirps(self):
    chirp_text = 'This is the text of a public chirp'
    self.chirp_data.new_chirp(chirp_text, self.user_data.current_user, testing=True)

    chirp = Chirp((chirp_text, self.user_data.current_user))
    self.assertTrue(chirp in self.chirp_data.chirps)

    # Clean up
    if len(self.chirp_data.chirps) > 1:
      self.chirp_data.chirps = self.chirp_data.chirps[:1]

  def test_create_private_chirp_appears_in_all_chirps(self):
    chirp_text = 'This is the text of a private chirp'
    self.chirp_data.new_chirp(chirp_text, self.user_data.current_user, private=True, receiver=00000002, testing=True)

    chirp = PrivateChirp((chirp_text, self.user_data.current_user, receiver=00000002))
    self.assertTrue(chirp in self.chirp_data.chirps)

    # Clean up
    if len(self.chirp_data.chirps) > 1:
      self.chirp_data.chirps = self.chirp_data.chirps[:1]

class TestUserLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.user_data = UserData('test_users.txt')

  def test_find_user_returns_true_false(self):
    self.assertTrue(self.user_data.find_user('test_acct'))
    self.assertFalse(self.user_data.find_user('chase'))

  def test_login_sets_correct_current_user(self):
    self.assertEqual(self.user_data.current_user, None)
    self.user_data.set_current_user('test_acct')
    self.assertEqual(self.user_data.current_user, 00000001)

    # Clean up
    self.user_data.current_user = None

  def test_create_new_user(self):
    self.assertEqual(self.user_data.current_user, None)
    self.user_data.new_user('New Test', 'new_test', testing=True)
    new = {
      full_name: 'New Test',
      username: 'new_test'
    }
    self.assertTrue(new in self.user_data.users)
    self.assertEqual(self.user_data.current_user, 00000002)

    # Clean up
    self.user_data.current_user = None
    if len(self.user_data.users) > 1:
      self.user_data.users = self.user_data.users[:1]

  class TestUserInterface:

    @classmethod
    def setUpClass(self):
      self.chirp_data = ChirpData('test_chirps.txt')
      self.user_data = UserData('test_users.txt')
      self.user_interface = UserInterface()

    def test_user_must_be_logged_in_to_chirp(self):
      self.assertEqual(self.user_data.current_user, None)
      self.assertRaises(Exception, self.user_interface.submit_new_chirp())


if __name__ == '__main__':
  unittest.main()
