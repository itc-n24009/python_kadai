def square():
    if not isinstance(x, (int, float)):
        if isinstance(x, str) and x.isdigit():
            x = int(x)
        else:
            raise ValueError("square", x)
    return x ** x

