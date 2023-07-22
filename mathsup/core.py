# -*- coding: utf-8 -*-
from . import helpers


def factorial(n):
    """Calculating n factorialx"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
