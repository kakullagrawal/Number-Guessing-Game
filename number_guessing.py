import random

print("**Welcome to NUMBER GUESSING GAME**")

while True:   

    level = input("\n1. easy : 1-100\n2. medium : 1-200\n3. hard : 1-500\nChoose level: ").lower()

    if level == "easy":
        number = random.randint(1, 100)
        max_attempts = 5
    elif level == "medium":
        number = random.randint(1, 200)
        max_attempts = 9
    elif level == "hard":
        number = random.randint(1, 500)
        max_attempts = 13
    else:
        print("Invalid input!")
        continue

    attempts = 0
    print(f"You have {max_attempts} attempts")

    while attempts < max_attempts:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess > number:
            print("Try lower!")
        elif guess < number:
            print("Try higher!")
        else:
            print(f"You win in {attempts} attempts!")
            break
    else:
        print(f"You lost! Number was {number}")

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break