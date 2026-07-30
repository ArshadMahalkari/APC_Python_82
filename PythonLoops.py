def squareroot(n):
    return n ** 0.5

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
for i in range(1, n):
    print(i)

n1 = int(input("Enter a number: "))
for i in range(1, n1):
    if n1 % 2 == 0:
        print(n1)

n2 = int(input("Enter a number: "))
for i in range(1, n2):
    if n2 % 2 != 0:
        print(n2)

n3 = int(input("Enter a number: "))
for i in range(1, n3):
    print(i * i)

n4 = int(input("Enter a number: "))
for i in range(1, n4):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    print(fact + 1)

n5 = int(input("Enter a square number: "))
root = squareroot(n5)
print(root)
if isPrime(root):
    print("The square root is a prime number")
else:
    print("The square root is not a prime number")


#A B C
#A B C
#A B C

for i in range(1, 3):
    for j in range(1, 3):
        var = 'A'
        print(var + " ", end="")
        var = var + 1
    print()

#A
#A B
#A B C
#A B C D

n = int(input("Enter a number: "))
for i in range(1, n):
    for j in range(1, i + 1):
        var = 'A'
        print(var + " ", end="")
        var = var + 1
    print()

#A B C D E
#A B C D
#A B C
#A B
#A

n = int(input("Enter a number: "))
for i in range(1, n):
    for j in range(1, n - i + 1):
        var = 'A'
        print(var + " ", end="")
        var = var + 1
    print()

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

n = int(input("Enter a number: "))
for i in range(1, n):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1

n = int(input("Enter a number: "))
for i in range(1, n):
    for j in range(1, n - i + 1):
        print(j, end=" ")
    print()

#1 
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

n = int(input("Enter a number: "))
for i in range(1, n):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1

n = int(input("Enter a number: "))
for i in range(1, n):
    for j in range(1, n - i + 1):
        print(i, end=" ")
    print()

