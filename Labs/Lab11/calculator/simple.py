from calculator import arguments

class SimpleCalculator():
    """
    A class to provide basic calculator functionality.

    ...

    Methods
    -------
    add(arguments: arguments.Arguments):
        Addtiion.
    substract(arguments: arguments.Arguments):
        Substract.
    multiply(arguments: arguments.Arguments):
        Multiply.
    divide(arguments: arguments.Arguments):
        Divide.
    """
    
    def add(self, arguments: arguments.Arguments):
        return float(arguments.first_param) + float(arguments.second_param)

    def subtract(self, arguments: arguments.Arguments):
        return float(arguments.first_param) - float(arguments.second_param)

    def multiply(self, arguments: arguments.Arguments):
        return float(arguments.first_param) * float(arguments.second_param)

    def divide(self, arguments: arguments.Arguments):
        try:
            return float(arguments.first_param) / float(arguments.second_param)
        except ValueError:
            return 0
        except ZeroDivisionError:
            return 0
        finally:
            print("There was a problem with the division.")