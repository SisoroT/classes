def precedence(op):
    """Function to find precedence of operators."""
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0


def operate(first: int, second: int, op: str) -> int:
    """Function to perform operations."""
    if op == "+":
        return first + second
    if op == "-":
        return first - second
    if op == "*":
        return first * second
    if op == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return first // second
    return 0


def calculate(expression: str) -> int:
    """Function that returns value of
    expression after evaluation.
    """
    # stack to store operators
    ops = []
    # stack to store integer values
    nums = []

    i = 0
    while i < len(expression):
        # if there is a space ignore it and keep moving
        if expression[i] == " ":
            i += 1
            continue
        # add numbers to the number stack
        if expression[i].isdigit():
            value = 0

            # handles multiple digit numbers
            while i < len(expression) and expression[i].isdigit():
                value = (value * 10) + int(expression[i])
                i += 1

            nums.append(value)
            i -= 1

        # push open parens to operator stack
        elif expression[i] == "(":
            ops.append(expression[i])

        # closing paren encountered, perform operations
        # until the next op is an open paren
        elif expression[i] == ")":
            while len(ops) != 0 and ops[-1] != "(":
                val2 = nums.pop()
                val1 = nums.pop()
                op = ops.pop()

                nums.append(operate(val1, val2, op))
            # get rid of the open paren
            ops.pop()

        # current character is an operator,
        # check the precedence before pushing
        else:
            # while current character is has lower precedence than the top of
            # the stack, perform the higher precedence operations
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(expression[i]):
                val2 = nums.pop()
                val1 = nums.pop()
                op = ops.pop()

                nums.append(operate(val1, val2, op))
            # push current character to 'ops'
            ops.append(expression[i])

        i += 1

    # entire expression has been processed,
    # perform operations until there are no more operators
    while len(ops) != 0:
        val2 = nums.pop()
        val1 = nums.pop()
        op = ops.pop()

        nums.append(operate(val1, val2, op))

    # pop the answer off the stack and return it
    return nums.pop()


if __name__ == "__main__":
    expression = "10 * (2 + 15) / 17"
    print(f"{expression} = {calculate(expression)}")
