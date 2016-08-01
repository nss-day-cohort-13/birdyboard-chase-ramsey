class ChirpData:
  """ The 'ChirpData' class holds a dictionary of data
      related to all chirps, retrieved from chirps.txt.
      It also has methods for accessing that data from
      outside.
  """

  def __init__(self):
    # _all_chirps = [load from chirps.txt]
    pass

  def load_chirps(self):
    """ Handles loading _all_chirps data from the
        chrips.txt file.
        Method arguments: n/a
    """
    pass

  def write_chirps(self):
    """ Handles writing any changes to _all_chirps data
        to the chirps.txt file.
        Method arguments: n/a
    """
    pass

  def get_public(self):
    """ Returns all public tweets
        Method arguments: n/a
    """
    pass

  def get_private(self, username):
    """ Returns private tweets matching the username
        provided as argument
        Method arguments
        ================
        username - the username to look for in the 'sent'
                   and 'received' categories of private chirps
    """
    pass

  def create_new(self, private=False):
    """ Method for creating a new chirp
        Method arguments
        ================
        private - set to False as default, creates a public chirp;
                  setting private to True will create a private chirp
    """
    pass


class Chirp:
  """ The 'Chirp' class defines how all basic chirp
      objects will be constructed.
  """

  def __init__(self):
    pass


class PrivateChirp(Chirp):
  """ The 'PrivateChirp' class inherits all properties from the
      'Chirp' class and also has extra properties related to
      private chirps.
  """

  def __init__(self):
    pass


class UserData:
  """ The 'UserData' class holds the list of users retrieved
      from user.txt and opens methods for accessing user data
  """

  def __init__(self):
    """ Creates a private variable called _users, loaded from a list
        of users stored in the serialized text file, users.txt
    """
    # _users = [load from users.txt]
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

  def new_user(self):
    """ Creates a new user object from user input
        Method arguments: n/a
    """
    pass

  def find_user(self, *args):
    """ Returns True/False if a user object is found in self.users
        that matches the search arguments passed in
        Method arguments
        ================
        search - username associated with the user object being searched for
        password - password associated with the user object being searched for
    """
    pass


class User:
  """ The 'User' class defines how all user objects
      should be constructed.
  """

  def __init__(self):
    pass
