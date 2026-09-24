"""Examples of classes, constructors, methods, and destructors in Python."""

import math


# Problem 1: Create Student objects and display their details and percentage.
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = list(marks)

    def percentage(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def display(self):
        print(
            f"Roll No: {self.roll_no}, Name: {self.name}, "
            f"Marks: {self.marks}, Percentage: {self.percentage():.2f}%"
        )


# Problem 2: Calculate HRA, DA, and gross salary for an employee.
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = float(basic_salary)

    def hra(self):
        return self.basic_salary * 0.20

    def da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.hra() + self.da()


# Problem 3: Calculate the area and perimeter of a rectangle.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = float(length)
        self.breadth = float(breadth)

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Problem 4: Calculate the area and circumference of a circle.
class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# Problem 5: Store and display information for three books.
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = float(price)

    def display(self):
        print(
            f"ID: {self.book_id}, Title: {self.title}, "
            f"Author: {self.author}, Price: ₹{self.price:.2f}"
        )


# Problem 6: Calculate an electricity bill using different unit slabs.
class ElectricityBill:

    def __init__(self, consumer_number, consumer_name, units_consumed):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units_consumed = max(0, float(units_consumed))

    def calculate_bill(self):
        units = self.units_consumed
        bill = 0
        previous_limit = 0
        for limit, rate in ((100, 1.50), (200, 2.50), (500, 4.00), (math.inf, 6.00)):
            slab_units = min(units, limit) - previous_limit
            if slab_units > 0:
                bill += slab_units * rate
            if units <= limit:
                break
            previous_limit = limit
        return bill

    def display(self):
        print(
            f"Consumer: {self.consumer_number} - {self.consumer_name}, "
            f"Units: {self.units_consumed:g}, Bill: ₹{self.calculate_bill():.2f}"
        )


# Problem 7: Display mobile specifications and calculate discounted price.
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = float(price)

    def display_specifications(self):
        print(
            f"Brand: {self.brand}, Model: {self.model}, "
            f"Storage: {self.storage}, Price: ₹{self.price:.2f}"
        )

    def price_after_discount(self, discount_percent):
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100 percent.")
        return self.price * (1 - discount_percent / 100)


# Problem 8: Display patient information and calculate the total bill.
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = float(consultation_fee)

    def total_bill(self):
        return self.consultation_fee

    def display(self):
        print(
            f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
            f"Disease: {self.disease}, Total Bill: ₹{self.total_bill():.2f}"
        )


# Problem 9: Implement an ATM with balance, deposit, withdrawal, and details.
class ATM:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = float(balance)

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def display_account_details(self):
        print(
            f"Account No: {self.account_number}, "
            f"Holder: {self.account_holder}, Balance: ₹{self.balance:.2f}"
        )

    # Problem 9: Run the ATM operations through a menu-driven program.
    def menu(self):
        while True:
            print("\n1. Check balance\n2. Deposit money\n3. Withdraw money")
            print("4. Display account details\n5. Exit")
            choice = input("Enter your choice: ").strip()
            try:
                if choice == "1":
                    print(f"Balance: ₹{self.check_balance():.2f}")
                elif choice == "2":
                    self.deposit(float(input("Enter deposit amount: ")))
                    print("Deposit successful.")
                elif choice == "3":
                    self.withdraw(float(input("Enter withdrawal amount: ")))
                    print("Withdrawal successful.")
                elif choice == "4":
                    self.display_account_details()
                elif choice == "5":
                    print("Thank you for using the ATM.")
                    break
                else:
                    print("Invalid choice.")
            except ValueError as error:
                print(f"Error: {error}")


# Problem 10: Rent and return vehicles and calculate rental charges.
class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate, availability=True):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = float(rental_rate)
        self.availability = availability

    def rent(self):
        if not self.availability:
            raise ValueError("Vehicle is not available.")
        self.availability = False
        print(f"Vehicle {self.vehicle_number} rented successfully.")

    def return_vehicle(self):
        self.availability = True
        print(f"Vehicle {self.vehicle_number} returned successfully.")

    def calculate_rental_charges(self, days):
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        return self.rental_rate * days


# Problem 11: Use a constructor, product methods, total bill, and destructor.
class ShoppingCart:
    # Problem 11: Constructor initializes the customer name and cart ID.
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    # Problem 11: Add a product to the shopping cart.
    def add_product(self, name, price, quantity=1):
        if price < 0 or quantity <= 0:
            raise ValueError("Price cannot be negative and quantity must be positive.")
        self.products.append({"name": name, "price": float(price), "quantity": quantity})

    # Problem 11: Remove a product from the shopping cart.
    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                return
        raise ValueError(f"Product '{name}' was not found.")

    # Problem 11: Calculate the total price of all products.
    def total_bill(self):
        return sum(item["price"] * item["quantity"] for item in self.products)

    # Problem 11: Destructor displays a message when the cart is destroyed.
    def __del__(self):
        print(f"Shopping cart {self.cart_id} for {self.customer_name} destroyed.")


