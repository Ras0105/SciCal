# ==============================
# IMPORTS
# ==============================

from utils import *
from basicop import *


# ==============================
# ROOT FUNCTIONS
# ==============================

def sqrt(n):

    if n < 0:
        return "Invalid Input"

    if n == 0:
        return 0

    guess = n / 2

    for i in range(20):
        guess = (guess + n / guess) / 2

    return guess


def cbrt(n):

    if n == 0:
        return 0

    guess = n / 3

    for i in range(20):
        guess = ((2 * guess) + (n / (guess * guess))) / 3

    return guess


# ==============================
# ROUNDING FUNCTIONS
# ==============================

def ceil(a):

    integer = int(a)

    if a > integer:
        return integer + 1

    return integer


def floor(a):

    integer = int(a)

    if a < 0 and a != integer:
        return integer - 1

    return integer


# ==============================
# POWER FUNCTIONS
# ==============================

def square(a):
    return a * a


def cube(a):
    return a * a * a


# ==============================
# TRIGONOMETRIC FUNCTIONS
# ==============================

def normalizeAngle(degree):
    return degree % 360


def sin(degree):

    degree = normalizeAngle(degree)

    x = toRadians(degree)

    term = x
    result = x

    for i in range(1, 15):
        term *= (-1 * x * x) / ((2 * i) * (2 * i + 1))
        result += term

    return result


def cos(degree):

    degree = normalizeAngle(degree)

    x = toRadians(degree)

    result = 1
    term = 1

    for i in range(1, 15):
        term *= (-1 * x * x) / ((2 * i - 1) * (2 * i))
        result += term

    return result


def tan(degree):

    denominator = cos(degree)

    if absolute(denominator) < 0.000001:
        return "Undefined"

    return sin(degree) / denominator


def cosec(degree):

    value = sin(degree)

    if absolute(value) < 0.000001:
        return "Undefined"

    return 1 / value


def sec(degree):

    value = cos(degree)

    if absolute(value) < 0.000001:
        return "Undefined"

    return 1 / value


def cot(degree):

    value = tan(degree)

    if value == "Undefined":
        return "Undefined"

    if absolute(value) < 0.000001:
        return "Undefined"

    return 1 / value


# ==============================
# LOG FUNCTIONS
# ==============================

def ln(x):

    if x <= 0:
        return "Invalid Input"

    n = 1000

    return n * ((x ** (1 / n)) - 1)


def log10(x):

    if x <= 0:
        return "Invalid Input"

    return ln(x) / ln(10)


# ==============================
# EXPONENTIAL FUNCTION
# ==============================

def exp(x):

    result = 1
    term = 1

    for i in range(1, 30):
        term *= x / i
        result += term

    return result


# ==============================
# HYPERBOLIC FUNCTIONS
# ==============================

def sinh(x):

    x = toRadians(x)

    return (exp(x) - exp(-x)) / 2


def cosh(x):

    x = toRadians(x)

    return (exp(x) + exp(-x)) / 2


def tanh(x):
    return sinh(x) / cosh(x)

# ==============================
# HELPER FUNCTIONS
# ==============================

def factorial(n):

    if n < 0:
        return "Invalid Input"

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result