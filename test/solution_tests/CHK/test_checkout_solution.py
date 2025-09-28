from solutions.CHK.checkout_solution import CheckoutSolution
import pytest

class TestCheckout():
    def test_checkout_basic(self):
        solution = CheckoutSolution()
        assert solution.checkout("A") == 50
        assert solution.checkout("B") == 30
        assert solution.checkout("C") == 20
        assert solution.checkout("D") == 15
        assert solution.checkout("E") == 40

    def test_multi_buy_offers(self):
        solution = CheckoutSolution()
        assert solution.checkout("AAA") == 130  # 3A for 130
        assert solution.checkout("AAAAA") == 200  # 5A for 200
        assert solution.checkout("AAAAAA") == 250  # 5A for 200 + 1A for 50
        assert solution.checkout("BB") == 45  # 2B for 45
        assert solution.checkout("BBBB") == 90  # 2B for 45 x2

    def test_cross_item_offer(self):
        solution = CheckoutSolution()
        assert solution.checkout("EEB") == 80  # 2E get one B free (B is free)
        assert solution.checkout("EEBB") == 110  # 2E get one B free, 1B left to pay for
        assert solution.checkout("EEEEBB") == 160  # 4E get two B free, both Bs are free

    def test_self_free_offer(self):
        solution = CheckoutSolution()
        assert solution.checkout("FF") == 20  # 2F for 20 (no free yet)
        assert solution.checkout("FFF") == 20  # 2F get one F free (pay for 2, 1 free)
        assert solution.checkout("FFFF") == 30  # 3F get one F free (pay for 3, 1 free)
        assert solution.checkout("FFFFFF") == 40  # 2 free Fs, pay for 4

    def test_group_and_other_offers(self):
        solution = CheckoutSolution()
        assert solution.checkout("HHHHH") == 45  # 5H for 45
        assert solution.checkout("HHHHHHHHHH") == 80  # 10H for 80
        assert solution.checkout("KK") == 150  # 2K for 150
        assert solution.checkout("PPPPP") == 200  # 5P for 200
        assert solution.checkout("QQQ") == 80  # 3Q for 80
        assert solution.checkout("VV") == 90  # 2V for 90
        assert solution.checkout("VVV") == 130  # 3V for 130

    def test_invalid_input(self):
        solution = CheckoutSolution()
        assert solution.checkout("a") == -1
        assert solution.checkout("1") == -1
        assert solution.checkout("A1B") == -1
        assert solution.checkout("") == 0