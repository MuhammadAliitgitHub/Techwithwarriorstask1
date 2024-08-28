# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        # Taking integer input from the user
        num = int(input("Enter an integer: "))
        result = check_even_odd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        # Handling the case where input is not an integer
        print("Please enter a valid integer.")


main()

