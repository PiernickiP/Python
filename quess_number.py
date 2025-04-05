import random

number = random.randint(0, 20)
print(number)
choice = 0

while (choice != number):
    choice = int(input("Quess the number: \n"))
    if choice < number:
        print("Chosen number is smaller!")
    elif choice == number:
        print("You are right on money!")
    else:
        print("Chosen number is bigger!")