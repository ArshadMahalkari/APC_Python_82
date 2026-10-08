"""Store and manage countries and their capitals using a dictionary."""


# Dictionary containing country names as keys and capitals as values.
country_capitals = {
    "India": "New Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
}


def add_country(country, capital):
    """Add a new country-capital pair to the dictionary."""
    country = country.strip()
    capital = capital.strip()

    if not country or not capital:
        print("Country and capital cannot be empty.")
        return
    if country in country_capitals:
        print(f"{country} already exists. Use the update option to change it.")
        return

    country_capitals[country] = capital
    print(f"{country} and its capital {capital} were added.")


def search_capital(country):
    """Search for and display the capital of a given country."""
    country = country.strip()
    capital = country_capitals.get(country)

    if capital is None:
        print(f"Country '{country}' was not found.")
    else:
        print(f"The capital of {country} is {capital}.")
    return capital


def display_all_countries():
    """Display every country and its capital."""
    if not country_capitals:
        print("The dictionary is empty.")
        return

    print("\nCountries and their capitals:")
    for country, capital in sorted(country_capitals.items()):
        print(f"{country}: {capital}")


def update_capital(country, new_capital):
    """Update the capital of an existing country."""
    country = country.strip()
    new_capital = new_capital.strip()

    if country not in country_capitals:
        print(f"Country '{country}' was not found.")
        return
    if not new_capital:
        print("The new capital cannot be empty.")
        return

    country_capitals[country] = new_capital
    print(f"The capital of {country} was updated to {new_capital}.")


def main():
    """Run a menu-driven country-capital program."""
    while True:
        print("\nCountry-Capital Dictionary")
        print("1. Add a country and capital")
        print("2. Search for a capital")
        print("3. Display all countries and capitals")
        print("4. Update a capital")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            country = input("Enter country: ")
            capital = input("Enter capital: ")
            add_country(country, capital)
        elif choice == "2":
            country = input("Enter country to search: ")
            search_capital(country)
        elif choice == "3":
            display_all_countries()
        elif choice == "4":
            country = input("Enter country to update: ")
            new_capital = input("Enter new capital: ")
            update_capital(country, new_capital)
        elif choice == "5":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
