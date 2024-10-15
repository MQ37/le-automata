class Machine:

    def __init__(self,
                 alphabet: str,
                 initial_state: str,
                 end_states: list[str],
                 transitions: list[tuple[str, str, str]]):
        """
        Initialize a Finite State Machine.

        Args:
            alphabet (str): The alphabet of the machine.
            initial_state (str): The initial state of the machine.
            end_states (list[str]): A list of end states of the machine.
            transitions (list[tuple[str, str, str]]): A list of tuples representing the transitions.
                Each tuple should be of the form (current_state, input_symbol, next_state).
        """
        self._alphabet: set[str] = set(alphabet)
        self._initial_state: str = initial_state
        self._end_states: set[str] = set(end_states)
        self._check_transitions(transitions)
        self._transitions = self._build_transision_dict(transitions)

    def _build_transision_dict(self, 
                               transitions: list[tuple[str, str, str]]
                               ) -> dict[tuple[str, str], str]:
        """
        Build a dictionary representation of the transitions.

        Args:
            transitions (list[tuple[str, str, str]]): A list of tuples representing the transitions.

        Returns:
            dict[tuple[str, str], str]: A dictionary where the key is a tuple of (current_state, input_symbol)
                and the value is the next_state.
        """
        _transitions = {}
        for (q, a, qn) in transitions:
            _transitions[(q, a)] = qn
        return _transitions

    def _check_transitions(self,
                           transitions: list[tuple[str, str, str]]):
        """
        Check if the transitions are valid.

        Args:
            transitions (list[tuple[str, str, str]]): A list of tuples representing the transitions.

        Raises:
            ValueError: If any state does not handle a symbol from the alphabet.
        """
        state_alphabet = {}
        for (q, a, qn) in transitions:
            if q not in state_alphabet:
                state_alphabet[q] = self._alphabet - {a}
                continue
            state_alphabet[q] = state_alphabet[q] - {a}

        for q, a in state_alphabet.items():
            if a:
                raise ValueError(f"Node '{q}' does not handle symbol '{a}'")

    def qn(self, q: str, a: str) -> str:
        """
        Get the next state from the current state q and symbol a.

        Args:
            q (str): The current state.
            a (str): The input symbol.

        Returns:
            str: The next state.
        """
        return self._transitions[(q, a)]

    def run(self, word: str) -> bool:
        """
        Check if the input word is valid for this machine.

        Args:
            word (str): The input word to check.

        Returns:
            bool: True if the word is valid, False otherwise.

        Raises:
            ValueError: If the word contains a symbol not in the alphabet.
        """
        if not set(word).issubset(self._alphabet):
            raise ValueError(f"Word '{word}' is not a subset of alphabet '{self._alphabet}'")

        states = [self._initial_state]
        for a in word:
            q = states[-1]
            qn = self.qn(q, a)
            states.append(qn)

        q = states[-1]
        return q in self._end_states
