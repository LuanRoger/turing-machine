from state import State
from direction import Direction
from machine_logger import MachineLogger


class Machine:
    def __init__(
        self,
        initial_state: State,
        input_word: str,
        _range: int,
        enable_logging: bool = True,
    ):
        self.current_state = initial_state
        self.input_word = input_word
        self.fita = []
        self.logger = MachineLogger(enabled=enable_logging)

        # Ideia para Turing Machine abaixo, onde _range*2 eh o tamanho da fita da maquina:
        self.set_fita_space(_range)
        self.init_fita(input_word)
        self.logger.log_initial_tape(self.fita, self.current)

    # Implementação da Maquina de Turing
    def run(self):
        if self.current_state is None or self.input_word is None:
            return False

        step = 0
        # Loop principal da máquina de Turing
        while True:
            step += 1
            # Lê o símbolo atual da fita
            current_symbol = self.fita[self.current]

            # Log current step
            self.logger.log_step(
                step, self.current_state.getName(), self.fita, self.current
            )

            # Busca a transição correspondente
            transition = self.current_state.transition(current_symbol)

            if transition is not None:
                edge = transition.getEdge()
                next_state = transition.getState()

                # Mostra a transição
                write_symbol = (
                    edge.getWrite() if edge.getWrite() is not None else current_symbol
                )
                direction = edge.getDirection()
                self.logger.log_transition(
                    self.current_state.getName(),
                    current_symbol,
                    next_state.getName(),
                    write_symbol,
                    direction,
                )

                # Escreve na fita
                if edge.getWrite() is not None:
                    self.fita[self.current] = edge.getWrite()

                # Move a cabeça de leitura
                if edge.getDirection() == Direction.RIGHT:  # Direita
                    self.current += 1
                elif edge.getDirection() == Direction.LEFT:  # Esquerda
                    self.current -= 1
                elif edge.getDirection() is None:
                    # Se não há direção, não é uma máquina de Turing válida para esta transição
                    self.logger.log_error("Transição sem direção definida!")
                    return False

                # Atualiza o estado
                self.current_state = next_state

                # Verifica limites da fita
                if self.current < 0 or self.current > self.max:
                    self.logger.log_error("Fita excedeu os limites!")
                    return False

            else:
                # Se não há transição, verifica se está em estado final
                if self.current_state.isFinal:
                    break
                # Se não está em estado final e não há transição, erro
                self.logger.log_error(
                    f"{current_symbol} nao pertence ao alfabeto ou nao possui transicao!!"
                )
                return False

        return self.print_result()

    def print_result(self):
        self.logger.log_final_result(self.input_word, self.current_state.isFinal)
        return self.current_state.isFinal

    def init_fita(self, word):
        for char in list(word):
            self.fita[self.current] = char
            self.current += 1

        self.current = self.range + 1

    def set_fita_space(self, _range):
        self.range = _range
        self.max = self.range * 2

        self.fita.append("#")
        for i in range(1, self.max + 2):
            self.fita.append(None)

        self.current = self.range + 1
        self.max = self.max + 1
