"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class History:

    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        History.history.clear()
        return True

    @staticmethod
    def count_history():
        return len(History.history)

    @staticmethod
    def get_last_calculation():
        return History.history[-1]

    @staticmethod
    def get_first_calculation():
        return History.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return History.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return History.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        History.add_calculation(Addition(values))
        return History.get_last_calculation().get_result()

    @staticmethod
    def add_subtraction_calculation(values):
        History.add_calculation(Subtraction(values))
        return History.get_last_calculation().get_result()

    @staticmethod
    def add_multiplication_calculation(values):
        History.add_calculation(Multiplication(values))
        return History.get_last_calculation().get_result()

    @staticmethod
    def add_division_calculation(values):
        History.add_calculation(Division(values))
        return History.get_last_calculation().get_result()
