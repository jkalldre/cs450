class Movie:

   def __init__(self, title = "", year = 0, runtime = 0):
      self.title = title
      self.year = year
      self.runtime = 0 if (runtime < 0) else runtime

   def __repr__(self):
      return "{} ({}) - {} mins".format(self.title, self.year, self.runtime)

   def getRuntime(self):
      hrs = int(self.runtime / 60)
      min = int(self.runtime % 60)
      return hrs, min
