#!/usr/bin/env python3
"""
A module that contains a function that returns a tuple
"""

import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    A func that takes in 2 args, "page" and "page_size" and returns a tuple
    containing the start and and end index for pagination
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
