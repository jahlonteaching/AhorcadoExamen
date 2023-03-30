import sys
from typing import Optional

from ahorcado.modelo.ahorcado import Ahorcado
from ahorcado.vista.renderizador import RenderizadorAhorcado


class UIConsola:

    def __init__(self):
        self.ahorcado: Ahorcado = Ahorcado()
        self.opciones = {
            "1": self.iniciar_nuevo_juego,
            "0": self.salir
        }

    @staticmethod
    def mostrar_menu():
        titulo = "AHORCADO"
        print(f"\n{titulo:_^30}")
        print("1. Iniciar nuevo juego")
        print("0. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        print("\nBIENVENID@ A UN NUEVO JUEGO DE AHORCADO")
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def iniciar_nuevo_juego(self):
        self.ahorcado.iniciar_juego()
        self.mostrar_palabra(self.ahorcado.palabra_objetivo)
        self.obtener_letra_jugador()

    def obtener_letra_jugador(self):
        while self.ahorcado.tiene_intentos_disponibles():
            letra = input("Ingrese una letra: ")
            if self.ahorcado.letra_usada(letra):
                print(f"\nLa letra {letra} ya ha sido usada")
            else:
                if self.ahorcado.agregar_letra(letra):
                    self.mostrar_palabra(self.ahorcado.palabra_objetivo)
                    if self.ahorcado.palabra_completa():
                        print("\n¡FELICIDADES! HAS GANADO.")
                        return
                else:

                    self.mostrar_palabra(self.ahorcado.palabra_objetivo)

                print(RenderizadorAhorcado.representacion_ahorcado(self.ahorcado.intentos))
            self.mostrar_letras_usadas(self.ahorcado.letras_usadas)

        print("\n¡LO SIENTO! HAS PERDIDO")
        print(f">>>La palabra era: {self.ahorcado.palabra_objetivo.texto}")

    @staticmethod
    def mostrar_letras_usadas(letras):
        texto = "Letras usadas: "
        for letra in letras:
            texto += f"{letra}, "
        print(texto[:-2])

    @staticmethod
    def mostrar_palabra(palabra):
        print(f"\n>>> Palabra: {str(palabra)}")

    @staticmethod
    def salir():
        print("\nGRACIAS POR JUGAR AHORCADO.")
        sys.exit(0)
