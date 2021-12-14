"""Subtraction Class"""
from calc.calculations.calculation import Calculation


class Subtraction(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """get the subtraction results"""
        # pylint: disable=unbalanced-tuple-unpacking
        value1, value2 = self.values[:2]
        print("value1", value1)
        print("value2", value2)
        result = value1 - value2
        res = self.values[2:]
        print(res)
        for val in enumerate(res):
            print("result", val)
            result = result - val[1]
        print("outside", result)
        return result
