#Take age, day, tickets from user
age = int(input("Enter age: "))
day = input("Enter day of week: ")
tickets = int(input("Enter number of tickets: "))
#Check if age is below 3
if age < 3:
    price = 0
    category = "Free"               #ticket is free
#check if age is 3 to 12   
elif 3 <= age <= 12:
    price = 150
    category = "Child" 
#check if age is 13 to 59
elif 13 <= age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"
# Calculate total amount before discount
base_amount = price * tickets
#calculate amount in weekend
if day in ["friday", "saturday", "sunday"]:
    discount = base_amount * 0.20
# monday to thursday no discount    
else:
    discount = 0
# sub discount from base amount
price_after_discount = base_amount - discount
#Display output
print("══════ Ticket Details ═══════")
print("Category: ",category)
print("Base price per ticket: ", price)
print("Total amount before discount: ",base_amount)
print("Discount: ",discount)
print("Price after discount: ", price_after_discount)
print("Total amount to pay: ",price_after_discount)
