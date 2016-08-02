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
