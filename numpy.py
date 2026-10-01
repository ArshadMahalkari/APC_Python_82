"""NumPy practice programs 1-25 with comments."""

import importlib
import os
import sys


# This file is named numpy.py, so remove its directory while importing NumPy.
_directory = os.path.dirname(os.path.abspath(__file__))
_original_path = sys.path[:]
sys.path = [path for path in sys.path
            if os.path.abspath(path or os.curdir) != _directory]
np = importlib.import_module("numpy")
sys.path = _original_path


# Problem 1: Display a one-dimensional array and its size, type, and dimensions.
def problem_1():
    array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("\nProblem 1:", array)
    print("Size:", array.size, "Data type:", array.dtype, "Dimensions:", array.ndim)


# Problem 2: Perform addition, subtraction, multiplication, division, and modulus.
def problem_2():
    first = np.array([10, 20, 30, 40, 50])
    second = np.array([2, 4, 5, 8, 10])
    print("\nProblem 2")
    print("Addition:", first + second)
    print("Subtraction:", first - second)
    print("Multiplication:", first * second)
    print("Division:", first / second)
    print("Modulus:", first % second)


# Problem 3: Find the maximum, minimum, sum, and average.
def problem_3():
    array = np.array([12, 45, 7, 89, 34, 23, 56, 9, 67, 41])
    print("\nProblem 3:", array)
    print("Maximum:", np.max(array), "Minimum:", np.min(array))
    print("Sum:", np.sum(array), "Average:", np.mean(array))


# Problem 4: Separate even and odd numbers with Boolean indexing.
def problem_4():
    array = np.arange(1, 21)
    print("\nProblem 4:", array)
    print("Even numbers:", array[array % 2 == 0])
    print("Odd numbers:", array[array % 2 != 0])


# Problem 5: Reshape numbers 1-12 into 2x6, 3x4, and 4x3 matrices.
def problem_5():
    array = np.arange(1, 13)
    print("\nProblem 5: Original:", array)
    print("2 x 6:\n", array.reshape(2, 6))
    print("3 x 4:\n", array.reshape(3, 4))
    print("4 x 3:\n", array.reshape(4, 3))


# Problem 6: Add two 3x3 matrices.
def problem_6():
    first = np.arange(1, 10).reshape(3, 3)
    second = np.arange(9, 0, -1).reshape(3, 3)
    print("\nProblem 6: Matrix addition:\n", first + second)


# Problem 7: Multiply two compatible matrices with np.matmul.
def problem_7():
    first = np.array([[1, 2, 3], [4, 5, 6]])
    second = np.array([[7, 8], [9, 10], [11, 12]])
    print("\nProblem 7: Matrix multiplication:\n", np.matmul(first, second))


# Problem 8: Display the transpose of a 3x4 matrix.
def problem_8():
    matrix = np.arange(1, 13).reshape(3, 4)
    print("\nProblem 8: Original:\n", matrix)
    print("Transpose:\n", matrix.T)


# Problem 9: Access selected rows, column, diagonal, and middle rows.
def problem_9():
    matrix = np.arange(1, 17).reshape(4, 4)
    print("\nProblem 9: Matrix:\n", matrix)
    print("First row:", matrix[0])
    print("Last column:", matrix[:, -1])
    print("Diagonal:", np.diag(matrix))
    print("Second and third rows:\n", matrix[1:3])


# Problem 10: Calculate the sum of each row and each column.
def problem_10():
    matrix = np.arange(1, 17).reshape(4, 4)
    print("\nProblem 10: Matrix:\n", matrix)
    print("Sum of each row:", np.sum(matrix, axis=1))
    print("Sum of each column:", np.sum(matrix, axis=0))


# Problem 11: Use slicing to display first, last, alternate, and reverse values.
def problem_11():
    array = np.arange(1, 21)
    print("\nProblem 11:", array)
    print("First 5:", array[:5])
    print("Last 5:", array[-5:])
    print("Alternate elements:", array[::2])
    print("Reverse order:", array[::-1])


# Problem 12: Replace all values greater than 50 with zero.
def problem_12():
    array = np.array([12, 65, 34, 78, 9, 51, 44, 90, 27, 60])
    array[array > 50] = 0
    print("\nProblem 12:", array)


# Problem 13: Display an unsorted array in ascending and descending order.
def problem_13():
    array = np.array([45, 12, 89, 3, 67, 24, 10])
    print("\nProblem 13: Ascending:", np.sort(array))
    print("Descending:", np.sort(array)[::-1])


# Problem 14: Find only the unique values.
def problem_14():
    array = np.array([4, 2, 7, 4, 2, 9, 7, 1, 9, 4])
    print("\nProblem 14: Unique elements:", np.unique(array))


