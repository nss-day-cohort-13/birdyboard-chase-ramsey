import pickle
from chirps import *

class ChirpData:
  """ The 'ChirpData' class holds a dictionary of data
      related to all chirps, retrieved from chirps.txt.
      It also has methods for accessing that data from
      outside.
  """

  def __init__(self, file):
    """ When instantiated, the data saved at chirps.txt (or test_chirps.txt)
        will be loaded into the variable all_chirps
        Method arguments
        ================
        file - the file to load chirp data from
    """
    self.chirp_file = file
    self.all_chirps = self.load_chirps()

  def load_chirps(self):
    """ Handles loading self.all_chirps data from the
        chrips.txt file.
        Method arguments: n/a
    """
    try:
      with open(self.chirp_file, 'rb') as f:
        return pickle.load(f)
    except EOFError:
      return dict()

  def write_chirps(self):
    """ Handles writing any changes to self.all_chirps data
        to the chirps.txt file.
        Method arguments: n/a
    """
    with open(self.chirp_file, 'wb') as f:
      pickle.dump(self.all_chirps, f)

  def get_public(self):
    """ Returns all public tweets
        Method arguments: n/a
    """
    public = list()
    for chirp_id, chirp in self.all_chirps.items():
      if chirp.private == False:
        public.append(chirp)
    return public

  def get_private(self, user_id):
    """ Returns private tweets matching the username
        provided as argument
        Method arguments
        ================
        username - the username to look for in the 'sent'
                   and 'received' categories of private chirps
    """
    private = list()
    for chirp_id, chirp in self.all_chirps.items():
      if chirp.private == True:
        if chirp.receiver_id == user_id:
          private.append(chirp)
        elif chirp.sender_id == user_id:
          private.append(chirp)
        else:
          pass
    return private

  def new_chirp(self, text, sender_id, private=False, receiver_id=None, testing=False):
    """ Method for creating a new chirp
        Method arguments
        ================
        text - the text of the chirp
        sender_id - user ID of the person chirping
        private - set to False as default, creates a public chirp;
                  setting private to True will create a private chirp
        receiver_id - user ID of the receiver (if private)
        testing - only set to true during testing
    """
    if private == False:
      new = Chirp(text, sender_id)
      self.all_chirps[len(self.all_chirps)] = new
    elif private == True:
      new = PrivateChirp(text, sender_id, receiver_id)
      self.all_chirps[len(self.all_chirps)] = new
    else:
      pass
    if testing == False:
      self.write_chirps()
    else:
      pass
