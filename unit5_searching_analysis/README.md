# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Design and Implementation
The implementation consists of the following functions:

- **`linear_search`**: Performs linear search over a list of items. Returns the item's index or -1 if it was not found.
- **`binary_search`**: Performs binary search over a list of items. Returns the item's index or -1 if it was not found.
- **`search_and_display`**: Handles the search calls, displays input, output, and elapsed time for comparisons.
- **`run_linear_and_binary_searches`**: Runs a linear and a binary search for the same dataset and target_values.

### Edge Cases
The main functions shows how the code handles the following edge cases.
- Empty list
- Single-element list
- Value not present
- Value at the first position
- Value at the last position

