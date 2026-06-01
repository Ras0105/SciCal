# ==============================
# CONSTANTS
# ==============================

PI = 3.141592653589793
E = 2.718281828459045


# ==============================
# UI HELPERS
# ==============================

def line():
    print("=" * 40)


def separator():
    print("-" * 40)


def space():
    print()


def title(text):
    line()
    print(text.center(40))
    line()


def showResult(result):
    print(f"\nResult: {result}")


# ==============================
# INPUT HELPERS
# ==============================

def getNumber(message):

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Invalid Number Input")


def continueChoice():

    choice = input("\nDo You Want To Continue? (y/n): ").lower()
    if choice=='\n':
        choice = input("\nDo You Want To Continue? (y/n): ").lower()
    return choice == 'y'


# ==============================
# CONVERSION HELPERS
# ==============================

def toRadians(degree):
    return degree * (PI / 180)