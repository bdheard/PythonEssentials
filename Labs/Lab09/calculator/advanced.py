from calculator import arguments, simple, operations
from pathlib import Path
from itertools import islice

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

    def write_log_entry(self, operation: str, input_arguments: arguments.Arguments):
        file_stream = open('labs\lab09\calculator_log.txt', 'a')
        file_stream.writelines(operation + '\t' + input_arguments.first_param + '\t' + input_arguments.second_param + '\n')
        file_stream.close()
    
    def read_log_entry(self, input_arguments: arguments.Arguments):
        last_n_lines = int(input_arguments.first_param)
        order = str(input_arguments.second_param)
        log_file = 'labs\lab09\calculator_log.txt'
        
        with open(log_file) as file:
            if order.upper() == 'ASC':
                for line in islice(file, last_n_lines):
                    print(line, end ='')
            else:
                for line in (file.readlines() [-last_n_lines:]):
                    print(line, end ='')

    def execute(self, operation: str, input_arguments: arguments.Arguments):
        
        self.write_log_entry(operation, input_arguments)

        if operations.Operations[operation] is operations.Operations.ADD:
            print(input_arguments.first_param, "+", input_arguments.second_param, "=", self.add(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.SUB:
            print(input_arguments.first_param, "-", input_arguments.second_param, "=", self.subtract(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.MUL:
            print(input_arguments.first_param, "*", input_arguments.second_param, "=", self.multiply(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.DIV:
            print(input_arguments.first_param, "/", input_arguments.second_param, "=", self.divide(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.UNION:
            print(f"Union: {self.union(input_arguments)}")
        elif operations.Operations[operation]  == operations.Operations.INTER:
            print(f"Intersection: {self.intersection(input_arguments)}")
        elif operations.Operations[operation]  == operations.Operations.SORT:
            print(f"Difference: {self.difference(input_arguments)}")
        elif operations.Operations[operation]  == 'Sort':
            print(self.sort_lists(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.STATS:
            print(self.calculate_stats(input_arguments))
        elif operations.Operations[operation] == operations.Operations.REDUCE:
            print(self.reduce_list(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.MAP:
            print(self.map_list(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.HIST:
            print(self.read_log_entry(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.QUIT:
            return
        else:
            print("Unknown operation.")

