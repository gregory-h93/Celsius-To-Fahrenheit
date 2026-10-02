#Convert Celsius to Fahrenheit using a function
celsius = int(input("Enter an integer for temperature in celsius: "))

def fahrenheit(cel):
    return round(1.8 * cel + 32, 1)


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")