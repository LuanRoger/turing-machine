from enum import Enum

class Direction(Enum):
    """Enum representing the direction of tape head movement in a Turing Machine"""
    RIGHT = 'D'  # Direita (Right)
    LEFT = 'E'   # Esquerda (Left)
    
    def __str__(self):
        return self.value
