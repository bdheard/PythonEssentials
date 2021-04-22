class Arguments():
    def __init__(self, first_param, second_param):
        self.first_param = first_param
        self.second_param = second_param

    @property
    def first_param(self):
        return self.__first_param
    
    @first_param.setter
    def first_param(self, value):
        self.__first_param = value

    @property
    def second_param(self):
        return self.__second_param
    
    @second_param.setter
    def second_param(self, value):
        self.__second_param = value

class SimpleCalculator():

    def add(self, arguments: Arguments):
        return float(arguments.first_param) + float(arguments.second_param)

    def subtract(self, arguments: Arguments):
        return float(arguments.first_param) - float(arguments.second_param)

    def multiply(self, arguments: Arguments):
        return float(arguments.first_param) * float(arguments.second_param)

    def divide(self, arguments: Arguments):
        try:
            return float(arguments.first_param) / float(arguments.second_param)
        except ValueError:
            return 0
        except ZeroDivisionError:
            return 0
        finally:
            print("There was a problem with the division.")

class AdvancedCalculator(SimpleCalculator):
    def union(self, arguments: Arguments):
        list_one = set(arguments.first_param.split(","))
        list_two = set(arguments.first_param.split(","))
        return list_one.union(list_two)

    def difference(self, arguments: Arguments):
        list_one = set(arguments.first_param.split(","))
        list_two = set(arguments.first_param.split(","))
        return list_one.difference(list_two)

    def intersection(self, arguments: Arguments):
        list_one = set(arguments.first_param.split(","))
        list_two = set(arguments.first_param.split(","))
        return list_one.intersection(list_two)

    def calculate_stats(self, arguments: Arguments):
        list_one = arguments.first_param.split(",")
        list_two = arguments.first_param.split(",")
        print(f"List 1 Min: {min(list_one)}")
        print(f"List 1 Max: {max(list_one)}")
        print(f"List 1 Length: {len(list_one)}")
        print(f"List 2 Min: {min(list_two)}")
        print(f"List 2 Max: {max(list_two)}")
        print(f"List 2 Length: {len(list_two)}")
        
    def sort_lists(self, arguments: Arguments):
        list_one = arguments.first_param.split(",")
        list_two = arguments.second_param.split(",")
        combined_list = list_one + list_two
        combined_list.sort()
        return combined_list

    def reduce_list(self, arguments: Arguments):
        from functools import reduce
        list_one = map(int,arguments.first_param.split(","))
        return reduce(lambda x, y: x + y, list_one)

    def map_list(self, arguments: Arguments):
        list_one = map(int,arguments.first_param.split(","))
        factor = int(arguments.second_param)
        return list(map(lambda x : x * factor, list_one))

from enum import Enum
class Operations(Enum):
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    SORT = "SORT"
    UNION = "UNION"
    DIFF = "DIFF"
    INTER = "INTER"
    MAP = "MAP"
    REDUCE = "REDUCE"
    STATS = "STATS"
    QUIT = "QUIT"

def main():

    advanced_calculator = AdvancedCalculator()

    while(True):
        operation = input("Please enter Operation:").upper()
        first_param = input("Please enter first parameter:")
        second_param = input("Please enter second parameter:")
        arguments = Arguments(first_param, second_param)

        if Operations[operation] is Operations.ADD:
            print(first_param, "+", second_param, "=", advanced_calculator.add(arguments))
        elif Operations[operation]  == Operations.SUB:
            print(first_param, "-", second_param, "=", advanced_calculator.subtract(arguments))
        elif Operations[operation]  == Operations.MUL:
            print(first_param, "*", second_param, "=", advanced_calculator.multiply(arguments))
        elif Operations[operation]  == Operations.DIV:
            print(first_param, "/", second_param, "=", advanced_calculator.divide(arguments))
        elif Operations[operation]  == Operations.UNION:
            print(f"Union: {advanced_calculator.union(arguments)}")
        elif Operations[operation]  == Operations.INTER:
            print(f"Intersection: {advanced_calculator.intersection(arguments)}")
        elif Operations[operation]  == Operations.SORT:
            print(f"Difference: {advanced_calculator.difference(arguments)}")
        elif Operations[operation]  == 'Sort':
            print(advanced_calculator.sort_lists(arguments))
        elif Operations[operation]  == Operations.STATS:
            print(advanced_calculator.calculate_stats(arguments))
        elif Operations[operation] == Operations.REDUCE:
            print(advanced_calculator.reduce_list(arguments))
        elif Operations[operation]  == Operations.MAP:
            print(advanced_calculator.map_list(arguments))
        elif Operations[operation]  == Operations.QUIT:
            break
        else:
            print("Unknown operation.")

if __name__ == "__main__":
    main()