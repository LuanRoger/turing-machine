from Direction import Direction

class Edge:
    def __init__(self, c: str, write: str = None, direction: Direction = None):
        self.c = c
        self.write = write
        self.direction = direction

    def getC(self): return self.c
    def getWrite(self): return self.write
    def getDirection(self): return self.direction

    @staticmethod
    def instance(c: str, write: str = None, direction: Direction = None):
        return Edge(c, write, direction)

    def equals(self, o):
        if isinstance(o, Edge):
            return Edge.testAB(self.c, o.getC())
        return False

    def __repr__(self):
        return f'[{self.c}]'

    @staticmethod
    def testAB(a: str, b: str):
        return a==b
