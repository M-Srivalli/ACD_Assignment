EPSILON = '#'

class NFA:
    def __init__(self, states, symbols, transitions, start_state, final_states):
        self.states = states
        self.symbols = symbols
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def epsilon_closure(self, state_set):
        stack = list(state_set)
        closure = set(state_set)
        while stack:
            state = stack.pop()
            for next_state in self.transitions.get((state, EPSILON), []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def move(self, state_set, symbol):
        result = set()
        for state in state_set:
            result.update(self.transitions.get((state, symbol), []))
        return result


def nfa_to_dfa(nfa):
    dfa_states = {}          # frozenset -> label like 'A', 'B', ...
    dfa_transitions = {}     # (label, symbol) -> label
    dfa_final_states = []
    label_counter = [0]

    def get_label(state_set):
        state_set = frozenset(state_set)
        if state_set not in dfa_states:
            label = f"D{label_counter[0]}"
            label_counter[0] += 1
            dfa_states[state_set] = label
        return dfa_states[state_set]

    start_set = frozenset(nfa.epsilon_closure({nfa.start_state}))
    start_label = get_label(start_set)

    unprocessed = [start_set]
    processed = set()

    while unprocessed:
        current_set = unprocessed.pop()
        if current_set in processed:
            continue
        processed.add(current_set)
        current_label = dfa_states[current_set]

        # mark final if it contains any NFA final state
        if current_set & set(nfa.final_states):
            if current_label not in dfa_final_states:
                dfa_final_states.append(current_label)

        for symbol in nfa.symbols:
            if symbol == EPSILON:
                continue
            moved = nfa.move(current_set, symbol)
            closure = frozenset(nfa.epsilon_closure(moved))

            if not closure:
                continue  # dead state, skip (or model explicitly if needed)

            next_label = get_label(closure)
            dfa_transitions[(current_label, symbol)] = next_label

            if closure not in processed:
                unprocessed.append(closure)

    return dfa_states, dfa_transitions, start_label, dfa_final_states


def print_dfa(dfa_states, dfa_transitions, start_label, dfa_final_states):
    print("\n--- Resulting DFA ---")
    print(f"Start state: {start_label}")
    print(f"Final states: {dfa_final_states}")
    print("\nState mapping (DFA state -> set of NFA states):")
    for state_set, label in dfa_states.items():
        print(f"  {label} = {set(state_set)}")

    print("\nTransition table:")
    for (state, symbol), next_state in dfa_transitions.items():
        print(f"  {state} --{symbol}--> {next_state}")


def get_nfa_input():
    states = input("Enter NFA states (comma separated): ").split(',')
    states = [s.strip() for s in states]

    symbols = input("Enter input symbols excluding epsilon (comma separated): ").split(',')
    symbols = [s.strip() for s in symbols]

    transitions = {}
    print(f"Enter transitions as: state,symbol,next_state  (use '{EPSILON}' for epsilon, 'done' to stop)")
    while True:
        line = input("> ")
        if line.strip().lower() == 'done':
            break
        s, sym, ns = [x.strip() for x in line.split(',')]
        transitions.setdefault((s, sym), []).append(ns)

    start_state = input("Enter start state: ").strip()
    final_states = input("Enter final states (comma separated): ").split(',')
    final_states = [s.strip() for s in final_states]

    return NFA(states, symbols, transitions, start_state, final_states)


if __name__ == "__main__":
    nfa = get_nfa_input()
    dfa_states, dfa_transitions, start_label, dfa_final_states = nfa_to_dfa(nfa)
    print_dfa(dfa_states, dfa_transitions, start_label, dfa_final_states)