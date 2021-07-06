"""Let us build all the worlds"""
from worlds import World, var_names
from variables import prod

universe=[]

def world_creator():
    """Create all the worlds"""
    conf= list(prod([0,1], repeat=len(var_names)))
    for i in conf:
        i = list(i)
        world = World()
        world.build_world(i)
        universe.append(world)

#def prob_get():
#    """Get probabilities of each member of universe"""
#    for i in universe:
#        for j in i.members:
#            for n in j.getprob:
