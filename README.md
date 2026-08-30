# 🔐 Finite Automata Visualization

A Python-based implementation and visualization of important concepts from **Theory of Computation**, including **DFA, NFA, and NFA to DFA Conversion**.

The project provides step-by-step **console-based visualization** of states, transitions, input processing, and automata conversion to make the concepts easier to understand and demonstrate.

---

## 🎥 Code Explanation Video

> 🚀 A complete video explanation of the DFA, NFA, and NFA → DFA implementations will be added here.

👉 [▶️ Watch Code Explanation Video](https://drive.google.com/file/d/1DS0Tm0786ll1KNS6t-Lfz9MGOcAH_Ugf/view?usp=sharing)

---

## 📌 Project Overview

Finite Automata are mathematical models used to represent systems that process input strings and determine whether they belong to a particular language.

This project implements three fundamental concepts of **Automata Theory** using Python:

- **DFA – Deterministic Finite Automaton**
- **NFA – Non-Deterministic Finite Automaton**
- **NFA → DFA Conversion using Subset Construction**

The programs are designed with simple console-based visualizations and step-by-step execution so that the working of each automaton can be easily observed.

---

## 🎯 Objectives

The main objectives of this project are:

- To understand the working of finite automata.
- To implement a DFA using Python.
- To implement an NFA using Python.
- To demonstrate state transitions for input strings.
- To understand the difference between DFA and NFA.
- To implement NFA to DFA conversion.
- To demonstrate the Subset Construction Algorithm.
- To determine whether an input string is accepted or rejected.
- To provide a simple visualization of automata execution.

---

## 📂 Project Structure

```text
ACD-ELA/
│
├── dfa.py
├── nfa.py
├── nfa_to_dfa.py
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x
- No external libraries required — uses only Python's standard library.

---

## ▶️ How to Run

Clone the repository and run any of the scripts directly:

```bash
python dfa.py
python nfa.py
python nfa_to_dfa.py
```

Each script will interactively prompt you for:

- States (comma separated)
- Input symbols (comma separated)
- Transitions (entered one at a time, type `done` when finished)
- Start state
- Final state(s)
- A test string (for `dfa.py` and `nfa.py`)

---

## 🧩 Module Details

### `dfa.py` — DFA Simulation
Simulates a Deterministic Finite Automaton on a given input string, printing the path of states visited and whether the string is **ACCEPTED** or **REJECTED**.

### `nfa.py` — NFA Simulation
Simulates a Non-Deterministic Finite Automaton, including support for **epsilon (ε) transitions** using `#` as the epsilon symbol. Tracks the full set of active states at each step.

### `nfa_to_dfa.py` — NFA to DFA Conversion
Converts a given NFA into an equivalent DFA using the **Subset Construction (Powerset Construction) Algorithm**. Prints:
- The generated DFA states (each representing a subset of NFA states)
- The complete DFA transition table
- The DFA's final states

---

## 📝 Input Format

- Transitions are entered as: `state,symbol,next_state` (e.g. `q0,a,q1`)
- Use `#` as the symbol for epsilon transitions in `nfa.py` and `nfa_to_dfa.py`. Do not list `#` as an input symbol — it's handled automatically.
- Type `done` to finish entering transitions.

---

## 💡 Example

**DFA accepting binary strings ending in `01`:**

```
States: q0,q1,q2
Symbols: 0,1
Transitions:
q0,0,q1
q0,1,q0
q1,0,q1
q1,1,q2
q2,0,q1
q2,1,q0
done
Start state: q0
Final states: q2
Test string: 1101
```

**Expected output:** `ACCEPTED`

---

## 📖 Concepts Demonstrated

| Concept | Description |
|---|---|
| Deterministic transitions | One next state per (state, symbol) pair |
| Non-deterministic transitions | Multiple possible next states per (state, symbol) pair |
| Epsilon closure | Set of states reachable via ε-moves alone |
| Subset construction | Building DFA states as sets of NFA states |
| Language acceptance | Determining ACCEPT/REJECT based on final state membership |

