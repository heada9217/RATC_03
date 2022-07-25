import math
import pandas


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
            response = int(input(question)) 
            
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
                chosen = var_list[0]
                is_valid = "yes"
                break

            #if choice is not valid, set is_valid to no 
            else:
                is_valid = "no"
                # print(error)
            
        #if the side/angle is not valid ask question again 
        if is_valid == "yes":
            return chosen
        else:
            print(error)
            return "Invalid choice"

def get_side(side):

    valid = False
    while not valid:
        yes_no_side = yes_no("Do you have the {}?: ".format(side))

        if yes_no_side == "yes":
            length_side = int_check("What is this length?: ", 0, 100)

        else:
            yes_no_side == "no"
            break

def get_side(side):

    sides = []

    hyp_side = []
    a_side = []
    b_side = []

    if side == "hypotenuse":
        yes_no_hyp = yes_no("Do you have the length of the Hypotenuse?")
        if yes_no_hyp == "yes":
            length_hyp = int_check("Length:", 0, 100)
            length = length_hyp
        else:
            length_hyp = ""
            response = "no"
            return response

        hyp_side.append(length)


    
    while side == 1:
        yes_no_side_1 = yes_no("Do you the length of side 1?: ")
        if yes_no_side_1 == "yes":
            length_side_1 = int_check("Length: ", 0, 100)
           
        else: 
            response = "no"
            length_side_1 = ""
                  
    a_side.append(length_side_1)

    while side == 2: 
        yes_no_side_2 = yes_no("Do you the length of side 2?: ")
        if yes_no_side_2 == "yes":
            length_side_2 = int_check("Length: ", 0, 100)
           
        else: 
            response = "no"
            length_side_2 = ""
    
    b_side.append(length_side_2)

    sides.append(hyp_side)
    sides.append(a_side)
    sides.append(b_side)

    print (sides)
 
    
    


        
angle_options = [["opposite", "oppo", "opp", "o"], ["adjacent", "adj", "a"]]

angle_error = "Please enter whether the angle is adjacent or opposite"

minimum_error = "You do not have enough information to find the sides of the right angled triangle."
