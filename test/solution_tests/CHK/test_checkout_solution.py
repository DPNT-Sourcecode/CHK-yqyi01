from solutions.CHK.checkout_solution import CheckoutSolution
import pytest

class TestCheckout():
    def test_checkout(self):
        solution = CheckoutSolution()
        assert solution.checkout("ABCD") == 115
        assert solution.checkout("AABCD") == 165
        assert solution.checkout("AAABCD") == 195
        assert solution.checkout("AAABBCD") == 210
        assert solution.checkout("AAAABBCD") == 260
        assert solution.checkout("AAAAAABBBB") == 340
        assert solution.checkout("EEB") == 80
        assert solution.checkout("AAAAA") == 200
        assert solution.checkout("AAAAAAAA") == 330
        assert solution.checkout("FF") == 20
        assert solution.checkout("FFF") == 20
        assert solution.checkout("FFFF") == 30
        assert solution.checkout("AAAAAAAABBBBFFF") == 440
        assert solution.checkout("abcd") == -1
        assert solution.checkout("ABCd") == -1
        assert solution.checkout("ABCDe") == -1
