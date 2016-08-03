import unittest
from main import *

class TestChirpLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.chirp_data = ChirpData('test_chirps.txt')
    self.user_data = UserData('test_users.txt')
    self.user_data.set_current_user('test_acct')

  def test_public_chirp_creation(self):
    chirp_text = 'This is the text of a public chirp'
    chirp = Chirp(chirp_text, self.user_data.current_user)
    uid = self.user_data.find_user('test_acct')

    self.assertEqual(chirp.text, chirp_text)
    self.assertEqual(chirp.sender_id, uid)
    self.assertFalse(chirp.private)

  def test_private_chirp_creation(self):
    chirp_text = 'This is the text of a private chirp'
    chirp = PrivateChirp(chirp_text, self.user_data.current_user, receiver_id=2)
    uid = self.user_data.find_user('test_acct')

    self.assertEqual(chirp.text, chirp_text)
    self.assertEqual(chirp.sender_id, uid)
    self.assertTrue(chirp.private)
    self.assertEqual(chirp.receiver_id, 2)

  def test_create_public_chirp_appears_in_all_chirps(self):
    chirp_text = 'This is the text of a public chirp'
    uid = self.user_data.current_user
    cid = len(self.chirp_data.all_chirps)
    self.chirp_data.new_chirp(chirp_text, uid, testing=True)

    self.assertIsNotNone(self.chirp_data.all_chirps[cid])
    self.assertTrue(self.chirp_data.all_chirps[cid].text, chirp_text)
    self.assertTrue(self.chirp_data.all_chirps[cid].sender_id, uid)
    self.assertFalse(self.chirp_data.all_chirps[cid].private)

  def test_create_private_chirp_appears_in_all_chirps(self):
    chirp_text = 'This is the text of a private chirp'
    uid = self.user_data.current_user
    cid = len(self.chirp_data.all_chirps)
    self.chirp_data.new_chirp(chirp_text, self.user_data.current_user, private=True, receiver_id=2, testing=True)

    self.assertIsNotNone(self.chirp_data.all_chirps[cid])
    self.assertTrue(self.chirp_data.all_chirps[cid].text, chirp_text)
    self.assertTrue(self.chirp_data.all_chirps[cid].sender_id, uid)
    self.assertTrue(self.chirp_data.all_chirps[cid].private)

class TestUserLogic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.user_data = UserData('test_users.txt')

  def test_find_user_returns_uid_or_none(self):
    self.assertIsNotNone(self.user_data.find_user('test_acct'))
    self.assertEqual(self.user_data.find_user('chase'), None)

  def test_login_sets_correct_current_user(self):
    self.assertEqual(self.user_data.current_user, None)
    self.user_data.set_current_user('test_acct')
    uid = self.user_data.find_user('test_acct')
    self.assertEqual(self.user_data.current_user, uid)

  def test_create_new_user(self):
    self.assertEqual(self.user_data.current_user, None)
    self.user_data.new_user('New Test', 'new_test', testing=True)
    new_id = self.user_data.find_user('new_test')
    self.assertIsNotNone(self.user_data.users[new_id])
    self.assertEqual(self.user_data.users[new_id].full_name, 'New Test')
    self.assertEqual(self.user_data.users[new_id].username, 'new_test')
    self.assertEqual(self.user_data.current_user, new_id)

    #Clean up
    self.user_data.current_user = None

  # class TestUserInterface(unittest.TestCase):

  #   @classmethod
  #   def setUpClass(self):
  #     self.chirp_data = ChirpData('test_chirps.txt')
  #     self.user_data = UserData('test_users.txt')
  #     self.user_interface = UserInterface()

  #   def test_user_must_be_logged_in_to_chirp(self):
  #     self.assertEqual(self.user_data.current_user, None)
  #     self.assertRaises(Exception, self.user_interface.submit_new_chirp())


if __name__ == '__main__':
  unittest.main()
