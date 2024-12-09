import random

# Generate a random integer between 0 and 20
random_number = random.randint(0, 20)

print("Welcome to the Number Guessing Game!")
print("Try to guess the number I'm thinking of between 0 and 20.")

while True:
    # Prompt the user to input a number
        number = int(input("Enter a number between 0 and 20: "))
        
        if number < 0 or number > 20:
            print("Please enter a number within the range of 0 to 20.")
            continue
        
        if number == random_number:
            print("Congratulations! You guessed the correct number.")
            break  # Exit the loop when the user guesses correctly
        elif number > random_number:
            print("Too high! Try a smaller number.")
        else:  # number < random_number
            print("Too low! Try a larger number.")
    
    