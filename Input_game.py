import random

# Generate a random integer between 0 and 20
random_number = random.randint(0, 20)

while True:
    # Prompt the user to input a number
    number = int(input("Enter a number between 0 and 20: "))
    
    if number ==random_number:
        print("Done")
        break
    else:
        print("It is not true. Try again.")