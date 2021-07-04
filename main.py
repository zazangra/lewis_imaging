"""Main py"""
from inputs import create_var, create_par, variables

create_var()
create_par()

for i in variables:
    print(i.stampa())
