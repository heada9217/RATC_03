import math

#test data

opp = 3
hyp = 5 
angle = 36.87

adjacent_pythag = math.sqrt (hyp ** 2 - opp ** 2)

print("Adjacent using pythagoras: {}".format (adjacent_pythag))

radians_degrees = (math.tan(36.87 * (math.pi /180))) 

adjacent_trig =  opp / radians_degrees

print("Adjacent using trigonometry: {}".format(adjacent_trig))






#radians -> degrees is (radians) * (math.pi / 100)

def pythag(hyp,opp,adj):
    if hyp == "":
        hyp = math.sqrt(adj ** 2 + opp ** 2)
        return hyp

    if opp == "":
        opp = math.sqrt(hyp ** 2 - adj **2)
        return opp

    if adj == "":
        adj = math.sqrt(hyp ** 2 - opp ** 2)
        return adj


def sides_trig(hyp,opp,adj,angle):

    hyp_row = ["Hypotenuse"]
    opp_row = ["Opposite"]
    adj_row = ["Adjacent"]

    calculated_sides = []



    if hyp != "":
        opp = math.sin(angle * (math.pi / 100)) * hyp
        opp_row.append(opp)
        adj = math.cos(angle) * (math.pi/100) * hyp
        adj_row.append(adj)
        
        calculated_sides.append(opp_row)
        calculated_sides.append(adj_row)

        return calculated_sides

    if opp != "":
        adj = opp / math.tan(angle * (math.pi / 180))
        adj_row.append(adj)
        hyp = opp / math.sin(angle * (math.pi / 180))
        hyp_row.append(hyp)

        calculated_sides.append(adj_row)
        calculated_sides.append(hyp_row)

        return calculated_sides

    if adj != "":
        opp = math.tan(angle * (math.pi / 180)) * adj
        opp_row.append(opp)
        hyp = adj / math.cos(angle * (math.pi / 180))
        hyp_row.append(hyp)

        calculated_sides.append(opp_row)
        calculated_sides.append(hyp_row)

        return calculated_sides


def angles(hyp, opp):
    calculated_angles = []
    
    angle_1 = math.asin(opp / hyp)
    angle_1_deg = angle_1 * (180 / math.pi)

    angle_2_deg = 90 - angle_1_deg
    
    angle_3_deg = 90

    calculated_angles.append(angle_1_deg)
    calculated_angles.append(angle_2_deg)
    calculated_angles.append(angle_3_deg)

    return calculated_angles

    
    
