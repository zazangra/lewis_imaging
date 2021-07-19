"""We will select worlds in which a given formula happens"""
from world.create_worlds import universe
from world.var.var_class import re
import ast

#maybe import from main is safer?

n_ant_worlds=[]
ant_worlds=[]
con_worlds=[]
n_con_worlds=[]
con_probs=[]


def valuations():
    formula_instring= input_to_formula()
    for i in universe:
        if eval(formula_instring):
            ant_worlds.append(i)
        else:
            n_ant_worlds.append(i)
    return ant_worlds, n_ant_worlds

def input_to_formula():
    """Transforming the input to correct formula string"""
    pattern_instring='[\s\S](?==)[\s\S](?<==)[\s\S]'
    string_formula= input('Tell me the antecedent of your counterfactual: ')
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
        i.draft_most_similar.append(ast.literal_eval(input('Most similar world to '+str(i.world)+' is: ')))



def similarity_functions():
    for i in n_ant_worlds:
        build_sim(i)
    for j in ant_worlds:
        j.draft_most_similar.append(j.world)
    for w in universe:
        for v in universe:
            if v.world in w.draft_most_similar:
                w.most_similar.append(v)

def prob_sim_sphere(i, j):
    denom=[]
    for v in j.most_similar:
        denom.append(v.prob)
    return i.prob/sum(denom)



def imaging():
    for w in ant_worlds:
        w.prob_ant=w.prob
    for w in n_ant_worlds:
        w.prob_ant=0
    for w in ant_worlds:
        for v in n_ant_worlds:
            if w in v.most_similar:
                w.prob_ant=w.prob_ant+(v.prob*prob_sim_sphere(w, v))
            else:
                w.prob_ant=w.prob_ant+0

def final_input_to_formula():
    """Transforming the input to correct formula string"""
    pattern_instring='[\s\S](?==)[\s\S](?<==)[\s\S]'
    string_formula= input('Tell me the consequent of your counterfactual: ')
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

def final_valuations():
    formula_instring= final_input_to_formula()
    for i in universe:
        if eval(formula_instring):
            con_worlds.append(i)
        else:
            n_con_worlds.append(i)
    return con_worlds, n_con_worlds

def final_prob():
    for w in con_worlds:
        con_probs.append(w.prob_ant)
    return(sum(con_probs))

   
