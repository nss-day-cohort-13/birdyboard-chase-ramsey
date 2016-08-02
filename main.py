class ChirpData:
  """ The 'ChirpData' class holds a dictionary of data
      related to all chirps, retrieved from chirps.txt.
      It also has methods for accessing that data from
      outside.
  """

  def __init__(self, file):
    """ When instantiated, the data saved at chirps.txt (or test_chirps.txt)
        will be loaded into the private variable _all_chirps
        Method arguments
        ================
        file - the file to load chirp data from
    """
    # _all_chirps = [load from chirps.txt / test_chirps.txt]
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

  def new_chirp(self, text, username, private=False, testing=False):
    """ Method for creating a new chirp
        Method arguments
        ================
        text - the text of the chirp
        username - username of the person chirping
        private - set to False as default, creates a public chirp;
                  setting private to True will create a private chirp
    """
    pass


class Chirp:
  """ The 'Chirp' class defines how all basic chirp
      objects will be constructed.
  """

  def __init__(self, text, sender, id):
    """ On init, a chirp will get the following properties:
        text - the actual text of the chirp
        sender - the user who created the chirp
        number - the unique number ID of the chirp
    """
    # self.text = text
    # self.sender = sender
    # self.id = id
    pass


class PrivateChirp(Chirp):
  """ The 'PrivateChirp' class inherits all properties from the
      'Chirp' class and also has extra properties related to
      private chirps.
  """

  def __init__(self, sender, text, id, receiver):
    """ On init, a private chirp will get all the properties of a
        public chirp, plus a 'receiver' property.
    """
    # super().__init__(sender, text, id)
    # self.receiver = receiver
    pass


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
    # self.current_user = None
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


class User:
  """ The 'User' class defines how all user objects
      should be constructed.
  """

  def __init__(self, username, password, id):
    """ On init, user objects will get the following properties:
        username - the unique username of each user profile
        password - the password to access the user's profile
        id - the unique ID number assigned to each user profile
    """
    pass

class UserInterface:
  """ The 'UserInterface' class will handle taking in all user
      input and passing it to the appropriate data class methods
  """

  def __init__(self):
    pass

  def submit_new_chirp(self):
    """ Takes user input and submits it to create a new chirp
        Method arguments: n/a
    """
    pass
