"""
A collection of simple math operations
"""

def simple_add(a,b):
    """The sum of two numbers

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    sum of a and b

    Example
    -------
    >>> simple_add(1,2)
    3
    """
    return a+b

def simple_sub(a,b):
    """The difference of two numbers

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    difference of a and b

    Example
    -------
    >>> simple_sub(2,1)
    1"""
    return a-b

def simple_mult(a,b):
    """The product of two numbers

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    product of a and b

    Example
    -------
    >>> simple_mult(2,1)
    2"""
    return a*b

def simple_div(a,b):
    """The division of two numbers

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    a and b difference

    Example
    -------
    >>> simple_div(4,2)
    2"""
    return a/b

def poly_first(x, a0, a1):
    """The first order polynom

    Parameters
    ----------
    x : integer
    a0 : integer
    a1 : integer

    Returns
    -------
    first order polynom: a0 + a1*x

    Example
    -------
    >>> poly_first(2,1,2)
    5"""
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """The second order polynom

    Parameters
    ----------
    x : integer
    a0 : integer
    a1 : integer
    a2 : integer

    Returns
    -------
    second order polynom: a0 + a1*x + a2*(x**2)

    Example
    -------
    >>> poly_second(2,1,2,2)
    13"""
    return poly_first(x, a0, a1) + a2*(x**2)

