from state import State
from machine import Machine
from direction import Direction


def teste_y_x():
    print("{ w in Σ^* | w é um número binario multiplo de 3}")
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q0.setFinal()

    q0.addTransition(q0, "0", "0", Direction.RIGHT)
    q0.addTransition(q1, "1", "1", Direction.RIGHT)

    q1.addTransition(q0, "1", "1", Direction.RIGHT)
    q1.addTransition(q2, "0", "0", Direction.RIGHT)

    q2.addTransition(q2, "1", "1", Direction.RIGHT)
    q2.addTransition(q1, "0", "0", Direction.RIGHT)

    w = "0000110"

    mt = Machine(q0, w, 10)
    mt.run()


if __name__ == "__main__":
    teste_y_x()
