""" 1: Count Letters
Count the number of unique letters in a string
"""
print("Q1:")
def uniq_letters(word):
    uniqs = []
    for letter in word:
        if letter not in uniqs:
            uniqs.append(letter)
    return len(uniqs)

print("The number of unique letters in Mississippi is " + str(uniq_letters("Mississippi")))

""" 2: Count X
Count the number of occurrences of a specific letter in a word
"""
print("Q2:")
def num_of_letter(word,target):
    count = 0
    for letter in word.lower():
        if letter == target.lower():
            count += 1
    return count

print("The letter 's' appears " + str(num_of_letter("Mississippi","s")) + " times in Mississippi")

""" 3: Count Multi X
Check for the presence of a substring within a larger string
"""
print("Q3:")
def is_within(string,substring):
    seperated = string.lower().split(substring.lower())
    return len(seperated)-1

print("The phrase 'in' appears " + str(is_within("Insulin","in")) + " times in the word 'Insulin'")
print("The phrase 'mop' appears " + str(is_within("Pants","mop")) + " times in the word 'Pants'")

""" 4: Substring Between
Extract a substring from a larger string given a starting and ending character
"""
print("Q4:")
def extract_from(string,start_letter,end_letter):
    start_index = string.find(start_letter)
    end_index = string.find(end_letter)
    if start_index == -1 or end_index == -1:
        return string
    else:
        return string[start_index+1:end_index]

print("The letters between 'l' and 'n' in 'Xylophone' are '" + str(extract_from("Xylophone",'l','n')) + "'")
print("The letters between 'u' and 'n' in 'Mullet' are '" + str(extract_from("Mullet",'u','n')) + "'")

""" 5: X Length
Check a sentence to see if each word is longer than x
"""
print("Q5:")
def each_are_longer(sentence,x):
    all_longer = True
    for word in sentence.split():
        if len(word) < x:
            all_longer = False
    return all_longer

print("Is every word in the sentence 'Howdy Doody' longer than 4 letters? " + str(each_are_longer("Howdy Doody",4)))
print("Is every word in the sentence 'The quick brown fox jumps over the lazy dog' longer than 4 letters? " + str(each_are_longer("The quick brown fox jumps over the lazy dog",4)))

""" 6: Check Name
Check is name is in a greeting sentence
"""
print("Q6:")
def name_in_greeting(greeting,name):
    if name.lower() in greeting.lower():
        return True
    else:
        return False

print("Does the greeting 'Hi there Mark!' contain the name 'Mark'? " + str(name_in_greeting("Hi there Mark!","Mark")))
print("Does the greeting 'What's up?' contain the name 'Thomas'? " + str(name_in_greeting("What's up?","Thomas")))

""" 7: Every other letter
Extract every other letter from a string
"""
print("Q7:")
def alternating_letters(string):
    alts = ""
    for i in range(len(string)):
        if i % 2 == 0:
            alts += string[i]
    return alts

print("The alternating letters of 'Python' are " + str(alternating_letters("Python")))

""" 8: Reverse
Return the reverse of a given string
"""
print("Q8:")
def reversal(string):
    new = ""
    for i in range(len(string)):
        new += string[-i-1]
    return new

print("The reverse of 'Avengers Assemble' is '" + reversal("Avengers Assemble") + "'")

""" 9: Make Spoonerism
"A Spoonerism is an error in speech when the first syllables of two words are switched"
Make a function that performs this effect on two given words' first characters
"""
print("Q9:")
def spoonerise(word1,word2):
    ini1 = word1[0]
    ini2 = word2[0]
    word1 = ini2 + word1[1:]
    word2 = ini1 + word2[1:]
    return word1 + " " + word2

print("The Spoonerism of 'Jelly Beans' is '" + spoonerise("Jelly","Beans") + "'")

""" 10: Add Exclamation
If a given string is less than 20 characters, fill the extra space with exclamation marks
"""
print("Q10:")
def exclaimer(string):
    length = len(string)
    if length < 20:
        for i in range(20-length):
            string += "!"
    return string

print("The string 'Snake Eyes' with exclamation marks upto 20 characters is '" + exclaimer("Snake Eyes") + "'")
print("The string 'The quick brown fox jumps over the lazy dog' with exclamation marks upto 20 characters is '" + exclaimer("The quick brown fox jumps over the lazy dog") + "'")