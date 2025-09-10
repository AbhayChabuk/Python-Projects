import random
number_range = input("Enter a number till you want to guess: ")

if number_range.isdigit():
    number_range = int(number_range)
    if number_range <= 0:
        print("Pls, type a number greater than 0")
        quit()
else:
    print("Pls, type a number next time")
    quit()

random_number  = random.randint(0, number_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("\nGuess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Pls, type a number next time")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    else:
        if user_guess > random_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

print("\nYou got it in", guesses, "guesses")