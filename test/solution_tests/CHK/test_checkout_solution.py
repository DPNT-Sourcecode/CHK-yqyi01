from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout:
    def test_basic_prices(self):
        solution = CheckoutSolution()
        assert solution.checkout("A") == 50
        assert solution.checkout("B") == 30
        assert solution.checkout("C") == 20
        assert solution.checkout("D") == 15
        assert solution.checkout("E") == 40
        assert solution.checkout("F") == 10
        assert solution.checkout("G") == 20
        assert solution.checkout("H") == 10
        assert solution.checkout("I") == 35
        assert solution.checkout("J") == 60
        assert solution.checkout("K") == 70
        assert solution.checkout("L") == 90
        assert solution.checkout("M") == 15
        assert solution.checkout("N") == 40
        assert solution.checkout("O") == 10
        assert solution.checkout("P") == 50
        assert solution.checkout("Q") == 30
        assert solution.checkout("R") == 50
        assert solution.checkout("S") == 20
        assert solution.checkout("T") == 20
        assert solution.checkout("U") == 40
        assert solution.checkout("V") == 50
        assert solution.checkout("W") == 20
        assert solution.checkout("X") == 17
        assert solution.checkout("Y") == 20
        assert solution.checkout("Z") == 21

    def test_multi_buy_offers(self):
        solution = CheckoutSolution()
        assert solution.checkout("AAA") == 130
        assert solution.checkout("AAAAA") == 200
        assert solution.checkout("AAAAAA") == 250
        assert solution.checkout("BB") == 45
        assert solution.checkout("BBBB") == 90
        assert solution.checkout("HHHHH") == 45
        assert solution.checkout("HHHHHHHHHH") == 80
        assert solution.checkout("KK") == 150
        assert solution.checkout("PPPPP") == 200
        assert solution.checkout("QQQ") == 80
        assert solution.checkout("VV") == 90
        assert solution.checkout("VVV") == 130

    def test_cross_item_offers(self):
        solution = CheckoutSolution()
        assert solution.checkout("EEB") == 80  # 2E get one B free
        assert solution.checkout("EEBB") == 110  # 2E get one B free, 1B left to pay for
        assert solution.checkout("EEEEBB") == 160  # 4E get two B free, both Bs are free
        assert solution.checkout("NNNM") == 120  # 3N get one M free (M is free)
        assert solution.checkout("RRRQ") == 150  # 3R get one Q free (Q is free)
        assert solution.checkout("UUUU") == 120  # 4U get one U free (pay for 3)

    def test_self_free_offer(self):
        solution = CheckoutSolution()
        assert solution.checkout("FF") == 20  # 2F for 20 (no free yet)
        assert solution.checkout("FFF") == 20  # 2F get one F free (pay for 2, 1 free)
        assert solution.checkout("FFFF") == 30  # 3F get one F free (pay for 3, 1 free)
        assert solution.checkout("FFFFFF") == 40  # 2 free Fs, pay for 4

    def test_group_offer(self):
        solution = CheckoutSolution()
        # buy any 3 of (S,T,X,Y,Z) for 45
        assert solution.checkout("STX") == 45
        assert solution.checkout("STXYZ") == 90
        assert solution.checkout("SSS") == 45
        assert solution.checkout("SST") == 45
        assert solution.checkout("SXYZ") == 62  # 3 for 45, 1X left at 17

    def test_invalid_input(self):
        solution = CheckoutSolution()
        assert solution.checkout("a") == -1
        assert solution.checkout("1") == -1
        assert solution.checkout("A1B") == -1
        assert solution.checkout("") == 0

