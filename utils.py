from scipy.integrate import quad


def fact(n):
    """Computes the factorial of a natural number.

    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n < 0:
        raise ValueError("Must be positive")
    for x in range(1, n):
        n *= x
    return n


def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.

    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
            to the roots of the ax^2 + bx + c polynomial.
    """
    delta = b * b - 4 * a * c
    if delta < 0:
        return tuple()
    elif delta == 0:
        return (-b / 2 / a,)
    else:
        x1 = (-b - delta ** (0.5)) / 2 / a
        x2 = (-b + delta ** (0.5)) / 2 / a
        return x1, x2


def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds

    Pre: 'function' is a valid Python expression with x as a variable,
            'lower' <= 'upper',
            'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
            of the specified 'function'.

    Hint: You can use the 'integrate' function of the module 'scipy' and
            you'll probably need the 'eval' function to evaluate the function
            to integrate given as a string.
    """

    def fun(x):
        return eval(function, {"x": x})

    return quad(fun, lower, upper)[0]


if __name__ == "__main__":
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate("x ** 2 - 1", -1, 1))
