dfa = {}

with open('dfa.txt', 'r') as file:
  first_line = file.readline().strip()
  second_line = file.readline().strip()
  third_line = file.readline().strip()
  fourth_line = file.readline().strip()

  states = first_line.split(',')
  alphabet = second_line.split(',')
  starting_state = third_line
  accept_state = fourth_line.split(',')

# Create a dictionary for the DFA
  dfa['states'] = states
  dfa['alphabet'] = alphabet
  dfa['starting_state'] = starting_state
  dfa['accept_states'] = accept_state
  dfa['transitions'] = {} 

  for line in file:
    line = line.strip()
    current_state, current_input, next_state = line.split(',')
    dfa['transitions'][(current_state, current_input)] = next_state
    #                   (q1) -0-> (q1)    |   (q1) -1-> (q2)


# Function to simulate DFA
def simulate_dfa(input_string):
  current_state = dfa['starting_state']

  for num in input_string:
    if num == '@':
      if (current_state, num) in dfa['accept_states']:
        return "accept"
      else:
        continue
      
    if (current_state, num) in dfa['transitions']:
      current_state = dfa['transitions'][(current_state, num)]
    else:
      return "reject"

  if current_state in dfa['accept_states']:
    return "accept"
  else:
    return "reject"

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
  for line in input_file:
    input_string = line.strip()
    result = simulate_dfa(input_string)
    output_file.write(result + '\n')