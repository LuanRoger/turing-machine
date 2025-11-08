from State import State
class Machine: #AFD = (Q, Σ, δ, q0, F)
    def __init__(self, q: State, w: str, _range: int):
        self.q = q
        self.w = w
        self.fita = []

        #Ideia para Turing Machine abaixo, onde _range*2 eh o tamanho da fita da maquina:
        self.set_fita_space(_range)
        self.init_fita(w)
        print(f'Fita: {self.fita}')

    # OBS: a self.fita ja esta pronta com os dados.
    # Por exemplo, voce pode usar o self.current como o indice de self.fita[self.current]. Como ficaria?
    def run(self):
        if(self.q==None or self.w==None):
            return False
        for c in list(self.w):
            transition = self.q.transition(c)
            if transition != None:
                qNext = transition.getState()
                print(f'{self.q.getName()} ({c}) -> {qNext.getName()}')
                self.q = qNext
            else:
                print(f'{c} nao pertence ao alfabeto ou nao possui transicao!!')
                return False

        return self.print_result()

    def print_result(self):
        """ Print and Return True (ok) or False (no ok)"""
        if(self.q.isFinal):
            print(f'reconheceu: {self.w}')
        else:
            print(f'Não reconheceu: {self.w}')
        return self.q.isFinal

    #Ideia para Turing Machine abaixo:
    def init_fita(self, w):
        for a in list(w):
            self.fita[self.current] = a
            self.current += 1

        self.current = self.range+1

        #print(f'{self.fita}\nLEN: {len(self.fita)}\nMAX: {self.max}')
        #print(f'current -> {self.fita[self.current]}')

    def set_fita_space(self, _range):
        self.range = _range
        self.max = self.range*2

        self.fita.append('#')
        for i in range(1, self.max+2):
            self.fita.append(None)

        self.current = self.range+1
        self.max = self.max+1
