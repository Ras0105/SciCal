# ==============================
# BASIC OPERATIONS
# ==============================

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):

    try:
        return a / b

    except ZeroDivisionError:
        return "Division by zero error"


def mod(a, b):

    try:
        return a % b

    except ZeroDivisionError:
        return "Division by zero error"


def floordiv(a, b):

    try:
        return a // b

    except ZeroDivisionError:
        return "Division by zero error"


def power(a, b):

    result = 1

    if b == 0:
        return 1

    if b < 0:
        b = -b
        a = 1 / a

    for i in range(int(b)):
        result *= a

    return result


# ==============================
# UNARY OPERATIONS
# ==============================

def positive(a):
    return +a


def negative(a):
    return -a


def absolute(a):

    if a < 0:
        return -a

    return a


# ==============================
# COMPARISON OPERATIONS
# ==============================

def equal(a, b):
    return a == b


def notEqual(a, b):
    return a != b


def greater(a, b):
    return a > b


def less(a, b):
    return a < b


def greaterEqual(a, b):
    return a >= b


def lessEqual(a, b):
    return a <= b

# ==============================
# UTILITY OPERATIONS
# ==============================

def reciprocal(a):

    try:
        return 1 / a

    except ZeroDivisionError:
        return "Division by zero error"


def percentage(a, b):

    try:
        return (a / b) * 100

    except ZeroDivisionError:
        return "Division by zero error"


def increment(a):
    return a + 1


def decrement(a):
    return a - 1