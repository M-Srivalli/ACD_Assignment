class DFA:
    def __init__(self, states, symbols, transitions, start_state, final_states):
        self.states = states
        self.symbols = symbols
        self.transitions = transitions  # dict: (state, symbol) -> state
        self.start_state = start_state
        self.final_states = final_states

    def simulate(self, input_string):
        current = self.start_state
        path = [current]

        for symbol in input_string:
            if symbol not in self.symbols:
                print(f"Invalid symbol: {symbol}")
                return False
            key = (current, symbol)
            if key not in self.transitions:
                print(f"No transition from {current} on '{symbol}'. REJECTED")
                return False
            current = self.transitions[key]
            path.append(current)

        print("Path taken:", " -> ".join(path))
        accepted = current in self.final_states
        print("ACCEPTED" if accepted else "REJECTED")
        return accepted


def get_dfa_input():
    states = input("Enter states (comma separated, e.g. q0,q1,q2): ").split(',')
    states = [s.strip() for s in states]

    symbols = input("Enter input symbols (comma separated, e.g. a,b): ").split(',')
    symbols = [s.strip() for s in symbols]

    transitions = {}
    print("Enter transitions as: state,symbol,next_state  (type 'done' to stop)")
    while True:
        line = input("> ")
        if line.strip().lower() == 'done':
            break
        s, sym, ns = [x.strip() for x in line.split(',')]
        transitions[(s, sym)] = ns

    start_state = input("Enter start state: ").strip()
    final_states = input("Enter final states (comma separated): ").split(',')
    final_states = [s.strip() for s in final_states]

    return DFA(states, symbols, transitions, start_state, final_states)


if __name__ == "__main__":
    dfa = get_dfa_input()
    test_string = input("Enter string to test: ").strip()
    dfa.simulate(test_string)