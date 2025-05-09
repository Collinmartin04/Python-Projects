tm = {}

# Read and parse the tm.txt file
with open('tm.txt', 'r') as file:
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    third_line = file.readline().strip()
    fourth_line = file.readline().strip()

    states = first_line.split(',')
    alphabet_input = second_line.split(',')
    tape_alphabet = third_line.split(',')
    starting_state = fourth_line.strip()

    tm['states'] = states
    tm['input_alphabet'] = alphabet_input     
    tm['tape_alphabet'] = tape_alphabet       
    tm['start_state'] = starting_state        
    tm['transitions'] = {}



# Read transitions
    for line in file:
        if not line.strip():
            continue
        curr_state, read_symbol, write_symbol, next_state, direction = line.strip().split(',')
        key = (curr_state, read_symbol)
        tm['transitions'][key] = (write_symbol, next_state, direction)



# Turing Machine simulator
def simulate_tm(tm, input_string):
    tape = list(input_string)
    head = 0
    state = tm['start_state']

    while True:
        if state in ('accept', 'reject'):
            return state

        if head < 0:
            tape.insert(0, '_')
            head = 0
        elif head >= len(tape):
            tape.append('_')

        symbol = tape[head]
        key = (state, symbol)

        if key not in tm['transitions']:
            return 'reject'

        write_symbol, next_state, direction = tm['transitions'][key]
        tape[head] = write_symbol
        state = next_state

        if direction == 'R':
            head += 1
        elif direction == 'L':
            head -= 1
        else:
            raise ValueError(f"Unknown direction: {direction}")



# Read inputs, simulate, write outputs
with open('input.txt', 'r') as infile:
    inputs = [line.strip() for line in infile if line.strip()]

results = []
for inp in inputs:
    results.append(simulate_tm(tm, inp))

with open('output.txt', 'w') as outfile:
    for r in results:
        outfile.write(r + '\n')