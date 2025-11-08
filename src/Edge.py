from direction import Direction


class Edge:
    def __init__(self, read_char: str, write: str = None, direction: Direction = None):
        self.read_char = read_char
        self.write = write
        self.direction = direction

    def getChart(self):
        return self.read_char

    def getWrite(self):
        return self.write

    def getDirection(self):
        return self.direction

    @staticmethod
    def instance(read_char: str, write: str = None, direction: Direction = None):
        return Edge(read_char, write, direction)

    def equals(self, other):
        if isinstance(other, Edge):
            return Edge.campare(self.read_char, other.getChart())
        return False

    def __repr__(self):
        return f"[{self.read_char}]"

    @staticmethod
    def campare(char_a: str, char_b: str):
        return char_a == char_b
