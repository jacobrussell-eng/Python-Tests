""" 1: Tenth Power
Create a function that accepts a number and returns that number raised to the tenth power
"""
print("Q1:")

def tenth_power(num):
    return num**10

print("8 to the power of 10 is " + str(tenth_power(8)))

""" 2: Square Root
Create a function that returns the square root of the inputted number
"""
print("Q2:")

def square_root(num):
    return num**(1/2)

print("The Square root of 64 is " + str(square_root(64)))
print("The Square root of 37.59 is " + str(square_root(37.59)))

""" 3: Win Percentage
Calculate the percentage of wins given the number of wins and losses
"""
print("Q3:")

def calc_win_rate(wins,losses):
    return str(100*wins/(wins+losses)) + "%"

print("The win rate for 5 wins and 5 losses is " + calc_win_rate(5,5))
print("The win rate for 10 wins and 0 losses is " + calc_win_rate(10,0))
print("The win rate for 1 wins and 100000 losses is " + calc_win_rate(0,100000))

""" 4: Average
Generate the average of two numbers
"""
print("Q4:")

def average(num1,num2):
    return (num1+num2)/2

print("The average of 2 and 5 is " + str(average(2,5)))
print("The average of -12 and 90 is " + str(average(-12,90)))

""" 5: Remainder
Take two numbers, double the first and halve the second, then calculate the remainder of the former divded by the latter
"""
print("Q5:")

def remainder(num,den):
    num *=2
    den/=2
    return num % den

print("The remainder of 1/64 after doubling the numerator and halving the denominator is " + str(remainder(1,64)))
print("The remainder of 35/29 after doubling the numerator and halving the denominator is " + str(remainder(35,29)))

""" 6: First three multiples
Create a function that prints out the first three multiples of a number and return the third.
"""
print("Q6:")

def first_three(num):
    print(str(num)+" times by 1 is "+str(num*1)+ ", "+str(num)+" times by 2 is "+str(num*2)+", "+str(num)+" times by 3 is "+str(num*3))
    return num*3

first_three(20)
first_three(-17)

""" 7: Tip
Calculate the amount of tip to pay based on an amount and a percentage
"""
print("Q7:")

def tip_calc(cost,tip):
    return (cost*tip)/100

print("For a $30 meal, a 5% tip would cost $" + str(tip_calc(30,5)))
print("For a $0 meal, a 25% tip would cost $" + str(tip_calc(0,25)))

""" 8: Bond, James Bond
Given a first and last name, reformat and return the names to match the movie quote
"""
print("Q8:")

def bondifier(first,last):
    return last + ", " + first +" "+ last

print("So, what's your name? " + bondifier("Arnold", "Schwarzeneggar"))

""" 9: Dog Years
Create a function that accepts a dog's name and age in human years, then return a string describing its age in dog years
"""
print("Q9:")

def dog_years(name,age):
    dog_age = 0
    match age:
        case 1:
            dog_age = 15
        case 2:
            dog_age = 24
        case _:
            dog_age = 24 + (age-2)*5
    return name + " is " + str(dog_age) + " in dog years!"

print("Although Rufus is 5 in human years, " + dog_years("Rufus",5))
print("Although Snowy is 1 in human years, " + dog_years("Snowy",1))
print("Although Churro is 2 in human years, " + dog_years("Churro",2))

""" 10: All Operations
Adding the first two inputs, then subtract the third and fourth inputs. After that, multiply the first result and the second result. 
In the end, return the remainder of the previous result divided by the first input. Also print each of the steps.
"""
print("Q10:")

def all_ops(one,two,three,four):
    sum = one + two
    print("The sum of "+str(one)+" and "+str(two)+" is equal to "+str(sum))
    sub = three - four
    print(str(three)+" minus "+str(four)+" is equal to "+str(sub))
    prod = sum * sub
    print("The product of the previous two answers is "+str(prod))
    return prod%one

all_ops(24,48,128,362)