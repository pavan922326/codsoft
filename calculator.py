def add(x, y):        return x + y
def subtract(x, y):   return x - y
def multiply(x, y):   return x * y
def divide(x, y):     return x / y

def calculator():
    while True:
        print("\nChoose operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
        choice = input("Enter 1‑5: ")
        if choice == '5':
            print("Goodbye!")
            break
        if choice not in ('1','2','3','4'):
            print("Invalid choice.")
            continue
        try:
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == '1': print(f"{n1} + {n2} = {add(n1, n2)}")
        elif choice == '2': print(f"{n1} - {n2} = {subtract(n1, n2)}")
        elif choice == '3': print(f"{n1} * {n2} = {multiply(n1, n2)}")
        elif choice == '4':
            if n2 != 0:
                print(f"{n1} / {n2} = {divide(n1, n2)}")
            else:
                print("Cannot divide by zero.")
