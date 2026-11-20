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
    """ Helper function that looks up a key and
        displays the corresponding value, or displays a not-found
        message.
    """

    # Look up key using built-in get method of the dictionary.
    # Use the built-in get() method of a dictionary to look up the item.
    result = gradebook.get(key)

    # Display value or a message that key was not found.
    if result is not None:
        print(f"{key}'s grade is {result}")
    else:
        print(f"{key} not found in gradebook.")

    # Return the value or None if key was not found.
    return result

def remove_key(gradebook, key_to_remove):
    """ Helper function that removes a key and
        handles the edge case of not-existing keys.
    """

    # Display key to remove.
    print(f"Removing {key_to_remove}'s grade")

    # Look up the key and remove only if the key is
    # in the table.
    if lookup_key(gradebook, key_to_remove) is not None:
        # Use the built-in pop() method of a dictionary to remove the item.
        removed_grade = gradebook.pop(key_to_remove)
        # Display removed entry.
        print(f"Removed entry: {key_to_remove}:{removed_grade}")

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

    # Create gradebook dictionary.
    gradebook = {"George":85, "Anna":92, "Chris":78, "Thomas":68}

    # Set lookup keys.
    lookup_keys = ["Chris", "Tom"]

    # Show current gradebook.
    print(f"Current gradebook: {gradebook.items()}")

    # Iteratively lookup keys using helper function lookup_key().
    for key in lookup_keys:
        print(f"Looking up {key}...")
        lookup_key(gradebook, key)
    # Show gradebook.
    print(f"Gradebook after lookup: {gradebook.items()}")

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

    # Show current gradebook.
    print(f"Current gradebook: {gradebook.items()}")

    # Set update item and display it.
    update_item = {"Chris":98}
    print(f"Updating the gradebook with item {update_item}")

    # Call built-in update() dictionary member and display updated
    # gradebook.
    gradebook.update(update_item)
    print(f"Updated gradebook: {gradebook.items()}")

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

    # Show current gradebook.
    print(f" Current gradebook: {gradebook.items()}")
    # Show key to remove.
    key_to_remove = "Anna"
    # Call helper function remove_key() to remove the key.
    remove_key(gradebook, key_to_remove)
    # Show gradebook after item removal.
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

    # Set lookup keys (one is missing)
    print("\nLook up present and missing keys.")
    lookup_keys = ["Chris", "Tom", "Jimmy"]
    # Show gradebook.
    print(f"Current gradebook: {gradebook.items()}")
    # Iteratively look the keys up by calling the helper function
    # lookup_key().
    for key in lookup_keys:
        lookup_key(gradebook, key)
    # Show gradebook.
    print(f"Gradebook after lookup: {gradebook.items()}")

    # Delete a missing key safely.
    print("\nDelete a missing key safely.")
    # Show gradebook.
    print(f"Current gradebook: {gradebook.items()}")
    # Show key to remove. The key is not in the gradebook.
    key_to_remove = "Noah"
    # Call helper remove_key() to remove the key and
    # see how it is handled.
    remove_key(gradebook, key_to_remove)
    # Show gradebook.
    print(f"Current gradebook: {gradebook.items()}")

    # Update a missing key.
    print("\nUpdate a missing key.")
    # Show gradebook.
    print(f"Current gradebook: {gradebook.items()}")
    # Set item to update. Item's key is not in the gradebook.
    item_to_update = {"Jake":58}
    # Show item to update.
    print(f"Update gradebook with {item_to_update}")
    # Call built-in dictionary update() member.
    gradebook.update(item_to_update)
    # Show updated gradebook.
    print(f"Updated gradebook: {gradebook.items()}")

if __name__ == "__main__":
    main()