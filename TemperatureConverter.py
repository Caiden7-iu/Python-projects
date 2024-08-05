import random, TemperatureConverter

#convert fahrenheit to celsius

#list of color based temperatures <90 Degrees and up: red> <75 - 89 Degrees yellow> <64 - 74 Degrees: green> <63 and Below: blue>











#1. import random
#2. from colorama Import Fore
#3. 5 variables to hold the color
    #i.e., red = Force.RED

#4 def temperatureConverter(user_input):
    #5. FAHERNHEIT_TO_CELSIUS = This variable is to do conversion from fahernheit to Celsius
    #6. Conditional if/elif/else: total of 4 statements 
        #6a. print statements that print Fahernheit and temperature i color associated
        #i.e., print("Fahernheit: ", red, temperature, black)


#call function and pass  parameters


import random 
from colorama import Fore # type: ignore

red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE

def temperatureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = (user_input - 32) * (5/9)

            



    if(user_input >=90): 
        print("Fahrenheit: ", red, user_input, black)
        print("Celsius: ", red, FAHRENHEIT_TO_CELSIUS, black)
    elif(user_input <= 75) & (user_input >= 89):
        print("Fahrenheit: ", yellow, user_input, black)
        print("Celsius ", yellow, FAHRENHEIT_TO_CELSIUS, black)
    elif(user_input >= 64) & (user_input <74) :
        print("Fahrenheit: ", green, user_input, black)
        print("Celsius", green, FAHRENHEIT_TO_CELSIUS, black)
    elif(user_input <=63) :
        print("Fahrenheit: ", blue, user_input, black)
        print("Celsius ", blue, FAHRENHEIT_TO_CELSIUS, black)

    
    
  
     #user=int(input("Enter a temperature in Fahrenheit to convert to Celsius")
        
        for x in range(5):
           # temperatureConverter(user)
            #user=int(input("Enter a temperature in Fahrenheit to convert to Celsius")