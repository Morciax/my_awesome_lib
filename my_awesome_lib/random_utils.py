# Operacje losowe

import random


def random_number(start: int, end: int) -> int:
    # Generuje losową liczbę z przedziału [start, end].
    return random.randint(start, end)


def shuffle_list(items: list) -> list:
    # Tasuje elementy listy w losowej kolejności.
    random.shuffle(items)
    return items


class RandomGenerator:
    # Klasa do generowania losowych wartości.

    @staticmethod
    def random_float(start: float, end: float) -> float:
        # Generuje losową liczbę zmiennoprzecinkową z przedziału [start, end].
        return random.uniform(start, end)
