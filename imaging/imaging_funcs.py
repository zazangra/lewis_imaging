"""We will select worlds in which a given formula happens"""
from world.create_worlds import universe
from world.var.var_class import re
import ast

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

def build_sim(i):
    """Build most similar worlds of n_ant_worlds"""
    sim_num = int(input('How many most similar worls have '+str(i.world)+'? '))
    for _ in range(sim_num):
        i.most_similar.append(ast.literal_eval(input('Most similar world to '+str(i.world)+' is: ')))

def similarity_functions():
    for i in n_ant_worlds:
        build_sim(i)
    for j in ant_worlds:
        j.most_similar.append(j.world)

