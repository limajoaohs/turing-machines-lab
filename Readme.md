# Turing Machines Lab

This repository contains my solutions for the Theory of Computation laboratory. The project focuses on implementing Deterministic Turing Machines (DTM) and Multitape Turing Machines (MNTM) using the Python `automata-lib` library.

The main goal was to design machines capable of modifying strings based on context and recognizing specific Context-Sensitive Languages using different tape configurations.

## Project Structure

The project is modularized into three separate components:

* **Q01_Transducer/**: A machine that modifies strings based on the preceding character.
* **Q02_Recognizer_DTM/**: Standard single-tape recognizer for the language $L = \{ a^i b^i c^k \mid i, k \geq 1 \}$.
* **Q03_Recognizer_MNTM/**: Optimized 2-tape recognizer for the same language.

## Implementation Details

### 1. Context-Dependent Transducer (Q01)
The task was to build a DTM that replaces an character `a` with `b`, but only if the `a` is immediately preceded by a `b`.

I implemented this by scanning the tape from left to right. When the machine encounters a `b`, it transitions to a state that "remembers" this context. If the very next character is an `a`, it overwrites it with `b` and resets. Otherwise, it continues scanning. This ensures that only the specific pattern is modified without affecting other parts of the string.

### 2. Language Recognizer - Single Tape (Q02)
This machine recognizes strings where the number of `a`s equals the number of `b`s, followed by at least one `c`.

Since this is a standard Deterministic Turing Machine with a single tape, I used a "zig-zag" approach:
1.  The machine marks an `a` (replacing it with a placeholder like `x`).
2.  It moves right to find a corresponding `b` and marks it (replacing it with `y`).
3.  It moves back to the left to find the next `a`.
4.  Once all `a`s and `b`s are matched, it verifies the presence of the trailing `c`s to accept the string.

### 3. Language Recognizer - 2-Tape Optimization (Q03)
For the final question, I implemented the same logic as Question 2 but used a Multitape Turing Machine to improve efficiency.

Using two tapes allowed me to avoid the back-and-forth movement:
- **Tape 1**: Holds the input string.
- **Tape 2**: Acts as a temporary storage (similar to a stack).

The machine simply reads the `a`s from Tape 1 and copies them onto Tape 2. When it encounters `b`s on the input, it reverses the head on Tape 2 to match them one-to-one. Finally, it checks for the `c`s. This makes the recognition process much more linear and cleaner compared to the single-tape version.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/limajoaohs/turing-machines-lab.git](https://github.com/limajoaohs/turing-machines-lab.git)
    cd turing-machines-lab
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run specific modules:**
    ```bash
    # Run Question 1
    python Q01_Transducer/main.py

    # Run Question 2
    python Q02_Recognizer_DTM/main.py

    # Run Question 3
    python Q03_Recognizer_MNTM/main.py

    ```
