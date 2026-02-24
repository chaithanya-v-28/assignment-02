#Ask user to enter marks for each subject
m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))
m4 = float(input("Enter marks in subject 4: "))
m5 = float(input("Enter marks in subject 5: "))
#Add all 5 subjects
total = m1 + m2 + m3 + m4 + m5
#Calculate percentage
percentage = (total / 500) * 100
if percentage >= 90:
    grade = "A+ (Outstanding)"

elif percentage >= 80:
    grade = "A (Excellent)" 

elif percentage >= 70:
    grade = "B (Good)"

elif percentage >= 60:
    grade = "c (Average)"  

elif percentage >= 50:
    grade = "D (pass)"      

else:
    grade = "F (Fail)"    

#check if all subjects are 40 or  above 
if m1 >=40 and  m2>= 40 and m3 >=40 and m4 >= 40 and m5 >= 40:
   result = "Pass"

else:
    result = "Fail"
# Display output

 # print total marks
print("Total: ", total, "/500")   
#print percentage rounded to 2 decimals
print("Percentage: ", round(percentage, 2)  )
#print calculated grade
print("Grade: ", grade)
#print pass or fail
print("Result: ", result)
