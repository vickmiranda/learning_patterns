"""
Just an example of the hollywood principle and template method
Notice that there is a hook on the template that is only called
by the higher component

"""

class Actor(object) :
  def __init__(self, name):
    self.name = name

  def you_got_the_part(self):
    print self.name, " you got the part"

  def perform(self):
    print self.name, " performs audition"


applicants = []
def audition(actor):
    actor.perform()
    applicants.append(actor)

def cast():
    import random
    selection = random.choice(applicants)
    selection.you_got_the_part()

alice = Actor("alice")
bob = Actor("bob")
carol = Actor("carol")
dave = Actor("dave")

audition(alice)
audition(bob)
audition(carol)
audition(dave)

cast()