# Operacje na danych


def count_words(text: str) -> int:
    # Zlicza liczbę słów w podanym tekście.
    return len(text.split())


class DataAnalyzer:
    # Prosta klasa do analizy tekstu.
    def __init__(self, text: str):
        self.text = text

    def unique_words(self) -> int:
        # Zwraca liczbę unikalnych słów w tekście.
        return len(set(self.text.split()))
