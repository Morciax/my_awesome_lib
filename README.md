# my_awesome_lib:
Biblioteka Python służąca do operacji na danych, plikach, matematyce, tekstach i losowych wartościach.

Folder tests/ → przechowuje testy jednostkowe.
Plik setup.py i pyproject.toml → umożliwiają instalację biblioteki.
Plik .gitignore → ignorowanie niepotrzebnych plików (np. __pycache__).

Jak zainstalować bibliotekę? Bardzo prosto wystarczy otworzyć terminal i podać komendę:
pip install my_awesome_lib

 PRZYKŁADOWY SPOSÓB UŻYCIA:

from my_awesome_lib.data_utils import count_words

text = "Witaj!"
print(count_words(text))  
