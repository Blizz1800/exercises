'''Reto de programación: Laberinto de Palabras'''
import random
import string
from typing import List

# Descripcion:
# Crea un programa que genere un laberinto de
# letras aleatorias y luego determine si una
# palabra dada se puede encontrar dentro del
# laberinto, conectando letras adyacentes
# (horizontal o verticalmente, no en diagonal).


class Laberynth:
    """Laberinto"""

    def __init__(self, size: int) -> None:
        self.size = size
        self.lab: List[List[str]] = []
        self.match = []
        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1
        self.generate_laberynth()

    def generate_laberynth(self, debug=False) -> List[List[str]]:
        """Genera un laberinto de NxN dimenciones"""
        if debug:
            self.lab = [
                list("OLLAAFSLDJ"),
                list("PQOWLOSLDJ"),
                list("PPPJOLNZXP"),
                list("MASDHAPSKJ"),
                list("DKFJSDKFAO"),
                list("SDIFOIWEMQ"),
                list("IASDKDFJKA"),
                list("KSDJFLSKDJ"),
                list("PQWODSFKLJ"),
                list("SJDFOQWIJD"),
            ]
            return
        self.lab.clear()
        for _ in range(self.size):
            self.lab.append([])
            for _ in range(self.size):
                self.lab[-1].append(random.choice(string.ascii_uppercase))

    def _search_horizontal_right(self, x, y, word, i=1) -> bool:
        if x < self.size - 1:
            x += 1
            if len(word) > i and self.lab[y][x] == word[i]:
                self.match.append(word[i])
                if len(self.match) == len(word):
                    return True, (x, y)
                return self._search_horizontal_right(x, y, word, i+1)
            self.match.clear()
            return False, (x, y)
        return False, (x, y)

    def _search_horizontal_left(self, x, y, word, i=1) -> bool:
        if x >= 0:
            x -= 1
            if len(word) > i and self.lab[y][x] == word[i]:
                self.match.append(word[i])
                if len(self.match) == len(word):
                    return True, (x, y)
                return self._search_horizontal_left(x, y, word, i+1)
            self.match.clear()
            return False, (x, y)
        return False, (x, y)

    def _search_vertical_up(self, x, y, word, i=1) -> bool:
        if y < self.size - 1:
            y += 1
            if len(word) > i and self.lab[y][x] == word[i]:
                self.match.append(word[i])
                if len(self.match) == len(word):
                    return True, (x, y)
                return self._search_vertical_up(x, y, word, i+1)
            self.match.clear()
            return False, (x, y)
        return False, (x, y)

    def _search_vertical_down(self, x, y, word, i=1) -> bool:
        if y >= 0:
            y -= 1
            if len(word) > i and self.lab[y][x] == word[i]:
                self.match.append(word[i])
                if len(self.match) == len(word):
                    return True, (x, y)
                return self._search_vertical_down(x, y, word, i+1)
            self.match.clear()
            return False, (x, y)
        return False, (x, y)

    def _search_horizontal(self, x, y, word):
        status = False
        status, (x2, y2) = self._search_horizontal_right(x, y, word)
        if not status:
            self.match.append(word[0])
            status, (x2, y2) = self._search_horizontal_left(x, y, word)
        return status, x2, y2

    def _search_vertical(self, x, y, word):
        status = False
        status, (x2, y2) = self._search_vertical_up(x, y, word)
        if not status:
            self.match.append(word[0])
            status, (x2, y2) = self._search_vertical_down(x, y, word)
        return status, x2, y2

    def find_word(self, word: str) -> bool:
        """Search for a `word` in the laberinth using N-Queens algorithm"""
        word = word.upper()
        founded = False

        for y, _ in enumerate(self.lab):
            if founded:
                break
            for x, letter in enumerate(_):
                if letter == word[0]:
                    self.match.append(letter)
                    h, x2, y2 = self._search_horizontal(x, y, word)
                    if h:
                        print(f"Word founded from [{y}, {x}] to [{y2}, {x2}]")
                        founded = True
                        self.x1 = x
                        self.y1 = y
                        self.x2 = x2
                        self.y2 = y2
                        break
                    self.match.append(letter)
                    v, x2, y2 = self._search_vertical(x, y, word)
                    if v:
                        print(f"Word founded from [{y}, {x}] to [{y2}, {x2}]")
                        founded = True
                        self.x1 = x
                        self.y1 = y
                        self.x2 = x2
                        self.y2 = y2
                        break
        return founded

    def __str__(self) -> str:
        """Convert laberinth into string"""
        l = len(str(self.size))
        space = " " * l
        r = " " + space
        r += " ".join([f"%{l}d" % (n+1) for n in range(self.size)])
        r += "\n"
        for i, _ in enumerate(self.lab):
            if not isinstance(_, list):
                continue

            r += f"%{l}d%s%s\n" % ((i+1), space, space.join(_))
        return r


if __name__ == "__main__":
    ARR_SIZE = input("Tamanno del laberinto: ")
    if not ARR_SIZE:
        ARR_SIZE = 8
    else:
        ARR_SIZE = int(ARR_SIZE) if ARR_SIZE.isdigit() else 8
    while True:
        WORD = input("Palabra a buscar: ")
        if WORD:
            if ARR_SIZE < len(WORD):
                ARR_SIZE = len(WORD) + 1
                print(f"Nuevo tamanno del laberinto: {ARR_SIZE}")
            break
        WORD = "HOLA"
        break

    lab = Laberynth(ARR_SIZE)
    print(lab)
    if lab.find_word(WORD):
        print(f"Se ha encontrado la palabra \"{WORD}\"!")
        print(f"Desde [{lab.x1}, {lab.y1}] hasta [{lab.x2}, {lab.y2}]")
    else:
        print("No se ha encontrado la palabra")
