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
    """ Creates a private variable called _users, loaded from a list
        of users stored in the serialized text file, users.txt
    """
    # _users = [load from users.txt / test_users.txt]
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

  def get_users(self):
    """ Returns the private list of user data, stored as _users
        Method arguments: n/a
    """
    pass

  def new_user(self, username, password, testing=False):
    """ Creates a new user object from user input, and sets
        new user as current user
        Method arguments
        ================
        username - new unique username chosen by user
        password - password chosen by user to access profile
    """
    pass

  def find_user(self, *args):
    """ Returns True/False if a user object is found in self.users
        that matches the search arguments passed in
        Method arguments
        ================
        Note: find_user looks up username if only one argument, username and
              password if two arguments
        username - username associated with the user object being searched for
        password - password associated with the user object being searched for
    """
    pass

  def set_current_user(self, username, password):
    """ Searches for user object matching the username and password, and
        when found, sets that user object as the current user.
        Method arguments
        ================
        username - the username of the profile being searched for
        passwoard - the password associated with the user profile
    """
    pass
