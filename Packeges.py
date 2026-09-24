"""
Modules and Packages - Combined Solutions

This single file demonstrates all 14 questions in one place.
In an actual Python project, modules/packages should be placed in separate files/folders.
"""

import math
import string
from collections import Counter


# ============================================================
# 1. CALCULATOR MODULE (simulated in one file)
# ============================================================

class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b == 0:
            return "Division by zero is not allowed"
        return a / b


# ============================================================
# 2. STUDENT RESULT MODULE
# ============================================================

class StudentModule:
    @staticmethod
    def total_marks(marks):
        return sum(marks)

    @staticmethod
    def percentage(marks):
        if len(marks) == 0:
            return 0
        return sum(marks) / len(marks)

    @staticmethod
    def grade(percent):
        if percent >= 90:
            return "A+"
        elif percent >= 80:
            return "A"
        elif percent >= 70:
            return "B"
        elif percent >= 60:
            return "C"
        elif percent >= 40:
            return "D"
        return "Fail"


# ============================================================
# 3. NUMBER UTILITIES MODULE
# ============================================================

class NumberUtils:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    @staticmethod
    def is_armstrong(n):
        digits = str(n)
        power = len(digits)
        return sum(int(digit) ** power for digit in digits) == n

    @staticmethod
    def is_perfect(n):
        if n <= 1:
            return False
        total = sum(i for i in range(1, n) if n % i == 0)
        return total == n


# ============================================================
# 4. STRING UTILITIES MODULE
# ============================================================

class StringUtils:
    @staticmethod
    def count_vowels(text):
        return sum(1 for ch in text.lower() if ch in "aeiou")

    @staticmethod
    def reverse_string(text):
        return text[::-1]

    @staticmethod
    def is_palindrome(text):
        text = text.lower().replace(" ", "")
        return text == text[::-1]

    @staticmethod
    def count_words(text):
        return len(text.split())

    @staticmethod
    def remove_spaces(text):
        return text.replace(" ", "")


# ============================================================
# 5. EMPLOYEE SALARY MODULE
# ============================================================

class Salary:
    @staticmethod
    def gross_salary(basic, hra, da):
        return basic + hra + da

    @staticmethod
    def deductions(gross):
        return gross * 0.10

    @staticmethod
    def net_salary(gross, deduction):
        return gross - deduction


# ============================================================
# 6. RECURSIVE FUNCTIONS MODULE
# ============================================================

