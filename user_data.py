from user import *

class UserData:
  """ The 'UserData' class holds the list of users retrieved from users.txt
      (or test_users.txt) and opens methods for accessing user data. Also
      includes a current user property that is set to the appropriate user
      object after successful login.
      Method arguments
      ================
      file - the file to load user data from
  """

  def __init__(self, file):
    """ Creates a variable called users, loaded from a list
        of users stored in the serialized text file, users.txt
    """
    # _users = [load from users.txt / test_users.txt]
    self.users = None
    self.current_user = None
    pass

  def load_user_list(self):
    """ Handles loading the serialized list of user data
        and storing it in self.users
        Method arguments: n/a
    """
    pass

  def write_user_list(self):
    """ Handles serializing user data and writing it to
        user.txt
        Method arguments: n/a
    """
    pass

  def new_user(self, full_name, username, testing=False):
    """ Creates a new user object from user input, and sets
        new user as current user
        Method arguments
        ================
        full_name - the user's full name
        username - new unique username chosen by user
    """
    pass

  def find_user(self, username):
    """ Returns True/False if a user object is found in self.users
        that matches the search argument passed in
        Method arguments
        ================
        username - username associated with the user object being searched for
    """
    pass

  def set_current_user(self, username):
    """ Searches for user object matching the username, and
        when found, sets that user object as the current user.
        Method arguments
        ================
        username - the username of the profile being searched for
    """
    pass
