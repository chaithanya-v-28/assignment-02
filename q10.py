# Set initial balance to 10000
balance = 10000
#creat a infinite loop
while True:
    print("ATM Simulator")
# show available options to the user
    print("1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")
# take input from the user
    choice = input("Enter choice: ")
# check if user entered 1
    if choice == "1":
    # print the available balance    
        print("Balance: ", balance)
     # check if user entered 2   
    elif choice == "2":
    # ask how much money to deposite    
        amount = int(input("Enter Deposite Amount: "))  
    # add deposite amount to the balance    
        balance = balance + amount
     # show success message        
        print("Deposite Successfull !")
    # print updated balance
        print("New balance: ",balance)
    # check if user entered 3
    elif choice == "3":
    # ask for withdrawl amount   
        amount = int(input("Enter Withdraw Amount: ")) 
    #check minimum balance is available    
        if amount <= balance - 500: 
    # sub withdrawl amt from bal   
           balance = balance - amount
    # display withdrawl successfull       
           print("Withdrawl Successfull !")
    # show updated balance        
           print("New balance: ",balance)
    # if min balance not available show error    
        else:
            print("Insufficient balance") 
    # check if user entered 4    
    elif choice == "4":
    # print exit
        print("Thank You!")
    else:
        print("Invalid Choice")           
         