# Operacje na tekstach
def is_palindrome(text: str) -> bool:
    # Sprawdza, czy tekst jest palindromem
    return text == text[::-1]


def reverse_text(text: str) -> str:
    # Odwraca podany ciąg znaków.
    return text[::-1]


class TextFormatter:
    # Klasa do formatowania tekstu.

    def __init__(self, text: str):
        self.text = text

    def capitalize_words(self) -> str:
        # Zamienia pierwszą literę każdego słowa na wielką.
        return " ".join(word.capitalize() for word in self.text.split())
