from os import access
import pandas
from pkg_resources import get_provider

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
            print()



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



def get_sides(int):

    side_error = "Please enter a valid side"
   
    #holds valid sides
    valid_sides = ["AB"], ["AC"], ["BC"]
    
    sides = []

    sides_row = []

    
    if int == 1:
        #asks user for the length of side and then which side
        side_length = input("What is the length of your side?(cm): ")
        desired_side = input("Which side is this length? (AB,AC,BC): ").upper()
        which_side = string_check(desired_side,valid_sides,side_error)

        sides_row.append(which_side)
        sides_row.append(side_length)

    else:
        count = 1
        two_sides = 2
        desired_side = ""
        #loops to find length and which side of side 1 and 2 
        while desired_side != "xxx" and count <= 2: 
        
            side_length = input("What is the length of side {}?(cm):".format(count))
            desired_side = input("Which side is this length? (AB,AC,BC): ").upper()
            which_side = string_check(desired_side,valid_sides,side_error)

            sides.append(side_length)
            sides.append(which_side)
            count += 1 

            print("You have chosen side {}".format(which_side))
            print()
        
        sides.append(sides_row)
    
    




        
        

#main routine
number_sides = int_check("Do you have 1 or 2 sides?: ", 1, 2)
find_sides = get_sides(number_sides)

for item in find_sides:
    print(item)

        






    
