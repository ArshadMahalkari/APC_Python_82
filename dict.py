print("Question 1:")
#1. Create a dictionary containing student details such as roll number,
#name, department, and marks. Display all key-value pairs.
student={"Roll Number":101,"Name":"Rahul","Department":"CSE","Marks":85}
for key,value in student.items():
    print(key,":",value)






print("\nQuestion 2:")
#2. Create a dictionary containing employee information and display
#the value associated with a specified key.
employee={"ID":101,"Name":"Amit","Department":"IT","Salary":40000}
print("Employee Name:",employee["Name"])







print("\nQuestion 3:")
#3. Create a dictionary of five products and their prices.
#Add a new product and price to the dictionary.
products={"Pen":10,"Book":50,"Bag":500,"Pencil":5,"Bottle":100}
products["Eraser"]=8
print("Products:",products)





print("\nQuestion 4:")
#4. Create a dictionary containing student marks.
#Update the marks of a specified student.
marks={"Rahul":80,"Priya":75,"Amit":90,"Sneha":85}
marks["Priya"]=88
print("Updated marks:",marks)




print("\nQuestion 5:")
#5. Create a dictionary of cities and their populations.
#Remove a specified city from the dictionary.
cities={
    "Pune":7000000,
    "Mumbai":20000000,
    "Delhi":19000000,
    "Kolhapur":500000
}
del cities["Delhi"]
print("Dictionary after removing city:",cities)





print("\nQuestion 6:")
#6. Create a dictionary of employee IDs and names.
#Ask the user for an employee ID and check whether it exists.
employee={
    101:"Rahul",
    102:"Priya",
    103:"Amit",
    104:"Sneha"
}
id=int(input("Enter employee ID: "))
if id in employee:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")






print("\nQuestion 7:")
#7. Create a dictionary containing student records and find
#the total number of key-value pairs.
student={
    "Roll Number":101,
    "Name":"Rahul",
    "Department":"CSE",
    "Marks":85
}
print("Total number of key-value pairs:",len(student))






print("\nQuestion 8:")
#8. Create a dictionary and display:
#All keys
#All values
#All key-value pairs
student={
    "Name":"Rahul",
    "Age":20,
    "Department":"CSE",
    "Marks":85
}
print("All keys:",student.keys())
print("All values:",student.values())
print("All key-value pairs:",student.items())






print("\nQuestion 9:")
#9. Create a dictionary of programming languages and their creators.
#Display each key and value using a loop.
languages={
    "Python":"Guido van Rossum",
    "C++":"Bjarne Stroustrup",
    "Java":"James Gosling",
    "JavaScript":"Brendan Eich"
}
for key,value in languages.items():
    print(key,":",value)





print("\nQuestion 10:")
#10. Accept five student names and their marks from the user
#and store them in a dictionary.
student={}
for i in range(5):
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))
    student[name]=marks
print("Student dictionary:",student)


print("\nQuestion 11:")
#11. Create a dictionary containing student names and marks.
#Find the student who has scored the highest marks.
marks={
    "Rahul":85,
    "Priya":92,
    "Amit":78,
    "Sneha":88
}
highest=0
student_name=""
for name,mark in marks.items():
    if mark>highest:
        highest=mark
        student_name=name
print("Student with highest marks:",student_name)
print("Highest marks:",highest)






print("\nQuestion 12:")
#12. Create a dictionary containing student names and marks.
#Find the student with the lowest marks.
marks={
    "Rahul":85,
    "Priya":92,
    "Amit":78,
    "Sneha":88
}
lowest=100
student_name=""
for name,mark in marks.items():
    if mark<lowest:
        lowest=mark
        student_name=name
print("Student with lowest marks:",student_name)
print("Lowest marks:",lowest)





print("\nQuestion 13:")
#13. Create a dictionary containing student names and marks.
#Calculate the average marks of all students.
marks={
    "Rahul":85,
    "Priya":92,
    "Amit":78,
    "Sneha":88
}
sum1=0
for mark in marks.values():
    sum1=sum1+mark
average=sum1/len(marks)
print("Average marks:",average)





print("\nQuestion 14:")
#14. Accept a string from the user and create a dictionary
#containing each character and its frequency.
string=input("Enter a string: ")
frequency={}
for character in string:
    if character in frequency:
        frequency[character]=frequency[character]+1
    else:
        frequency[character]=1
