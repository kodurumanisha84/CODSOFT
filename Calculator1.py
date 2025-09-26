print("Welcome to Simple  Calculator Application!!")

#Taking input from the user 
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))

#Displaying list of  operations
print("Operation choices:")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
operation=int(input("Enter choice:"))

#Taking the choice of operation to be performed and computing accordingly
if(operation in [1,2,3,4]):
    if(operation==1):
        result=n1+n2
    elif(operation==2):
        result=n1-n2 
    elif(operation==3):
          result=n1*n2
    elif(operation==4):
         result=n1/n2    
else:
    print("Invalid operation!")

#Displaying the result    
print("The result is {}".format(result))

print("Thank you for using Calculator Application!! ")
