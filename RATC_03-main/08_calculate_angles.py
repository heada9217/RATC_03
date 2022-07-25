import math
import pandas

def angles(hyp, opp):
    calculated_angles = []
    #calculate first angle using trig
    angle_1 = math.asin(opp / hyp)
    angle_1 = angle_1 * (180 / math.pi)

    #second angle is found 
    angle_2 = 90 - angle_1
    #third angle is always 90
    angle_3 = 90
    
    #add angles to list
    calculated_angles.append(angle_1)
    calculated_angles.append(angle_2)
    calculated_angles.append(angle_3)

    return calculated_angles

#Main

angle_1 = []
angle_2 = []
angle_3 = []

angles_data_dict = {
    "Opposite angle:": angle_1,
    "Adjacent angle:": angle_2,
    "Hypotenuse angle:": angle_3    
}

angle_headings = ["Opposite angle:", "Adjacent angle:", "Hypotenuse angle:"]

angle_data = []

angle_dict = {
    "Angle": angle_headings,
    "Degrees": angle_data
    
}


hyp = 5 
opp = 4 

calculate_angles = angles(hyp,opp)

for item in calculate_angles:
    angle_data.append(item)
    
calculated_angle_info_frame = pandas.DataFrame(angle_dict)
calculated_sides_info_frame = calculated_angle_info_frame.set_index("Angle")

pandas.set_option('display.max_columns', None)

#print angles frame
print("*** Full angles information ***")
print(calculated_angle_info_frame)