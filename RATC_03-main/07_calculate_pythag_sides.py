import math
from optparse import OptParseError

def pythag(hyp,opp,adj):

    calculated_side = []

    if hyp == "":
        calculated_side.append("Hypotenuse")
        hyp = math.sqrt(adj ** 2 + opp ** 2)
        calculated_side.append(hyp)
        

    if opp == "":
        calculated_side.append("Opposite")
        opp = math.sqrt(hyp ** 2 - adj **2)
        calculated_side.append(opp)
        

    if adj == "":
        calculated_side.append("Adjacent")
        adj = math.sqrt(hyp ** 2 - opp ** 2)
        calculated_side.append(adj)
        
    return calculated_side
    
#main 

hyp = 5
opp = 4
adj = ""

calculate_sides = pythag(hyp,opp,adj)

print(calculate_sides)

#Working