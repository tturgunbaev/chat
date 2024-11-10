def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers together
    Args:
    a (int): first number
    b (int): second number
    Returns:
    int: the product of a and b
    """
    return a * b

def add(a: int, b: int) -> int:
    """
    Add two numbers together
    Args:
    a (int): first number
    b (int): second number
    Returns:
    int: the sum of a and b
    """
    return a + b

def divide(a: int, b: int) -> float:
    """
    Divide two numbers
    Args:
    a (int): the dividend
    b (int): the divisor
    Returns:
    float: the quotient of a and b
    """
    return a / b

tools = [multiply, add, divide]