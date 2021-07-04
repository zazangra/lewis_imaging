import lewis_func
import numpy as np
from lewis_func import variables

exo_var=[]
caused_var=[]
gen_var=[]

def genetic_finder():
    exo_num=int(input('How many exo-variables do you need? '))
    print('Which are the exogenous vars?')

    for i in range(exo_num):
        exo_var.append(input('Enter var name: '))
    
    caused_var= np.setdiff1d(variables, exo_var)
    for i in caused_var:
        gen_num=int(input('How many parents have '+i+' ?'))
        var_ar=[]
        for j in range(gen_num):
            var_ar.append(input('Par of '+i+' is: '))
        gen_var.append(var_ar)
    print(gen_var)
    return gen_var 


