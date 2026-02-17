import random

print("\nNumber Guessing Game...")
random_number = random.randint(1,100)
attempts = 0
while True:
    try:
        choice = int(input("Enter a number (1-100): "))
    except ValueError:
        print("Invalid Input!")
        continue
    attempts+=1
    
    if choice == random_number:
        print(f"Congratulations you guessed it right in {attempts} attempts, it's {random_number}")
        break
    elif choice > random_number:
        print("Too High")
    elif choice < random_number:
        print("Too Low")