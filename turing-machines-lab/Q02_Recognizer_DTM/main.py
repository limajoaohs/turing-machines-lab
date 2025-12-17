from automata.tm.dtm import DTM

def run_q02():
    print("--- Running Q02: Language Recognizer (Single Tape) ---")
    print("Language: L = { a^i b^i c^k | i, k >= 1 }")

    dtm = DTM(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        input_symbols={'a', 'b', 'c'},
        tape_symbols={'a', 'b', 'c', '.', 'x', 'y', 'z'},
        transitions={
            'q0': {
                'a': ('q1', 'x', 'R'),
                'y': ('q3', 'y', 'R'),
            },
            'q1': {
                'a': ('q1', 'a', 'R'),
                'b': ('q2', 'y', 'L'),
                'y': ('q1', 'y', 'R')
            },
            'q2': {
                'a': ('q2', 'a', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q3': {
                'y': ('q3', 'y', 'R'),
                'c': ('q4', 'z', 'R')
            },
            'q4': {
                'c': ('q4', 'z', 'R'),
                '.': ('q5', '.', 'R')
            }
        },
        initial_state='q0',
        blank_symbol='.',
        final_states={'q5'}
    )

    test_input = "aabbcc"
    print(f"Testing input: {test_input}")
    
    if dtm.accepts_input(test_input):
        print("ACCEPTED")
    else:
        print("REJECTED")

if __name__ == "__main__":
    run_q02()