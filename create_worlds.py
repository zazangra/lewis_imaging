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

def prob_get():
    """Get probabilities of each member of universe"""
    for i in universe:
        for j in i.members:
            value = j.name
#            print('eccomi')
#            print(value)
            for n in j.getprob:
#                print(n)
                res = list(n)
                res_one = {res[m]: res[m+1] for m in range(0, len(res),2)}
#                print('qua')
#                print(res_one)
                if all(s in i.world.items() for s in res_one.items()):
                    i.p_world[value] = j.getprob[n]
