from automata.tm.dtm import DTM

def run_q01():
    print("--- Running Q01: Context-Dependent Transducer ---")
    
    dtm = DTM(
        states={'q0', 'q1', 'q2'},
        input_symbols={'a', 'b'},
        tape_symbols={'a', 'b', '.'},
        transitions={
            'q0': {
                'a': ('q0', 'a', 'R'),
                'b': ('q1', 'b', 'R'),
                '.': ('q2', '.', 'R')
            },
            'q1': {
                'a': ('q0', 'b', 'R'), 
                'b': ('q1', 'b', 'R'),
                '.': ('q2', '.', 'R')
            }
        },
        initial_state='q0',
        blank_symbol='.',
        final_states={'q2'}
    )

    test_input = "abaa"
    print(f"Input: {test_input}")
    
    try:
        final_config = dtm.read_input_stepwise(test_input)
        for config in final_config:
            print(config)
        print("Result: Accepted/Processed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_q01()