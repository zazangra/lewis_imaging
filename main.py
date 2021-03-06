"""Main py"""

from world.var.inputs import create_var, create_par, variables
from world.create_worlds import universe, world_creator, prob_get
from world.worlds_class import build_var_names
from imaging.imaging_funcs import final_prob, final_valuations, imaging, valuations, ant_worlds, n_ant_worlds, similarity_functions, con_probs

create_var()
create_par()


for i in variables:
    i.build_prob()
    print(i.prob)
    print(i.getprob)


build_var_names()
world_creator()
prob_get()
for i in universe:
    print(i.world)
    i.build_world_prob()
    print(i.p_world)
    print(i.prob)

valuations()
print('this is antworlds')
for i in ant_worlds:
    print(i.world)
print('this is nantworlds')
for i in n_ant_worlds:
    print(i.world)

similarity_functions()
for i in n_ant_worlds:
    print(i.draft_most_similar)
for j in ant_worlds:
    print(j.draft_most_similar)

imaging()
for i in universe:
    print(i.prob_ant)

final_valuations()
final_prob()
print(sum(con_probs))
