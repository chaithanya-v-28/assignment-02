# take num from user
num = int(input("Enter a number: "))
#check if num is negative
if num < 0:
    print("Factorial not defined for negative numbers")
#check if num is 0
elif  num == 0:
    print("0! = 1")  
# when num is positive
else:
    fact = 1
# print a number    
    print(f"{num}! = ", end = "")   
# loop run from entered number to 1
    for i in range(num, 0, -1):
# mul and store result        
        fact *= i
        print(i, end=" x " if i != 1 else "") 
    print("=", fact)    