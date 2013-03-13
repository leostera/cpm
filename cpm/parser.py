import tomlpython

class Parser(object):
  """Parse a package.toml file and prepare the apropiate structures"""

  def __init__(self, arg):
    super(Parser, self).__init__()
    self.arg = arg

  def load(self, filename):
    with open(filename) as datafile:
      self.raw = tomlpython.parse(datafile)
    return
    