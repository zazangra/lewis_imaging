"""Defining input for building vars"""
from world.var.var_class import Var

variables = []

def create_var():
    """Creating Var obj from inputs"""
    var_num = int(input('How many variables do you need? '))
    print('Tell me your vars')
    for _ in range(var_num):
        variables.append(Var(input('Enter var name: ')))
    print('Your var set:',[n.name for n in variables])

def build_par(i):
    """Build parents of caused Var"""
    par_num = int(input('How many parents have '+i.name+'? '))
    for _ in range(par_num):
        i.par.append(Var(input('Parent of '+i.name+' is: ')))

def create_par():
    """Putting Var' parents in self.parents"""
    for i in variables:
        is_exo = input('Does '+str(i.name)+' have parents?[y/n] ')
        if is_exo =='y':
            build_par(i)
        elif is_exo == 'n':
            i.par = []
        else:
            print('Incorret Option')
