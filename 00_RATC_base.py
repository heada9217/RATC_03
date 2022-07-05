
import math
import pandas
import numpy
#functions go here

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
    
def sides_trig(hyp,opp,adj,angle):

    hyp_row = ["Hypotenuse"]
    opp_row = ["Opposite"]
    adj_row = ["Adjacent"]

    calculated_sides = []



    if hyp != "":
        opp = math.sin(angle * (math.pi / 180)) * hyp
        opp_row.append(opp)
        adj = math.cos(angle * (math.pi/180)) * hyp
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

#Main Routine goes here

    # get 2 components of triangle

    #calculate the rest of the components

    # print all sides and angles