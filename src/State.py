from __future__ import annotations
from Edge import Edge
from Transition import Transition
from Direction import Direction


class State:
    name: str
    isFinal: bool
    transitions: list[Transition]
    
    def __init__(self, name: str):
        self.name = name
        self.isFinal = False
        self.transitions = []

    def getName(self):
        return self.name

    def setFinal(self):
        self.isFinal = True

    def addTransition(
        self, state, read_char: str, write: str, direction: Direction
    ):
        return self.addTransitions(state, Edge.instance(read_char, write, direction))

    def addTransitions(self, state, *edges):
        for edge in edges:
            transition = Transition(state, edge)
            if transition in self.transitions:
                continue
            self.transitions.append(transition)
        return self

    def transition(self, symbol: str):
        for trans in self.transitions:
            edge = trans.getEdge()
            if edge.getChart() == symbol:
                return trans
        return None

    def equals(self, other_state):
        if isinstance(other_state, State):
            return other_state.getName() == self.getName()
        return False

    def hashCode(self):
        return hash(self.getName())
