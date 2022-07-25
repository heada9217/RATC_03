import math

def sides_trig(hyp,opp,adj,angle):

    hyp_row = ["Hypotenuse"]
    opp_row = ["Opposite"]
    adj_row = ["Adjacent"]

    calculated_sides = []



    if hyp != []:
        opp = math.sin(angle * (math.pi / 180)) * hyp
        opp_row.append(opp)
        adj = math.cos(angle * (math.pi/180)) * hyp
        adj_row.append(adj)
        
        calculated_sides.append(opp_row)
        calculated_sides.append(adj_row)
        
        return calculated_sides

    if opp != []:
        adj = opp / math.tan(angle * (math.pi / 180))
        adj_row.append(adj)
        hyp = opp / math.sin(angle * (math.pi / 180))
        hyp_row.append(hyp)

        calculated_sides.append(adj_row)
        calculated_sides.append(hyp_row)

        return calculated_sides

    if adj != []:
        opp = adj / (math.tan(angle * (math.pi / 180)))
        opp_row.append(opp)
        hyp = adj / (math.sin(angle * (math.pi / 180)))
        hyp_row.append(hyp)

        calculated_sides.append(opp_row)
        calculated_sides.append(hyp_row)

        return calculated_sides
    
opp = 4 
angle = 53.13
hyp = []
adj = []

calculate_sides = sides_trig(hyp,opp,adj,angle)

print(calculate_sides)

#Working