class Recursion:
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * Recursion.factorial(n - 1)

    @staticmethod
    def fibonacci(n):
        if n <= 1:
            return n
        return Recursion.fibonacci(n - 1) + Recursion.fibonacci(n - 2)

    @staticmethod
    def sum_digits(n):
        n = abs(n)
        if n == 0:
            return 0
        return n % 10 + Recursion.sum_digits(n // 10)

    @staticmethod
    def binary(n):
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        return Recursion.binary(n // 2) + str(n % 2)


# ============================================================
# 7. MATHUTILS PACKAGE
# ============================================================

class MathBasic:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b if b != 0 else "Cannot divide by zero"


class MathNumber:
    prime = staticmethod(NumberUtils.is_prime)
    palindrome = staticmethod(NumberUtils.is_palindrome)
    armstrong = staticmethod(NumberUtils.is_armstrong)


class MathStatistics:
    @staticmethod
    def mean(numbers):
        return sum(numbers) / len(numbers)

    @staticmethod
    def maximum(numbers):
        return max(numbers)

    @staticmethod
    def minimum(numbers):
        return min(numbers)


# ============================================================
# 8. STUDENT PACKAGE
# ============================================================

class StudentMarks:
    @staticmethod
    def total(marks):
        return sum(marks)

    @staticmethod
    def percentage(marks):
        return sum(marks) / len(marks)


class StudentGrade:
    calculate_grade = staticmethod(StudentModule.grade)


class Attendance:
    @staticmethod
    def eligible(attended, total):
        if total == 0:
            return False
        return (attended / total) * 100 >= 75


# ============================================================
# 9. BANKING PACKAGE
# ============================================================

class BankingAccount:
    @staticmethod
    def create_account(name, balance):
        return {"name": name, "balance": balance}

    @staticmethod
    def show_balance(account):
        return account["balance"]


class BankingTransaction:
    @staticmethod
    def deposit(account, amount):
        if amount > 0:
            account["balance"] += amount
        return account["balance"]

    @staticmethod
    def withdraw(account, amount):
        if amount > 0 and amount <= account["balance"]:
            account["balance"] -= amount
            return True
        return False


class Loan:
    @staticmethod
    def calculate_interest(amount, rate, years):
        return (amount * rate * years) / 100

    @staticmethod
    def total_loan(amount, rate, years):
        return amount + Loan.calculate_interest(amount, rate, years)


# ============================================================
# 10. TEXTTOOLS PACKAGE
# ============================================================

class Cleaning:
    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans("", "", string.punctuation))

    @staticmethod
    def remove_extra_spaces(text):
        return " ".join(text.split())


class Tokenization:
    @staticmethod
    def tokenize(text):
        return text.split()


class Frequency:
    @staticmethod
    def word_frequency(words):
        return dict(Counter(word.lower() for word in words))


# ============================================================
# 11. COLLEGE PROJECT
# ============================================================

class CollegeStudent:
    @staticmethod
    def student_info(name, roll, branch):
        return f"Name: {name}, Roll No: {roll}, Branch: {branch}"

    @staticmethod
    def student_marks(marks):
        return f"Marks: {marks}"


class Faculty:
    @staticmethod
    def faculty_info(name, department):
        return f"Faculty Name: {name}, Department: {department}"


# ============================================================
# 12. LIBRARY APPLICATION
# ============================================================

class Books:
    @staticmethod
    def display_book(title, author):
        return f"Title: {title}, Author: {author}"

    @staticmethod
    def search_book(book_list, name):
        return name.lower() in [book.lower() for book in book_list]


class Members:
    @staticmethod
    def display_member(name, member_id):
        return f"Name: {name}, Member ID: {member_id}"

    @staticmethod
    def register_member(name):
        return f"{name} registered successfully"


class LibraryTransactions:
    @staticmethod
    def issue_book(book):
        return f"{book} issued successfully"

    @staticmethod
    def return_book(book):
        return f"{book} returned successfully"


# ============================================================
# 13. E-COMMERCE PROJECT
# ============================================================

class Products:
    @staticmethod
    def show_product(name, price):
        return f"Product: {name}, Price: {price}"

    @staticmethod
    def check_stock(quantity):
        return "In Stock" if quantity > 0 else "Out of Stock"


class Customers:
    @staticmethod
    def show_customer(name):
        return f"Customer: {name}"

    @staticmethod
    def register(name):
        return f"{name} registered successfully"


class Orders:
    @staticmethod
    def create_order(product):
        return f"Order created for {product}"

    @staticmethod
    def track_order(order_id):
        return f"Tracking Order ID: {order_id}"


class Payments:
    @staticmethod
    def make_payment(amount):
        return f"Payment successful: {amount}"

    @staticmethod
    def process_refund(amount):
        return f"Refund processed: {amount}"


# ============================================================
# 14. HOSPITAL MANAGEMENT PROJECT
# ============================================================

class Patient:
    @staticmethod
    def patient_info(name, age):
        return f"Patient Name: {name}, Age: {age}"

    @staticmethod
    def admit_patient(name):
        return f"{name} admitted successfully"


class Doctor:
    @staticmethod
    def doctor_info(name, specialization):
        return f"Doctor: {name}, Specialization: {specialization}"

    @staticmethod
    def book_appointment(patient, doctor):
        return f"Appointment booked for {patient} with Dr. {doctor}"


class Billing:
    @staticmethod
    def calculate_bill(room_charge, medicine_charge):
        return room_charge + medicine_charge

    @staticmethod
    def payment_status(amount):
        return f"Payment of {amount} successful"


class MedicalRecords:
    @staticmethod
    def create_record(patient, disease):
        return f"Patient: {patient}, Diagnosis: {disease}"

    @staticmethod
    def prescribe(medicine):
        return f"Medicine prescribed: {medicine}"


# ============================================================
# DEMONSTRATION OF ALL SOLUTIONS
# ============================================================

def main():
    print("=" * 60)
    print("1. CALCULATOR")
    print("=" * 60)
    print("Addition:", Calculator.addition(10, 5))
    print("Subtraction:", Calculator.subtraction(10, 5))
    print("Multiplication:", Calculator.multiplication(10, 5))
    print("Division:", Calculator.division(10, 5))

    print("\n" + "=" * 60)
    print("2. STUDENT RESULT")
    print("=" * 60)
    marks = [85, 90, 78, 88, 92]
    percent = StudentModule.percentage(marks)
    print("Marks:", marks)
    print("Total:", StudentModule.total_marks(marks))
    print("Percentage:", percent)
    print("Grade:", StudentModule.grade(percent))

    print("\n" + "=" * 60)
    print("3. NUMBER UTILITIES")
    print("=" * 60)
    n = 153
    print("Number:", n)
    print("Prime:", NumberUtils.is_prime(n))
    print("Palindrome:", NumberUtils.is_palindrome(n))
    print("Armstrong:", NumberUtils.is_armstrong(n))
    print("Perfect:", NumberUtils.is_perfect(n))

    print("\n" + "=" * 60)
    print("4. STRING UTILITIES")
    print("=" * 60)
    text = "Madam is a good programmer"
    print("Text:", text)
    print("Vowels:", StringUtils.count_vowels(text))
    print("Reverse:", StringUtils.reverse_string(text))
    print("Palindrome:", StringUtils.is_palindrome(text))
    print("Words:", StringUtils.count_words(text))
    print("Without spaces:", StringUtils.remove_spaces(text))

    print("\n" + "=" * 60)
    print("5. EMPLOYEE SALARY")
    print("=" * 60)
    gross = Salary.gross_salary(50000, 10000, 5000)
    deduction = Salary.deductions(gross)
    print("Gross Salary:", gross)
    print("Deductions:", deduction)
    print("Net Salary:", Salary.net_salary(gross, deduction))

    print("\n" + "=" * 60)
    print("6. RECURSIVE FUNCTIONS")
    print("=" * 60)
    n = 5
    print("Factorial of 5:", Recursion.factorial(n))
    print("Fibonacci Series:", [Recursion.fibonacci(i) for i in range(n)])
    print("Sum of digits of 12345:", Recursion.sum_digits(12345))
    print("Binary of 25:", Recursion.binary(25))

    print("\n" + "=" * 60)
    print("7. MATHUTILS PACKAGE")
    print("=" * 60)
    numbers = [10, 20, 30, 40, 50]
    print("Addition:", MathBasic.add(10, 20))
    print("Prime 17:", MathNumber.prime(17))
    print("Armstrong 153:", MathNumber.armstrong(153))
    print("Mean:", MathStatistics.mean(numbers))
    print("Maximum:", MathStatistics.maximum(numbers))
    print("Minimum:", MathStatistics.minimum(numbers))

    print("\n" + "=" * 60)
    print("8. STUDENT PACKAGE")
    print("=" * 60)
    marks = [80, 85, 90, 75, 88]
    percent = StudentMarks.percentage(marks)
    print("Total:", StudentMarks.total(marks))
    print("Percentage:", percent)
    print("Grade:", StudentGrade.calculate_grade(percent))
    print("Attendance Eligible:", Attendance.eligible(80, 100))

    print("\n" + "=" * 60)
    print("9. BANKING PACKAGE")
    print("=" * 60)
    account = BankingAccount.create_account("Arshad", 5000)
    print("Initial Balance:", BankingAccount.show_balance(account))
    BankingTransaction.deposit(account, 2000)
    print("After Deposit:", BankingAccount.show_balance(account))
    BankingTransaction.withdraw(account, 1000)
    print("After Withdrawal:", BankingAccount.show_balance(account))
    print("Total Loan:", Loan.total_loan(100000, 10, 2))

    print("\n" + "=" * 60)
    print("10. TEXTTOOLS PACKAGE")
    print("=" * 60)
    text = "Hello,   world! Hello Python."
    clean = Cleaning.remove_punctuation(text)
    clean = Cleaning.remove_extra_spaces(clean)
    words = Tokenization.tokenize(clean)
    print("Cleaned Text:", clean)
    print("Tokens:", words)
    print("Frequency:", Frequency.word_frequency(words))

    print("\n" + "=" * 60)
    print("11. COLLEGE PROJECT")
    print("=" * 60)
    print(CollegeStudent.student_info("Arshad", 101, "Computer Engineering"))
    print(CollegeStudent.student_marks(85))
    print(Faculty.faculty_info("Rahul Sir", "Computer Engineering"))

    print("\n" + "=" * 60)
    print("12. LIBRARY APPLICATION")
    print("=" * 60)
    books = ["Python", "Java", "C++"]
    print(Books.display_book("Python", "Guido van Rossum"))
    print("Python Found:", Books.search_book(books, "Python"))
    print(Members.display_member("Arshad", 101))
    print(Members.register_member("Arshad"))
    print(LibraryTransactions.issue_book("Python"))
    print(LibraryTransactions.return_book("Python"))

    print("\n" + "=" * 60)
    print("13. E-COMMERCE PROJECT")
    print("=" * 60)
    print(Products.show_product("Laptop", 50000))
    print(Products.check_stock(10))
    print(Customers.show_customer("Arshad"))
    print(Customers.register("Arshad"))
    print(Orders.create_order("Laptop"))
    print(Orders.track_order(1001))
    print(Payments.make_payment(50000))
    print(Payments.process_refund(5000))

    print("\n" + "=" * 60)
    print("14. HOSPITAL MANAGEMENT PROJECT")
    print("=" * 60)
    print(Patient.patient_info("Arshad", 20))
    print(Patient.admit_patient("Arshad"))
    print(Doctor.doctor_info("Patil", "Cardiologist"))
    print(Doctor.book_appointment("Arshad", "Patil"))
    bill = Billing.calculate_bill(5000, 2000)
    print("Total Bill:", bill)
    print(Billing.payment_status(bill))
    print(MedicalRecords.create_record("Arshad", "Fever"))
    print(MedicalRecords.prescribe("Paracetamol"))


if __name__ == "__main__":
    main()
