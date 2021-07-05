"""Creating a class for worlds' variables"""
from itertools import product as prod

class Var():
    """ par is an array of Var' parents (Var themselves); probability is a dic"""

    def __init__(self, name):

        self.name = str(name)
        self.value = bool
        self.par = []
        self.prob = {}

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

    def stampa(self):
        """Debug"""
        return "Object: "+self.name+" "+str(self.value)+" "+str(self.build_parname())
