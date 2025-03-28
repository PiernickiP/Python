import math

print("What do you want to calculate?\n")
print("Possible operations: +, -, *, /, **, abs, ele.")
user_input = input("Operation: ")
user_input_list = user_input.split(" ")

num1 = int(user_input_list[0])
num2 = int(user_input_list[2])
operator = user_input_list[1]

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Error! We can't divide by 0!")
    else:
        print(f"Result: {num1 / num2}")
elif operator == "**":
    print(f"Result: {num1 ** num2}")
elif operator == "ele":
    print(f"Result: {math.sqrt(num1)}")
elif operator == "abs":
    print(f"Result: {abs(num1)}, {abs(num2)}")
else:
    print("Error! Unknown operator!")