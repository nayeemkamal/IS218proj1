"""Testing Addition"""
from calc.calculations.division import Division

def test_calculation_division():
    #Arrange
    mynumbers = (4.0,2.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 2.0

