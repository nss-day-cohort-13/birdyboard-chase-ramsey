class User:
  """ The 'User' class defines how all user objects
      should be constructed.
  """

  def __init__(self, full_name, username):
    """ On init, user objects will get the following properties:
        full_name - the user's full name
        username - the unique username of each user profile
    """
    self.full_name = full_name
    self.username = username
