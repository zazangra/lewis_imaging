"""Let's create our worlds!"""

from inputs import variables

var_names=[]

def build_var_names():
    """create array of names"""
    for i in variables:
        var_names.append(i.name)

class World():
    """Every world will be an object: two dics e 1 prob"""
    def __init__(self):

        self.members = var_names
        self.world = {}
        self.p_world = {}
        self.prob = float

    def build_world(self, i):
        """Populate a single world with value (see create_worlds)"""

        self.world={self.members[n]: i[n] for n in range(len(self.members))}

    def buil_world_prob(self):
        """Multiply all values in p_world"""
        prob = 1
        for i in self.p_world:
            prob = prob*self.p_world[i]
        self.prob = prob
        return self.prob
