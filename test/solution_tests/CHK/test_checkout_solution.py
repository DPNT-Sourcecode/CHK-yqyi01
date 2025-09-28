from solutions.CHK.checkout_solution import CheckoutSolution
import pytest

class TestCheckout():
    def test_checkout(self):
        solution = CheckoutSolution()
        assert solution.checkout(self, "ABCD") == 115
        assert solution.checkout(self, "AABCD") == 165
        assert solution.checkout(self, "AAABCD") == 195
        assert solution.checkout(self, "AAABBCD") == 210
        assert solution.checkout(self, "AAAABBCD") == 260
        assert solution.checkout(self, "AAAAAABBBB") == 350
        assert solution.checkout(self, "abcd") == -1
        assert solution.checkout(self, "ABCd") == -1
        assert solution.checkout(self, "ABCDe") == -1



