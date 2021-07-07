"""Creating a class for worlds' variables"""
from itertools import product as prod
import re

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

    def build_get_prob(self, string_two, t_key, f_key):
        """Add dictionary of conf to getprob"""

        string_gprob = re.sub("'", "", string_two)
        string_gprob = re.sub("=", " ", string_gprob )
        string_gprob = re.sub("Tprob", " ", string_gprob)
        sg_s = string_gprob.split()
        sg_s.append(self.name)
        sg_s.append(1)
        sg_p = []
        for i, num in enumerate(sg_s):
            if i%2:
                num = int(num)
                sg_p.append(num)
            else:
                sg_p.append(num)
        self.getprob[t_key] = {sg_p[m]: sg_p[m+1] for m in range(0, len(sg_p), 2)}
        sg_p.pop()
        sg_p.append(0)
        self.getprob[f_key] = {sg_p[m]: sg_p[m+1] for m in range(0, len(sg_p), 2)}

    def build_prob(self):
        """Build probability dictionary and call for getprob dic"""

        if len(self.par) ==0:
            prob_num= round(float(input('Which is the probability of '+self.name+'? ')),5)
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
                self.prob[string_one] = round(float(input(string_input+string_two+" ?")), 5)
                t_key = self.prob[string_one]
                f_key = 1-self.prob[string_one]
                string_three = "Fprob "+string_two
                self.prob[string_three]= 1-self.prob[string_one]
                string_one = re.sub("'", "", string_one)
                string_one = re.sub("=", " ", string_one )
                self.build_get_prob(string_two, t_key, f_key)

    def stampa(self):
        """Debug"""

        return "Object: "+self.name+" "+str(self.value)+" "+str(self.build_parname())
