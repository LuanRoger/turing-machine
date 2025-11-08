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

    # Implementação da Maquina de Turing
    def run(self):
        if(self.q==None or self.w==None):
            return False
        
        # Loop principal da máquina de Turing
        while True:
            # Lê o símbolo atual da fita
            current_symbol = self.fita[self.current]
            
            # Busca a transição correspondente
            transition = self.q.transition(current_symbol)
            
            if transition != None:
                edge = transition.getEdge()
                qNext = transition.getState()
                
                # Mostra a transição
                write_symbol = edge.getWrite() if edge.getWrite() != None else current_symbol
                direction = edge.getDirection()
                print(f'{self.q.getName()} ({current_symbol}) -> {qNext.getName()} [write: {write_symbol}, dir: {direction}]')
                
                # Escreve na fita
                if edge.getWrite() != None:
                    self.fita[self.current] = edge.getWrite()
                
                # Move a cabeça de leitura
                if edge.getDirection() == 'D':  # Direita
                    self.current += 1
                elif edge.getDirection() == 'E':  # Esquerda
                    self.current -= 1
                elif edge.getDirection() == None:
                    # Se não há direção, não é uma máquina de Turing válida para esta transição
                    print(f'Erro: Transição sem direção definida!')
                    return False
                
                # Atualiza o estado
                self.q = qNext
                
                # Verifica limites da fita
                if self.current < 0 or self.current > self.max:
                    print(f'Fita excedeu os limites!')
                    return False
                    
            else:
                # Se não há transição, verifica se está em estado final
                if self.q.isFinal:
                    break
                # Se não está em estado final e não há transição, erro
                print(f'{current_symbol} nao pertence ao alfabeto ou nao possui transicao!!')
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
