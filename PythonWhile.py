n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i = i + 1

n1 = int(input("Enter a number: "))
i = 1
while i <= n1:
    if i % 2 == 0:
        print(i)
    i = i + 1

n2 = int(input("Enter a number: "))
i = 1
while i <= n2:
    if i % 2 != 0:
        print(i)
    i = i + 1

n3 = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n3:
    sum = sum + i
    i = i + 1
print(sum)

n4 = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n4:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)

n5 = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n5:
    if i % 2 != 0:
        sum = sum + i
    i = i + 1
print(sum)

n6 = int(input("Enter a number: "))
while n6 > 0:
    print(n6)
    n6 = n6 - 1

#fibonacci series
n7 = int(input("Enter a number: "))
i = 1
a = 0
b = 1
while i <= n7:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1

#factorial
n8 = int(input("Enter a number: "))
i = 1
fact = 1
while i <= n8:
    fact = fact * i
    i = i + 1
print(fact)

#prime number
n9 = int(input("Enter a number: "))
i = 2
while i < n9:
    if n9 % i == 0:
        print("Not a prime number")
        break
    i = i + 1
else:
    print("Prime number")

#sum of digits
n10 = int(input("Enter a number: "))
sum = 0
while n10 > 0:
    digit = n10 % 10
    sum = sum + digit
    n10 = n10 // 10
print(sum)

#palindrome
n11 = int(input("Enter a number: "))
temp = n11
rev = 0
while n11 > 0:
    digit = n11 % 10
    rev = rev * 10 + digit
    n11 = n11 // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not a palindrome")


#reverse of a number
n11 = int(input("Enter a number: "))
rev = 0
while n11 > 0:
    digit = n11 % 10
    rev = rev * 10 + digit
    n11 = n11 // 10
print(rev)

#multiplication table
n12 = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n12, "x", i, "=", n12 * i)
    i = i + 1

