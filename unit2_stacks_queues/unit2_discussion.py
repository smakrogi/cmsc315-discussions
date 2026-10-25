"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._my_stack = list()

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # The item is appended to the right. Pop will return the last item on the right.
        # This implements stack LIFO functionality.
        self._my_stack.append(value)
        print(f"Pushed item. Stack contents: {self._my_stack}")

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # In this implementation we return None if the stack is empty.
        try:
            value = self._my_stack.pop()
            print(f"Popped item. Stack contents: {self._my_stack}")
        except IndexError:
            print(f"Popping from empty stack. Returning None")
            value = None
        return value

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # peek tries to return the last list item.
        # Returns None if the list is empty
        try:
            value = self._my_stack[-1]
            print(f"Peeked item with value {value}")
        except IndexError:
            print(f"The stack is empty. Returning None.")
            value = None
        return value

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        if len(self._my_stack) == 0:
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty")
            return False

class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._my_queue = deque()


    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Add item to the end of the deque.
        self._my_queue.append(value)
        print(f"Enqueued item. Queue contents: {self._my_queue}")


    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Pop item from the left of the queue to implement FIFO operation.
        # Handle empty queue by returning None.
        try:
            value = self._my_queue.popleft()
            print(f"Dequeued item. Queue contents: {self._my_queue}")
        except IndexError:
            print(f"Dequeuing empty queue. Returning None.")
            value = None
        return value


    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        try:
            value = self._my_queue[0]
            print(f"Front item: {value}")
        except IndexError:
            print(f"The queue is empty. Returning None.")
            value = None
        return value


    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        if len(self._my_queue) == 0:
            print("Queue is empty")
            return True
        else:
            print("Queue is not empty")
            return False


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")

    # Create stack.
    print("\nCreate a stack")
    stack_example = Stack()

    # Push items to stack.
    print("\nPush items to stack")
    stack_example.push("Apple")
    stack_example.push("Orange")
    stack_example.push("Strawberry")
    stack_example.push("Banana")

    # Pop items from stack.
    print("\nPop items from stack")
    stack_example.pop()
    stack_example.pop()
    stack_example.pop()
    stack_example.pop()
    stack_example.is_empty()

    # Peek in stack.
    print(f"\nPeeking inside the empty stack: {stack_example.peek()}")

    print("\nTry to pop an item from empty stack")
    stack_example.pop()

    print("\nAnother stack example")
    stack_example_2 = Stack()
    stack_example_2.push("Strawberry")
    stack_example_2.pop()
    print(f"Peek inside the empty stack: {stack_example_2.peek()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")

    # Create a Queue
    print("\nCreate a queue")
    queue_example = Queue()

    # Enqueue and dequeue items
    print("\nEnqueue items")
    queue_example.enqueue("Lion")
    queue_example.enqueue("Tiger")
    queue_example.enqueue("Cheetah")
    queue_example.enqueue("Leopard")

    print("\nDequeue items")
    queue_example.dequeue()
    queue_example.dequeue()
    queue_example.dequeue()
    queue_example.dequeue()
    queue_example.is_empty()

    # Front item in queue.
    print(f"\nFront item in the queue: {queue_example.front()}")

    print("\nTry to dequeue an item from empty queue")
    queue_example.dequeue()

    print("\nAnother queue example")
    queue_example_2 = Queue()
    queue_example_2.enqueue("Strawberry")
    queue_example_2.dequeue()
    print(f"\nFront item in the queue: {queue_example_2.front()}")

if __name__ == "__main__":
    main()
