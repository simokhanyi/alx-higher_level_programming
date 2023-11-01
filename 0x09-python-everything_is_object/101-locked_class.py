#!/usr/bin/python3
"""Low memory
"""


class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    """
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' no attribute '" + name + "'")
        super().__setattr__(name, value)
