"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Insert value at the specified index.
    # Shift successive nodes to the next position.
    # Insertion will take O(len(lst)-index) operations.
    # For example, insertion at tbe second-to-last index of the list will take 1 shift and have
    # O(1) time complexity.
    lst.insert(index, value)

    # Return the list
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Check for edge cases and return None if index is invalid.
    try:
        # Remove and return the value at the given index.
        return lst.pop(index)
    except IndexError:
        # Return None if the index is invalid.
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # Use a try/except block to handle the ValueError and return -1.
    # This is a linear search because it checks each item of the list against the value.
    # It scans the list sequentially so that it returns the index of first occurrence of value
    # to save computational time.
    try:
        # Return the index of first value occurrence.
        return lst.index(value)
    except ValueError:
        # Return -1, if the value was not found.
        return -1




def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Create a list with four items.
    my_list = ["red", "yellow", "green", "blue"]
    # Print the list.
    print(f"Original list: {my_list}")

    # Demonstrate insertion into the list at multiple positions
    # using a `for` loop.
    for idx in (0, 2, 4):
        print(f"Insertion at index {idx}: {insert_at(my_list, idx, "orange")}")


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    print("Now let's demonstrate deletions.")

    # Take the previous list.
    print(f"Original list: {my_list}")
    # Use a `for` loop to delete items from the list iteratively
    # and show the output of deletions.
    for idx in (0, 2, 4, 5):
        print(f"Deletion at index {idx}: {delete_at(my_list, idx)}")
        print(f"Current list: {my_list}")


# ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Search for a value that exists and a value that does not exist
    # using a `for` loop.
    # Define queries.
    queries = ["red", "yellow"]
    # Iterate over the queries and perform search.
    for query in queries:
        # Show query and list.
        print(f"Searching for {query} in {my_list}... ")
        # Search.
        idx = search_value(my_list, query)
        # Display messages according to success or failure of search.
        if idx == -1:
            print(f"{query} not found!")
        else:
            print(f"{query} found at index {idx}!")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # First edge case: insert an item into an empty list at index 2.
    print(f"\nDemonstrate insertion into an empty list...")
    my_list_2 = []
    value = "red"
    index = 2
    # Display value, list, index, and insertion output.
    # It seems it appends the value regardless of index
    # because the list was originally empty.
    print(f"Inserting {value} into list {my_list_2} at index {index}...")
    print(f"Current list: {insert_at(my_list_2, index, value)}")

    # Second edge case: delete items from list with a single item.
    print(f"\nDemonstrate deletions from multiple positions...")
    # Use iterator over multiple indices.
    for index in (0, 0):
        # Delete at index.
        print(f"\nDeletion at index {index}...")
        output = delete_at(my_list_2, index)
        # Check for failure to delete.
        if output is not None:
            # If no failure, show the deleted item and current list.
            print(f"Retrieved item value: {output}.")
            print(f"Current list: {my_list_2}")
        else:
            # Otherwise, show there is no item at requested index.
            print(f"No item found at index {index}!")

if __name__ == "__main__":
    main()