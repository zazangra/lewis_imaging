"""Main py"""

from inputs import create_var, create_par, variables
from create_worlds import universe, world_creator
from worlds import build_var_names

create_var()
create_par()

build_var_names()
world_creator()
for i in universe:
    print(i.world)

for i in variables:
    i.build_prob()
    print(i.stampa())
    print(i.prob)
