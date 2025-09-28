from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3
        assert SumSolution().compute(0, 100) == 100
        assert SumSolution().compute(1, 100) == 101
        assert SumSolution().compute(-1, 100) == ValueError




