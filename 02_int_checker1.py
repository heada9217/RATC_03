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
for item in range(0,6):
    number_sides = int_check("Do you have 1 or 2 sides?: ", 1, 2)
    print("You said {}".format(number_sides))