from calculator import advanced, simple, arguments, input_parser

def main():
    
    advanced_calculator = advanced.AdvancedCalculator()

    skip_lines = 0

    while(True):
        try:
            operation, first_param, second_param = input_parser.get_input_from_json(skip_lines)
            if operation == "QUIT":
                break
            input_arguments = arguments.Arguments(first_param, second_param)
            advanced_calculator.execute(operation, input_arguments)
            skip_lines += 1
        except:
            print("Finished!")
            break
        
if __name__ == "__main__":
    main()