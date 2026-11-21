import random

print("Hey Hii.. Welcome to the simple timepass game")

# Generate the system value once
sys_val = random.randint(10, 15)

max_attempts = 5
attempt = 0

while attempt < max_attempts:

    user_input = int(input("Enter your choice between 10 and 15 to check your luck: "))

    # Validate input
    if user_input < 10 or user_input > 15:
        print("You are not following the rules... Between 10 and 15 only.")
        print("Try again...")
        attempt += 1
        continue

    # Check guess
    if user_input == sys_val:
        print("Congrats! Your guess is correct..")
        print("You got Rs. 10/- Enjoy the day..")
        break

    else:
        attempt += 1

        if attempt < max_attempts:
            print(f"Better luck next time. Try again... ({max_attempts - attempt} attempts left)")
        else:
            print("Game over! Visit again.")

print("Thanks!... See you again!")