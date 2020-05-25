import sys


def operations(operand_1, operand_2):
    sum = 0
    difference = 0
    product = 0
    quotien = 0
    reminder = 0
    sum = operand_1 + operand_2
    difference = operand_1 - operand_2
    product = operand_1 * operand_2
    if operand_2 != 0:
        quotien = operand_1 / operand_2
        reminder = operand_1 % operand_2
    return sum, difference, product, quotien, reminder


def error_message():
    print("Usage: python operations.py <number1> <numb1er2>\n")
    print("Example: \n")
    print("\tpython operations.py 10 3\n")


if __name__ == "__main__":
    params = sys.argv

    if len(params) < 3:
        error_message()
        sys.exit(0)

    if len(params) > 3:
        print("InputError: too many arguments\n")
        error_message()
        sys.exit(0)

    if not params[1].isdigit() or not params[2].isdigit():
        print(" only numbers \n")
        error_message()
        sys.exit(0)

    op_1 = int(params[1])
    op_2 = int(params[2])

    sum, difference, product, quotien, reminder = operations(op_1, op_2)
    print("Sum:\t\t", sum)
    print("Difference:\t", difference)
    print("Product:\t", product)

    if op_2:
        print("Quotient:\t", quotien)
        print("Remainder:\t", reminder)
    else:
        print("Quotient:\t ERROR (div by zero)")
        print("Remainder:\t ERROR (modulo by zero)")
