# Operacje matematyczne


def factorial(n: int) -> int:
    # Oblicza silnię liczby n.
    if n == 0:
        return 1
    return n * factorial(n - 1)


class MathOperations:
    # Zbiór operacji matematycznych.

    @staticmethod
    def gcd(a: int, b: int) -> int:
        # Oblicza największy wspólny dzielnik (NWD) dwóch liczb.
        while b:
            a, b = b, a % b
        return a