print("Character frequency:",frequency)






print("\nQuestion 15:")
#15. Accept a sentence and create a dictionary containing
#each word and the number of times it occurs.
sentence=input("Enter a sentence: ")
words=sentence.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]=frequency[word]+1
    else:
        frequency[word]=1
print("Word frequency:",frequency)





print("\nQuestion 16:")
#16. Create two dictionaries and merge them into a single dictionary.
dict1={
    "A":10,
    "B":20,
    "C":30
}
dict2={
    "D":40,
    "E":50,
    "F":60
}
dict3=dict1.copy()
dict3.update(dict2)
print("Merged dictionary:",dict3)





print("\nQuestion 17:")
#17. Given two dictionaries, find the keys that are common
#to both dictionaries.
dict1={
    "A":10,
    "B":20,
    "C":30
}
dict2={
    "B":40,
    "C":50,
    "D":60
}
print("Common keys:")
for key in dict1:
    if key in dict2:
        print(key)





print("\nQuestion 18:")
#18. Given two dictionaries, identify the values that are common
#to both dictionaries.
dict1={
    "A":10,
    "B":20,
    "C":30
}
dict2={
    "D":20,
    "E":30,
    "F":40
}
print("Common values:")
for value in dict1.values():
    if value in dict2.values():
        print(value)





print("\nQuestion 19:")
#19. Create a dictionary containing duplicate values and remove
#duplicate values while retaining the corresponding keys.
dict1={
    "A":10,
    "B":20,
    "C":10,
    "D":30,
    "E":20
}
dict2={}
for key,value in dict1.items():
    if value not in dict2.values():
        dict2[key]=value
print("Dictionary after removing duplicate values:",dict2)






print("\nQuestion 20:")
#20. Create a dictionary and display its elements in ascending order of keys.
dict1={
    4:"D",
    2:"B",
    1:"A",
    5:"E",
    3:"C"
}
keys=list(dict1.keys())
keys.sort()
for key in keys:
    print(key,":",dict1[key])





print("\nQuestion 21:")
#21. Create a dictionary containing numbers from 1 to 10 as keys
#and their squares as values.
square={}
for number in range(1,11):
    square[number]=number*number
print(square)







print("\nQuestion 22:")
#22. Create a dictionary containing numbers from 1 to 20 as keys
#and their squares as values, but include only even numbers.
square={}
for number in range(1,21):
    if number%2==0:
        square[number]=number*number
print(square)








print("\nQuestion 23:")
#23. Given a list of numbers, create a dictionary containing
#each unique number and its frequency.
numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}
for number in numbers:
    if number in frequency:
        frequency[number]=frequency[number]+1
    else:
        frequency[number]=1
print("Frequency:",frequency)












print("\nQuestion 24:")
#24. Create a dictionary containing integers from 1 to 10 and their cubes.
cube={}
for number in range(1,11):
    cube[number]=number*number*number
print(cube)












print("\nQuestion 25:")
#25. Create a dictionary containing student names and marks.
#Develop a program to:
#Add a student
#Update marks
#Delete a student
#Search for a student
#Display all students
#Find the highest marks
#Calculate the average
students={
    "Rahul":85,
    "Priya":90,
    "Amit":78
}
students["Sneha"]=88
students["Rahul"]=92
del students["Amit"]
name=input("Enter student name to search: ")
if name in students:
    print("Student found")
    print("Marks:",students[name])
else:
    print("Student not found")
print("All students:")
for name,mark in students.items():
    print(name,":",mark)
highest=0
for mark in students.values():
    if mark>highest:
        highest=mark
print("Highest marks:",highest)
sum1=0
for mark in students.values():
    sum1=sum1+mark
average=sum1/len(students)
print("Average marks:",average)









print("\nQuestion 26:")
#26. Create a dictionary containing employee names and salaries.
#Find:
#Highest salary
#Lowest salary
#Average salary
#Employees earning more than Rs. 50,000
salary={
    "Rahul":45000,
    "Priya":60000,
    "Amit":75000,
    "Sneha":40000
}
highest=0
lowest=salary["Rahul"]
sum1=0
for name,sal in salary.items():
    sum1=sum1+sal
    if sal>highest:
        highest=sal
    if sal<lowest:
        lowest=sal
