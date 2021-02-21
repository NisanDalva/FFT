
from FFT import FFT

if __name__ == '__main__':
    A = [1, 0, 1]
    B = [3, -2]
    fft = FFT(A=A, B=B)
    C = fft.run()
    print(f'y_A = {fft.y_A}')
    print(f'y_B = {fft.y_B}')
    print(f'n = {fft.n}')
    print()
    print(f'C = {C}')
    fft.print_as_polynomial()

    print('-' * 50)

    A = [1, 0, 1]
    B = [3, -2]
    fft = FFT(A=A, B=B, n=8)
    C = fft.run()
    print(f'y_A = {fft.y_A}')
    print(f'y_B = {fft.y_B}')
    print(f'n = {fft.n}')
    print()
    print(f'C = {C}')
    fft.print_as_polynomial()

    print('-' * 50)

    A = [2, 0, 5]
    B = [1, -1, 0, 2, 0]
    fft = FFT(A=A, B=B)
    C = fft.run()
    print(f'y_A = {fft.y_A}')
    print(f'y_B = {fft.y_B}')
    print(f'n = {fft.n}')
    print()
    print(f'C = {C}')
    fft.print_as_polynomial()

    print('-' * 50)

    A = [3, 0, 2, 0]
    fft = FFT(A=A, reverse=True)
    C = fft.run()
    print(f'n = {fft.n}')
    print()
    print(f'C = {C}')
    fft.print_as_polynomial()

    print('-' * 50)

    A = [3, 0, 2, 0]
    fft = FFT(A=A) ** -1
    C = fft.run()
    print(f'n = {fft.n}')
    print()
    print(f'C = {C}')
    fft.print_as_polynomial()

    print('-' * 50)

