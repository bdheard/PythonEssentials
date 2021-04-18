import json

def get_input_from_console():
    operation = input("Please enter Operation:").upper()
    first_param = input("Please enter first parameter:")
    second_param = input("Please enter second parameter:")
    return operation, first_param, second_param

def get_input_from_json(skip_line: int):
    try:
        with open('C:\src\git\PythonEssentials\Labs\Lab12\calculator_input.json') as json_list:
            for _ in range(skip_line):
                next(json_list)
            for entry in json_list:
                calculation = json.loads(entry)
                operation = calculation['operation']
                first_param = calculation['first']
                second_param = calculation['second']
                return operation, first_param, second_param
    except:
        return "QUIT", "0", "0"
       