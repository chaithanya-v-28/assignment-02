# take number and range  from user
number = int(input("Enter number: "))
end = int(input("Enter range (end): "))
# print heading
print("Full Multiplication table( 1 to 10)")
#loop start from 1 and ends at given range
for i in range(1, 11):
    for j in range(1,11):
# multiplication step        
        print(i * j, end = "\t")
    print()    