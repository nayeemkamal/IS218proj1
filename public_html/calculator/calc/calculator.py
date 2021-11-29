""" This is the increment function"""
from calc.history.history import History

# the calculator class just contains the methods to calculate


class Calculator:
    """ This is the Calculator class"""
    # the calculator class just calls methods on History.class
    @staticmethod
    def get_last_result_value():
        """ This is the gets the value of result of the calculation"""
        return History.get_last_calculation().get_result()

    @staticmethod
    def get_last_result():
        """ This is the gets the result of the calculation"""
        return History.get_last_calculation().get_result()

    @staticmethod
    def clear_history():
        """ This is the clears history of the calculation"""
        return History.clear_history()

    @staticmethod
    def count_history():
        """ This is the count history of the calculation"""
        return History.count_history()

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """ adds list of numbers"""
        History.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        History.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplication number from result"""
        History.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ division number from result"""
        History.add_division_calculation(tuple_values)
        return True
