import math

number_a = int(input("Please enter first number: "))
number_b = int(input("Please enter second number: "))

print("Choose number of operation \n")
print("1.Addition\n")
print("2.Subtraction\n")
print("3.Multiplication\n")
print("4.Division\n")
print("5.Exponentiation\n")
print("6.Elementalization\n")
print("7.Absolute value\n")

choice = str(input())

match(choice):
    case ("1"):
        summary = number_a + number_b
        print(f"Result of summing {number_a} + {number_b} is {summary}")
    case ("2"):
        subtraction = number_a - number_b
        print(f"Result of subtracting {number_a} - {number_b} is {subtraction}")
    case ("3"):
        multiplication = number_a * number_b
        print(f"Result of multiplication {number_a} * {number_b} is {multiplication}")
    case ("4"):
        if number_b == 0:
            print("Error! We can't devise by 0!")
        else:
            division = number_a / number_b
            print(f"Result of division {number_a} / {number_b} is {division}")
    case ("5"):
        exponentiation = number_a ** number_b
        print(f"Result of exponentition {number_a} ^ {number_b} is {exponentiation}")
    case ("6"):
        elementation = math.sqrt(number_a)
        print(f"Result of elementation {number_a} is {elementation}")
    case ("7"):
        absolute1 = abs(number_a)
        absolute2 = abs(number_b)
        print(f"Absolute nmubers of {number_a} and {number_b} are {absolute1} and {absolute2}")