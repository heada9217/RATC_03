import string

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
        
def instructions():
    yes_no = ["yes", "no","y","n"]
    
    show_help = "Invalid choice"
    show_error = "Please answer with either yes or no"
    
    while show_help == "Invalid choice":
        show_help = input("Would you like to read the instructions?").lower()
        show_help = string_check(show_help, yes_no, show_error)
        
    if show_help == "Y":
        print()
        print(" *** Right Angled Triangle Calculator Instructions *** ")
        print() 
        #print instructions
        print("Instructions go here")   

        
for item in range(0,2):
      
    instructions()

    print()
    print("Program Launching...")
            
