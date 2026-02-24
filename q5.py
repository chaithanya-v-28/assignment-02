#Ask for user input
total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))
#calculate tax 
tax_amount =(tax_percent / 100) * total_bill
#Bill after tax
after_tax = total_bill + tax_amount
#calculate tip
tip_amount = (tip_percent/ 100) * total_bill
#total bill including tax and tip
total_bill_final = after_tax + tip_amount
#amount per person
per_person = total_bill_final / num_people

#Display bill breakdown
print(" ═════ BILL BREAKDOWN ═════ ")
print(f"Subtotal: {total_bill: .2f}")
print(f"Tax({tax_percent}%): {tax_amount: .2f}")
print(f"After tax: {after_tax: .2f}")
print(f"Tip({tip_percent}%):{tip_amount:.2f}")
print(f"Total: {total_bill_final:.2f}")
print(f"per person: {per_person:.2f}")