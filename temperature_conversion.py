print("Choose operation:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

user_choice = input("Please choose an option (1 or 2): ")

match user_choice:
    case "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32  
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
    case "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9  
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
    case _:
        print("Invalid option. Please choose 1 or 2.")
        