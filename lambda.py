try:
    value_to_add = float(input("Enter a number to add to 25: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

add_25 = lambda x: x + 25

result = add_25(value_to_add)

print(f"Result: {result}")

