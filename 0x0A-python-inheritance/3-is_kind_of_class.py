#!/usr/bin/python3
  """
    Check if the object is an instance of, or if it is an instance of a class
    that inherited from the specified class.

    Args:
    - obj: The object to check.
    - a_class: The specified class to check against.

    Returns:
    - True if obj is an instance of a_class or any class derived from it; otherwise, False.
    """


    def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
