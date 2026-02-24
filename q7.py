# define functions for each temp formula
def c_to_f(t): return (t * 9/5) +32
def f_to_c(t): return (t - 32) * 5/9
def c_to_k(t): return t + 273.15
def k_to_c(t): return t - 273.15
def f_to_k(t): return (t - 32) * 5/9 + 273.15
def k_to_f(t): return (t - 273.15) * 9/5 + 32
#Creat a Dictionary
conversions = { 
    "1": c_to_f,
    "2": f_to_c,
    "3": c_to_k,
    "4": k_to_c,
    "5": f_to_k,
    "6": k_to_f,
}

#initialize variables 
choice = ""
#loop run until user enters 7
while choice != "7":
    print("\n1.c→f 2.f→f 3.c→k 4.k→c 5.f→k 6.k→f 7.Exit")
    choice = input("Choice: ")
# check if user selected valid opt    
    if choice in conversions:
 #take temp input
       temp = float(input("enter temperature: "))  
 #call function using dict
       print("Result: ",round(conversions[choice](temp),2))   
#if input is not 1 to 7 show error
    elif choice != "7":
        print("Invalid choice")
print("Program Ended")
 

