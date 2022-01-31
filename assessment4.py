# optimize the following code to the equivalent list comprehension

list = []
for x in range(10):
        list.append(2*x+1)
print(list)        


list =[2*x+1 for x in range(10)]     # 2*x+1 expression for x variable in iterable
print(list)