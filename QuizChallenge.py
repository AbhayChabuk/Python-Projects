print("Welcome to Quiz Challenge")

enter = input("What you like to play? ")
if enter.lower() != "yes":
    print("Thank you for playing")
    exit()

print("\nLets Play Quiz! ")
score = 15

answer = input("\nWhat does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")
    score -= 5

answer = input("\nWhat is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
    score -= 5

answer = input("\nWhat is the full form of GPU? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    score -= 5


print("\nscore = " + str(score))
print("Hence you got " + str(score) + " points!")

if score == 15:
    print("All  correct answers!")
elif score == 10:
    print("2 correct answer!")
elif score == 5:
    print("1 Correct answer!")
else:
    print("No correct answer!")

print("\npercentage= " + str((score / 15) * 100))
print("Hence you got " + str((score / 15) * 100) + "%.")




