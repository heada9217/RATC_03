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