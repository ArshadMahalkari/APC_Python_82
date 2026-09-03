#1. Create student.txt and write student details
from email.mime import text
from importlib.resources import contents

from grpc import Status
from pyparsing import Combine
from pyparsing import Combine
from yfinance import Search

with open("student.txt", "w") as file:
    file.write("Name: Arshad Mahalkari\n")
    file.write("Roll Number: 101\n")
    file.write("Branch: Computer Engineering\n")
    file.write("Semester: 5\n")

print("File created successfully.")


#2. Open a text file and display complete contents
with open("student.txt", "r") as file:
    data = file.read()

print(data)


#3. Append additional information without deleting previous contents
with open("student.txt", "a") as file:
    file.write("\nCollege: ABC College")
    file.write("\nCity: Pune")

print("Information appended successfully.")


#4. Read a file line by line
with open("student.txt", "r") as file:
    for line in file:
        print(line, end="")


#5. Count total number of lines
with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))


#6. Count total number of words
with open("student.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total words:", len(words))


#7. Count total number of characters including spaces
with open("student.txt", "r") as file:
    data = file.read()

print("Total characters:", len(data))


#8. Display lines in reverse order
with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end="")


#9. Count vowels and consonants
with open("student.txt", "r") as file:
    data = file.read().lower()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


#10. Count alphabets, digits, spaces, and special characters
with open("student.txt", "r") as file:
    data = file.read()

alphabets = digits = spaces = special = 0

for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


#11. Find the longest word
with open("student.txt", "r") as file:
    words = file.read().split()

longest = max(words, key=len)

print("Longest word:", longest)


#12. Count occurrences of each word using a dictionary
with open("student.txt", "r") as file:
    words = file.read().lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


#13. Search for a word and display occurrences and line numbers
word = input("Enter word to search: ")

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        occurrences = line.lower().split().count(word.lower())

        if occurrences > 0:
            count += occurrences
            line_numbers.append(line_no)

print("Occurrences:", count)
print("Found in lines:", line_numbers)


#14. Replace a specified word with another word
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    data = file.read()

data = data.replace(old_word, new_word)

with open("modified.txt", "w") as file:
    file.write(data)

print("Word replaced successfully.")


#15. Remove single-line comments from a Python file
with open("program.py", "r") as file:
    lines = file.readlines()

with open("without_comments.py", "w") as new_file:
    for line in lines:
        if "#" in line:
            line = line.split("#")[0]

        new_file.write(line)

print("Comments removed successfully.")

#Note: This simple version may also remove # inside strings.



#16. Create another file containing uppercase text
with open("student.txt", "r") as file:
    data = file.read()

with open("uppercase.txt", "w") as file:
    file.write(data.upper())

print("Uppercase file created successfully.")


#17. Student Records
# Contents of students.txt:
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78

#Program
students = []

with open("students.txt", "r") as file:
    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append({
            "roll": roll,
            "name": name,
            "marks": int(marks)
        })

print("All Records:")
for student in students:
    print(student["roll"], student["name"], student["marks"])

highest = max(students, key=lambda x: x["marks"])
print("\nHighest Marks Student:")
print(highest["name"], "-", highest["marks"])

average = sum(student["marks"] for student in students) / len(students)
print("\nAverage Marks:", average)

print("\nStudents scoring more than 80:")
for student in students:
    if student["marks"] > 80:
        print(student["name"], "-", student["marks"])


#18. Employee Records
# File: employees.txt
# E101,Amit,IT,50000
# E102,Priya,HR,60000
# E103,Rahul,Finance,55000
# Program
def read_employees():
    employee_records = []

    with open("employees.txt", "r") as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(",")

            employee_records.append({
                "id": emp_id,
                "name": name,
                "department": dept,
                "salary": float(salary)
            })

    return employee_records


def display_all(employees):
    for emp in employees:
        print(emp)


def highest_paid(employees):
    emp = max(employees, key=lambda x: x["salary"])
    print("Highest Paid:", emp["name"], emp["salary"])


def average_salary(employees):
    avg = sum(emp["salary"] for emp in employees) / len(employees)
    print("Average Salary:", avg)


def above_salary(employees, amount):
    for emp in employees:
        if emp["salary"] > amount:
            print(emp["name"], emp["salary"])


employees = read_employees()

display_all(employees)
highest_paid(employees)
average_salary(employees)

amount = float(input("Enter salary amount: "))
above_salary(employees, amount)


#19. Student Attendance
# File: attendance.txt

# Format:

# 101,Amit,80,100
# 102,Priya,90,100
# 103,Rahul,70,100

# Format is:

# Format: RollNo,Name,AttendedClasses,TotalClasses
# Program
with open("attendance.txt", "r") as file:
    for line in file:
        roll, name, attended, total = line.strip().split(",")

        attended = int(attended)
        total = int(total)

        percentage = (attended / total) * 100

        print(name, "-", percentage, "%")

        if percentage < 75:
            print("Below 75% attendance:", name)


#20. Deposits and Withdrawals
# File: transactions.txt
# Deposit,5000
# Withdrawal,1200
# Deposit,3000
# Withdrawal,500
# Deposit,2000
# Program
total_deposit = 0
total_withdrawal = 0
largest_transaction = 0

with open("transactions.txt", "r") as file:
    for line in file:
        transaction_type, amount = line.strip().split(",")

        amount = float(amount)

        if transaction_type.lower() == "deposit":
            total_deposit += amount
        elif transaction_type.lower() == "withdrawal":
            total_withdrawal += amount

        if amount > largest_transaction:
            largest_transaction = amount

final_balance = total_deposit - total_withdrawal

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)


#21. Library Book Management

#File: books.txt

#Format:

#BookID,Title,Author,Status

def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")

    with open("books.txt", "a") as file:
        file.write(f"{book_id},{title},{author},Available\n")

    print("Book added successfully.")


def search_book():
    keyword = input("Enter book title or ID: ").lower()

    with open("books.txt", "r") as file:
        for line in file:
            if keyword in line.lower():
                print(line.strip())


def update_status(book_id, new_status):
    books = []

    with open("books.txt", "r") as file:
        books = file.readlines()

    with open("books.txt", "w") as file:
        for line in books:
            data = line.strip().split(",")

            if data[0] == book_id:
                data[3] = new_status

            file.write(",".join(data) + "\n")


def issue_book():
    book_id = input("Enter Book ID: ")
    update_status(book_id, "Issued")
    print("Book issued.")


def return_book():
    book_id = input("Enter Book ID: ")
    update_status(book_id, "Available")
    print("Book returned.")


def display_available():
    with open("books.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[3].lower() == "available":
                print(line.strip())


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        break
    else:
        print("Invalid choice")


#22. Combine contents of two files into a third file
with open("file1.txt", "r") as file1:
    data1 = file1.read()

with open("file2.txt", "r") as file2:
    data2 = file2.read()

with open("combined.txt", "w") as file3:
    file3.write(data1)
    file3.write("\n")
    file3.write(data2)

print("Files combined successfully.")


#23. Compare two files and identify the first different line
with open("file1.txt", "r") as file1:
    lines1 = file1.readlines()

with open("file2.txt", "r") as file2:
    lines2 = file2.readlines()

min_length = min(len(lines1), len(lines2))

for i in range(min_length):
    if lines1[i] != lines2[i]:
        print("Files are different.")
        print("First difference at line:", i + 1)
        print("File 1:", lines1[i].strip())
        print("File 2:", lines2[i].strip())
        break
else:
    if len(lines1) == len(lines2):
        print("Files are identical.")
    else:
        print("Files are different.")
        print("First difference at line:", min_length + 1)