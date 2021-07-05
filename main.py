"""Main py"""
from inputs import create_var, create_par, variables

create_var()
create_par()

for i in variables:
    i.build_prob()
    print(i.stampa())
    print(i.prob)
