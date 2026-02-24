# ask user to choose a pattern
print("Choose Pattern: ")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")
# take height and pattern number from user
choice = int(input("Enter pattern number(1-4): "))
height = int(input("Enter height: "))
# check if user selected pattern 1
if choice == 1:
    # runs from 1 to height
    for i in range(1,height + 1 ):
    #runs from 1 to current row number
        for j in range(1, i + 1):
        # print j    
            print(j, end = " ")
        print( )

elif choice == 2:
    for i in range(1, height + 1 ):
        for j in range(i):
            print(i, end = " ")
        print( )    

elif choice == 3:
    for i in range(height, 0, -1 ):
        for j in range(i, 0, - 1):
            print(j, end = " ")
        print( )

elif choice == 4:
    for i in range(1,height + 1 ):
        for j in range(1, i + 1):
            print(j, end = " ")
        for j in range(i - 1, 0, -1):
            print(j, end = " ")   
        print( )    
else:
    print("Invalid choice !")