# QUESTION ONE
# part 1
def men(weight,height,age):
    output = (13.7516*weight)+(5.0033*height) - (6.755*age) + 66.473
    print(output)

def women(weight,height,age):
    output = (9.5634*weight)+(1.8496*height) - (4.6756*age) + 655.0955
    print(output)

# part 2

def chocw(weight,height,age):
    bmr = (9.5634*weight)+(1.8496*height) - (4.6756*age) + 655.0955
    chocolate = bmr/214
    print(chocolate)

def chocm(weight,height,age):
    bmr = (13.7516*weight)+(5.0033*height) - (6.755*age) + 66.473
    chocolate = bmr/214
    print(chocolate)

# part 3
print("Enter weight in kilograms, height in centimeters, and age in years")

chocw(59,167,25)
chocm(70,175,30)

print("The above calculates the number of chocolate bars required for both a man and a woman with the given inputs")

# QUESTION TWO
def degrees(celcius):
    fahrenheit = celcius*(9/5)+32
    print(fahrenheit)

print("Insert a temperature in celcius")
degrees(3)


# QUESTION THREE

import math

def time(seconds):
    hours = math.floor(seconds/3600)
    hour_string = str(hours)
    left_after_hours = seconds-(hours*3600)
    minutes = math.floor(left_after_hours/60)
    min_string = str(minutes)
    seconds = left_after_hours-(minutes*60)
    sec_string = str(seconds)
    print("that number of seconds yields, " + hour_string + " hours, " + min_string + " minutes, and " + sec_string + " seconds.")

time(5344505)