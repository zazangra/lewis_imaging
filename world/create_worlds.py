"""Let us build all the worlds"""
from world.worlds_class import World, var_names
from world.var.var_class import prod

universe=[]

def world_creator():
    """Create all the worlds"""
    conf= list(prod([0,1], repeat=len(var_names)))
    for i in conf:
        i = list(i)
        world = World()
        world.build_world(i)
        universe.append(world)

def prob_get():
    """Get probabilities of each member of universe"""
    for i in universe:
        for j in i.members:
            value = j.name
            for k in j.getprob:
                res = list(k)
                res_one = {res[m]: res[m+1] for m in range(0, len(res),2)}
                if all(s in i.world.items() for s in res_one.items()):
                    i.p_world[value] = j.getprob[k]
