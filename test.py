class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self, name, age):
    self.name
    self.age
hippo = Animal("popota", 3)
sloth = Animal("snoopy", 5)
ocelot = Animal("miau", 4)
hippo.description()
print hippo.health, sloth.health, ocelot.health
