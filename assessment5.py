# Explain the difference between the following statements.
data = [1,4,9,16,25]
# statement 1
values = [x**3 for x in data]   #here data list is store in  values  which is list comprehension   
# statement 2
value = (x**3 for x in data)    #whereas data list is store in value which is  generator comprehension


print(type(values))
print(type(value))

