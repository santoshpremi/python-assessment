
# outer loop to handle number of rows  
for i in range(0, 5):
     
        # inner loop to handle number of columns
        # values changing according to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\t")


n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*2-1,end=" ")
    print("\r")

    


  