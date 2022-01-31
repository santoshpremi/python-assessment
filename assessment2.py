# Create a dictionary of key values from a range of 1 to 100 where key contains the number and
# value contains the square of it


result=dict()                           #initializing the empty dictionary and storing in result variable       
for i in range(1,101):
    instance = {i:i**2}                  #storing key and value to instance variable 
    result.update(instance)            #appending instance to result 
print(result)

# result=dict()                          #initializing the empty dictionary and storing in result variable
# for i in range(1,101):                 #for loop range 1 to 100 
#     result[i]= i*i                     # appending [i] key and i*i value to result
# print(result)    

# result = {x:x*x for x in range(1,101)}
# print(result)

   

 