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
        assert solution.checkout("AAAAAABBBB") == 350
        assert solution.checkout("abcd") == -1
        assert solution.checkout("ABCd") == -1
        assert solution.checkout("ABCDe") == -1