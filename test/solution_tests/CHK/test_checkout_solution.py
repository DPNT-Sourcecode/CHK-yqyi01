from solutions.CHK.checkout_solution import CheckoutSolution
import pytest

class TestSum():
    def test_sum(self):
        assert CheckoutSolution.checkout(self, "ABCD") == 115
        assert CheckoutSolution.checkout(self, "AABCD") == 165
        assert CheckoutSolution.checkout(self, "AAABCD") == 195
        assert CheckoutSolution.checkout(self, "AAABBCD") == 210
        assert CheckoutSolution.checkout(self, "AAAABBCD") == 260
        assert CheckoutSolution.checkout(self, "AAAAAA") == 260
        
        
        

