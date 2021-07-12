"""Main py"""

from inputs import create_var, create_par, variables
from create_worlds import universe, world_creator, prob_get
from worlds import build_var_names

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

