# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Design and Implementation
The implementation consists of the following functions:

- **`lookup_key`**: Helper function that looks up a key and displays the corresponding value, or displays a not-found message.
- **`remove_key`**: Helper function that removes a key and handles the edge case of not-existing keys.
- **`main`**: Creates and populates a dictionary, demonstrates lookup, update, and delete operations, and tests edge cases. Real world scenario is a course gradebook.
 
### Edge Cases
The main functions shows how the code handles the following edge cases.
- Look up present and missing keys
- Delete a missing key safely
- Update a missing key