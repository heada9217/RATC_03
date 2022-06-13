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
            
        #if the side/angle is not valid ask question again 
        if is_valid == "yes":
            return chosen
        else:
            print(error)
            return "Invalid choice"

side_options = [["opposite", "oppo", "opp", "o"], ["adjacent", "adj", "a"], ["hypotenuse", "hyp", "h"]]
side_error = "Please enter a valid side (o,a,h)"

have_side = "Invalid choice"
while have_side == "Invalid choice":
#Ask user for a side
   desired_side = input("What side do you have?").lower()
   valid_side = string_check(desired_side,side_options,side_error)

if valid_side == "yes":
    lenght = int_check("How big?: ", 0 , 100)



