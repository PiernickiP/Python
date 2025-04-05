user_input = input("Please enter a word: ").lower()

if user_input == user_input[::-1]:
    print(f"{user_input} is a palindrome")
else:
    print(f"{user_input} is not a palindrome")