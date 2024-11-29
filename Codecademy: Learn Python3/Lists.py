""" 1: Append Size
Create a function that takes in a list, finds its length, and appends that number (length) to the list
"""
print("Q1:")

def Append_Size(input_list):
    input_length = len(input_list)
    input_list.append(input_length)
    return input_list

print("Appending the size to [45, 33, 21, 10]: " + str(Append_Size([45,33,21,10])))

""" 2: Append Sum
Create a Fibbonaci function that appends the sum of the last two elements of a list, three times
"""
print("Q2:")

def Threebbonaci(input_list):
    for i in range(3):
        last_two = input_list[-1] + input_list[-2]
        input_list.append(last_two)
    return input_list

print("Appending the sum of the last two, three times for [1, 1, 2]: " + str(Threebbonaci([1,1,2])))

""" 3: Larger List
Let's say we are working with two conveyor belts that contain items represented by a numerical ID. 
If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. 
In the case where they have the same number of items, return the last item from the first conveyor belt.
"""
print("Q3:")

def Conveyor_extend(con1,con2):
    if len(con1) < len(con2):
        return con2[-1]
    else:
        return con1[-1]
    
print("End item of the longer list out of [5, 23, 2] and [2, 23, 23, 5]: " + str(Conveyor_extend([5,23,2],[2,23,23,5])))
print("End item of the longer list out of [5, 23, 2, 8, 8] and [2, 23, 23, 5]: " + str(Conveyor_extend([5,23,2,8,8],[2,23,23,5])))
print("End item of the longer list out of [5, 23, 2, 8] and [2, 23, 23, 5]: " + str(Conveyor_extend([5,23,2,8],[2,23,23,5])))

""" 4: More than N
Check if we have enough items of a certain snack in our inventory. 
For this, we need to write a Python function that does the following:
- Accept a list of numbers representing the ids of snack on the conveyor belt as its first input, 
    the id of snack we are looking for as its second input, 
    and the desired number of that type of snack on the conveyor belt as its third input.
- Return True if the desired snack appears more than the specified number of times, Otherwise return False
"""
print("Q4:")

def enough_snacks(inv, id, n):
    num_of_snack = inv.count(id)
    if num_of_snack > n:
        return True
    else:
        return False

print("Are there at least 3 snacks of id 8 in the inventory [2,8,3,8,8,2,1,8]? " + str(enough_snacks([2,8,3,8,8,2,1,8],8,3)))
print("Are there at least 3 snacks of id 1 in the inventory [2,8,3,8,8,2,1,8]? " + str(enough_snacks([2,8,3,8,8,2,1,8],1,3)))

""" 5: Combine Sort
Create a function that combines two different lists together and then sorts them.
"""
print("Q5:")

def combine_and_sort(list1,list2):
    new_list = list1 + list2
    return sorted(new_list)

print("The sorted combination of [5,1,8] and [90,4,11,7]: " + str(combine_and_sort([5,1,8],[90,4,11,7])))