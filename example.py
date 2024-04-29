import datetime

def calculate_birth_year(current_year, age):
    return current_year - age

def main():
    current_year = datetime.datetime.now().year

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    birth_year = calculate_birth_year(current_year, age)

    print(f"Hello {name}! You were born in {birth_year}.")

if __name__ == "__main__":
    main()
