# Task 1: Begin by asking the user to enter the temperature in Fahrenheit.

temp_fahr = input("Please enter today's temperature in degrees Fahrenheit: ")


# Task 2 Temperature Conversion: Write a function that converts the Fahrenheit 
#temperature to Celsius. Remeber that the formula is [(Fahrenheit - 32) * 5/9]

def temp_conversion(Fahrenheit):                                                                   #defined a function to convert from Fahrnheit to Celcius
    return (Fahrenheit - 32) * 5/9

temp_fahr = input("Please enter today's temperature in degrees Fahrenheit: ")

try:                                                                                              #try block to convet the user input into a float type
    temp_fahr = float(temp_fahr) 
    
except ValueError:                                                                               #excpet block for a ValueError incase the input is non-convertable, will print a message letting the user know
    print("ValueError: input was not a number.")   



# Task3 User Experiance: Implement an else block that prints the converted temperature
#in a user-friendly format.

def temp_conversion(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

temp_fahr = input("Please enter today's temperature in degrees Fahrenheit: ")

try:
    temp_fahr = float(temp_fahr) 
    
except ValueError:
    print("ValueError: input was not a number.")   

else:                                                                                               #added an else statement that will call the conversion function and print out the conveted temperature
    long_temp_cels = temp_conversion(temp_fahr)
    temp_cels = round(long_temp_cels, 2)
    print(f"{temp_fahr} degrees Fahrenheit is {temp_cels} degreees when converted to Celcius.")


# Task 4 Finally: Add a fianlly block that thanks the user for usingthe weather forcast application,
#ensuring that this message is displayed regardless of whether an exception was caught or not.

def temp_conversion(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

temp_fahr = input("Please enter today's temperature in degrees Fahrenheit: ")

try:
    temp_fahr = float(temp_fahr) 
    
except ValueError:
    print("ValueError: input was not a number.")   

else:                                                                                               
    long_temp_cels = temp_conversion(temp_fahr)
    temp_cels = round(long_temp_cels, 2)
    print(f"{temp_fahr} degrees Fahrenheit is {temp_cels} degreees when converted to Celcius.")

finally:                                                                                           #added a finally statement thanking the user for using the app
    print("Thank you for using the weather forecast app!")    