average=sum1/len(salary)
print("Highest salary:",highest)
print("Lowest salary:",lowest)
print("Average salary:",average)
print("Employees earning more than Rs. 50,000:")
for name,sal in salary.items():
    if sal>50000:
        print(name,":",sal)











print("\nQuestion 27:")
#27. Create a dictionary containing product names and quantities.
#Perform:
#Add a product
#Update quantity
#Delete a product
#Search for a product
#Display products with quantity below 10
products={
    "Pen":20,
    "Book":15,
    "Pencil":8,
    "Bag":5
}
products["Bottle"]=12
products["Pen"]=25
del products["Book"]
name=input("Enter product name to search: ")
if name in products:
    print("Product found")
    print("Quantity:",products[name])
else:
    print("Product not found")
print("Products with quantity below 10:")
for name,quantity in products.items():
    if quantity<10:
        print(name,":",quantity)










print("\nQuestion 28:")
#28. Create a dictionary containing names and phone numbers.
#Implement:
#Add contact
#Search contact
#Update contact
#Delete contact
#Display all contacts
contacts={
    "Rahul":"9876543210",
    "Priya":"9876543211",
    "Amit":"9876543212"
}
contacts["Sneha"]="9876543213"
name=input("Enter name to search: ")
if name in contacts:
    print("Phone number:",contacts[name])
else:
    print("Contact not found")
contacts["Rahul"]="9999999999"
del contacts["Amit"]
print("All contacts:")
for name,phone in contacts.items():
    print(name,":",phone)








print("\nQuestion 29:")
#29. Create a dictionary containing book IDs and book names.
#Implement:
#Add a book
#Search a book
#Remove a book
#Display all books
#Count total books
books={
    101:"Python",
    102:"Java",
    103:"C++"
}
books[104]="Data Structures"
id=int(input("Enter book ID to search: "))

if id in books:
    print("Book name:",books[id])
else:
    print("Book not found")
del books[103]
#Display all books
print("All books:")
for id,name in books.items():
    print(id,":",name)
#Count total books
print("Total books:",len(books))









print("\nQuestion 30:")
#30. Take a dictionary containing student names and their departments.
#Create a new dictionary that groups students according to their department.
students={
    "Rahul":"CSE",
    "Priya":"IT",
    "Amit":"CSE",
    "Sneha":"ECE",
    "Neha":"IT"
}
department={}
for name,dept in students.items():
    if dept in department:
        department[dept].append(name)
    else:
        department[dept]=[name]
print("Students grouped by department:")
for dept,names in department.items():
    print(dept,":",names)






print("\nQuestion 31:")
#31. Take a list of words, create a dictionary where the key is
#the word length and the value is a list of words having that length.
words=["cat","dog","apple","bat","mango","banana"]
word_dict={}
for word in words:
    length=len(word)
    if length in word_dict:
        word_dict[length].append(word)
    else:
        word_dict[length]=[word]
print("Words grouped by length:",word_dict)











print("\nQuestion 32:")
#32. Take a list of integers and a target value, find two numbers
#whose sum is equal to the target using a dictionary.
numbers=[2, 7, 11, 15]
target=9
number_dict={}
for number in numbers:
    required=target-number
    if required in number_dict:
        print("Two numbers are:",required,"and",number)
        break
    number_dict[number]=number










print("\nQuestion 33:")
#33. Take a string, use a dictionary to find the first character
#that occurs only once.
string=input("Enter a string: ")
frequency={}
for character in string:
    if character in frequency:
        frequency[character]=frequency[character]+1
    else:
        frequency[character]=1
for character in string:
    if frequency[character]==1:
        print("First character occurring only once:",character)
        break








print("\nQuestion 34:")
#34. Take a string, use a dictionary to find the first character
#that occurs more than once.
string=input("Enter a string: ")
frequency={}
for character in string:
    if character in frequency:
        frequency[character]=frequency[character]+1
    else:
        frequency[character]=1
for character in string:
    if frequency[character]>1:
        print("First character occurring more than once:",character)
        break









print("\nQuestion 35:")
#35. Accept a paragraph and create a dictionary where:
#Key = word length
#Value = number of words having that length
paragraph=input("Enter a paragraph: ")
words=paragraph.split()
length_dict={}
for word in words:
    length=len(word)
    if length in length_dict:
        length_dict[length]=length_dict[length]+1
    else:
        length_dict[length]=1
print("Word length frequency:",length_dict)