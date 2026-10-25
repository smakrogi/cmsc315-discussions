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

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I reviewed how a Python List implements stack LIFO functionality. By applying push and pop operations, I observed how the order of insertion determines the order of removal.
I also reviewed how a Python deque container to implement queue FIFO functionality. Deque is a generalization of stacks and queues. It is effectively a double-ended queue so it can be used as a queue and as a stack.
A deque supports memory efficient appends and pops with approximately the same O(1) performance in either direction.
2. What challenges did you encounter, and how did you overcome them?
While the Stack and Queue were already implemented in python, it's always good to double-check that the solution developed here, addresses the requirements in the guidelines.
3. Explain the differences between stacks and queues as this relates to real-world applications.
I think that stacks and queues find numerous applications in computer systems and applications. Stacks and queues are used in computer organization to access memory for different tasks. 
In applications, stacks are useful for implementing undo lists and function call hierarchies because the most recent item is accessed first.
Queues can be used to buffer operations in user interfaces and in data transmision in networks because items are accessed and processed sequentially. 
This information significantly helps to choose the right type of data structure based on the application's requirements. 