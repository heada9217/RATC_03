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

def get_sides():

    angle_options = [["opposite", "oppo", "opp", "o"], ["adjacent", "adj", "a"]]
    
    angle_error = "Please enter whether the angle is adjacent or opposite"

    #ask user whether they have a hypotenuse or not
    yes_no_hyp = yes_no("Do you have the length of the hypotenuse?: ")
    print()
    #if yes, ask for length and another length
    if yes_no_hyp == "yes":
        length_hyp = int_check("What is this length?: ",0, 100)
        print()

        #if user has another length, program continues, else ask for angle
        yes_no_side = yes_no("Do you have another side?: ")
        
        if yes_no_side == "yes":
            length_side_a = int_check("What is this length?: ", 0, 100)
        
        else:
            angle = int_check("What is an angle given?: ", 0, 90)


    #if user does not have the hypotenuse, ask for another side
    else:
        length_side_a = int_check("What is another side?: ", 0, 100)


        #if user has another side, program continues, else ask for angle
        side_b = yes_no("Do you have another given side?")
        if side_b == "yes":
            length_side_b = int_check("What is this length?: ", 0, 100)

        else:
            angle = int_check("What is a given angle?: ", 0, 90)
        
        #ask user where the angle is relative to given side
            desired_angle = input("Is this angle opposite or adjacent to the given side?").lower()

            oppo_adj = string_check(desired_angle, angle_options, angle)


#Main Routine

        