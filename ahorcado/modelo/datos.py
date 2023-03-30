import random


class ProveedorPalabras:

    def __init__(self):
        with open("data/data.txt", mode='r', encoding='utf8') as f:
            contenido = f.read()
            self.__palabras: list[str] = [word.strip()[1:-1] for word in contenido.split(",")]

    def proveer_palabra(self) -> str:
        return random.choice(self.__palabras)
