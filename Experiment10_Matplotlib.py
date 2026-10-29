"""Create a simple line chart with Matplotlib."""

import matplotlib.pyplot as plt


def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    sales = [12, 18, 15, 23, 28]

    plt.plot(months, sales, marker="o", color="blue")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales (thousands)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
