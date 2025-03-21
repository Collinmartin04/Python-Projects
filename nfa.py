nfa = {}

with open('nfa.txt', 'r') as file:
  first_line = file.readline().strip()
  second_line = file.readline().strip()
  third_line = file.readline().strip()
  fourth_line = file.readline().strip()

  if not first_line or not second_line or not third_line or not fourth_line:
    raise ValueError("Invalid NFA format in nfa.txt")

  states = first_line.split(',')
  alphabet = second_line.split(',')
  starting_state = third_line
  accept_state = fourth_line.split(',')

  nfa['states'] = states
  nfa['alphabet'] = alphabet
  nfa['starting_state'] = starting_state
  nfa['accept_states'] = accept_state
  nfa['transitions'] = {}

  for line in file:
    line = line.strip()
    parts = line.split(',')
    if len(parts) != 3:
      continue  # Ignore malformed lines
    current_state, current_input, next_state = parts

    if (current_state, current_input) not in nfa['transitions']:
      nfa['transitions'][(current_state, current_input)] = set()
    
    nfa['transitions'][(current_state, current_input)].add(next_state)

# Function to compute epsilon-closure of a set of states
def epsilon_closure(states):
  closure = set(states)
  stack = list(states)

  while stack:
    state = stack.pop()
    if (state, '@') in nfa['transitions']:
      for next_state in nfa['transitions'][(state, '@')]:
        if next_state not in closure:
          closure.add(next_state)
          stack.append(next_state)
  return closure

# Function to simulate NFA
def simulate_nfa(nfa, input_string):
  current_states = epsilon_closure(set([nfa['starting_state']]))  # Ensure it's always a set
  print(f"Initial states: {current_states}")  # Debug

  if input_string == '@':
    return any(state in nfa['accept_states'] for state in current_states)

  for num in input_string:
    next_states = set()
    for state in current_states:
      if (state, num) in nfa['transitions']:
        next_states.update(nfa['transitions'][(state, num)])
    
    current_states = epsilon_closure(next_states)

  return any(state in nfa['accept_states'] for state in current_states)

# Process input.txt and write results to output.txt
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
  results = []
  for line in input_file:
    input_string = line.strip()
    result = simulate_nfa(nfa, input_string)
    results.append('accept' if result else 'reject')
  
  output_file.write("\n".join(results))  # Write all results without an extra newline

