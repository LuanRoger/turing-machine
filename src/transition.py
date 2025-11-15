from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state import State

from edge import Edge


class Transition:
    state: State
    edge: Edge

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

    def __repr__(self):
        return f"{self.edge} --> {self.state.getName()}"
