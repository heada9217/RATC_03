def string_check(choice, options, error):

    for var_list in options:

        #if the snack is in one of the lists, return the full
        if choice in var_list:

            #Get full name of snack and put it 
            #in title case so it looks nice when outputted
            chosen = var_list[0]
            is_valid = "yes"
            break

        #if choice is not valid, set is_valid to no 
        else:
            is_valid = "no"
            return(error)
        
    #if the answer is not in variable list, return question
    if is_valid == "yes":
        return chosen
    else:
        print(error)
        return "Invalid choice"

yes_no = [["yes","y"], ["no","n"]]
yes_no_answer = input("Do you want to use Radians?:").lower()
units = ""


units = string_check(yes_no_answer, yes_no, "Please enter either yes / no")
    
        
        
