# Create a function convert_me() that inputs a list of string and returns the whole sentence as a
# string. 

def convert_me(list):                   # creating function to convert list to string   
    str = ""                            # initializing an empty string

    for i in list:                      # iterating and adding the list element to the str variable  
        str += i + " "

    return str                          # return string  
           
list = ['A', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
sentence = convert_me(list)             # storing function to sentence variable
print(sentence)