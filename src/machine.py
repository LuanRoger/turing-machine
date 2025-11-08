from State import State
from Direction import Direction
from machine_logger import MachineLogger
from constants import BLANK


class Machine:
    current_state: State
    input_word: str
    tape: list[str]
    logger: MachineLogger
    range: int
    current: int
    max: int
    
    def __init__(
        self,
        initial_state: State,
        input_word: str,
        _range: int,
        enable_logging: bool = True,
    ):
        self.current_state = initial_state
        self.input_word = input_word
        self.tape = []
        self.logger = MachineLogger(enabled=enable_logging)

        self.set_tape_space(_range)
        self.init_tape(input_word)
        self.logger.log_initial_tape(self.tape, self.current)

    def run(self):
        step = 0
        while True:
            step += 1
            # Lê o símbolo atual da fita
            current_symbol = self.tape[self.current]

            # Log current step
            self.logger.log_step(
                step, self.current_state.getName(), self.tape, self.current
            )

            # Busca a transição correspondente
            transition = self.current_state.transition(current_symbol)

            if transition is not None:
                edge = transition.getEdge()
                next_state = transition.getState()

                write_symbol = edge.getWrite()
                direction = edge.getDirection()
                self.logger.log_transition(
                    self.current_state.getName(),
                    current_symbol,
                    next_state.getName(),
                    write_symbol,
                    direction,
                )

                self.tape[self.current] = edge.getWrite()

                if edge.getDirection() == Direction.RIGHT:
                    self.current += 1
                elif edge.getDirection() == Direction.LEFT:
                    self.current -= 1

                self.current_state = next_state

                if self.current < 0 or self.current > self.max:
                    self.logger.log_error("Fita excedeu os limites!")
                    return False

            else:
                if self.current_state.isFinal:
                    break
                self.logger.log_error(
                    f"{current_symbol} nao pertence ao alfabeto ou nao possui transicao!!"
                )
                return False

        return self.print_result()

    def print_result(self):
        is_final = self.current_state.isFinal
        self.logger.log_final_result(self.input_word, is_final)

        return is_final

    def init_tape(self, word):
        for char in list(word):
            self.tape[self.current] = char
            self.current += 1

        self.current = self.range + 1

    def set_tape_space(self, _range):
        self.range = _range
        total_size = self.range * 2 + 2

        self.tape = ["#"] + [BLANK] * (total_size - 1)

        self.current = self.range + 1
        self.max = total_size - 1
