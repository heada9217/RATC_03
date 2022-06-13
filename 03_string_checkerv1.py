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


side_error = "Please enter a valid side"

#holds valid sides
valid_sides = ["AB"], ["AC"], ["BC"]

for item in range (0,6):
    desired_side = input("Which side is this length?(AB, AC, BC): ")

    which_side = string_check(desired_side, valid_sides, side_error)
