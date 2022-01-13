import random

range_number = input("Please enter a number to select the range: ")



if range_number.isdigit():
    range_number = int(range_number)
    random_number = random.randint(0, range_number)
else:
    print("Please select valid numbers only")
    quit()

guess_count = 0

while True:
    guess_count += 1
    guess_number = input("Guess a number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Please enter valid number")
        continue
    if guess_number == random_number:
        print("You got it right!")
        break
    
    elif guess_number > random_number:
        print("Guest a lower number!")
    else:
        print("Guest a higher number!")
    
print("You have taken", guess_count, "guesses!")