import math
import cmath


def determine_n(P, Q):
    d = len(P) + (len(Q) if Q is not None else 0) - 1
    return 2 ** math.ceil(math.log(d, 2))


def omega(j, n):
    """
    :param j: number between 0 to n-1
    :param n: order of FFT
    :return: the unit root j of n

    since sin(pi) is not equal to zero (although it really is), because of the accuracy of the floating point,
    we must round it to zero
    """
    tol = 1e-14
    cos_res = cmath.cos((2 * cmath.pi * j) / n)
    sin_res = cmath.sin((2 * cmath.pi * j) / n)
    if abs(cos_res) < tol:
        cos_res = 0
    if abs(sin_res) < tol:
        sin_res = 0
    return complex(cos_res, sin_res)


def split_even_odd(P):
    """
    split given vector P to even and odd according to indexes
    :param P: the vector to split
    :return: two different vectors, evens and odds
    indexes:              2  1  0
    >>> split_even_odd(P=[1, 2, 3])
    ([1, 3], [2])
    """
    even = []
    odd = []
    tmp = P[::-1]

    for i, x in enumerate(tmp):
        if i % 2 == 0:
            even.insert(0, x)
        else:
            odd.insert(0, x)
    return even, odd


def set_in_polynomial(P, x):
    """
    set number x in polynomial p
    for example: if P=[3, -2] and x=4 ---> P(x)=3x - 2 -> P(4)=3 * 4 - 2 = 10
    :return: the result after the set, with this example it will return 10
    """
    power = len(P) - 1
    sum = 0
    for i in P:
        sum += i * (x ** power)
        power -= 1
    return sum


def evaluate_polynomial_of_unit_roots(P, n):
    """
    evaluate the polynomial P with 2 unit roots (omega(0, 2) and omega(1, 2))
    THIS is the base case of FFT
    :param P: vector
    :param n: order of FFT
    :return:
    """
    lst = []
    for j in range(0, 2):
        lst.append(set_in_polynomial(P, omega(j, n)))
    return lst


def multiply_vectors(P, Q):
    """
    :param P: vector
    :param Q: vector
    :return: P * Q
    >>> multiply_vectors(P=[1, 2, 3], Q=[3, 5, 2])
    [3, 10, 6]
    """
    return list(map(lambda x, y: x * y, P, Q))


def multiply_each_element_by_unit_root(P, n):
    """
    :param P: vector
    :param n: order of FFT
    :return: the vector multiplied by each unit roots
     assume n = 4, the unit roots are: 1, i, -1, -i
    >>> multiply_each_element_by_unit_root(P=[1, 2, 3, 4], n=4)
    [1, 2i, -3, -4i]
    """
    new = []
    for j in range(n):
        new.append(P[j] * omega(j, n))
    return new


def divide_each_element_by_n(P, n):
    """
    :param P: vector
    :param n: order of FFT
    :return: the vector divided by n
    assume n = 4
    >>> divide_each_element_by_n(P=[10, 4, 5, 8])
    [2.5, 1, 1.25, 2]
    """
    return [i / n for i in P]


def reverse_vector(P):
    """
    :param P: vector
    :return: reversed vector
    >>>  reverse_vector(P=[1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return P[::-1]


def round_complex(i, n=None):
    """
    :param i: the complex number from cmath
    :param n: how many digit after the point will appear
    :return: rounded complex number
    >>> round_complex(i=(2.234+4.358j), n=2)
    (2.23+4.36j)
    """
    return complex(round(i.real, n), round(i.imag, n))


def round_list_complex(lst, n=None):
    """
    round the complex numbers as above for entire lise
    :param lst: list of complex number
    :param n: how many digit after the point will appear
    :return: the rounded list
    """
    return [round_complex(i, n) for i in lst]
