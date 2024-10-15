from le_automata import Machine

# machine that detects odd number of 'b'
m = Machine(
        alphabet="ab",
        initial_state="q0",
        end_states=["q1"],
        transitions=[
            ("q0", "a", "q0"),
            ("q0", "b", "q1"),
            ("q1", "a", "q1"),
            ("q1", "b", "q0"),
        ])

assert m.run("aba") is True
assert m.run("abba") is False


# machine that detects if word ends with 'abba'
m = Machine(
        alphabet="ab",
        initial_state="q0",
        end_states=["q4"],
        transitions=[
            ("q0", "b", "q0"),
            ("q0", "a", "q1"),

            ("q1", "a", "q1"),
            ("q1", "b", "q2"),

            ("q2", "b", "q3"),
            ("q2", "a", "q1"),

            ("q3", "a", "q4"),
            ("q3", "b", "q0"),

            ("q4", "a", "q1"),
            ("q4", "b", "q0"),
        ])

assert m.run("aba") is False
assert m.run("abba") is True
assert m.run("aabba") is True
assert m.run("babba") is True
assert m.run("abababababababba") is True
assert m.run("abbab") is False
assert m.run("abbaa") is False

