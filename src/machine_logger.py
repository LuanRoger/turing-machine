import logging


class MachineLogger:
    """Logger for Turing Machine execution state and tape visualization"""

    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        self._setup_logger()

    def _setup_logger(self):
        """Setup logging configuration"""
        self.logger = logging.getLogger("TuringMachine")
        self.logger.setLevel(logging.INFO)

        # Remove existing handlers to avoid duplicates
        self.logger.handlers.clear()

        # Create console handler with custom formatting
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        # Custom format for better readability
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def log_initial_tape(self, tape, current_pos):
        """Log the initial tape state"""
        if not self.enabled:
            return
        self.logger.info(f"Initial Tape: {self._format_tape(tape, current_pos)}")

    def log_transition(
        self, current_state, symbol, next_state, write_symbol, direction
    ):
        """Log a state transition"""
        if not self.enabled:
            return
        dir_str = str(direction) if direction else "None"
        self.logger.info(
            f"{current_state} ({symbol}) -> {next_state} [write: {write_symbol}, dir: {dir_str}]"
        )

    def log_tape_state(self, tape, current_pos, current_state):
        """Log current tape state with pointer"""
        if not self.enabled:
            return
        self.logger.info(
            f"State: {current_state} | {self._format_tape(tape, current_pos)}"
        )

    def log_final_result(self, word, is_accepted):
        """Log the final result"""
        if not self.enabled:
            return
        if is_accepted:
            self.logger.info(f"✓ Reconheceu: {word}")
        else:
            self.logger.info(f"✗ Não reconheceu: {word}")

    def log_error(self, message):
        """Log an error message"""
        if not self.enabled:
            return
        self.logger.error(f"ERROR: {message}")

    def _format_tape(self, tape, current_pos):
        """Format tape with current position indicator"""
        # Create a visual representation of the tape
        tape_str = "["
        for i, symbol in enumerate(tape):
            if symbol is None:
                symbol_repr = "_"
            elif symbol == "#":
                symbol_repr = "#"
            else:
                symbol_repr = str(symbol)

            if i == current_pos:
                tape_str += f">{symbol_repr}<"
            else:
                tape_str += f" {symbol_repr} "

            if i < len(tape) - 1:
                tape_str += ""
        tape_str += "]"

        return tape_str

    def log_step(self, step_num, state, tape, current_pos):
        """Log a complete execution step"""
        if not self.enabled:
            return
        self.logger.info(f"\n--- Step {step_num} ---")
        self.log_tape_state(tape, current_pos, state)
