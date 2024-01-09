#!/usr/bin/python3
"""
Contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    while obj.__class__ is not None:
        if obj.__class__ == a_class:
            return True
        obj = obj.__class__.__base__

    return False 
