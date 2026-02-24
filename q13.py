# ask userhow many number want to enter
count = int(input("How many numbers: "))
# initialize sum var
total = 0
# initialize no max value
max_num = None
#initialize no min val
min_num = None
# Loop run as many times as user enterd
for i in range(1, count + 1):
#take num each time
    num = int(input(f"enter number {i}: "))  
# add all number to total
    total = total + num
#first num become max and compare each num
    if max_num is None or num > max_num:
        max_num = num
#first num become min and update if smaller num        
    if min_num is None or num < min_num:
        min_num = num
#Calculate avg
average = total / count
# print results
print("Sum: ",total)
print("Average: ",average)
print("Maximum: ",max_num)
print("Minimum: ",min_num)