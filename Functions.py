


# 1. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("1. Factorial:", factorial(5))


# 2. Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print("2. Even/Odd:", check_even_odd(10))


# 3. Greater of Two Numbers
def greater(a, b):
    if a > b:
        return a
    return b

print("3. Greater:", greater(20, 15))


# 4. Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

print("4. Simple Interest:", simple_interest(10000, 5, 2))


# 5. Prime Number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print("5. Prime:", is_prime(7))


# 6. Area of Circle
def area_circle(r):
    return 3.14 * r * r

print("6. Area:", area_circle(5))


# 7. Sum of First n Natural Numbers
def natural_sum(n):
    return n * (n + 1) // 2

print("7. Natural Sum:", natural_sum(10))


# 8. Power
def power(base, exponent):
    return base ** exponent

print("8. Power:", power(2, 5))


# 9. Largest Without max()
def largest(numbers):
    large = numbers[0]

    for n in numbers:
        if n > large:
            large = n

    return large

print("9. Largest:", largest([10, 50, 20, 40, 30]))


# 10. Count Vowels
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

print("10. Vowels:", count_vowels("Hello Python"))


# 11. Reverse String
def reverse_string(text):
    return text[::-1]

print("11. Reverse:", reverse_string("Python"))


# 12. Palindrome
def palindrome(value):
    value = str(value)

    return value == value[::-1]

print("12. Palindrome:", palindrome("madam"))


# 13. Average
def average(numbers):
    return sum(numbers) / len(numbers)

print("13. Average:", average([10, 20, 30, 40, 50]))


