"""Basic Pandas examples using a small student data table."""

import importlib
import os
import sys


def load_pandas():
    """Import the third-party package even though this file is named pandas.py."""
    directory = os.path.dirname(os.path.abspath(__file__))
    original_path = sys.path[:]
    sys.path = [
        path for path in sys.path
        if os.path.abspath(path or os.curdir) != directory
    ]
    try:
        return importlib.import_module("pandas")
    finally:
        sys.path = original_path


def main():
    pd = load_pandas()
    students = pd.DataFrame(
        {
            "name": ["Asha", "Rahul", "Mina"],
            "marks": [82, 67, 91],
        }
    )
    students["result"] = students["marks"].apply(
        lambda marks: "Pass" if marks >= 40 else "Fail"
    )

    print("Student data:")
    print(students)
    print("\nAverage marks:", students["marks"].mean())
    print("\nStudents scoring at least 75:")
    print(students[students["marks"] >= 75])


if __name__ == "__main__":
    main()