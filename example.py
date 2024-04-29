import datetime

def calculate_birth_year(current_year, age):
    return current_year - age

def main():
    # Get current year
    current_year = datetime.datetime.now().year

    # Get user input for name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate birth year
    birth_year = calculate_birth_year(current_year, age)

    # Print greeting message with birth year
    print(f"Hello {name}! You were born in {birth_year}.")

if __name__ == "__main__":
    main()
