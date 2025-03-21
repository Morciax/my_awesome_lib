# Operacje na plikach


def read_file(filename: str) -> str:
    # Odczytuje zawartość pliku i zwraca ją jako string.
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


class FileWriter:
    # Klasa do operacji na plikach.

    @staticmethod
    def write_file(filename: str, content: str) -> None:
        # Zapisuje podany tekst do pliku.
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
