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

- **insert_at:** Added an item to the indexed position in the list.
- **delete_at:** Removed and returned the item from the indexed position.
- **search_value:** Returned the index of first value occurrence.

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