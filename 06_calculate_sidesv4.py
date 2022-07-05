import math
import pandas
import numpy

def yes_no(question):

    yes_no_answers = ["yes", "no","y","n"]

    valid = False 
    while not valid:

        response = input(question).lower().strip()

        for var_item in yes_no_answers:
            if response == var_item:
                return response
            elif response == var_item:
                return var_item
        
        print("Please enter either yes or no...\n")

def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)
    
    valid = False 
    while not valid:

        try:
            response = float(input(question)) 
            
            if low_num < response < high_num:
                return response
            
            else:
                print (error)
        
        except ValueError:
            print(error)

def string_check(choice, options, error):

        for var_list in options:

            #if side/angle is one in the list return the full
            if choice in var_list:

                #Get full name of side/angle 
                chosen = var_list[0].title()
                is_valid = "yes"
                break

            #if choice is not valid, set is_valid to no 
            else:
                is_valid = "no"
            
        #if the side/angle is not valid ask question again 
        if is_valid == "yes":
            return chosen
        else:
            print(error)
            return "Invalid choice"
            



def get_sides():

    sides = []

    used_sides = []


    side_options = [["opposite", "oppo", "opp", "o"], 
    ["adjacent", "adj", "a"], 
    ["hypotenuse", "hyp", "h"],
    ]

    side_error = "Please enter a valid side (o,a,h)"

    desired_side = ""
    while desired_side != "xxx":



        sides_row = []

        #Ask user for a side
        desired_side = input("What side do you have?").lower().strip()

        if desired_side == "xxx":
            return sides
        
        #check if desired side is valid

        valid_side = string_check(desired_side,side_options,side_error)


        #checks if valid side has been used before
        if valid_side in used_sides:
            print("You cannot have 2 of the same side.")
            valid_side = "Invalid choice"
        
        
        #ask user for length size if choice is valid
        if valid_side != "Invalid choice":

            side_length = int_check("How big?: ", 0, 100)
            
            #add amount to side row and side length to side row and used_sides
            sides_row.append(side_length)
            sides_row.append(valid_side)

            used_sides.append(valid_side)
        
        #check that side is not the exit code before adding
        if valid_side != "xxx" and valid_side != "Invalid choice":
            sides.append(sides_row)
        
        #if user has already given 2 sides, continue
        if len(sides) == 2:
            return sides


          
    
        
#Main routine    

sides_info = get_sides()
angle = ""

#if user only has 1 side, ask for angle aswell
if len(sides_info) == 1:
        angle = int_check("Angle?: ", 0, 90)

print("***Current Information***")

for item in sides_info:
    print(item)

if angle != "":
    print("Angle: {} degrees".format(angle))

# print()
# print(sides_info)



# side_1 = sides_info[0]
# length_1 = side_1[0]
# type_1 = side_1[1]

# print(side_1)
# print(length_1)
# print(type_1)

#begin to calculate sides

opp = ""
adj = ""
hyp = ""

side_1 = sides_info[0]
length_1 = side_1[0]
type_1 = side_1[1]

if type_1 == "Opposite":
    opp = length_1

elif type_1 == "Adjacent":
    adj = length_1

elif type_1 == "Hypotenuse":
    hyp = length_1

side_2 = sides_info[1]
length_2 = side_2[0]
type_2 = side_2[1]

if type_2 == "Opposite":
    opp = length_2

elif type_2 == "Adjacent":
    adj = length_2

elif type_2 == "Hypotenuse":
    hyp = length_2






    
    

    
        

    


        

    

    
    

    






