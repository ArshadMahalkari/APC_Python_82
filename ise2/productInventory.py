"""Product inventory system using a nested dictionary."""


# Product names are keys; each product stores its attributes in another dictionary.
inventory = {
    "Laptop": {
        "price": 55000.0,
        "quantity": 10,
        "category": "Electronics",
    },
    "Notebook": {
        "price": 80.0,
        "quantity": 50,
        "category": "Stationery",
    },
}


def add_product(product_name, price, quantity, category):
    """Add a new product to the inventory."""
    product_name = product_name.strip()
    category = category.strip()

    if not product_name or not category:
        print("Product name and category cannot be empty.")
        return
    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return
    if product_name in inventory:
        print(f"{product_name} already exists in the inventory.")
        return

    inventory[product_name] = {
        "price": float(price),
        "quantity": int(quantity),
        "category": category,
    }
    print(f"{product_name} was added to the inventory.")


def update_stock(product_name, quantity):
    """Update the stock quantity of an existing product."""
    product_name = product_name.strip()

    if product_name not in inventory:
        print(f"{product_name} was not found in the inventory.")
        return
    if quantity < 0:
        print("Quantity cannot be negative.")
        return

    inventory[product_name]["quantity"] = int(quantity)
    print(f"Stock for {product_name} was updated to {quantity}.")


def list_by_category(category):
    """Display all products belonging to a specific category."""
    category = category.strip()
    products = [
        (name, details)
        for name, details in inventory.items()
        if details["category"].lower() == category.lower()
    ]

    if not products:
        print(f"No products found in the category '{category}'.")
        return

    print(f"\nProducts in the {category} category:")
    for name, details in sorted(products):
        print(
            f"{name}: Price = {details['price']:.2f}, "
            f"Quantity = {details['quantity']}, Category = {details['category']}"
        )


def total_inventory_value():
    """Calculate and display the total value of all products in stock."""
    total = sum(
        details["price"] * details["quantity"]
        for details in inventory.values()
    )
    print(f"Total value of items in stock: {total:.2f}")
    return total


def display_inventory():
    """Display all products and their attributes."""
    if not inventory:
        print("The inventory is empty.")
        return

    print("\nProduct Inventory:")
    for name, details in sorted(inventory.items()):
        print(
            f"{name}: Price = {details['price']:.2f}, "
            f"Quantity = {details['quantity']}, Category = {details['category']}"
        )


def read_number(prompt, number_type=float):
    """Read a numeric value and return None when the input is invalid."""
    try:
        return number_type(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    """Run the menu-driven inventory program."""
    while True:
        print("\nProduct Inventory System")
        print("1. Add new product")
        print("2. Update product stock")
        print("3. List products by category")
        print("4. Display total inventory value")
        print("5. Display all products")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter product name: ")
            price = read_number("Enter price: ")
            quantity = read_number("Enter quantity: ", int)
            category = input("Enter category: ")
            if price is not None and quantity is not None:
                add_product(name, price, quantity, category)
        elif choice == "2":
            name = input("Enter product name: ")
            quantity = read_number("Enter new stock quantity: ", int)
            if quantity is not None:
                update_stock(name, quantity)
        elif choice == "3":
            list_by_category(input("Enter category: "))
        elif choice == "4":
            total_inventory_value()
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
