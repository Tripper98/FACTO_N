# -*- coding: utf-8 -*-

from .context import mathsup

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_factorial_n(self):
        x = mathsup.core.factorial(2)
        assert x == 2, "Should be 2"


if __name__ == '__main__':
    unittest.main()