from solutions.CHK.checkout_solution import CheckoutSolution
import pytest

class TestSum():
    def test_sum(self):
        assert CheckoutSolution.checkout(self, "cd") == 35
        
        
