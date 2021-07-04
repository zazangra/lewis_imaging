#Attempt to separate files; trying to build possible words

from itertools import product as pro
import numpy as np
variables=[]


def world_builder():

    num_var = int(input('How many variables do you need? '))
    print('Tell me your vars')
    for i in range(num_var):
        variables.append(input('Enter var name: '))
    # Construct the product
    print('Here your var set:', variables)
    print('Here your var combinations for values 0,1:')
    worlds= list(pro([0,1], repeat=num_var))
    
    #print
    print(worlds)
    return worlds


