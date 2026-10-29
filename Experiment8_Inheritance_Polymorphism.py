"""Simple examples of inheritance and polymorphism."""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


def describe_animal(animal):
    """The same function works with different Animal subclasses."""
    print(f"{animal.name} says {animal.sound()}")


def main():
    animals = [Dog("Bruno"), Cat("Mimi")]
    for animal in animals:
        describe_animal(animal)


if __name__ == "__main__":
    main()
