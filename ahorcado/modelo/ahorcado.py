from dataclasses import dataclass, field

from ahorcado.modelo.datos import ProveedorPalabras

LETRA_VACIA: str = "_"
INTENTOS_MAXIMOS: int = 7


class Palabra:

    # TODO: Método inicializador

    # TODO: Método contiene_letra

    def posiciones_letra(self, letra: str) -> list[int]:
        return [i for i, ch in enumerate(self.texto) if ch == letra]

    # TODO: Método agregar_letra

    # TODO: Método esta_completa

    # TODO: Método especial


# TODO: Definición de la clase Ahorcado

    # TODO: Atributo intentos
    letras_usadas: list[str] = field(default_factory=list, init=False)
    proveedor_palabras: ProveedorPalabras = ProveedorPalabras()
    palabra_objetivo: Palabra = None

    def generar_texto(self) -> str:
        return self.proveedor_palabras.proveer_palabra()

    # TODO: Método iniciar_juego

    # TODO: Método letra_usada

    def palabra_completa(self) -> bool:
        return self.palabra_objetivo.esta_completa()

    # TODO: Método tiene_intentos_disponibles

    # TODO: Método agregar_letra
