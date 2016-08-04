from chirp_data import *
from user_data import *

class UserInterface:
  """ The 'UserInterface' class will handle taking in all user
      input and passing it to the appropriate data class methods
  """

  def __init__(self, chirp_file, user_file):
    """ On init, this class will get instances of ChirpData and
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
      print('')
      for uid, user in self.user_data.users.items():
        print(user.username)
      print('')
      print('Who are you?')
      user = input('> ')
      self.user_data.set_current_user(user)
      print('')

  def create_new_user(self):
    print('')
    print('What is your name?')
    full_name = input ('> ')
    print('What would you like your username to be?')
    username = input('> ')
    self.user_data.new_user(full_name, username)
    print('')

  def submit_new_public_chirp(self):
    """ Takes user input and submits it to create a new public chirp
        Method arguments: n/a
    """
    login = self.check_sign_in()
    if login == False:
      return
    else:
      print('What would you like to say?')
      text = input('> ')
      self.chirp_data.new_chirp(text, self.user_data.current_user)

  def submit_new_private_chirp(self):
    """ Takes user input and submits it to create a new private chirp
        Method arguments: n/a
    """
    login = self.check_sign_in()
    if login == False:
      return
    else:
      print('Who are you sending this chirp to?')
      receiver = input('> ')
      print('What would you like to say?')
      text = input('> ')
      receiver_id = self.user_data.find_user(receiver)
      self.chirp_data.new_chirp(text, self.user_data.current_user, private=True, receiver_id=receiver_id)

  def view_all_chirps(self):
    public = self.chirp_data.get_public()
    private = self.chirp_data.get_private(self.user_data.current_user)

    print('')
    print('##### Public Chirps #####')
    print('')
    if len(public) == 0:
      print('No public chirps yet')
    else:
      for chirp in public:
        username = self.user_data.users[chirp.sender_id].username
        i = public.index(chirp) + 1
        print('{0}. {1}: {2}'.format(i, username, chirp.text))
    print('')

    print('')
    print('##### Private Chirps #####')
    if len(private) == 0:
      print('No private chirps yet')
    else:
      for chirp in private:
        your_username = self.user_data.users[chirp.sender_id].username
        their_username = self.user_data.users[chirp.receiver_id].username
        i = private.index(chirp) + 1
        print('{0}. {1}: {2}  (sent to {3})'.format(i, your_username, chirp.text, their_username))
      print('')
    print('')

    print('Enter "public / private" plus the number of a chirp to reply (i.e. "public 2"), or type "back" to go back to the main menu.')

    choice = input('> ')
    if choice.lower() == 'back':
      self.show_menu()
    else:
      choice = choice.split(' ')
      num = int(choice[1]) - 1
      if choice[0].lower() == 'public':
        print(public[num].text)
      elif choice[0].lower() == 'private':
        print(private[num].text)

  def show_menu(self):
    """ Shows the main user interface that initiates all of the
        program's functionality
        Method arguments: n/a
    """
    if self.user_data.current_user == None:
      print('Welcome to Birdyboard!')
      print('Make a selection from the menu below')
    else:
      first_name = self.user_data.users[self.user_data.current_user].full_name.split(' ')
      first_name = first_name[:1]
      username = self.user_data.users[self.user_data.current_user].username
      print('Hi {0}! You\'re signed in as {1}'.format(first_name[0], username))
    print('\n')
    for item in self.menu_data:
      i = self.menu_data.index(item) + 1
      print('{0}. {1}'.format(i, item[:-1]))
    print('\n')
    choice = input('> ')

    if choice != '6':

      if choice == '1':
        self.sign_in_user()

      elif choice == '2':
        self.create_new_user()

      elif choice == '3':
        self.view_all_chirps()

      elif choice == '4':
        self.submit_new_public_chirp()

      elif choice == '5':
        self.submit_new_private_chirp()

      self.show_menu()

    elif choice == '6':
      print('Are you sure you want to leave? [ y / n ]')
      choice = input('> ')
      if choice.lower() == 'y':
        quit()
      else:
        self.show_menu()
