class Chirp:
  """ The 'Chirp' class defines how all basic chirp
      objects will be constructed.
  """

  def __init__(self, text, sender_id):
    """ On init, a chirp will get the following properties:
        text - the actual text of the chirp
        sender_id - the user ID of the person who created the chirp
        private - set to False or True, noting whether a chirp is
                  public or private (public by default)
    """
    self.text = text
    self.sender_id = sender_id
    self.private = False

class PrivateChirp(Chirp):
  """ The 'PrivateChirp' class inherits all properties from the
      'Chirp' class and also has extra properties related to
      private chirps.
  """

  def __init__(self, text, sender_id, receiver_id):
    """ On init, a private chirp will get all the properties of a
        public chirp, plus a 'receiver' property.
    """
    super().__init__(text, sender_id)
    self.private = True
    self.receiver_id = receiver_id
