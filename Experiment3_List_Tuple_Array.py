"""Simple examples of lists, tuples, and arrays."""

from array import array


def main():
    # A list is ordered and mutable.
    fruits = ["apple", "banana", "mango"]
    fruits.append("orange")
    fruits[0] = "grapes"
    print("List:", fruits)

    # A tuple is ordered and immutable.
    student = ("Arshad", 82, 85)
    name, roll_number, marks = student
    print("Tuple:", student)
    print(f"Student: {name}, Roll number: {roll_number}, Marks: {marks}")

    # An array stores values of one declared type.
    numbers = array("i", [10, 20, 30, 40])
    numbers.append(50)
    print("Array:", numbers.tolist())
    print("Array sum:", sum(numbers))


if __name__ == "__main__":
    main()
