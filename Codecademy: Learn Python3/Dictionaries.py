sample_dict = {
    1: 5,
    2: -8,
    3: 14,
    4: 50,
    15: 11
}

""" 1: Sum Values
Make a function to return the total sum of all values within a given dictionary
"""
print("Q1:")
def value_summer(dict):
    sum = 0
    for val in dict.values():
        sum += val
    return sum

print("The sum of all the Dictionary values is " + str(value_summer(sample_dict)))

""" 2: Even Keys
Same as before, but only for keys that are even
"""
print("Q2:")
def even_key_summer(dict):
    sum = 0
    for key in dict.keys():
        if key % 2 == 0:
            sum += dict[key]
    return sum

print("The sum of even keys within the Dictionary is " +  str(even_key_summer(sample_dict)))

""" 3: Add Ten
For each value in a dictionary, add 10 to that value then return the modified dictionary
"""
print("Q3:")
def add_ten_to_each(dict):
    for key in dict.keys():
        dict[key] += 10
    return dict

print("Adding ten to each value in the Dictionary leads to " + str(add_ten_to_each(sample_dict)))

""" 4: Values that are Keys
Check through a dictionary and return any values that are also keys
"""
print("Q4:")
def vals_that_are_keys(dict):
    mutuals = []
    for val in dict.values():
        if val in dict.keys():
            mutuals.append(val)
    return mutuals

print("The values in the Dictionary that are also keys are: " + str(vals_that_are_keys(sample_dict)))

""" 5: Largest Value
Find the maximum value in a dictionary and return the associated key
"""
print("Q5:")
def key_of_max_value(dict):
    highest_key = 0
    highest_val = 0
    for key,value in dict.items():
        if value > highest_val:
            highest_val = value
            highest_key = key
    return highest_key

print("The key of the highest value in the Dictionary is " + str(key_of_max_value(sample_dict)))

""" 6: Word Length Dict
Create a new dictionary based on a list of strings, where the key is a string and the value is the length of that string
"""
print("Q6:")
def len_dict_maker(strings):
    new_dict = {}
    for string in strings:
        new_dict[string] = len(string)
    return new_dict

print("The dictionary of string lengths from ['Abra','Kadabra','Alakazam','Wow'] is " + str(len_dict_maker(['Abra','Kadabra','Alakazam','Wow'])))

""" 7: Frequency Count
Similar to the last, but instead of length, set the value equal to the number of appearances
"""
print("Q7:")
def freq_dict_maker(strings):
    new_dict = {}
    for string in strings:
        if string in new_dict.keys():
            new_dict[string] += 1
        else:
            new_dict[string] = 1
    return new_dict

print("The dictionary of string frequencies from ['This', 'is', 'That', 'and', 'That', 'is', 'This'] is " + str(freq_dict_maker(['This', 'is', 'That', 'and', 'That', 'is', 'This'])))

""" 8: Unique Values
Return the number of unique values within a given dictionary
"""
print("Q8:")
def uniq_in_dict(dict):
    uniqs = []
    for val in dict.values():
        if val not in uniqs:
            uniqs.append(val)
    return len(uniqs)

dict_8 = {
    1: 4,
    2: 4,
    3: 2,
    4: 20,
    5: 7,
    6: 11,
    7: 11,
    8: 90
}

print("The number of unique values in Dictionary_8 is " + str(uniq_in_dict(dict_8)))

""" 9: Count First Letter
This function accepts a dictionary where the keys are last names and the values are lists of first names of people who have that last name. 
Calculate the number of people who have the same first letter in their last name.
"""
print("Q9:")
def count_initials(dict):
    letters = {}
    for key in dict.keys():
        if key[0] not in letters:
            letters[key[0]] = len(dict[key])
        else:
            letters[key[0]] += len(dict[key])
    return letters

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

print("The Number of people with each Surname initial are " + str(count_initials(names)) + " from " + str(names))
