# .\.venv\Scripts\python.exe -m pip install readchar
#import threading
#import readchar
from State import State
from Transition import Transition
from Edge import Edge
from Machine import Machine

def teste_y_x():
    print("{ w in Σ^* | w é um número binario multiplo de 3}")
    q0 = State('q0')
    q1 = State('q1')
    q2 = State('q2')
    q0.setFinal()

    q0.addTransition(q0, '0', '0', 'D')
    q0.addTransition(q1, '1', '1', 'D')

    q1.addTransition(q0, '1', '1', 'D')
    q1.addTransition(q2, '0', '0', 'D')

    q2.addTransition(q2, '1', '1', 'D')
    q2.addTransition(q1, '0', '0', 'D')

    w = '0000110'

    mt = Machine(q0, w, 20)
    mt.run()

if __name__ == "__main__":
    teste_y_x()
