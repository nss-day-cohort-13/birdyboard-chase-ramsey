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
    self.menu_data = self.read_menu()

  def read_menu(self):
    menu_list = list()
    with open('menu.txt', 'r') as menu:
      for item in menu:
        menu_list.append(item)
    return menu_list

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

  def sign_in_user(self):
    if len(self.user_data.users) == 0:
      print('There are no users just yet. Be the first! Select "New user" from the main menu.')
    else:
      i = 0
      for uid, user in self.user_data.users:
        i += 1
        print('{0}. {1}'.format(i, user.username))

  # @check_sign_in
  def submit_new_chirp(self):
    """ Takes user input and submits it to create a new chirp
        Method arguments: n/a
    """
    login = self.check_sign_in()
    if login == False:
      return
    else:
      print('What would you like to say?')
      text = input('> ')
      self.chirp_data.new_chirp(test, self.user_data.current_user)

  def show_menu(self):
    """ Shows the main user interface that initiates all of the
        program's functionality
        Method arguments: n/a
    """
    print('Welcome to Birdyboard!')
    print('Make a selection from the menu below')
    print('\n')
    for item in self.menu_data:
      i = self.menu_data.index(item) + 1
      print('{0}. {1}'.format(i, item[:-1]))
    print('\n')
    choice = input('> ')

    if choice == '1':
      self.sign_in_user()
