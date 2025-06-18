from enum import Enum
import math

DEBUG = False  # Set to True to enable debug prints


class Operation(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MOD = "%"
    EXPONENT = "^"
    LOGARITHM = "log_"  # Using a placeholder for logarithm operation


def GeneralSyntax(toCalculate: str):
    """
    This function checks the general syntax of the expression toCalculate.
    It ensures that:
    1. There are an equal number of opening and closing parentheses.
    2. There are no invalid characters in the expression.
    3. There are no consecutive operators.
    4. There are no invalid sequences like a number followed by an opening parenthesis or a closing parenthesis followed by a number (with the exception of logorithms).

    Parameters:
    toCalculate (str): The mathematical expression to validate.
    returns:
    None: If the expression is valid.

    """

    # o7
    # We want to check if there are an equal number of opening and closing parentheses
    if DEBUG:
        print("in GeneralSyntax, toCalculate: ", toCalculate)
        # o7
    openParens = toCalculate.count("(")
    closeParens = toCalculate.count(")")
    if openParens != closeParens:
        raise ValueError("Mismatched parentheses. Please check your expression.")
    # Check for valid characters (digits, operators, parentheses)
    validChars = set("0123456789+-*/%^().log_")
    for char in toCalculate:
        if char not in validChars:
            raise ValueError(f"Invalid character '{char}' in expression.")
    # Check for consecutive operators or invalid sequences
    for i in range(len(toCalculate) - 1):
        if (
            toCalculate[i] in "+-*/%^"
            and toCalculate[i + 1] in "+-*/%^"
            and not (toCalculate[i] == "-" and i == 0)  # Allow leading negative sign
        ):
            raise ValueError(
                "Consecutive operators found. Please check your expression."
            )
    # We also do not want to allow an opening parenthesis directly after a number,
    # Or closing parenthesis directly before a number
    # With the exception of a logarithm, which will be checked here as well
    # For example, "2(3+4)" or "(3+4)2" are not valid expression
    for i in range(len(toCalculate) - 1):
        if (
            toCalculate[i].isdigit()
            and toCalculate[i + 1] == "("
            and Operation.LOGARITHM.value not in toCalculate[i + 1 : i + 4]
        ):
            raise ValueError(
                "Invalid syntax: opening parenthesis cannot follow a number."
            )
        if (
            toCalculate[i] == ")"
            and toCalculate[i + 1].isdigit()
            and Operation.LOGARITHM.value not in toCalculate[i - 3 : i + 1]
        ):
            raise ValueError(
                "Invalid syntax: closing parenthesis cannot precede a number."
            )


def Add(expression: str) -> str:
    """
    This function adds two numbers together.
    It expects the expression to be in the format "a+b" where a and b are numbers.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "a+b".
    Returns:
        str: The result of the addition as a string.
    """

    if DEBUG:
        print("in add, expression: ", expression)
    # Expecting expression like "a+b"
    parts = expression.split(Operation.ADD.value)
    if len(parts) != 2:
        raise ValueError("Addition requires exactly two operands.")
    try:
        a = float(parts[0].strip())
        b = float(parts[1].strip())
    except ValueError:
        raise ValueError("Operands must be numbers.")
    return str(a + b)


def Subtract(expression: str) -> str:
    """
    This function subtracts two numbers.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "a-b"

    Returns:
        str: The result of the subtraction as a string.
    """

    if DEBUG:
        print("in subtract, expression: ", expression)
    # Expecting expression like "a-b"
    parts = expression.split(Operation.SUBTRACT.value)
    if len(parts) != 2:
        raise ValueError("Subtraction requires exactly two operands.")
    try:
        a = float(parts[0].strip())
        b = float(parts[1].strip())
    except ValueError:
        raise ValueError("Operands must be numbers.")
    return str(a - b)


def Multiply(expression: str) -> str:
    """
    This function multiplies two numbers.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "a*b"

    Returns:
        str: The result of the multiplication as a string.
    """

    if DEBUG:
        print("in multiply, expression: ", expression)
    # Expecting expression like "a*b"
    parts = expression.split(Operation.MULTIPLY.value)
    if len(parts) != 2:
        raise ValueError("Multiplication requires exactly two operands.")
    try:
        a = float(parts[0].strip())
        b = float(parts[1].strip())
    except ValueError:
        raise ValueError("Operands must be numbers.")
    return str(a * b)


def Divide(expression: str) -> str:
    """
    This function divides two numbers.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "a/b"

    Returns:
        str: The result of the division as a string.
    """

    if DEBUG:
        print("in divide, expression: ", expression)
    # Expecting expression like "a/b"

    parts = expression.split(Operation.DIVIDE.value)
    if len(parts) != 2:
        raise ValueError("Division requires exactly two operands.")
    try:
        a = float(parts[0].strip())
        b = float(parts[1].strip())
    except ValueError:
        raise ValueError("Operands must be numbers.")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return str(a / b)


def Mod(expression: str) -> str:
    """
    This function performs modulus operation on two numbers.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "a%b"

    Returns:
        str: The result of the modulo as a string.
    """

    if DEBUG:
        print("in mod, expression: ", expression)
    # Expecting expression like "a%b"

    parts = expression.split(Operation.MOD.value)
    if len(parts) != 2:
        raise ValueError("Modulus requires exactly two operands.")
    try:
        a = float(parts[0].strip())
        b = float(parts[1].strip())
    except ValueError:
        raise ValueError("Operands must be numbers.")
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return str(a % b)


def Exponent(expression: str) -> str:
    """
    This function raises a number to the power of another number.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "a^b"

    Returns:
        str: The result of the exponentiation as a string.
    """

    if DEBUG:
        print("in exponent, expression: ", expression)
    # Expecting expression like "a^b"
    # Print("in exponent, expression: ", expression)
    parts = expression.split(Operation.EXPONENT.value)
    if len(parts) != 2:
        raise ValueError("Exponentiation requires exactly two operands.")
    try:
        a = float(parts[0].strip())
        b = float(parts[1].strip())
    except ValueError:
        raise ValueError("Operands must be numbers.")
    return str(a**b)


def Logarithm(expression: str) -> str:
    """
    This function calculates the logarithm of a number with a given base.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "base,argument"

    Returns:
        str: The result of the logoritm as a string.
    """

    # expecting "base,argument"
    if DEBUG:
        print("in logarithm, expression: ", expression)
    parts = expression.split(",")
    if len(parts) != 2:
        raise ValueError("Logarithm requires exactly two operands: base and argument.")
    try:
        base = EvaluateExpression(parts[0].strip())  # Ensure base is a valid expression
        arg = EvaluateExpression(parts[1].strip())
        # Ensure argument is a valid expression
        base = float(base)
        arg = float(arg)
    except ValueError as e:
        raise ValueError("Invalid operands for logarithm: " + str(e))

    return str(math.log(arg, base))


def FindStartAndEnd(expresion: str, operator: str):
    """
    This function finds the start and end indices of the left and right operands
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format "a-b" or "a*b" etc.
        operator (str): The operator to find in the expression, e.g., "+", "-", "*", "/", "%", "^".

    Returns:
        tuple: The start and end indices of the left and right operands as a tuple (start, end).
    """

    if DEBUG:
        print("in findStartAndEnd, expresion: ", expresion, ", operator: ", operator)
    operatorPos = expresion.rfind(operator)
    # Find the start of the left operand
    start = operatorPos - 1
    # Move left until we find a non-digit, non-decimal, and non-negative sign
    # We also need to handle negative numbers, so we check if the character before the '-' is a digit
    while start >= 0 and (
        expresion[start].isdigit()
        or expresion[start] == "."
        or (
            expresion[start] == "-"
            and (start == 0 or not expresion[start - 1].isdigit())
        )
    ):
        start -= 1
    start += 1  # Adjust to the first digit of the left operand

    # Find the end of the right operand
    end = operatorPos + 1
    while end < len(expresion) and (
        expresion[end].isdigit()
        or expresion[end] == "."
        or (expresion[end] == "-" and (end == operatorPos + 1))
    ):
        end += 1

    return start, end


def FindLogarithmDetails(toCalculate: str):
    """
    This function finds the details of the logarithm operation in the expression.
    Parameters:
        expression (str): The mathematical expression to evaluate, expected to be in the format
        "log_base(argument)" or "log_(base)(argument)".

    Returns:
        tuple: A tuple containing the start index of the logarithm, the base expression, the argument expression, and the end index of the argument.
    """

    # Find the last occurrence of "log_"
    start = toCalculate.rfind(Operation.LOGARITHM.value)
    if start == -1:
        raise ValueError("No logarithm found in expression.")

    # Find where the base starts (immediately after "log_")
    baseStart = start + len(Operation.LOGARITHM.value)

    # Case 1: base is wrapped in parentheses, e.g. log_((9*2)+(4/2))(10)
    if toCalculate[baseStart] == "(":
        # Find the matching ')' for the base
        parenCount = 1
        baseEnd = baseStart + 1
        while baseEnd < len(toCalculate) and parenCount > 0:
            if toCalculate[baseEnd] == "(":
                parenCount += 1
            elif toCalculate[baseEnd] == ")":
                parenCount -= 1
            baseEnd += 1
        if parenCount != 0:
            raise ValueError("Mismatched parentheses in logarithm base.")
        baseExpr = toCalculate[baseStart + 1 : baseEnd - 1]
        # Argument must be immediately after base's ')'
        if baseEnd >= len(toCalculate) or toCalculate[baseEnd] != "(":
            raise ValueError(
                "Invalid syntax for logarithm argument. Use log_(base)(argument)."
            )
        argOpen = baseEnd
    else:
        # Case 2: base is a number, e.g. log_2(16)
        baseEnd = baseStart
        while baseEnd < len(toCalculate) and (
            toCalculate[baseEnd].isdigit() or toCalculate[baseEnd] == "."
        ):
            baseEnd += 1
        baseExpr = toCalculate[baseStart:baseEnd]
        if baseEnd >= len(toCalculate) or toCalculate[baseEnd] != "(":
            raise ValueError(
                "Invalid syntax for logarithm argument. Use log_base(argument)."
            )
        argOpen = baseEnd

    # Now, find the matching ')' for the argument
    parenCount = 1
    argEnd = argOpen + 1
    while argEnd < len(toCalculate) and parenCount > 0:
        if toCalculate[argEnd] == "(":
            parenCount += 1
        elif toCalculate[argEnd] == ")":
            parenCount -= 1
        argEnd += 1
    if parenCount != 0:
        raise ValueError("Mismatched parentheses in logarithm argument.")

    argExpr = toCalculate[argOpen + 1 : argEnd - 1]
    return start, baseExpr, argExpr, argEnd


def TestCases():
    """
    This function tests the basic functionality of the calculator.
    Parameters:
        None

    Returns:
        None
    """

    # Regular basic cases

    assert Add("2+3") == "5.0"
    assert Subtract("5-3") == "2.0"
    assert Multiply("2*3") == "6.0"
    assert Divide("6/3") == "2.0"
    assert Mod("5%2") == "1.0"
    assert Exponent("2^3") == "8.0"
    assert Logarithm("2,8") == "3.0"

    # Basic edge cases
    try:
        Divide("5/0")
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

    try:
        Mod("5%0")
    except ValueError as e:
        assert str(e) == "Cannot perform modulus by zero."

    # More complex cases
    assert EvaluateExpression("2+3*4") == "14.0"
    assert EvaluateExpression("10-2^3") == "2.0"
    assert EvaluateExpression("log_10(100)") == "2.0"
    assert EvaluateExpression("2*(3+4)") == "14.0"
    assert EvaluateExpression("2^3*4") == "32.0"
    assert EvaluateExpression("(2^2^(2+1))") == "256.0"
    # 2^2^(2+1) is 2^2^2 = 2^8 = 256
    assert EvaluateExpression("log_2(16)/2") == "2.0"
    assert EvaluateExpression("log_2(8)+1") == "4.0"
    assert EvaluateExpression("(47)*(2/47)+2") == "4.0"

    print("MY STUFF WORKS????")


def EvaluateExpression(toCalculate: str) -> str:
    """
    This function evaluates a mathematical expression.
    Parameters:
        toCalculate (str): The mathematical expression to evaluate, expected to be in the format
        "a+b", "a-b", "a*b", "a/b", "a%b", "a^b", or "log_b(a)".
        or a chain of the above operations.

    Returns:
        str: The result of the evaluation as a string.
    """

    # I want to see if the expression is fully evaluated at this point,
    # So i will itterate through each character starting from the 2nd postion (since the first is always a digit or a - for negative numbers)
    # If it's a digit or decimal, we keep going
    # If it's an operator, we will break out of the loop and continue with the logic below
    # But what if the user inputs something of length 1?
    if len(toCalculate) == 1:
        if toCalculate[0].isdigit():
            # If the input is a single digit, we can return the expression as is
            return toCalculate
        else:
            # Length is 1 but it is not a digit
            return "\nYou fool.\nYou absolute buffoon.\nYour mother was a hamster and your father smelt of elderberry.\nGet you and your galoping coconuts out of here."

    # Range(1, len(toCalculate)) is used to skip the first character
    for i in range(1, len(toCalculate)):
        if toCalculate[i].isdigit() or toCalculate[i] == ".":
            if i == len(toCalculate) - 1:
                # If we are at the last character and it's a digit or decimal, we can assume the expression is fully evaluated
                # So we can return the expression as is
                return toCalculate
            # If we are not at the last character, we continue to the next character
            continue
        else:
            # If we hit a non-digit, non-decimal, non-negative sign, we break out of the loop
            # This means that the expression is not fully evaluated yet
            break
    if DEBUG:
        print("in evaluateExpression, toCalculate: ", toCalculate)

    # Since a given input will only be one operation,
    # We can use a switch case to determine the operation
    match True:

        # I want to do it in order of PEMDAS, so I will handle parentheses first
        # If there an opening parenthasis, that is not part of a logarithm, we will handle it first
        case _ if (
            "(" in toCalculate
            and ")" in toCalculate
            and Operation.LOGARITHM.value not in toCalculate
        ):
            # Handle innermost parentheses first

            # Finds the last opening parenthasis
            start = toCalculate.rfind("(")
            # Finds the first closing parenthasis after the opening parenthasis
            end = toCalculate.find(")", start)
            if start == -1 or end == -1:
                raise ValueError("Mismatched parentheses.")
            innerExpression = toCalculate[start + 1 : end]
            innerResult = EvaluateExpression(innerExpression)  # Recursive call

            # 3 parts in the return value:
            # 1. The part of the string before the parentheses
            # 2. The result of the inner expression
            # 3. The part of the string after the parentheses
            # Replace the inner expression with its result
            # After evaluating the inner expression, we call evaluateExpression again
            # To handle any remaining operations in the rest of the expression
            return EvaluateExpression(
                toCalculate[:start] + str(innerResult) + toCalculate[end + 1 :]
            )

        case _ if Operation.LOGARITHM.value in toCalculate:
            # The logic for logarithm is a bit (AAAAAAAAAAAAAAAAAAAAAA) more complex,
            # So i will be placing it an entirely sepreate method
            # Which will be called FindLogarithmDetails(toCalculate)

            start, arg1, arg2, argEnd = FindLogarithmDetails(toCalculate)

            logResult = Logarithm(arg1 + "," + arg2)
            newExpr = toCalculate[:start] + logResult + toCalculate[argEnd:]
            return EvaluateExpression(newExpr)

        case _ if Operation.EXPONENT.value in toCalculate:
            start, end = FindStartAndEnd(toCalculate, Operation.EXPONENT.value)
            expResult = Exponent(toCalculate[start:end])
            newExpr = toCalculate[:start] + expResult + toCalculate[end:]
            return EvaluateExpression(newExpr)

        case _ if Operation.MULTIPLY.value in toCalculate:
            start, end = FindStartAndEnd(toCalculate, Operation.MULTIPLY.value)
            mulResult = Multiply(toCalculate[start:end])
            newExpr = toCalculate[:start] + mulResult + toCalculate[end:]
            return EvaluateExpression(newExpr)

        case _ if Operation.DIVIDE.value in toCalculate:
            start, end = FindStartAndEnd(toCalculate, Operation.DIVIDE.value)
            divResult = Divide(toCalculate[start:end])
            newExpr = toCalculate[:start] + divResult + toCalculate[end:]
            return EvaluateExpression(newExpr)

        case _ if Operation.MOD.value in toCalculate:
            start, end = FindStartAndEnd(toCalculate, Operation.MOD.value)
            modResult = Mod(toCalculate[start:end])
            newExpr = toCalculate[:start] + modResult + toCalculate[end:]
            return EvaluateExpression(newExpr)

        case _ if Operation.ADD.value in toCalculate:
            start, end = FindStartAndEnd(toCalculate, Operation.ADD.value)
            addResult = Add(toCalculate[start:end])
            newExpr = toCalculate[:start] + addResult + toCalculate[end:]
            return EvaluateExpression(newExpr)

        case _ if Operation.SUBTRACT.value in toCalculate:
            start, end = FindStartAndEnd(toCalculate, Operation.SUBTRACT.value)
            subResult = Subtract(toCalculate[start:end])
            newExpr = toCalculate[:start] + subResult + toCalculate[end:]
            return EvaluateExpression(newExpr)

        case _:
            raise ValueError(
                "Invalid operation. Please use +, -, *, /, %, ^, or log_b(a)."
            )


def main():
    """
    This function serves as the main entry point for the calculator program.
    It prompts the user for a mathematical expression, and then validates, evaluates, and prints it.
    Parameters:
        None

    Returns:
        None
    """

    # Uncomment the line below to run test cases
    TestCases()

    print("Welcome to le calculator! (honhon baguette)")
    while True:
        toCalculate = input("Enter an expression (or 'quit' to exit): ")
        if toCalculate.lower() == "quit":
            # using lower() so i don't need to care about casing for the input so my enum will work

            print("quiter :/")
            break
        try:
            GeneralSyntax(toCalculate)
            # o7
            if not toCalculate:
                raise ValueError("Input cannot be empty.")
            toCalculate = toCalculate.replace(
                " ", ""
            )  # Remove spaces for easier parsing
            result = EvaluateExpression(toCalculate)
            # Print the result
            print("Result: ", result)

        except Exception as reeeeeeeeeeeeeeEEEEEEEEEEEEEEEEE:
            print("Error:", reeeeeeeeeeeeeeEEEEEEEEEEEEEEEEE)


if __name__ == "__main__":
    main()
