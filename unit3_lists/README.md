# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

# Unit 3 Discussion: List Operations (Python)

## Overview

This assignment explored list operations in Python.
I implemented and tested their core operations in Python to demonstrate item insertion, deletion, and searching.

## Implementation Summary

I used a Python list and completed the `insert_at()`, `delete_at()`, and `search_value()` methods.

- **insert_at:** Added an item to the end of the list.
- **delete_at:** Removed and returned the last item, demonstrating LIFO behavior.
- **search_value:** Returned the last item without removing it.

The deletion method handles invalid index values by catching `IndexError` and returning `None`.
The search method handles not-found patterns by catching `ValueError` and returning -1.

## Design Approach and Real-World Applications

I used a Python list because it implements the requested functionalities of a linked list.
This approach is suitable for applications such as song playlist management.
Linked lists can also be used for representation and management of graphs.

## Testing

The program demonstrated multiple list operations following the guidelines.
These operations include insertion tests at multiple positions in the list, deletion
tests at multiple positions, successful and failed search tests.
Regarding edge cases, we tested insertion of an item into an empty list and iterative 
deletions of items from a list and attempt to delete from an empty list.
The code handles index exceptions during deletion by returning `None`.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
In this assignment, I learned how to perform linked list operations using Python's `List` data type.
I used `insert()`, `pop()`, and `index()` methods to implement insertion, deletion, and search operations.
I developed tests to observe how the list changed after each operation.

2. What challenges did you encounter, and how did you overcome them?
Particular attention needs to be paid to how the implementation handles edge cases.

3. How do list operations impact performance in real-world applications?
Time and space complexity needs to be considered especially for large scale applications.
Python lists are implemented as dynamic arrays, not as linked lists.
Therefore, accessing items by index is time efficient, but item insertion requires shifting 
and potential memory re-allocation, which may increase space and time complexity.
