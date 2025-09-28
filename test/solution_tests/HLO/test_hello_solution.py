from solutions.HLO.hello_solution import HelloSolution
import pytest

class TestHLO():
    def test_hello(self):
        assert HelloSolution.hello(self, "Bob") == "Hello, Bob!"
        
        with pytest.raises(TypeError):
            HelloSolution.hello(self, 1)
