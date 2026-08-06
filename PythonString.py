#1. String Length (Without len())
s = input("Enter a string: ")

count = 0
for ch in s:
    count += 1

print("Length =", count)


#2. Count Vowels, Consonants, Digits, Spaces, Special Characters
s = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)


#3. Reverse a String
s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

print("Reversed String:", rev)


#4. Palindrome Check
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#5. Count Uppercase and Lowercase Letters
s = input("Enter a string: ")

upper = lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)


#6. Replace Characters
s = input("Enter a string: ")
old = input("Character to replace: ")
new = input("New character: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print(result)


#7. Remove Spaces
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)


#8. Frequency of a Character
s = input("Enter a string: ")
ch = input("Enter character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency:", count)


#9. First and Last Character
s = input("Enter a string: ")

print("First Character:", s[0])
print("Last Character:", s[-1])


#10. Display ASCII Values
s = input("Enter a string: ")

for ch in s:
    print(ch, ":", ord(ch))


#11. Count Words
s = input("Enter a sentence: ")

words = s.split()

print("Total Words:", len(words))


#12. Longest Word
s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)


#13. Shortest Word
s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word:", shortest)


#14. Title Case
s = input("Enter a sentence: ")

print(s.title())


#15. Duplicate Characters
s = input("Enter a string: ")

printed = ""

for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch


#16. Character Frequency
s = input("Enter a string: ")

printed = ""

for ch in s:
    if ch not in printed:
        print(ch, ":", s.count(ch))
        printed += ch


#17. Anagram Check
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


#18. Remove Duplicate Characters
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)


#19. Substring Search
s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring Found")
else:
    print("Substring Not Found")


#20. Count Occurrences of a Word
sentence = input("Enter sentence: ")
word = input("Enter word: ")

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences:", count)


#21. Password Validator
password = input("Enter password: ")

upper = lower = digit = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")


#22. Run-Length Encoding
s = input("Enter string: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

print(result)


#23. String Compression
s = input("Enter string: ")

compressed = ""
count = 1

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

if len(compressed) < len(s):
    print(compressed)
else:
    print(s)


#24. Most Frequent Character
s = input("Enter string: ")

max_char = ""
max_count = 0

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Most Frequent:", max_char)


#25. Second Most Frequent Character
s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_chars) >= 2:
    print("Second Most Frequent:", sorted_chars[1][0])
else:
    print("Not Available")


#26. Caesar Cipher
text = input("Enter message: ")
shift = int(input("Enter shift: "))

encrypted = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch)-base+shift)%26+base)
    else:
        encrypted += ch

print("Encrypted:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        decrypted += chr((ord(ch)-base-shift)%26+base)
    else:
        decrypted += ch

print("Decrypted:", decrypted)


#27. Email Validator
email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")


#28. Word Frequency Dictionary
paragraph = input("Enter paragraph: ")

words = paragraph.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


#29. Reverse Order of Words
sentence = input("Enter sentence: ")

words = sentence.split()

print(" ".join(words[::-1]))


#30. String Rotation Check
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")