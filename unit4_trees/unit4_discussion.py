"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Initializing instance variables.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # Set root to None to create an empty tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # If BST is empty, create and assign a node with the
        # given value to the tree's root node and return.
        if self.root is None:
            self.root = Node(value)
            return

        # If the value does not exist in the tree,
        # call recursive insertion.
        if not self.search(value):
            self._insert_recursive(self.root, value)
        else:
            # Otherwise abort insertion.
            print(f"Value {value} already in the tree. Aborting insertion.")


    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        current_node = node
        # While node has existing value.
        while not current_node.value is None:
            # If insertion value smaller than current value,
            if current_node.value > value:
                # Check the left child.
                if current_node.left is None:
                    # If the child is empty, insert new node with value
                    # and return.
                    current_node.left = Node(value)
                    return current_node
                else:
                    # Otherwise continue searching the left child.
                    current_node = current_node.left
            else:
                # If insertion value greater than current value,
                # Check the right child.
                if current_node.right is None:
                    # If the child is empty, insert new node with value
                    # and return.
                    current_node.right = Node(value)
                    return current_node
                else:
                    # Otherwise continue searching the right child.
                    current_node = current_node.right

        return current_node


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # If the tree is empty, end search and return False.
        if self.root is None:
            return False

        # Call recursive search starting from the root
        # of the tree and return False if it returns None.
        if self._search_recursive(self.root, value) is None:
            return False

        # Search found the value. Return true.
        return True


    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Use a while loop to search recursively in the BST.
        current_node = node
        while not current_node is None:
            # We found the queried value and return the node.
            if current_node.value == value:
                return current_node
            # Node value is smaller than the query.
            # Move search to the right child.
            elif current_node.value < value:
                current_node = current_node.right
            else:
                # Node value is greater than the query.
                # Move search to the left child.
                current_node = current_node.left

        return None

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Call recursive inorder function.
        values = self._inorder_recursive(self.root, [])
        # Return the list of values that were found in the appropriate order.
        return values


    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # Return if the search node is None.
        if node is None:
            return

        # Go to the left branch and call self.
        self._inorder_recursive(node.left, values)
        # Append start node to the list.
        values.append(node.value)
        # Go to the right branch and call self.
        self._inorder_recursive(node.right, values)
        # Return values.
        return values

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Create an empty BST.
    my_bst = BST()
    # Set values to be inserted.
    values = [10, 20, 3, 15, 7, 22, 1]
    print(f"Constructing a tree by entering the following values from first to last:\n {values}")
    # Insert values in the tree in the given order.
    for value in values:
        my_bst.insert(value)


    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # Traverse the tree in-order.
    print("In-order traversal of my BST")
    # Display the traversal output.
    print(my_bst.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Setting two queries present in the tree and another two that
    # are not contained in the tree.
    queries = [15, 20, 100, 200]
    # Loop over the queries.
    for query in queries:
        # Search for these values and print outcome.
        if my_bst.search(query):
            print(f"{query} is in my BST")
        else:
            print(f"{query} is not in my BST")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # First edge case:
    # Create an empty tree.
    empty_bst = BST()
    query = 20
    # Search for a value inside the empty tree and
    # print results.
    print(f"Searching for {query} in an empty tree...")
    result = empty_bst.search(query)
    print(f"Query output: {result}")

    # Second edge case:
    # Create tree and add one value.
    value = 50
    print(f"Creating a BST with one node with value {value}...")
    bst_single_node = BST()
    bst_single_node.insert(value)
    # Traverse the tree in-order and display output.
    print("In-order traversal of this BST")
    print(bst_single_node.inorder())

    # Third edge case:
    # Try to insert the same value into the tree and see
    # how it is handled.
    # The code recognizes value is repeated and aborts insertion.
    print(f"Re-inserting {value} in the same BST...")
    bst_single_node.insert(value)



if __name__ == "__main__":
    main()