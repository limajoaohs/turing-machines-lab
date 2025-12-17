from automata.tm.mntm import MNTM

def run_q03():
    print("--- Running Q03: Language Recognizer (2-Tape Optimization) ---")
    
    mntm = MNTM(
        states={'q0', 'q1', 'q2', 'q3'},
        input_symbols={'a', 'b', 'c'},
        tape_symbols={'a', 'b', 'c', '.'},
        n_tapes=2,
        transitions={
            'q0': {
                ('a', '.'): [('q0', (('a', 'R'), ('a', 'R')))], 
                ('b', '.'): [('q1', (('b', 'N'), ('.', 'L')))], 
            },
            'q1': {
                ('b', 'a'): [('q1', (('b', 'R'), ('.', 'L')))], 
                ('c', '.'): [('q2', (('c', 'R'), ('.', 'N')))], 
            },
            'q2': {
                ('c', '.'): [('q2', (('c', 'R'), ('.', 'N')))],
                ('.', '.'): [('q3', (('.', 'R'), ('.', 'N')))],
            }
        },
        initial_state='q0',
        blank_symbol='.',
        final_states={'q3'}
    )

    test_input = "aabbcc"
    print(f"Testing input: {test_input}")

    if mntm.accepts_input(test_input):
        print("ACCEPTED")
    else:
        print("REJECTED")

if __name__ == "__main__":
    run_q03()