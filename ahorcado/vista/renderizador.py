
CABEZA: str = "O"
LINEA: str = "│"
EXTREMO: str = "\u2534"
MANO: str = "_"
PIE_1: str = "/"
PIE_2: str = "\\"


class RenderizadorAhorcado:

    @staticmethod
    def representacion_ahorcado(intentos: int) -> str:
        hangman = f"{'╔════╗':>9}"
        hangman += f"\n{'║    ║':>9}"
        if intentos == 1:
            hangman += f"\n{CABEZA+'    ║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'══════════':^12}"
        elif intentos == 2:
            hangman += f"\n{CABEZA + '    ║':>9}"
            hangman += f"\n{LINEA + '    ║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'══════════':^12}"
        elif intentos == 3:
            hangman += f"\n{CABEZA + '    ║':>9}"
            hangman += f"\n{MANO + LINEA + '    ║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'══════════':^12}"
        elif intentos == 4:
            hangman += f"\n{CABEZA + '    ║':>9}"
            hangman += f"\n{MANO + LINEA + MANO + '   ║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'══════════':^12}"
        elif intentos == 5:
            hangman += f"\n{CABEZA + '    ║':>9}"
            hangman += f"\n{MANO + LINEA + MANO + '   ║':>9}"
            hangman += f"\n{LINEA + '    ║':>9}"
            hangman += f"\n{'║':>9}"
            hangman += f"\n{'══════════':^12}"
        elif intentos == 6:
            hangman += f"\n{CABEZA + '    ║':>9}"
            hangman += f"\n{MANO + LINEA + MANO + '   ║':>9}"
            hangman += f"\n{LINEA + '    ║':>9}"
            hangman += f"\n{PIE_1 + '     ║':>9}"
            hangman += f"\n{'══════════':^12}"
        elif intentos == 7:
            hangman += f"\n{CABEZA + '    ║':>9}"
            hangman += f"\n{MANO + LINEA + MANO + '   ║':>9}"
            hangman += f"\n{LINEA + '    ║':>9}"
            hangman += f"\n{PIE_1 + ' ' + PIE_2 +'   ║':>9}"
            hangman += f"\n{'══════════':^12}"
        else:
            return ""

        return hangman
