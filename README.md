# my_awesome_lib:
Jest to biblioteka Python, która zawiera moduły do pracy z danymi, plikami, operacjami matematycznymi, tekstami i wartościami losowymi. Zapewnia proste i intuicyjne funkcje, które ułatwiają codzienną pracę programisty.

1. Operacje na danych (data_utils.py)

Funkcje:
count_words(text: str) -> int - Zlicza liczbę słów w podanym tekście.
DataAnalyzer.unique_words() -> int - Zwraca liczbę unikalnych słów w tekście.

2. Operacje na plikach (file_operations.py)

Funkcje:
read_file(filename: str) -> str - Odczytuje zawartość pliku jako string.
FileWriter.write_file(filename: str, content: str) -> None - Zapisuje treść do wskazanego pliku.

3. Operacje matematyczne (math_tools.py)

Funkcje:
factorial(n: int) -> int - Oblicza silnię liczby n.
MathOperations.gcd(a: int, b: int) -> int - Oblicza największy wspólny dzielnik (NWD).

4. Operacje na tekstach (text_processing.py)

Funkcje:
is_palindrome(text: str) -> bool - Sprawdza, czy tekst jest palindromem.
reverse_text(text: str) -> str - Odwraca podany ciąg znaków. ("abc" -> "cba")
TextFormatter.capitalize_words() -> str - Zamienia pierwszą literę każdego słowa na wielką.

5. Operacje losowe (random_utils.py)

Funkcje:
random_number(start: int, end: int) -> int - Generuje losową liczbę całkowitą z podanego przedziału.
shuffle_list(items: list) -> list - Tasuje elementy listy.
RandomGenerator.random_float(start: float, end: float) -> float - Generuje losową liczbę zmiennoprzecinkową.

Jak zainstalować bibliotekę? Aby skorzystać z biblioteki, sklonuj repozytorium i zainstaluj pakiet lokalnie:
git clone https://github.com/Morciax/my_awesome_lib.git
cd my_awesome_lib
pip install .

lub 

pip install my_awesome_lib

PRZYKŁADOWY SPOSÓB UŻYCIA:

Operacje na danych:
from my_awesome_lib.data_utils import count_words, DataAnalyzer

text = "Witaj!"
print(count_words(text))  #Output: 1

text = "To jest test testowy"
print(count_words(text))  # Output: 4
analyzer = DataAnalyzer(text)
print(analyzer.unique_words())  # Output: 3


Operacje matematyczne:
from my_awesome_lib.math_tools import factorial, MathOperations

print(factorial(5))  # Output: 120
print(MathOperations.gcd(48, 18))  # Output: 6

Operacje na tekstach:
from my_awesome_lib.text_processing import reverse_text, is_palindrome

print(reverse_text("Python"))  # Output: "nohtyP"
print(is_palindrome("radar"))  # Output: True

Operacje losowe:
from my_awesome_lib.random_utils import random_number, shuffle_list

print(random_number(1, 10))  # Losowa liczba 1-10
print(shuffle_list([1, 2, 3, 4, 5]))  # Przetasowana lista





