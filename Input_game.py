import random as rd
import time as tm

# Welcome message
print("Welcome to the Number Guessing Game!")

# Get participant's name
participant_name = input("Please enter your name: ")
print(f"Hello, {participant_name}! Try to guess the number I'm thinking of between 0 and 20.")

# Generate a random integer between 0 and 20
random_number = rd.randint(0, 20)

# Initialize attempt counter and start the timer
attempts = 0
start_time = tm.time()

while True:
    try:
        # Prompt the user to input a number
        number = int(input("Enter a number between 0 and 20: "))
        
        # Increment the attempt counter
        attempts += 1

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
    except ValueError:
        print("Invalid input. Please enter an integer.")

# End the timer
end_time = tm.time()
elapsed_time = end_time - start_time

# Final message
final_message = (
    f"\n{participant_name}, you guessed the number in {attempts} attempts and completed the game "
    f"in {elapsed_time:.3f} seconds. Well done!"
)
print(final_message)

# Save game information to a file
filename = "game_results.txt"
with open(filename, "a") as file:
    file.write(
        f"Participant: {participant_name}, Attempts: {attempts}, Time: {elapsed_time:.3f} seconds\n"
    )

print(f"Your game information has been saved to '{filename}'.")

    
    
