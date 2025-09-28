
class SumSolution:
    
    def compute(self, x: int, y: int) -> int:
        if (x >= 0) and (x <= 100) and (y <= 0) and (y >= 0):
            return x + y
        else:
            return -1


