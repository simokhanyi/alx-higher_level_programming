#!/usr/bin/python3
"""
Module mylist that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Print the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# Test the code


if __name__ == '__main__':
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)  # Original list
    my_list.print_sorted()  # Sorted list
    print(my_list)  # Original list remains unchanged
