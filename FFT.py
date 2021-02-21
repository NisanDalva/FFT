from Utilities import *
from sympy import *


class FFT:
    def __init__(self, A=None, B=None, n=None, round_results=3, reverse=False, tol=0.001):
        """
        :param A, B: vector of coefficient of polynomial A(x)
                    examples: A(x)=x^2 + 1 --> A=[1, 0, 1]
                              A(x)=3x - 2 --> A=[3, -2]
                              A(x)=x^7 + x^3 + x --> A=[1, 0, 0, 0, 1, 0, 1, 0]
        :param n: optional, default is None. FFT order. if None it will be determined automatically
        :param round_results: optional, default is 3. how many digits after the point will appear.
        :param reverse: optional, default is False. True if wanted a FFT^-1
        :param tol: optional, default is 0.001. used only for printing as a polynomial. it is used to check if need to
                    round to the closest integer
        """
        if A is None and B is None:
            raise ValueError("you need to specify at least one vector")
        if not isinstance(A, (list, tuple)) or not isinstance(B, (list, tuple, type(None))):
            raise ValueError('vector must be a list or tuple')

        self.A = A
        self.B = B
        self.n = determine_n(self.A, self.B) if n is None else n
        self.round_results = round_results
        self.reverse = reverse
        self.tol = tol
        self.y_A = None
        self.y_B = None
        self.C = None

    def __DFT(self, P):
        if self.n == 2:
            return evaluate_polynomial_of_unit_roots(P, self.n)

        even, odd = split_even_odd(P)
        p_even = FFT(A=even, n=self.n // 2).run()
        p_odd = FFT(A=odd, n=self.n // 2).run()
        lst = []

        # P(x) = P_even(x^2) + xP_odd(x^2) for all x = omega(j, n) where 0 <= j <= n-1
        # omega(j, n)^2 = omega(j mod n/2, n/2)
        for j in range(self.n):
            num = p_even[j % (self.n // 2)] + omega(j, self.n) * p_odd[j % (self.n // 2)]
            lst.append(num)

        lst = round_list_complex(lst, self.round_results)
        return lst

    def __reverse_DFT(self, y_C=None):
        if y_C is None:
            self.y_A = self.__DFT(self.A)
            self.y_B = self.__DFT(self.B)
            self.C = multiply_vectors(self.y_A, self.y_B)
            self.C = self.__DFT(self.C)
        else:
            self.C = self.__DFT(y_C)

        self.C = multiply_each_element_by_unit_root(self.C, self.n)
        self.C = divide_each_element_by_n(self.C, self.n)
        self.C = reverse_vector(self.C)
        self.C = round_list_complex(self.C, self.round_results)
        return self.C

    def run(self):
        if self.reverse:
            return self.__reverse_DFT(self.A)

        if self.B is None:
            return self.__DFT(self.A)
        return self.__reverse_DFT()

    def print_as_polynomial(self):
        init_printing(use_unicode=True)
        x = symbols('x')
        to_string = ''
        power = len(self.C) - 1
        for i in range(power + 1):
            num = self.C[i].real
            num = round(num) if abs(round(num) - num) < self.tol else num
            to_string += f'{num}*{x} ** {power} '
            power -= 1
            try:
                to_string += '+' if self.C[i + 1].real >= 0 else ''
            except:
                pass

        p = eval(to_string)
        to_string = maple_code(p)
        to_string = f'C(x) = {to_string}'
        print(to_string)

    def __pow__(self, power, modulo=None):
        if power == -1:
            return FFT(self.A, reverse=True)
        raise ValueError(f'its not possible to raise power of {power}. -1 is allowed')

