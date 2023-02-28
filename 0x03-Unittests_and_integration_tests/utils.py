#!/usr/bin/env python3
"""
This module defines the function access_nested_map
"""

from typing import List, Tuple, Any


def access_nested_map(nested_map: dict, path: List[str]) -> Any:
    """
    Accesses a key in nested dictionary of arbitrary depth

    Args:
        nested_map (dict): The nested dictionary to access
        path (list): List of keys representing the path to access the value

    Returns:
        Any: The value at the end of the path in the nested dictionary

    Raises:
        KeyError: If a key in the path is not found in the nested dictionary
    """
    for key in path:
        if key not in nested_map:
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map
