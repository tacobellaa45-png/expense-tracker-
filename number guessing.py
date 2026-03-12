import random 



number = random.randint(1,100)
attempts = 0

print("Guess the number(between 1 and 100)")

while True:
    guess = input("your guest:")
    if not guess.isdigit():
        print("Enter a valid number!")
        continue 

    guess = int(guess)
    attempts += 1

    if guess == number :
        print(f"Correct! you guessed it in {attempts} tries.")
        break 
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")