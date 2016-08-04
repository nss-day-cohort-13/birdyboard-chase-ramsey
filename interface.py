from chirp_data import *
from user_data import *

class UserInterface:
  """ The 'UserInterface' class will handle taking in all user
      input and passing it to the appropriate data class methods
  """

  def __init__(self, chirp_file, user_file):
    """ On init, this class will get instances of ChripData and
        UserData to run the program
    """
    self.chirp_data = ChirpData(chirp_file)
    self.user_data = UserData(user_file)

  def check_sign_in(self):
    """ Checks to make sure a there is a current user;
        returns True or False
        Method arguments: n/a
    """
    if self.user_data.current_user == None:
      print('You have to be signed in to do that. Sign in as an existing user or create a new user from the main menu.\n')
      return False
    else:
      return True

  # @check_sign_in
  def submit_new_chirp(self):
    """ Takes user input and submits it to create a new chirp
        Method arguments: n/a
    """
    login = self.check_sign_in()
    if login == False:
      return
    else:
      print('Got past sign in.')
