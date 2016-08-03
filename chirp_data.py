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
    # self.all_chirps = [load from chirps.txt / test_chirps.txt]
    pass

  def load_chirps(self):
    """ Handles loading _all_chirps data from the
        chrips.txt file.
        Method arguments: n/a
    """
    pass

  def write_chirps(self):
    """ Handles writing any changes to self.all_chirps data
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
    pass
