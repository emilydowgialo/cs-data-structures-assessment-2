# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.

def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """

    # Check to see if i is the value of the index of the last element in the list
    # This is the stopping condition
    if (i == len(my_list)):
        return

    # Print the element at index i
    print my_list[i]

    # Call this same function but set i to one value higher
    print_item(my_list, i+1)


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """

    # Print the data for that node
    print tree.data

    # For every child, call this again
    for child in tree.children:
        print_all_tree_data(child)


# 3. Write a function that uses recursion to find the length of a list.

def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """

    # If my list is empty
    if not my_list:
        return 0

    # Call this function sliced at index 1 plus 1
    return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """

    # Set a counter to 0 to start
    counter = 0

    # Iterate over the node's children and increase the counter by the number
    # of children that node has
    for child in tree.children:
        counter += num_nodes(child)

    # Return the counter plus 1
    # The 1 represents the parent node
    return counter + 1

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
