# Write a program to implement LR Parser.
# Define the grammar as a dictionary
grammar = {
    'S': [['A', 'B'], ['b', 'C']],
    'A': [['a']],
    'B': [['b']],
    'C': [['c']]
}

# Define the parsing table (action and goto)
# This is a simplified example and may not cover all cases
action_table = {
    (0, 'a'): ('shift', 1),
    (0, 'b'): ('shift', 2),
    (1, 'b'): ('shift', 3),
    (2, 'c'): ('shift', 4),
    (3, '$'): ('reduce', 'S -> A B'),
    (4, '$'): ('reduce', 'S -> b C'),
    (7, '$'): ('accept',)  # Add this entry to handle the accept state
}

goto_table = {
    (0, 'A'): 1,
    (0, 'B'): 2,
    (0, 'C'): 3,
    (1, 'B'): 5,
    (2, 'C'): 6,
    (0, 'S'): 7  # Add this entry to handle the reduction to 'S'
}

# Define the input string
input_string = "ab"

# Tokenize the input string
input_tokens = list(input_string) + ['$']  # Add end-of-input marker

# Initialize the stack with state 0
stack = [0]

# Function to perform the shift operation
def shift(state):
    token = input_tokens.pop(0)
    stack.append(token)
    stack.append(state)
    print(f"Shift: {token}, Stack: {stack}, Input: {input_tokens}")

# Function to perform the reduce operation
def reduce(production):
    lhs, rhs = production.split(' -> ')
    rhs_symbols = rhs.split()
    for _ in range(len(rhs_symbols) * 2):
        stack.pop()
    current_state = stack[-1]
    stack.append(lhs)
    stack.append(goto_table[(current_state, lhs)])
    print(f"Reduce: {lhs} -> {rhs}, Stack: {stack}, Input: {input_tokens}")

# Parsing loop
print("Starting LR Parsing...\n")
while True:
    current_state = stack[-1]
    current_token = input_tokens[0]
    action = action_table.get((current_state, current_token))

    if not action:
        print("Error: Invalid input or state.")
        break

    if action[0] == 'shift':
        shift(action[1])
    elif action[0] == 'reduce':
        reduce(action[1])
    elif action[0] == 'accept':
        print("Parsing successful!")
        break
    else:
        print("Error: Unknown action.")
        break