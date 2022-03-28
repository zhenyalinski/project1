""" These are the Operation Classes"""
# added Division

class Addition:
    """ This is the addition class"""

    # this defines a static method that you can use without instantiating the calculator class
    # If you can go to the store and buy it and it is an object if you can't buy it then its a static method
    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return value_1 + value_2


class Subtraction:
    """ This is the subtraction class"""

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the add method"""
        return value_1 - value_2


class Multiplication:
    """ This is the subtraction class"""

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the add method"""
        return value_1 * value_2


class Division:
    """This is the division class"""

    @staticmethod
    # have to do the math
    def divide(value_1, value_2):
        """This is the divide method"""
        quotient = value_1 / value_2
        return quotient
