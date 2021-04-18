from calculator import arguments, simple

class AdvancedCalculator(simple.SimpleCalculator):
    """
    A class to provide advanced calculator functionality.

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
    def union(self, arguments: arguments.Arguments):
        from ast import literal_eval
        list_one = set(literal_eval(arguments.first_param))
        list_two = set(literal_eval(arguments.second_param))
        return list_one.union(list_two)

    def difference(self, arguments: arguments.Arguments):
        from ast import literal_eval
        list_one = set(literal_eval(arguments.first_param))
        list_two = set(literal_eval(arguments.second_param))
        return list_one.difference(list_two)

    def intersection(self, arguments: arguments.Arguments):
        from ast import literal_eval
        list_one = set(literal_eval(arguments.first_param))
        list_two = set(literal_eval(arguments.second_param))
        return list_one.intersection(list_two)

    def calculate_stats(self, arguments: arguments.Arguments):
        list_one = arguments.first_param.split(",")
        list_two = arguments.first_param.split(",")
        print(f"List 1 Min: {min(list_one)}")
        print(f"List 1 Max: {max(list_one)}")
        print(f"List 1 Length: {len(list_one)}")
        print(f"List 2 Min: {min(list_two)}")
        print(f"List 2 Max: {max(list_two)}")
        print(f"List 2 Length: {len(list_two)}")
        
    def sort_lists(self, arguments: arguments.Arguments):
        list_one = arguments.first_param.split(",")
        list_two = arguments.second_param.split(",")
        combined_list = list_one + list_two
        combined_list.sort()
        return combined_list

    def reduce_list(self, arguments: arguments.Arguments):
        from functools import reduce
        list_one = map(int,arguments.first_param.split(","))
        even_filter_flag = bool(arguments.second_param)
        return reduce(lambda x, y: x + y, list_one)

    def map_list(self, arguments: arguments.Arguments):
        list_one = map(int,arguments.first_param.split(","))
        factor = int(arguments.second_param)
        return list(map(lambda x : x * factor, list_one))