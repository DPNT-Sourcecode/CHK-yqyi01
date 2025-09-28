from solutions.SUM.sum_solution import SumSolution
import pytest

class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3
        assert SumSolution().compute(0, 100) == 100
        assert SumSolution().compute(1, 100) == 101
        
        with pytest.raises(ValueError):
            SumSolution().compute(-1, 50)
            SumSolution().compute(-1, 101)
            SumSolution().compute(1, 101)





