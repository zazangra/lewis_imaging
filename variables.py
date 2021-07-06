"""Creating a class for worlds' variables"""
from itertools import product as prod
import numpy as np

class Var():
    """ par is an array of Var' parents (Var themselves); probability is a dic"""

    def __init__(self, name):

        self.name = str(name)
        self.value = int
        self.par = []
        self.prob = {}
        self.getprob = {}

    def build_parname(self):
        """For some reason, we need this to add an array of par names"""

        par_names=[]
        for i in self.par:
            par_names.append(i.name)
        return par_names

    def build_cond_string(self):
        """catch the right string for getting cond prob"""

        par_names = self.build_parname()
        string_cond = str(par_names)+"|"+self.name
        string_cond= string_cond.replace("[","")
        string_cond= string_cond.replace("]","")
        string_cond= string_cond.replace("'","")
        string_cond= string_cond.replace(" ","")
        string_cond= "("+string_cond+")"
        return str(string_cond)

    def build_prob(self):
        """Build probability dictionary """

        if len(self.par) ==0:
            prob_num= float(input('Which is the probability of '+self.name+'? '))
            self.prob["Tprob"]= prob_num
            self.prob["Fprob"]= 1-prob_num
        else:
            par_names = self.build_parname()
            conf = prod([0,1], repeat=len(self.par))
            for i in conf:
                string_one = "Tprob "
                good_i = list(i)
                for j,k in zip(good_i, par_names):
                    string_one += k + "=" + str(j)+" "
                string_one= "'"+string_one+"'"
                string_two = string_one.replace("Tprob ", "")
                string_input="Which is probability of "+self.build_cond_string()+" if "
                self.prob[string_one] = float(input(string_input+string_two+" ?"))
                string_three = "Fprob "+string_two
                self.prob[string_three]= 1-self.prob[string_one]

    def build_getprob(self):
        """Building a dic of probs for better acces by worlds"""
        print(len(self.prob))
        #if len(self.prob)>3:
        par_names = self.build_parname()
        true_dic = {k:v for (k,v) in self.prob.items() if "Tprob" in k}
        print(true_dic)
        conf = prod([0,1], repeat=len(self.par))
        for i,o in zip(conf, true_dic):
            good_n = list(i)
            getprob_key = ""
            for j,k in zip(par_names, good_n):
                getprob_key += j+str(k)
            gprob_key = self.name+'1'+getprob_key
            print('me la luppo e k='+getprob_key)
            self.getprob[gprob_key] = true_dic[o]
        
        false_dic = {k:v for (k,v) in self.prob.items() if "Fprob" in k}
        print(false_dic)
        breakpoint()
        for n,m in zip(conf, false_dic):
            print('Im in the loop')
            good_n = list(n)
            getprob_key = ""
            for x,y in zip(par_names, good_n):
                getprob_key += x+str(y)
            gprob_key = self.name+'0'+getprob_key
            print('me la luppo 2 e k='+getprob_key)
            self.getprob[gprob_key] = false_dic[m]
#       _names = self.build_parname()
#       if len(self.prob)>2:
#            conf = prod([0,1], repeat=len(self.par))
#            for n in self.prob:
#                for i in conf:
#                    good_i = list(i)
#                    print(i)
#                    getprob_key = ""
#                    for j,k in zip(par_names, good_i):
#                        getprob_key += j+str(k)
#                print('looping in'+n+str(self.prob[n]))
#                if "Tprob" in n:
#                    gprob_key = self.name+'1'+getprob_key
#                    self.getprob[gprob_key] = self.prob[n]
#                else:
#                    gprob_key = self.name+'0'+getprob_key
#                    self.getprob[gprob_key] = self.prob[n]
#
    def stampa(self):
        """Debug"""

        return "Object: "+self.name+" "+str(self.value)+" "+str(self.build_parname())
