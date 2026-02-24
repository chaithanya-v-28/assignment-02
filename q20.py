import math
# factorial
def factorial(n):
    if n< 0:
        return "Undefined for negative numbers"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
#prime check
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    # fibonacci nth number
    def fibonacci(n):
        a,b = 0,1
        for _ in range(n-1):
           a,b = b, a+b
        return b if n> 0 else 0
    #sum of digits
    def sum_of_digits(n):
        return sum(int(d) for d in str(abs(n)))  
    #reverse number
    def reverse_number(n):
        sign = -1 if n < 0 else 1
        return sign * int(str(abs(n))[::-1]) 
    #armstrong check
    def is_armstrong(n):
        s = str(abs(n))
        return sum(int(d)**len(s) for d in s) == abs(n)
    #gcd
    def gcd(a,b):
        return math.gcd(a,b)
    #LCM
    def lcm(a,b):
        return abs(a*b)//gcd(a,b) if a and b else 0
    #perfect num chech
    def is_perfect_number(n):
        if n < 1: 
            return False
        return sum(i for i in range(1,n) if n%i==0) ==n
    
    #menu function
    def math_menu():
        while True:
            print(" ═══════ NUMBER SYSTEM MENU ═══════")
            print("1. Factorial")
            print("2. Prime check")
            print("3. Fibonacci")
            print("4. Sum of digits")
            print("5. Reverse Number")
            print("6. Armstrong check")
            print("7. GCD")
            print("8. LCM")
            print("9. Perfect number check")
            print("10. Exit")
            choice = input("enter choice(1 - 10): ")

            if choice == "10":
                print("exiting menu")
                break
            if choice == "1":
                n = int(input("enter number: "))
                print("Factorial:", factorial(n))
            elif choice == "2":
                n = int(input("Enter number: "))
                print("prime:","yes" if is_prime(n) else "No")
            elif choice == "3":
                n = int(input("enter position n: "))
                print(f"Fibonacci({n}):", fibonacci(n)) 
            elif choice == "4":
                n = int(input("enter number:"))   
                print("sum of digits:", sum_of_digits(n)) 
            elif choice == "5":
                n = int(input("enter number: "))    
                print("Reversed number:", reverse_number(n))   
            elif choice == "6":
                n = int(input("enter number:"))
                print("Armstrong:", "Yes" if is_armstrong(n) else "No")  
            elif choice == "7":
                a = int(input("enter first number: "))
                b = int(input("enter second number: "))  
                print("GDC:", gdc(a,b))   
            elif choice == "8":
                 a = int(input("enter first number: "))
                 b = int(input("enter second number: "))      
                 print("LCM:", lcm(a,b)) 
            elif choice == "9":
                n = int(input("enter number: "))  
                print("Perfect number:", "Yes" if is_perfect_number(n) else "No")  
            else:
                print("Invalid choice")

    math_menu()
        
               