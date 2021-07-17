"""We will select worlds in which a given formula happens"""
from world.create_worlds import universe
from world.var.var_class import re

#maybe import from main is safer?

n_ant_worlds=[]
ant_worlds=[]


def valuations():
    formula_instring= input_to_formula()
    for i in universe:
        if eval(formula_instring):
            ant_worlds.append(i)
        else:
            n_ant_worlds.append(i)
    return ant_worlds

def input_to_formula():
    """Transforming the input to correct formula string"""
    pattern_instring='[\s\S](?==)[\s\S](?<==)[\s\S]'
    string_formula= input('Tell me parents configuration of your counterfactual: ')
    repla= re.findall(pattern_instring, string_formula)
    print('this is repla') 
    print(repla)
    for k in repla:
        print('this is k')
        print(k)
        print('this is replacement')
        replacement='i.world[\''+k[0]+'\']=='+k[2]
        print(replacement)
        string_formula = string_formula.replace(k, replacement)
    return string_formula

