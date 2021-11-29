"""Calculation history Class"""
import history


class Calculations:
    # pylint: disable=too-few-public-methods

    def __init__(self) -> None:
        self.history = History()

    @staticmethod
    def get_result(self):
        return self.history.get_last_calculation()


    @staticmethod
    def add_calculation(self, calculation):
        """ get a specific calculation from history"""
        return self.history.add_calculation(calculation)

    @staticmethod
    def add_number(self, values):
        self.history.add_addition_calculation(values)
        return self.history.get_last_calculation().get_result()

    @staticmethod
    def subtract_number(self, values):
        self.history.add_subtraction_calculation(values)
        return self.history.get_last_calculation().get_result()

    @staticmethod
    def multiply_numbers(self, values):
        self.history.add_multiplication_calculation(values)
        return self.history.get_last_calculation().get_result()

    @staticmethod
    def divide_numbers(self, values):
        self.history.add_division_calculation(values)
        return self.history.get_last_calculation().get_result()
