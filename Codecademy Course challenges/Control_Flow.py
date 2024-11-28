""" 1: Not Sum to Ten
Given two stored numbers, set the variable 'not_ten' equal to False if it's equal to 10, or equal to True if not. 
"""
print("Q1:")
def sum_to_ten(num1, num2):
    if num1 + num2 == 10:
        return False
    else:
        return True

not_ten = sum_to_ten(5, 5)
print("Not equal to ten? " + str(not_ten))

""" 2: Over budget
You are given a monthly budget and some expenses, and need to check if the sum of the expenses goes over budget
"""
print("Q2:")
# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# My answer
total_expenses = food_bill + electricity_bill + internet_bill + rent
is_over_budget = True if total_expenses > budget else False
print("Over Budget? " + str(is_over_budget))

""" 3: Large Power
Create a function named large_power() that takes two parameters named base and exponent. 
If base raised to the exponent is greater than 5000, return True, otherwise return False.
"""
print("Q3:")

def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

print("Is 2^13 over 5000? " + str(large_power(2,13)))
print("Is 2^12 over 5000? " + str(large_power(2,12)))

""" 4: Twice as Large
Determine if one number is twice as large as another number
"""
print("Q4:")

def more_than_double(num1, num2):
    if num1 > (num2*2):
        return True
    else:
        return False

print("Is 13 more than twice as large as 5? " + str(more_than_double(13,5)))
print("Is 21 more than twice as large as 11? " + str(more_than_double(21,11)))

""" 5: Divisible by Ten
Create a function that determines whether or not a number is divisible by ten.
"""
print("Q5:")

def is_divisble_by_ten(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
    
print("Is 10,000 divisible by ten? " + str(is_divisble_by_ten(10000,10)))
print("Is 101 divisible by ten? " + str(is_divisble_by_ten(101,10)))

""" 6: In Range
Test if a given number falls in a given range
"""
print("Q6:")

def is_between(num,lower,upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False
    
print("Is 10 between 10 and 10? " + str(is_between(10,10,10)))
print("Is 5 between 10 and 20? " + str(is_between(5,10,20)))

""" 7: Same Name
Write a program that checks if two names are the same
"""
print("Q7:")

def is_the_same(name1,name2):
    if name1==name2:
        return True
    else:
        return False
    
print("Are Michael and Michael the same name? " + str(is_the_same("Michael","Michael")))
print("Are Michael and Michelle the same name? " + str(is_the_same("Michael","Michelle")))

""" 8: Always False
Write a conditional function that contains a contradiction, and hence always returns False
"""
print("Q8:")

def always_false(num):
    if num > (num*2) and num > 0:
        return True
    else:
        return False

print("Number = 14? " + str(always_false(14)))
print("Number = -5? " + str(always_false(-5)))

""" 9: Movie Review
Create a function that will help us rate movies. 
Our function will split the ratings into different ranges and tell the user how the movie was based on the movie's rating.
"""
print("Q9:")

def movie_rating(score):
    if score <= 5:
        return "Avoid at all Costs!"
    elif score > 5 and score < 9:
        return "This one was fun."
    else:
        return "Outstanding!"
    
print("How was 'The Room'? " + movie_rating(2))
print("How was 'Tropic Thunder'? " + movie_rating(6))
print("How was 'The Thing'? " + movie_rating(10))

""" 10: Max Number
Use a function to determine which of 3 inputs is the maximum value
"""
print("Q10:")

def max_number(num1,num2,num3):
    match max(num1,num2,num3):
        case ans if ans == num1:
            return num1
        case ans if ans == num2:
            return num2
        case _:
            return num3
        
print("Which number is greatest out of 5, 7, and 3? " + str(max_number(5,7,3)))
print("Which number is greatest out of 151, -60, and 32? " + str(max_number(151,-60,32)))
print("Which number is greatest out of 5, 70, and 300? " + str(max_number(5,70,300)))