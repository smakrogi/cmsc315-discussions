"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Loop through lst.
    for idx in range(0,len(lst)):
        # Check if the current list item
        # equals the target.
        if lst[idx] == target:
            # If so, return the index.
            return idx

    # Target not found, returning -1.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Set initial low and high indices
    # to the beginning and end of the list.
    low_index = int(0)
    high_index = int(len(lst) - 1)

    # While the bounds are ordered correctly.
    while high_index >= low_index:
        # Computer mid index for comparison.
        mid = (low_index + high_index) // 2
        # Compare list item with target and
        # modify search bounds or return
        # the index if value was found.
        if lst[mid] > target:
            high_index = mid - 1
        elif lst[mid] < target:
            low_index = mid + 1
        else:
            return mid

    # Target not found, returning -1.
    return -1

def search_and_display(data, target_value, method="Linear"):
    # Helper function to handle search methods and console messages.

    # List data
    if len(data) <= 100:
        print(f"\nDataset: {data}")
    else:
        print(f"\nDataset has {len(data)} items, min value {data[0]}, max value {data[-1]}.")

    # Show target value.
    print(f"Searching for {target_value} using *{method}* search...")

    # If data is empty.
    if len(data) == 0:
        print("The dataset is empty, exiting.")
        return

    # Perform linear or binary search.
    flag = None
    start = time.time()
    if method=="Linear":
        flag = linear_search(data, target_value)
    elif method=="Binary":
        flag = binary_search(data, target_value)
    else:
        ValueError("Unknown search method")
    end = time.time()
    print(f"Elapsed time sec: {end-start}")

    # Display informational message.
    if flag != -1:
        print(f"Value {target_value} found in the data set.")
    else:
        print(f"Value {target_value} not found in the data set.")

    return

def run_linear_and_binary_searches(data, target_values):
    # Perform searches
    for target_value in target_values:
        # Perform linear search.
        search_and_display(data, target_value)
        # Perform binary search.
        search_and_display(data, target_value, "Binary")

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Create small ordered dataset.
    print(f"\n\n*** Small dataset ***")
    data_1 = list(range(3, 20, 2))

    # Set target values: first value is in data_1, the remaining are not.
    target_values = [5, 21, 18]

    # Perform searches
    run_linear_and_binary_searches(data_1, target_values)

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Create large ordered dataset.
    data_2 = list(range(3, 2000003, 2))
    print(f"\n\n*** Large dataset ***")

    # Set target values.
    target_values = [21, 18, 5]
    # Perform searches
    run_linear_and_binary_searches(data_2, target_values)

# ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    print(f"\n\n***Empty dataset***")
    no_data = []
    run_linear_and_binary_searches(no_data, target_values)

    print(f"\n\n***Single-point dataset***")
    data_with_one_point = [57]
    run_linear_and_binary_searches(data_with_one_point, target_values)


    # Large dataset, search value in first and last position.
    # Set target values.
    print(f"\n\n***Values at first and last position***")
    target_values = [3, 2000001]
    run_linear_and_binary_searches(data_2, target_values)

if __name__ == "__main__":
    main()