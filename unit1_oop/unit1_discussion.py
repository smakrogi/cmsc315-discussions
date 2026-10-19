"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class AnimalClass:
    """
    Parent class representing an animal
    """
    name = "Lion"

    def __init__(self, age: int, weight: float):
        if age <= 0 or weight <= 0:
            raise ValueError("Problem in name, age, or weight")
        self._age = age
        self._weight = weight

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Weight: {self._weight}")





# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Fish(AnimalClass):
    """
    Child class for fish
    """
    name = "Shark"

    def __init__(self, age: int, weight: float, number_of_fins):
        super().__init__(age, weight)
        if number_of_fins <= 0:
            raise ValueError("Problem in number_of_fins")
        self._number_of_fins = number_of_fins
        self._habitat = None
        self._food = []

    def set_habitat(self, habitat:str):
        self._habitat = habitat

    def set_food(self, food:str):
        self._food.append(food)

    def get_food(self):
        return self._food

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Weight: {self._weight}")
        print(f"A {self.name} has {self._number_of_fins} fins, lives in the {self._habitat}, and eats {self._food}")



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Shark
    fish_1 = Fish(3, 350, 6)
    print(f"First fish name: {Fish.name}")

    # Dolphin
    fish_2 = Fish(7, 250, 5)
    fish_2.name = "Dolphin"
    print(f"Second fish name: {Fish.name}")
    fish_2.display_info()

    # Display namespaces
    print(f"First fish namespace: {fish_1.__dict__}")
    print(f"Second fish namespace: {fish_2.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Shark food
    dolphin_food = ["Fish", "Crustaceans"]

    # Shallow copy copies the pointer to dolphin food.
    shallow_food_copy = dolphin_food
    print(f"Shallow food copy: {shallow_food_copy}")
    dolphin_food.append("Squid")
    print(f"Shallow food copy points to source variable: {shallow_food_copy}")

    # Deep copy creates a distinct copy of dolphin_food
    deep_food_copy = deepcopy(dolphin_food)
    print(f"Deep food copy: {deep_food_copy}")
    dolphin_food.append("Crabs")
    print(f"Deep food copy is a separate variable: {deep_food_copy}")



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n*** Parent object ***")
    animal_1 = AnimalClass(8, 355.5)
    animal_1.display_info()

    print("\n*** Child object ***")
    animal_2 = Fish(4, 401.3, 4)
    animal_2.set_habitat("Ocean")
    animal_2.display_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()