# ask usr to enter a number
num = int(input("enter a number: "))
# check if number is 0 or 1
if num <= 1:
#print its not a prime num    
    print(num, "is NOT prime")
# check if num is 2    
elif num == 2:
# print a message prime    
    print("2 is prime") 
else:
# loop to check if it divides    
    for i in range(2,int(num** 0.5)+1):
# check if divisible by i        
        if num % i == 0:
# print not prime            
            print(num,"is not prime") 
            break
    else:
        print(num,"is prime")    
# ask user for start range and end range
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
primes = [n for n in range(start, end +1) if n > 1 and all(n%i !=0 for i in range(2,int(n**0.5)+1))]
print("Prime numbers: ", ", ".join(map(str, primes)))