# Problem 12: Calculate a food order bill including tax.
class FoodOrder:
    TAX_RATE = 0.05

    # Problem 12: Constructor initializes all order details.
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = float(price)

    # Problem 12: Calculate subtotal plus tax.
    def total_bill(self):
        subtotal = self.quantity * self.price
        return subtotal + subtotal * self.TAX_RATE

    # Problem 12: Destructor displays the order completion message.
    def __del__(self):
        print(f"Order {self.order_id} for {self.customer_name} completed.")


# Problem 13: Calculate total, percentage, and grade for five subjects.
class StudentResult:
    # Problem 13: Constructor initializes the student and five subject marks.
    def __init__(self, student_name, marks):
        if len(marks) != 5:
            raise ValueError("Exactly five subject marks are required.")
        self.student_name = student_name
        self.marks = list(marks)

    # Problem 13: Calculate marks obtained in all five subjects.
    def total(self):
        return sum(self.marks)

    # Problem 13: Calculate the student's percentage.
    def percentage(self):
        return self.total() / 5

    # Problem 13: Assign a grade based on the percentage.
    def grade(self):
        percentage = self.percentage()
        if percentage >= 90:
            return "A+"
        if percentage >= 80:
            return "A"
        if percentage >= 70:
            return "B"
        if percentage >= 60:
            return "C"
        if percentage >= 50:
            return "D"
        return "F"

    # Problem 13: Destructor displays a message when the result is destroyed.
    def __del__(self):
        print(f"Result record for {self.student_name} destroyed.")


# Demonstration program for Problems 1 through 8 and 10 through 13.
def demonstrate_classes():
    # Problem 1: Create multiple Student objects and display their details.
    print("STUDENTS")
    for student in (Student(1, "Asha", [85, 90, 88]), Student(2, "Ravi", [76, 81, 79])):
        student.display()

    # Problem 2: Create an Employee and display salary components.
    employee = Employee(101, "Neha", 30000)
    print(f"\nEMPLOYEE: HRA ₹{employee.hra():.2f}, DA ₹{employee.da():.2f}, "
          f"Gross ₹{employee.gross_salary():.2f}")

    # Problem 3: Create a Rectangle and display its area and perimeter.
    rectangle = Rectangle(10, 5)
    print(f"RECTANGLE: Area {rectangle.area():.2f}, Perimeter {rectangle.perimeter():.2f}")

    # Problem 4: Create a Circle and display its measurements.
    circle = Circle(7)
    print(f"CIRCLE: Area {circle.area():.2f}, Circumference {circle.circumference():.2f}")

    # Problem 5: Create and display three Book objects.
    print("\nBOOKS")
    for book in (
        Book(1, "Python Basics", "A. Author", 450),
        Book(2, "Object-Oriented Python", "B. Author", 600),
        Book(3, "Learning Programming", "C. Author", 525),
    ):
        book.display()

    # Problem 6: Create an electricity bill and display the calculated amount.
    ElectricityBill("C101", "Maya", 250).display()
    # Problem 7: Display phone specifications and its discounted price.
    phone = MobilePhone("Example", "X1", "128 GB", 30000)
    phone.display_specifications()
    print(f"Discounted price (10%): ₹{phone.price_after_discount(10):.2f}")
    # Problem 8: Display patient information and consultation bill.
    Patient(1, "Arun", 35, "Fever", 500).display()

    # Problem 10: Rent, calculate charges, and return a vehicle.
    vehicle = Vehicle("MH01AB1234", "Sedan", 1500)
    vehicle.rent()
    print(f"Rental charges for 3 days: ₹{vehicle.calculate_rental_charges(3):.2f}")
    vehicle.return_vehicle()

    # Problem 11: Create a cart, add products, and calculate its total.
    cart = ShoppingCart("Maya", "C001")
    cart.add_product("Notebook", 50, 2)
    cart.add_product("Pen", 10, 3)
    print(f"SHOPPING CART total: ₹{cart.total_bill():.2f}")
    # Problem 12: Create an order and calculate the bill including tax.
    order = FoodOrder(1, "Maya", "Pizza", 2, 250)
    print(f"FOOD ORDER total including tax: ₹{order.total_bill():.2f}")
    # Problem 13: Create a result and display total, percentage, and grade.
    result = StudentResult("Maya", [90, 85, 88, 92, 87])
    print(f"RESULT: {result.student_name}, Total {result.total()}, "
          f"Percentage {result.percentage():.2f}%, Grade {result.grade()}")


if __name__ == "__main__":
    # Run demonstrations for all non-interactive problems.
    demonstrate_classes()
    # Problem 9: Create an ATM object and start its menu-driven interface.
    print("\nATM MENU")
    ATM("A1001", "Maya", 5000).menu()
