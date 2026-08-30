EPSILON = '#'

class NFA:
    def __init__(self, states, symbols, transitions, start_state, final_states):
        self.states = states
        self.symbols = symbols
        self.transitions = transitions  # dict: (state, symbol) -> list of states
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

    def simulate(self, input_string):
        current_states = self.epsilon_closure({self.start_state})
        print(f"Start: {current_states}")

        for symbol in input_string:
            if symbol not in self.symbols:
                print(f"Invalid symbol: {symbol}")
                return False

            next_states = set()
            for state in current_states:
                next_states.update(self.transitions.get((state, symbol), []))

            current_states = self.epsilon_closure(next_states)
            print(f"After '{symbol}': {current_states}")

            if not current_states:
                print("REJECTED - dead state")
                return False

        accepted = bool(current_states & set(self.final_states))
        print("ACCEPTED" if accepted else "REJECTED")
        return accepted


def get_nfa_input():
    states = input("Enter states (comma separated): ").split(',')
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
    test_string = input("Enter string to test: ").strip()
    nfa.simulate(test_string)