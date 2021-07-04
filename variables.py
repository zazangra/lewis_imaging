"""Creating a class for worlds' variables"""
class Var():

    def __init__(self, name):

        self.name = str(name)
        self.value = bool
        self.par = []
        self.prob = float
#        self.probability = probability

#    def buildProb(self):
#        if len(self.genitors) ==0:
#            pass
#        else:
#            self.probability = {
#           }
    def stampa(self):
        """Debug"""
        par_names=[]
        for i in self.par:
            par_names.append(i.name)
        return "Object: "+str(self.name)+" "+str(self.value)+" "+str(par_names)+" "+str(self.prob)