# Problem 15: Concatenate arrays horizontally and vertically.
def problem_15():
    first = np.array([[1, 2], [3, 4]])
    second = np.array([[5, 6], [7, 8]])
    print("\nProblem 15: Horizontal:\n", np.hstack((first, second)))
    print("Vertical:\n", np.vstack((first, second)))


# Problem 16: Calculate statistics for marks of 10 students.
def problem_16():
    marks = np.array([78, 85, 92, 67, 88, 74, 95, 81, 69, 90])
    print("\nProblem 16: Marks:", marks)
    print("Highest:", np.max(marks))
    print("Lowest:", np.min(marks))
    print("Average:", np.mean(marks))
    print("Median:", np.median(marks))
    print("Standard deviation:", np.std(marks))


# Problem 17: Display marks that are above the class average.
def problem_17():
    marks = np.array([55, 72, 81, 64, 90, 48, 77, 85, 69, 92,
                      58, 74, 88, 61, 79, 95, 66, 70, 83, 52])
    average = np.mean(marks)
    print("\nProblem 17: Class average:", average)
    print("Marks above average:", marks[marks > average])


# Problem 18: Display a 3D array and its dimensions, shape, and size.
def problem_18():
    array = np.arange(1, 25).reshape(2, 3, 4)
    print("\nProblem 18:\n", array)
    print("Dimensions:", array.ndim, "Shape:", array.shape, "Size:", array.size)


# Problem 19: Access specified elements in a 3D array.
def problem_19():
    array = np.arange(1, 25).reshape(2, 3, 4)
    print("\nProblem 19: First:", array[0, 0, 0])
    print("Last:", array[-1, -1, -1])
    print("At [0, 1, 2]:", array[0, 1, 2])
    print("At [1, 2, 3]:", array[1, 2, 3])


# Problem 20: Calculate total, layer, row-axis, and column-axis sums.
def problem_20():
    array = np.arange(1, 25).reshape(2, 3, 4)
    print("\nProblem 20: Sum of all elements:", np.sum(array))
    print("Sum of each layer:", np.sum(array, axis=(1, 2)))
    print("Sum along rows (per layer):\n", np.sum(array, axis=2))
    print("Sum along columns (per layer):\n", np.sum(array, axis=1))


# Problem 21: Replace random 3D-array values greater than 50 with zero.
def problem_21():
    rng = np.random.default_rng(21)
    array = rng.integers(1, 101, size=(2, 3, 4))
    print("\nProblem 21: Original:\n", array)
    array[array > 50] = 0
    print("After replacement:\n", array)


# Problem 22: Calculate six statistics for a random (3,4,5) array.
def problem_22():
    rng = np.random.default_rng(22)
    array = rng.integers(1, 101, size=(3, 4, 5))
    print("\nProblem 22: Mean:", np.mean(array))
    print("Median:", np.median(array))
    print("Standard deviation:", np.std(array))
    print("Variance:", np.var(array))
    print("Minimum:", np.min(array), "Maximum:", np.max(array))


# Problem 23: Flatten a (2,3,4) array and display both arrays.
def problem_23():
    array = np.arange(1, 25).reshape(2, 3, 4)
    print("\nProblem 23: Original:\n", array)
    print("Flattened:", array.flatten())


# Problem 24: Flatten numbers 1-27 and calculate four statistics.
def problem_24():
    array = np.arange(1, 28).reshape(3, 3, 3)
    flattened = array.flatten()
    print("\nProblem 24: Flattened:", flattened)
    print("Sum:", np.sum(flattened))
    print("Average:", np.mean(flattened))
    print("Maximum:", np.max(flattened), "Minimum:", np.min(flattened))


# Problem 25: Filter a random flattened 3D array using three conditions.
def problem_25():
    rng = np.random.default_rng(25)
    array = rng.integers(1, 101, size=(3, 4, 5))
    flattened = array.flatten()
    average = np.mean(flattened)
    print("\nProblem 25: Flattened array:", flattened)
    print("Greater than 50:", flattened[flattened > 50])
    print("Even numbers:", flattened[flattened % 2 == 0])
    print("Less than average (", average, "):", flattened[flattened < average])


def main():
    """Run all 25 NumPy examples."""
    for problem in (
        problem_1, problem_2, problem_3, problem_4, problem_5,
        problem_6, problem_7, problem_8, problem_9, problem_10,
        problem_11, problem_12, problem_13, problem_14, problem_15,
        problem_16, problem_17, problem_18, problem_19, problem_20,
        problem_21, problem_22, problem_23, problem_24, problem_25,
    ):
        problem()


if __name__ == "__main__":
    main()
