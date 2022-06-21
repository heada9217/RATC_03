#import statements
import math 
import pandas



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
            response = int(input(question)) 
            
            if low_num <= response <= high_num:
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

#Checks that user has entered yes / no to a question 

#Main Routine goes here

    # get 2 components of triangle

    #calculate the rest of the components

    # print all sides and angles