"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        try:
            result = 1.0
            for value in self.values:
                result = value / result
            return result
        except ZeroDivisionError as error:
            raise ValueError
