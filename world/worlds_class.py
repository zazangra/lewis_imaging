"""Let's create our worlds!"""

from world.var.inputs import variables

var_names=[]

def build_var_names():
    """create array of names"""
    for i in variables:
        var_names.append(i.name)

class World():
    """Every world will be an object: two dics e 1 prob"""
    def __init__(self):

        self.members = variables
        self.world = {}
        self.p_world = {}
        self.prob = float
        self.draft_most_similar = []
        self.most_similar = []
        self.prob_ant = float

    def build_world(self, i):
        """Populate a single world with value (see create_worlds)"""

        self.world={var_names[n]: i[n] for n in range(len(self.members))}

    def build_world_prob(self):
        """Multiply all values in p_world"""
        prob = 1
        for k in self.p_world.values():
            prob = prob*k
        self.prob = round(prob, 5)
        return self.prob

    
