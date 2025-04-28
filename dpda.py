dpda = {}

# Read and parse dpda.txt
with open('dpda.txt', 'r') as file:
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    third_line = file.readline().strip()
    fourth_line = file.readline().strip()
    fifth_line = file.readline().strip()

    states = first_line.split(',')
    alphabet_DPDA = second_line.split(',')
    stack_alphabet = third_line.split(',')
    starting_state = fourth_line.strip()
    final_states = fifth_line.split(',')

    dpda['states'] = states
    dpda['alphabet_DPDA'] = alphabet_DPDA
    dpda['stack_alphabet'] = stack_alphabet
    dpda['starting_state'] = starting_state
    dpda['final_states'] = final_states
    dpda['transitions'] = {}

# Read transitions
    for line in file:
        if not line.strip():
            continue
        curr_state, input_sym, stack_top, new_state, stack_push = line.strip().split(',')
        key = (curr_state, input_sym, stack_top)
        dpda['transitions'][key] = (new_state, stack_push)

# DPDA simulator
def simulate_dpda(dpda, input_string):
    current_state = dpda['starting_state']
    stack = ['$']
    i = 0
    input_len = len(input_string)

    while True:
        input_sym = input_string[i] if i < input_len else '@'
        stack_top = stack[-1] if stack else '@'

        for sym in [input_sym, '@']:
            for top in [stack_top, '@']:
                key = (current_state, sym, top)
                if key in dpda['transitions']:
                    new_state, push_symbol = dpda['transitions'][key]
                    if top != '@':
                        stack.pop()
                    if push_symbol != '@':
                        for s in reversed(push_symbol):
                            stack.append(s)
                    if sym != '@':
                        i += 1
                    current_state = new_state
                    break
            else:
                continue
            break
        else:
            break

    return (current_state in dpda['final_states']) and (i == input_len)

# Read input.txt, simulate, and write output.txt
results = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_str = line.strip()
        result = "accept" if simulate_dpda(dpda, input_str) else "reject"
        results.append(result)

with open('output.txt', 'w') as out:
    out.write('\n'.join(results))