# 14. Count Occurrence
def occurrence(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count += 1

    return count

print("14. Occurrence:", occurrence([10, 20, 10, 30, 10], 10))


# 15. Unique Elements
def unique(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

print("15. Unique:", unique([10, 20, 10, 30, 20, 40]))


# 16. Second Largest
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]

print("16. Second Largest:", second_largest([10, 50, 20, 40, 30]))


# 17. Fibonacci
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

print("17. Fibonacci:", fibonacci(7))


# 18. Percentage and Grade
def student_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = [80, 85, 90, 75, 88]
print("18. Percentage/Grade:", student_result(marks))


# 19. Electricity Bill
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

print("19. Electricity Bill:", electricity_bill(250))


# 20. Gross Salary
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    return basic + hra + da

print("20. Gross Salary:", gross_salary(30000))


# 21. Shopping Bill
def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

prices = [1000, 500, 200]
quantities = [2, 1, 3]

print("21. Shopping Bill:", total_bill(prices, quantities))


# 22. Minimum, Maximum, Sum and Average
def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = total / len(numbers)

    return minimum, maximum, total, avg

print("22. Calculate:", calculate([10, 20, 30, 40, 50]))


# 23. Student Records
def student_result2(name, roll, marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return name, roll, total, percentage, grade


students = [
    ("Amit", 1, [80, 85, 90, 75, 88]),
    ("Rahul", 2, [70, 75, 72, 68, 80]),
    ("Neha", 3, [90, 92, 88, 95, 91])
]

results = []

for student in students:
    results.append(
        student_result2(student[0], student[1], student[2])
    )

print("23. Student Records:")
for result in results:
    print(result)


# 24. Bank Account
balance = 10000
history = []


def deposit(amount):
    global balance
    balance += amount
    history.append("Deposit: " + str(amount))


def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        history.append("Withdraw: " + str(amount))
    else:
        print("Insufficient Balance")


def enquiry():
    return balance


def transactions():
    return history


deposit(2000)
withdraw(3000)

print("24. Balance:", enquiry())
print("Transactions:", transactions())


# 25. Library Management
books = {
    "Python": True,
    "Java": True,
    "C++": True
}


def add_book(book):
    books[book] = True


def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book issued:", book)
    else:
        print("Book not available")


def return_book(book):
    if book in books:
        books[book] = True
        print("Book returned:", book)


def search_book(book):
    if book in books:
        print("Book found:", book)
    else:
        print("Book not found")


def display_books():
    print("Available Books:")
    for book in books:
        if books[book]:
            print(book)


add_book("HTML")
issue_book("Python")
return_book("Python")
search_book("Java")

print("25.")
display_books()


# 26. Electricity Bill with Fixed Charges, Tax and Discount
def electricity_bill2(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 500 + (units - 100) * 7
    else:
        bill = 1200 + (units - 200) * 10

    fixed_charge = 100
    tax = bill * 0.05

    total = bill + fixed_charge + tax

    if total > 3000:
        total = total - total * 0.05

    return total

print("26. Final Electricity Bill:", electricity_bill2(300))


# 27. Hospital Bill
def consultation():
    return 500


def laboratory():
    return 1000


def medicine():
    return 1500


def room():
    return 2000


def final_hospital_bill(category):
    total = consultation() + laboratory() + medicine() + room()

    if category == "senior":
        total -= total * 0.20
    elif category == "child":
        total -= total * 0.10

    return total


print("27. Hospital Bill:", final_hospital_bill("senior"))


# 28. Shopping Cart
cart = []


def add_product(name, price):
    cart.append([name, price])


def remove_product(name):
    for item in cart:
        if item[0] == name:
            cart.remove(item)


def subtotal():
    total = 0

    for item in cart:
        total += item[1]

    return total


def final_invoice(coupon):
    total = subtotal()

    if coupon == "SAVE10":
        total -= total * 0.10

    gst = total * 0.18

    return total + gst


add_product("Laptop", 50000)
add_product("Mouse", 1000)

print("28. Subtotal:", subtotal())
print("Final Invoice:", final_invoice("SAVE10"))


# 29. Recursive Binary Search
def binary_search(numbers, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == key:
        return mid
    elif key < numbers[mid]:
        return binary_search(numbers, low, mid - 1, key)
    else:
        return binary_search(numbers, mid + 1, high, key)


numbers = [10, 20, 30, 40, 50]

print("29. Binary Search:",
      binary_search(numbers, 0, len(numbers) - 1, 30))


# 30. Decimal to Binary Using Recursion
def decimal_binary(n):
    if n == 0:
        return ""

    return decimal_binary(n // 2) + str(n % 2)


n = 10

if n == 0:
    print("30. Binary: 0")
else:
    print("30. Binary:", decimal_binary(n))


# 31. Recursive Palindrome
def recursive_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return recursive_palindrome(text[1:-1])


print("31. Recursive Palindrome:",
      recursive_palindrome("madam"))


# 32. Functions as Arguments
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate_operation(a, b, operation):
    return operation(a, b)


print("32. Add:", calculate_operation(10, 5, add))
print("Subtract:", calculate_operation(10, 5, subtract))
print("Multiply:", calculate_operation(10, 5, multiply))
print("Divide:", calculate_operation(10, 5, divide))



# LAMBDA FUNCTIONS



# 33. Square
square = lambda x: x * x

print("33. Square:", square(5))


# 34. Cube
cube = lambda x: x ** 3

print("34. Cube:", cube(3))


# 35. Even
even = lambda x: x % 2 == 0

print("35. Even:", even(10))


# 36. Maximum of Two
maximum = lambda a, b: a if a > b else b

print("36. Maximum:", maximum(10, 20))


# 37. Simple Interest
simple_interest_lambda = lambda p, r, t: (p * r * t) / 100

print("37. Simple Interest:",
      simple_interest_lambda(10000, 5, 2))


# 38. Squares using map()
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("38. Squares:", squares)


# 39. Cubes using map()
numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda x: x ** 3, numbers))

print("39. Cubes:", cubes)


# 40. Sum of Two Lists using map()
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

result = list(map(lambda x, y: x + y, a, b))

print("40. Sum of Lists:", result)



# FILTER AND SORTED



# 41. Even Numbers using filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("41. Even Numbers:", even_numbers)


# 42. Prime Numbers using filter()
def prime_check(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(
    filter(prime_check, numbers)
)

print("42. Prime Numbers:", prime_numbers)


# 43. Positive Numbers
numbers = [-5, 10, -2, 8, -7, 20]

positive = list(
    filter(lambda x: x > 0, numbers)
)

print("43. Positive Numbers:", positive)


# 44. Numbers Greater Than 50
numbers = [20, 60, 45, 80, 30, 90]

greater_50 = list(
    filter(lambda x: x > 50, numbers)
)

print("44. Greater Than 50:", greater_50)


# 45. Words More Than 5 Characters
words = [
    "apple",
    "banana",
    "cat",
    "elephant",
    "computer"
]

long_words = list(
    filter(lambda x: len(x) > 5, words)
)

print("45. Long Words:", long_words)


# 46. Sort Words by Length
words = [
    "apple",
    "cat",
    "elephant",
    "dog",
    "banana"
]

sorted_words = sorted(
    words,
    key=lambda x: len(x)
)

print("46. Sorted Words:", sorted_words)


# 47. Sort Students by Marks
students = [
    ("Amit", 85),
    ("Rahul", 70),
    ("Neha", 95),
    ("Priya", 80)
]

sorted_students = sorted(
    students,
    key=lambda x: x[1]
)

print("47. Students by Marks:", sorted_students)


# 48. Sort Employees by Salary
employees = [
    ("Amit", 40000),
    ("Rahul", 60000),
    ("Neha", 50000),
    ("Priya", 70000)
]

sorted_employees = sorted(
    employees,
    key=lambda x: x[1]
)

print("48. Employees by Salary:", sorted_employees)


# 49. Student Marks
students = [
    ("Amit", 80),
    ("Rahul", 65),
    ("Neha", 90),
    ("Priya", 75)
]

# Average
average_marks = sum(
    map(lambda x: x[1], students)
) / len(students)

# Above 75
above_75 = list(
    filter(lambda x: x[1] > 75, students)
)

# Sort
sorted_students = sorted(
    students,
    key=lambda x: x[1]
)

print("49. Average:", average_marks)
print("Above 75:", above_75)
print("Sorted:", sorted_students)


# 50. Employee Records
employees = [
    ("Amit", "IT", 45000),
    ("Rahul", "HR", 60000),
    ("Neha", "IT", 75000),
    ("Priya", "Sales", 50000)
]

# Salary more than 50000
high_salary = list(
    filter(lambda x: x[2] > 50000, employees)
)

# Increase salary by 10%
increased_salary = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10),
        employees)
)

# Sort by salary
sorted_employees = sorted(
    employees,
    key=lambda x: x[2]
)

print("50. High Salary:", high_salary)
print("10% Increased:", increased_salary)
print("Sorted Employees:", sorted_employees)


# 51. Products
products = [
    ("Laptop", 50000, 1),
    ("Mouse", 500, 2),
    ("Mobile", 20000, 2),
    ("Keyboard", 1500, 1)
]

# Total value
total_value = list(
    map(lambda x: (x[0], x[1] * x[2]), products)
)

# Products costing more than 1000
above_1000 = list(
    filter(lambda x: x[1] > 1000, total_value)
)

# Sort according to total value
sorted_products = sorted(
    total_value,
    key=lambda x: x[1]
)

print("51. Total Value:", total_value)
print("Above 1000:", above_1000)
print("Sorted Products:", sorted_products)


# 52. Words
words = [
    "apple",
    "banana",
    "cat",
    "elephant",
    "computer",
    "dog"
]

# Length of every word
lengths = list(
    map(lambda x: len(x), words)
)

# Words having more than 5 characters
long_words = list(
    filter(lambda x: len(x) > 5, words)
)

# Sort according to length
sorted_words = sorted(
    words,
    key=lambda x: len(x)
)

print("52. Word Lengths:", lengths)
print("Long Words:", long_words)
print("Sorted Words:", sorted_words)
