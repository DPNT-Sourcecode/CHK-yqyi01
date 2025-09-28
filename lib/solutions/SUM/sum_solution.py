
class SumSolution:
    
    def compute(self, x: int, y: int) -> int:
        if not ((x >= 0) and (x <= 100) and (y >= 0) and (y <= 100)):
            raise ValueError("Input values must be between 0 and 100.")
        
        return (x + y)
