#ask user for the input
year = int(input("Enter year: "))
#check if divide by 4
if year % 4 == 0:
    #check if not divide by 100
    if year % 100 != 0:
        #print result
        print(year, "is leap year")
        print("Reason: Divisible by 4 and not divisible by 100")
    #check if year is divide by 400 , only if above condition is false
    elif year % 400 ==0:
        #print result
        print(year, "is a leap year")
        #show reason
        print("Reason: Divisible by 400") 
    else:
        print(year,"is NOT a leap year") 
        print("Reason: Divisible by 100 but not by 400")    
else:
    print(year, "is NOT a leap year")  
    print("Reason: Not divisiblr by 4")     