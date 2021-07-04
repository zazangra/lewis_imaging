"""Main py"""
from inputs import create_var, create_par, variables

create_var()
create_par()

for i in variables:
    if len(i.par) == 0:
        i.build_prob()
    print(i.stampa())
    print(i.prob)
