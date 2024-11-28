""" 1: Divisble by Ten
Count how many numbers in a list are divisible by ten, then return the final count
"""
print("Q1:")

def num_multiples_of_ten(numbers):
    counter = 0
    for el in numbers:
        if el % 10 == 0:
            counter+=1
    return counter

print("Number of multiples of ten in the list [1,5,10,20,40,80,95]: " + str(num_multiples_of_ten([1,5,10,20,40,80,95])))
print("Number of multiples of ten in the list [1,5,7]: " + str(num_multiples_of_ten([1,5,7])))

""" 2: Greetings 
Write a function to say hello to every name in a list
"""
print("Q2:")

def greet_list(names):
    greetings = []
    for name in names:
        print("Hello, "+name+"!")
    return greetings

print("To greet Hal, Malcolm and Reese: ")
greet_list(["Hal","Malcolm","Reese"])

""" 3: Delete Starting Even Numbers
Create a function that repeatedly removes the first element of a list if it is not odd, or unless it runs out of elements.
It should return the remaining list
"""
print("Q3:")

def remove_starting_evens(seq):
    while len(seq) != 0:
        if seq[0] % 2 == 0:
            seq.pop(0)
        else:
            break
    return seq

print("Removing the starting evens from [4,2,8,3,5] leaves: " + str(remove_starting_evens([4,2,8,3,3])))
print("Removing the starting evens from [4,2,8,10,12] leaves: " + str(remove_starting_evens([4,2,8,10,12])))

""" 4: Odd Indices
Return the values from a list at every Odd index
"""
print("Q4:")

def return_odd_indices(seq):
    odds = []
    for idx in range(0,len(seq),2):
        odds.append(seq[idx])
    return odds

print("The values at Odd indices of [1,2,3,4,5,6,7,8] are: " + str(return_odd_indices([1,2,3,4,5,6,7,8])))

""" 5: Exponents
Design a function that accepts two lists, and raises every number in the first list to the power of every number in the second list
"""
print("Q5:")

def list_to_the_power_of_list(bases,powers):
    answers = []
    for base in bases:
        for pow in powers:
            answers.append(base**pow)
    return answers

print("[1,2,3] to the power of [4,5,6] = " + str(list_to_the_power_of_list([1,2,3],[4,5,6])))
print("[1,2,3,4,5,6,7,8,9,10] to the power of [1,2,3,4,5,6,7,8,9,10] \n(Multiples of 1, then 2, then 3, ...) = " + str(list_to_the_power_of_list([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10])))

""" 6: Larger Sums
Find which of two lists has the larger sum
"""
print("Q6:")

def larger_list_sum(list1,list2):
    if sum(list1) > sum(list2):
        return list1
    else:
        return list2

print("The list with the larger sum between [23,11,43] and [26,27,28] is " + str(larger_list_sum([23,11,43],[26,27,28])))
print("The list with the larger sum between [20,10,40,30] and [24,22,20] is " + str(larger_list_sum([20,10,40,30],[24,22,20])))

""" 7: Over 9000
Sum up values in a list until the sum reaches 9000, then return the final value where it stopped
"""
print("Q7:")

def sum_to_9000(seq):
    running_total = 0
    for num in seq:
        if running_total + num < 9000:
            running_total += num
        else:
            break
    return running_total

print("The sum upto 9000 of [6000,1200,500,200,400,230,1000,530,1000] reaches " +str(sum_to_9000([6000,1200,500,200,400,230,1000,530,1000]))+ " before stopping")
print("The sum upto 9000 of [2000,3001,4002,5003,6004,7005] reaches " +str(sum_to_9000([2000,3001,4002,5003,6004,7005]))+ " before stopping")

""" 8: Max Num
Define a max() function from scratch
"""
print("Q8:")

def max_number(seq):
    biggest_number = 0
    for num in seq:
        if num > biggest_number:
            biggest_number = num
    return biggest_number

print("The biggest number in the list [5, 6, 8, 9, 5, -4, 0] is " + str(max_number([5, 6, 8, 9, 5, -4, 0])))

""" 9: Same Values
Create a function that loops through two lists, identifying if any indices have the same value in both, then return those indices
"""
print("Q9:")

def compare_indices(list1,list2):
    if len(list1) == len(list2):
        shared_indices = []
        for idx, val in enumerate(list1):
            if val == list2[idx]:
                shared_indices.append(idx)
        if shared_indices != []:
            return shared_indices
        else:
            return "None."
    else:
        return "List lengths are not compatible."

print("The indices with the same values between [2,4,7,5,1,10,4] and [1,4,3,2,1,9,4] are " + str(compare_indices([2,4,7,5,1,10,4],[1,4,3,2,1,9,4])))
print("The indices with the same values between [1,2,3] and [4,5,6] are " + str(compare_indices([1,2,3],[4,5,6])))
print("The indices with the same values between [1,3,2] and [1,3] are " + str(compare_indices([1,3,2],[1,3])))

""" 10: Reversed List
Compare two lists to check if one is the reverse of the other
"""
print("Q10:")

def compare_if_lists_are_reversed(list1,list2):
    if len(list1) == len(list2):
        is_reversed = True
        for idx,val in enumerate(list1):
            if val != list2[-1-idx]:
                is_reversed = False
        return is_reversed
    else:
        return "List lengths are not compatible."

print("Is [1,2,3,4,5] the same as [5,4,3,2,1] in reverse? " + str(compare_if_lists_are_reversed([1,2,3,4,5],[5,4,3,2,1])))
print("Is [4,2,1] the same as [2,1,4] in reverse? " + str(compare_if_lists_are_reversed([4,2,1],[2,1,4])))
print("Is [4,2,1] the same as [1,2,4,3] in reverse? " + str(compare_if_lists_are_reversed([4,2,1],[1,2,4,3])))
