from State import State
from Machine import Machine
from Direction import Direction


def teste_anbn():  # Livre de contexto
    print("{ a^nb^n | n>=0 }")
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")
    q4 = State("q4")
    qf = State("qf")
    qf.setFinal()

    q0.addTransition(q1, "a", "A", Direction.RIGHT)
    q0.addTransition(q3, "_", "_", Direction.LEFT)
    q0.addTransition(q4, "B", "B", Direction.RIGHT)

    q1.addTransition(q1, "a", "a", Direction.RIGHT)
    q1.addTransition(q1, "B", "B", Direction.RIGHT)
    q1.addTransition(q2, "b", "B", Direction.LEFT)

    q2.addTransition(q2, "a", "a", Direction.LEFT)
    q2.addTransition(q2, "B", "B", Direction.LEFT)
    q2.addTransition(q0, "A", "A", Direction.RIGHT)

    q4.addTransition(q4, "B", "B", Direction.RIGHT)
    q4.addTransition(q3, "_", "_", Direction.LEFT)

    q3.addTransition(q3, "A", "A", Direction.LEFT)
    q3.addTransition(q3, "B", "B", Direction.LEFT)
    q3.addTransition(qf, "_", "_", Direction.RIGHT)

    w = "aaabbb"

    mt = Machine(q0, w, 20)
    mt.run()


def teste_y_x():  # Regular
    print("{ w in Σ^* | w é um número binario multiplo de 3}")
    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q0.setFinal()

    q0.addTransition(q0, "0", "a", Direction.RIGHT)
    q0.addTransition(q1, "1", "b", Direction.RIGHT)

    q1.addTransition(q0, "1", "b", Direction.RIGHT)
    q1.addTransition(q2, "0", "a", Direction.RIGHT)

    q2.addTransition(q2, "1", "b", Direction.RIGHT)
    q2.addTransition(q1, "0", "a", Direction.RIGHT)

    w = "0000110"

    mt = Machine(q0, w, 20)
    mt.run()


if __name__ == "__main__":
    teste_anbn()
