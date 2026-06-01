# ==============================
# IMPORTS
# ==============================

from utils import *
from basicop import *
from scientificop import *


# ==============================
# MENU
# ==============================

operations = {

    '1': ("Addition", add),
    '+': ("Addition", add),

    '2': ("Subtraction", sub),
    '-': ("Subtraction", sub),

    '3': ("Multiplication", mul),
    '*': ("Multiplication", mul),

    '4': ("Division", div),
    '/': ("Division", div),

    '5': ("Modulus", mod),
    '%': ("Modulus", mod),

    '6': ("Floor Division", floordiv),
    '//': ("Floor Division", floordiv),
    
    '7': ("Power", power),
    '^': ("Power", power),
    '%': ("Power", power),

    '8': ("Equal To", equal),
    '==': ("Equal To", equal),
    '=': ("Equal To", equal),

    '9': ("Not Equal To", notEqual),
    '!=': ("Not Equal To", notEqual),

    '10': ("Greater Than", greater),
    '>': ("Greater Than", greater),

    '11': ("Less Than", less),
    '<': ("Less Than", less),

    '12': ("Greater Than Equal To", greaterEqual),
    '>=': ("Greater Than Equal To", greaterEqual),

    '13': ("Less Than Equal To", lessEqual),
    '<=': ("Less Than Equal To", lessEqual),

    '14': ("Square Root", sqrt),
    '15': ("Cube Root", cbrt),

    '16': ("Square", square),
    
    '17': ("Cube", cube),

    '18': ("Sine", sin),
    'sin': ("Sine", sin),
    '19': ("Cosine", cos),
    'cos': ("Cosine", cos),
    '20': ("Tangent", tan),
    'tan': ("Tangent", tan),
    '21': ("Cosecant", cosec),
    'cosec': ("Cosecant", cosec),
    '22': ("Secant", sec),
    'sec': ("Secant", sec),
    '23': ("Cotangent", cot),
    'cot': ("Cotangent", cot),
    '24': ("Factorial", factorial),
    '!': ("Factorial", factorial),
    'factorial': ("Factorial", factorial),
    '25': ("Natural Log", ln),
    'ln': ("Natural Log", ln),
    '26': ("Log10", log10),
    'log10': ("Log10", log10),
    '27': ("Exponential", exp),
    'exp': ("Exponential", exp),
    '28': ("Sinh", sinh),
    'sinh': ("Sinh", sinh),
    '29': ("Cosh", cosh),
    'cosh': ("Cosh", cosh),
    '30': ("Tanh", tanh),
    'tanh': ("Tanh", tanh),
    '31': ("Reciprocal", reciprocal),
    'reciprocal': ("Reciprocal", reciprocal),
    '32': ("Percentage", percentage),
    'percentage': ("Percentage", percentage),
    '33': ("Absolute", absolute),
    'abs': ("Absolute", absolute),
    '34': ("Ceil", ceil),
    'ceil': ("Ceil", ceil),
    '35': ("Floor", floor),
    'floor': ("Floor", floor)
}
menu = {

    '1': "Addition",
    '2': "Subtraction",
    '3': "Multiplication",
    '4': "Division",
    '5': "Modulus",
    '6': "Floor Division",
    '7': "Power",

    '8': "Equal To",
    '9': "Not Equal To",
    '10': "Greater Than",
    '11': "Less Than",
    '12': "Greater Than Equal To",
    '13': "Less Than Equal To",

    '14': "Square Root",
    '15': "Cube Root",
    '16': "Square",
    '17': "Cube",

    '18': "Sine",
    '19': "Cosine",
    '20': "Tangent",
    '21': "Cosecant",
    '22': "Secant",
    '23': "Cotangent",

    '24': "Factorial",

    '25': "Natural Log",
    '26': "Log10",
    '27': "Exponential",

    '28': "Sinh",
    '29': "Cosh",
    '30': "Tanh",

    '31': "Reciprocal",
    '32': "Percentage",
    '33': "Absolute",

    '34': "Ceil",
    '35': "Floor"
}

# ==============================
# CALCULATOR
# ==============================

def cal():

    title("SCIENTIFIC CALCULATOR")

    for key, value in menu.items():
        print(f"{key:>2} : {value}")
    op = input("\nChoose Operation Number: ")

    if op not in operations:
        return f"Operation '{op}' Does Not Exist"

    operation_name, function = operations[op]

    print(f"\nChosen Operation: {operation_name}")

    binary_ops = {
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Modulus",
    "Floor Division",
    "Power",
    "Equal To",
    "Not Equal To",
    "Greater Than",
    "Less Than",
    "Greater Than Equal To",
    "Less Than Equal To",
    "Percentage"
}

    if operation_name in binary_ops:

        a = getNumber("Enter 1st Operand: ")
        b = getNumber("Enter 2nd Operand: ")

        return function(a, b)

    else:

        a = getNumber("Enter Operand: ")

        if op == '24':
            return function(int(a))

        return function(a)


# ==============================
# MAIN
# ==============================

print("\nWelcome To Scientific Calculator!!")

while True:

    result = cal()

    showResult(result)

    if not continueChoice():
        print("\nCalculator Closed.")
        break