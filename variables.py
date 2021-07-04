"""Creating a class for worlds' variables"""
class Var():
    """ par is an array of Var' parents (Var themselves); probability is a dic"""

    def __init__(self, name):

        self.name = name
        self.value = bool
        self.par = []
        self.prob = {}

    def build_prob(self):
        """Build probability dictionary """

        if len(self.par) ==0:
            prob_num= float(input('Which is the probability of '+self.name+'? '))
            self.prob["Tprob"]= prob_num
            self.prob["Fprob"]= 1-prob_num
        else:
            self.prob = { #this is going to be huge
           }

    def stampa(self):
        """Debug"""
        par_names=[]
        for i in self.par:
            par_names.append(str(i.name))
        return "Object: "+str(self.name)+" "+str(self.value)+" "+str(par_names)+" "
