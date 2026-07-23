#1. read the value
n = int(input("Enter a number: "))
if n == 0:
    print("Zero")
else:
    print("Non Zero")


#2.lagerst of two nums
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First number is larger")
elif b > a:
    print("Second number is larger")
else:
    print("Both numbers are equal")

#3.positive or negative
x = int(input("Enter a number: "))
if x > 0 :
    print("positive")
elif x < 0:
    print("Negative")
else:
    print("zero")

#4. Vowel or consonent
c = input("enter a char")
if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
    print("vowel")
else:
    print("consonent")

##average progrmas
#1. Student peformance
marks = int(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    print("A grade")
elif marks >= 80 and marks < 90:
    print("B grade")
elif marks >= 70 and marks < 80:
    print("C grade")
elif marks >= 60 and marks < 70:
    print("D grade")
else:
    print("Fail")

#2. largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("First number is largest")
elif b > a and b > c:
    print("Second number is largest")
else:
    print("Third number is largest")

#3. smallest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a < b and a < c:
    print("First number is smallest")
elif b < a and b < c:
    print("Second number is smallest")
else:
    print("Third number is smallest")


##Above average programs
#1. Even or odd
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#2. Leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#3. driver insurance eligibility
isMarried = input("Are you married? (yes/no): ")
if isMarried.lower() == "yes":
    print("Eligible for insurance")
else:
    gender = input("Enter your gender (male/female): ")
    if gender.lower() == "female":
        age = int(input("Enter your age: "))
        if age >= 25:
            print("Eligible for insurance")
        else:
            print("Not eligible for insurance")
    elif gender.lower() == "male":
        age = int(input("Enter your age: "))
        if age >= 30:
            print("Eligible for insurance")
        else:
            print("Not eligible for insurance")


