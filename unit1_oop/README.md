# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Implementation

### TODO 1 -- Parent Class (`AnimalClass`)

`AnimalClass` was created as the parent class to represent a generic animal. It included:

- **Class variable:** `name`, set to `"Lion"`, shared across all instances of the class.
- **Instance variables:** `_age` (int) and `_weight` (float), both initialized through the constructor and prefixed with an underscore to signal protected access.
- **Constructor (`__init__`):** Accepted `age` and `weight` as parameters and stored them as instance attributes.
- **Method (`display_info`):** Printed the animal's name, age, and weight to the console using an f-string.

### TODO 2 -- Child Class (`Fish`)

`Fish` was created as a child class inheriting from `AnimalClass`. It extended the parent in the following ways:

- **Inheritance:** `Fish` inherited from `AnimalClass` using `class Fish(AnimalClass)` syntax and called `super().__init__()` to initialize the parent's instance variables.
- **New class variable:** `name` was overridden to `"Shark"`, demonstrating how a child class can shadow a parent's class variable.
- **New instance variables:** `_number_of_fins`, `_habitat` (initialized to `None`), and `_food` (initialized to an empty list) were added to capture fish-specific attributes.
- **New methods:**
  - `set_habitat(habitat)` -- assigned a habitat string to the instance.
  - `set_food(food)` -- appended a food item to the `_food` list.
  - `get_food()` -- returned the `_food` list.
- **Overridden method:** `display_info()` was overridden to print both the inherited attributes (name, age, weight) and the new fish-specific attributes (fins, habitat, food).

### TODO 3 -- Namespace Demonstration (`demonstrate_namespaces`)

A standalone function was written to illustrate how Python resolves names through class and instance namespaces:

- Two `Fish` objects (`fish_1` and `fish_2`) were instantiated.
- The class variable `name` was accessed through the class itself (`Fish.name`), which returned `"Shark"`.
- A new instance-level `name` attribute was assigned directly to `fish_2` (`fish_2.name = "Dolphin"`), demonstrating that instance attributes shadow class attributes without modifying the class namespace.
- After the assignment, `Fish.name` still returned `"Shark"`, confirming that only `fish_2`'s instance namespace was affected.
- The `__dict__` attribute of each object was printed to show the difference: `fish_1.__dict__` contained only the constructor-assigned attributes, while `fish_2.__dict__` also contained the instance-level `name`.

### TODO 4 -- Copy Demonstration (`demonstrate_copying`)

A function was written to demonstrate the behavioral difference between shallow and deep copies:

- A list `dolphin_food` was created with `["Fish", "Crustaceans"]`.
- **Shallow copy:** `shallow_food_copy = dolphin_food` created a reference (alias), not an independent copy. When `"Squid"` was appended to `dolphin_food`, `shallow_food_copy` reflected the change because both variables pointed to the same list object in memory.
- **Deep copy:** `deep_food_copy = deepcopy(dolphin_food)` created a fully independent copy. When `"Crabs"` was appended to `dolphin_food`, `deep_food_copy` remained unchanged, proving that the deep copy did not share any references with the original.

### TODO 5 -- Main Function (`main`)

The `main` function tied all components together:

- A parent `AnimalClass` object was created with `age=8` and `weight=355.5`, and its `display_info()` method was called to demonstrate the parent class in isolation.
- A child `Fish` object was created with `age=1`, `weight=401.3`, and `number_of_fins=4`. Its `set_habitat("Ocean")` method was called before `display_info()`, demonstrating inheritance and the child's extended functionality.
- `demonstrate_namespaces()` was called to show class vs. instance namespace behavior.
- `demonstrate_copying()` was called to show shallow vs. deep copy behavior.
- The script used the `if __name__ == "__main__"` guard to ensure `main()` only ran when executed directly.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150--200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I explored the concepts of inheritance, namespaces, and object copying. 
I designed an "Animal" parent class and a "Fish" subclass to explore the concept of Inheritance.
This concept allowed me to use the existing structure and functionality in Animal and 
extend it to Fish. Regarding namespaces, I understood that the class variables and instance 
variables have different scopes. The class variable value is shared across all class objects.
On the hand, instance variables can take on different values when they are instantiated. 
I also learned the differences between shallow and deep variable copy. Simply put, shallow copy copies the pointer to the original variable. 
So if the original variable changes, the copy changes too. Deep copy creates a copy of the variable values.
In this way the origin and target variables are changed independently. I practiced the skills of configuring and using IntelliJ to write the programs.
I also practiced the use of github as a version control system for writing and managing software.

2. What challenges did you encounter, and how did you overcome them?
I think it was important to understand the instructions and to develop a solution that addresses the main questions.
Design of the classes may take longer time than their implementation because the main questions are mostly about OO design. 
After implementation, I tested the code using different value sets.

3. Compare OOP to procedural programming.
In my opinion, OOP is a superset of procedural programming. 
OOP helps a developer to think proactively and to design the solution first.
It helps to produce modular code, which is easier to debug, to build on it, 
and to share it with others developers.

4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.
Maintainability and reusability are two of the main benefits of OOP. In this assignment, 
the AnimalClass parent class was designed once and reused by the Fish subclass through inheritance. 
If we needed to add more animal types such as birds or reptiles, we could extend the same parent class 
without modifying existing code. This demonstrates reusability and reduces development overhead because 
common attributes and methods are defined in one place. Maintainability is also improved because changes to shared behavior 
only need to happen in the parent class, and all child classes inherit the update automatically. 
In practical application development, this modularity means that teams can work on
different subclasses independently. For future use, a well-designed class hierarchy serves as a foundation that 
can grow with the project requirements.