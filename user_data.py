import pickle
import uuid
from user import *

class UserData:
  """ The 'UserData' class holds the list of users retrieved from users.txt
      (or test_users.txt) and opens methods for accessing user data. Also
      includes a current user property that is set to the appropriate user
      object after successful login.
  """

  def __init__(self, file):
    """ Creates a variable called users, loaded from a list
        of users stored in the serialized text file, users.txt
        Method arguments
        ================
        file - the file to load user data from, saved at self.user_file
    """
    self.user_file = file
    self.users = self.load_user_list()
    self.current_user = None

  def load_user_list(self):
    """ Handles loading the serialized list of user data
        and storing it in self.users
        Method arguments: n/a
    """
    try:
      with open(self.user_file, 'rb') as f:
        return pickle.load(f)
    except EOFError:
      return dict()

  def write_user_list(self):
    """ Handles serializing user data and writing it to
        user.txt
        Method arguments: n/a
    """
    with open(self.user_file, 'wb') as f:
      pickle.dump(self.users, f)

  def new_user(self, full_name, username, testing=False):
    """ Creates a new user object from user input, and sets
        new user as current user
        Method arguments
        ================
        full_name - the user's full name
        username - new unique username chosen by user
    """
    new = User(full_name, username)
    uid = uuid.uuid4()
    self.users[uid] = new
    self.set_current_user(username)
    if testing == False:
      self.write_user_list()
    else:
      pass

  def find_user(self, username):
    """ Returns uid if a user object is found in self.users
        that matches the username passed in. Returns None if not found.
        Method arguments
        ================
        username - username associated with the user object being searched for
    """
    user = None
    for uid, profile in self.users.items():
      if profile.username == username:
        user = uid
    return user

  def set_current_user(self, username):
    """ Searches for user object matching the username, and
        when found, sets that user object as the current user.
        Method arguments
        ================
        username - the username of the profile being searched for
    """
    current = self.find_user(username)
    self.current_user = current
