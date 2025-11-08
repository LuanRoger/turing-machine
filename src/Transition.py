class Transition:
    def __init__(self, state, edge):
        self.state = state
        self.edge = edge

    def getEdge(self):
        return self.edge

    def getState(self):
        return self.state

    def equals(self, other_transition):
        if isinstance(other_transition, Transition):
            return other_transition.getEdge().equals(
                self.edge
            ) and other_transition.getState().equals(self.state)
        return False

    def hashCode(self):
        hash_code = self.state.hashCode() if self.state != None else 0
        hash_code = 47 * hash_code + (self.edge.hashCode() if self.edge != None else 0)
        return hash_code

    def __repr__(self):
        return f"{self.edge} --> {self.state.getName()}"
