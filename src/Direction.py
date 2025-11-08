from enum import Enum


class Direction(Enum):
    RIGHT = "D"  # Direita
    LEFT = "E"  # Esquerda

    def __str__(self):
        return self.value
