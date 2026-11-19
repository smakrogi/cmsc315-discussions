"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""
from typing import Protocol

def lookup_key(gradebook, key):
    result = gradebook.get(key)

    if result is not None:
        print(f"{key}'s grade is {result}")
    else:
        print(f"{key} not found in gradebook.")

    return result

def remove_key(gradebook, key_to_remove):

    print(f"Removing {key_to_remove}'s grade")

    if lookup_key(gradebook, key_to_remove) is not None:
        removed_grade = gradebook.pop(key_to_remove)
        print(f"Removed entry: {key_to_remove}:{removed_grade}")

    return gradebook

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    gradebook = {"George":85, "Anna":92, "Chris":78, "Thomas":68}

    lookup_keys = ["Chris", "Tom"]

    for key in lookup_keys:
        result = gradebook.get(key)
        if result is not None:
            print(f"{key}'s grade is {result}")
        else:
            print(f"{key} not found in gradebook.")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print(gradebook.items())
    gradebook.update({"Chris":98})
    print(gradebook.items())

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f" Current gradebook: {gradebook.items()}")
    key_to_remove = "Anna"
    print(f"Removing {key_to_remove}"'s grade')
    removed_grade = gradebook.pop(key_to_remove)

    if removed_grade is None:
        print(f"{key_to_remove}"'s grade not found')
    else:
        print(f"Removed entry: {key_to_remove}:{removed_grade}")

    print(f"Current gradebook after removal: {gradebook.items()}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Lookup keys (one is missing)
    lookup_keys = ["Chris", "Tom", "Jimmy"]
    print(f"Current gradebook: {gradebook.items()}")
    for key in lookup_keys:
        lookup_key(gradebook, key)

    # Delete a missing key safely.
    print(f"Current gradebook: {gradebook.items()}")
    key_to_remove = "Noah"
    remove_key(gradebook, key_to_remove)

    # Update a missing key.
    print(f"Current gradebook: {gradebook.items()}")
    item_to_update = {"Jake":58}
    print(f"Update gradebook with {item_to_update}")
    gradebook.update(item_to_update)
    print(f"Updated gradebook: {gradebook.items()}")

if __name__ == "__main__":
    main()