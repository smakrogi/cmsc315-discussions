# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.


# Unit 2 Discussion: Stacks and Queues (Python)

## Overview

This assignment explored two fundamental data structures: stacks and queues. 
I implemented and tested their core operations in Python to demonstrate how they manage items in different orders.

## Implementation Summary

I implemented the stack using a Python list and completed the `push()`, `pop()`, `peek()`, and `is_empty()` methods.

- **Push:** Added an item to the end of the list.
- **Pop:** Removed and returned the last item, demonstrating LIFO behavior.
- **Peek:** Returned the last item without removing it.
- **Is empty:** Checked whether the stack contained any items.

I implemented the queue using Python's `collections.deque` and completed the `enqueue()`, `dequeue()`, `front()`, and `is_empty()` methods.

- **Enqueue:** Added an item to the back of the queue.
- **Dequeue:** Removed and returned the item at the front, demonstrating FIFO behavior.
- **Front:** Returned the first item without removing it.
- **Is empty:** Checked whether the queue contained any items.

The removal and inspection methods handled empty data structures by catching `IndexError` and returning `None`. 
The program demonstrated stack operations using fruit names and queue operations using animal names. 
It also included attempts to remove or inspect items when the structures were empty.

## Design Approach and Real-World Applications

I used a Python list for the stack because appending and removing the last item support the LIFO principle. 
This approach is suitable for applications such as undo functionality, where the most recent action is reversed first.

I used `collections.deque` for the queue because it supports efficient operations at both ends. 
Adding items at the back and removing them from the front supports FIFO processing. 
A real-world example is a task-processing system in which requests are generally handled in arrival order.

## Testing

The program demonstrated multiple stack and queue operations, including adding and removing items, inspecting the next item, and attempting operations on empty structures. 
The single-item examples were intended to examine behavior when the last item was removed. 
Explicitly calling `is_empty()` after those removals provides an additional verification of these edge cases.
