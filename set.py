print("\nQuestion 1:")
#Write a Python program to create a set containing five integers and display all its elements.
set1 = {1, 2, 3, 4, 5}
print("Set elements:", set1)






print("\nQuestion 2:")
#Create a list containing duplicate values. Convert the list into a set and display the resulting set.
list1 = [1, 2, 2, 3, 4, 4, 5]
set2 = set(list1)
print("Set after converting from list:", set2)





print("\nQuestion 3:")
#3.	Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
fruits = {"apple", "banana", "orange", "grape", "mango"}
fruits.add("pineapple")
fruits.add("kiwi")
print("Updated set of fruits:", fruits)





print("\nQuestion 4")
#4.	Create a set of numbers and remove a specified number from the set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("Set after removing 3:", numbers)





print("\nQuestion 5:")
#5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
names={"Anna","Alia","Pooja","Riya","Sita"}
name=input("Enter a student name: ")
if name in names:
    print("Student exists in the set")


print("\nQuestion 6")
#6.	Create a set of cities and determine the total number of cities using an appropriate function.
cities={"Mumbai","Delhi","Kolkata","Pune"}
print("Total number of cities:", len(cities))


print("\nQuestion 7:")
#7.	Create a set of programming languages and display each language using a for loop.
languages={"Python","Java","C++","JavaScript","Ruby"}
print("Programming languages:")
for lang in languages:
    print(lang)



print("\nQuestion 8:")
#8.	Create a list containing duplicate numbers, use a set to remove the duplicates.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("List with duplicates:", numbers)
print("Set after removing duplicates:", unique_numbers)


print("\nQuestion 9:")
#9.	Create two sets of integers and find their union.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of the two sets:", union_set)



print("\nQuestion 10:")
#10.	Create two sets and find the elements common to both sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common_set = set1.intersection(set2)
print("Common elements in both sets:", common_set)





print("\nQuestion 11:")
#11.	Create two sets and find:
#•	Elements present in the first set but not the second 
#•	Elements present in the second set but not the first
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff1 = set1.difference(set2)
diff2 = set2.difference(set1)
print("Elements in the first set but not the second:", diff1)
print("Elements in the second set but not the first:", diff2)



print("\nQuestion 12:")
#12.	Create two sets of numbers and find the elements that are present in either set but not in both.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set1.symmetric_difference(set2)
print("Elements present in either set but not in both:", symmetric_diff)



print("\nQuestion 13:")
#13.	Create two sets and determine whether the first set is a subset of the second set.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print("Is the first set a subset of the second set?", is_subset)



print("\nQuestion 14:")
#14.Create two sets and determine whether the first set is a superset of the second set.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
is_superset = set1.issuperset(set2)
print("Is the first set a superset of the second set?", is_superset)






print("\nQuestion 15:")
#15.	Create two sets and determine whether the first set is a superset of the second set.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
is_superset = set1.issuperset(set2)
print("Is the first set a superset of the second set?", is_superset)





print("\nQuestion 16:")
#16.	Create two sets and check whether they are equal.
set1 = {1, 2, 3}
set2 = {3, 2, 1}
are_equal = set1 == set2
print("Are the two sets equal?", are_equal)





print("\nQuestion 17:")
#17.	Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1_subjects = {"Math", "Science", "English"}
student2_subjects = {"Science", "History", "English"}
common_subjects = student1_subjects.intersection(student2_subjects)
print("Subjects studied by both students:", common_subjects)





print("\nQuestion 18:")
#18.	Create a set of numbers and find the largest and smallest number in the set without using max() and min().
number_set = {10, 25, 5, 40, 15}
largest = max(number_set)
smallest = min(number_set)
print("Largest number in the set:", largest)
print("Smallest number in the set:", smallest)



print("\nQuestion 19:")
#19.	Create two sets:
#•	Students present in the morning session 
#•	Students present in the afternoon session 
#Find:
#•	Students present in both sessions 
#•	Students present only in the morning 
#•	Students present only in the afternoon 
#•	Students present in at least one session
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"Charlie", "David", "Eve"}
both_sessions = set1.intersection(set2)
morning_only = set1.difference(set2)
afternoon_only = set2.difference(set1)
at_least_one_session = set1.union(set2)
print("Students present in both sessions:", both_sessions)
print("Students present only in the morning:", morning_only)
print("Students present only in the afternoon:", afternoon_only)
print("Students present in at least one session:", at_least_one_session)





print("\nQuestion 20:")
#20.	Create sets representing students enrolled in:
#•	Python 
#•	Java 
#Find students enrolled in both courses and students enrolled in only one course.
set_python = {"Alice", "Bob", "Charlie"}
set_java = {"Charlie", "David", "Eve"}
both_courses = set_python.intersection(set_java)
only_python = set_python.difference(set_java)
only_java = set_java.difference(set_python)
print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only Python:", only_python)
print("Students enrolled in only Java:", only_java)





print("\nQuestion 21:")
#22.	Create two sets representing technical skills of two employees. Find:
#•	Common skills 
#•	Skills unique to Employee 1 
#•	Skills unique to Employee 2 
#•	All available skills
employee1_skills = {"Python", "Java", "C++"}
employee2_skills = {"Java", "JavaScript", "C++"}
common_skills = employee1_skills.intersection(employee2_skills)
unique_to_employee1 = employee1_skills.difference(employee2_skills)
unique_to_employee2 = employee2_skills.difference(employee1_skills)
all_available_skills = employee1_skills.union(employee2_skills)
print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_to_employee1)
print("Skills unique to Employee 2:", unique_to_employee2)
print("All available skills:", all_available_skills)







print("\nQuestion 22:")
#23.	Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Book A", "Book B", "Book C", "Book D"}
requested_books = {"Book B", "Book E", "Book C"}    
available_requested_books = requested_books.intersection(available_books)
print("Requested books that are available:", available_requested_books)




print("\nQuestion 23:")
#24.	Store visitor IDs from two different days in separate sets. Determine:
#•	Unique visitors across both days 
#•	Returning visitors 
#•	Visitors who came only on the first day 
#•	Visitors who came only on the second day
#•	Create sets representing products belonging to different categories. Find products that belong to both categories.
set_day1 = {101, 102, 103, 104}
set_day2 = {103, 104, 105, 106}
unique_visitors = set_day1.union(set_day2)
returning_visitors = set_day1.intersection(set_day2)
only_day1 = set_day1.difference(set_day2)
only_day2 = set_day2.difference(set_day1)

print("Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors who came only on the first day:", only_day1)
print("Visitors who came only on the second day:", only_day2)



print("\nQuestion 25:")
#25.	Represent the friends of two users using sets. Find:
#•	Mutual friends 
#•	Friends unique to User 1 
#•	Friends unique to User 2 
#•	Total unique friends
user1_friends = {"Alice", "Bob", "Charlie"}
user2_friends = {"Charlie", "David", "Eve"}
mutual_friends = user1_friends.intersection(user2_friends)
unique_to_user1 = user1_friends.difference(user2_friends)
unique_to_user2 = user2_friends.difference(user1_friends)
total_unique_friends = user1_friends.union(user2_friends)
print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_to_user1)
print("Friends unique to User 2:", unique_to_user2)
print("Total unique friends:", total_unique_friends)
