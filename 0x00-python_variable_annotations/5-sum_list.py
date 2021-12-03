#!/usr/bin/env python3
from typing import List
"""Annotation of list"""


def sum_list(input_list: List[float]) -> float:
    """takes a float list and returns the sum as float"""
    sum: float = 0
    for val in input_list:
        sum += val
    return sum
