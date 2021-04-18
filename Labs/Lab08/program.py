from calculator import advanced, simple, arguments, operations

def main():
    
    advanced_calculator = advanced.AdvancedCalculator()

    while(True):
        operation = input("Please enter Operation:").upper()
        first_param = input("Please enter first parameter:")
        second_param = input("Please enter second parameter:")
        input_arguments = arguments.Arguments(first_param, second_param)

        if operations.Operations[operation] is operations.Operations.ADD:
            print(first_param, "+", second_param, "=", advanced_calculator.add(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.SUB:
            print(first_param, "-", second_param, "=", advanced_calculator.subtract(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.MUL:
            print(first_param, "*", second_param, "=", advanced_calculator.multiply(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.DIV:
            print(first_param, "/", second_param, "=", advanced_calculator.divide(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.UNION:
            print(f"Union: {advanced_calculator.union(input_arguments)}")
        elif operations.Operations[operation]  == operations.Operations.INTER:
            print(f"Intersection: {advanced_calculator.intersection(input_arguments)}")
        elif operations.Operations[operation]  == operations.Operations.SORT:
            print(f"Difference: {advanced_calculator.difference(input_arguments)}")
        elif operations.Operations[operation]  == 'Sort':
            print(advanced_calculator.sort_lists(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.STATS:
            print(advanced_calculator.calculate_stats(input_arguments))
        elif operations.Operations[operation] == operations.Operations.REDUCE:
            print(advanced_calculator.reduce_list(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.MAP:
            print(advanced_calculator.map_list(input_arguments))
        elif operations.Operations[operation]  == operations.Operations.QUIT:
            break
        else:
            print("Unknown operation.")

if __name__ == "__main__":
    main()