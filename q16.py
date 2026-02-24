import random

best_score = None

while True:
    number = random. randint(1,100)
    print("Guess a number between 1-100(7 attempts):")

    for attempt in range(1,8):
        guess = int(input(f"Attempt {attempt}: "))
        if guess == number:
            print(f" Correct! Attempts used: {attempt}")
            if best_score is None or attempt < best_score:
                best_score = attempt
                print(f" New best score: {best_score}")
                break
            elif guess < number:
                message= f"Too low! Attempts left: {7-attempt}"
            else:    
                message = f"Too high! Attempts left: {7-attempt}"
            if abs(number - guess)<= 5:
                message+= " very close!"
            print(message)
        else:    
            print(f" sorry! The number was {number}")
        if input("Play again (yes/no): ").lower() != "yes":
           print("Thanks for playing! ")
        break    