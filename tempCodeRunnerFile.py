grammar = {
    'S': [['A', 'B'], ['b', 'C']],
    'A': [['a']],
    'B': [['b']],
    'C': [['c']]
}

# Define the input string
input_string = "ab"

# Tokenize the input string
input_tokens = list(input_string) + ['$']  # Add end-of-input marker

# Initialize the stack
stack = ['$']

# Function to perform the shift operation
def shift():
    token = input_tokens.pop(0)
    stack.append(token)
    print(f"Shift: {token}")
    print(f"Stack: {stack}")
    print(f"Input: {input_tokens}\n")

# Function to perform the reduce operation
def reduce():
    for lhs, productions in grammar.items():
        for production in productions:
            if stack[-len(production):] == production:
                for _ in range(len(production)):
                    stack.pop()
                stack.append(lhs)
                print(f"Reduce: {lhs} -> {' '.join(production)}")
                print(f"Stack: {stack}")
                print(f"Input: {input_tokens}\n")
                return True
    return False

# Parsing loop
print("Starting Shift-Reduce Parsing...\n")
while input_tokens:
    shift()
    while reduce():
        pass

# Check if the parsing was successful
if stack == ['$', 'S']:
    print("Parsing successful!")
else:
    print("Parsing failed.")