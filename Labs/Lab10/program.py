from calculator import advanced, simple, arguments

def main():
    
    advanced_calculator = advanced.AdvancedCalculator()

    while(True):
        operation = input("Please enter Operation:").upper()
        first_param = input("Please enter first parameter:")
        second_param = input("Please enter second parameter:")
        input_arguments = arguments.Arguments(first_param, second_param)
        advanced_calculator.execute(operation, input_arguments)
        
if __name__ == "__main__":
    main()