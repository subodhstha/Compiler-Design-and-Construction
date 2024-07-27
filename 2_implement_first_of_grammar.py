# Write a program to implement First of grammar.
# Define the grammar as a dictionary
grammar = {
    'S': [['A', 'B'], ['b', 'C']],
    'A': [['a'], ['ε']],
    'B': [['b']],
    'C': [['c']]
}

# Initialize the First sets
first = {non_terminal: set() for non_terminal in grammar}

# Function to compute the First set of a symbol
def compute_first(symbol):
    if symbol not in grammar:  # Terminal symbol
        return {symbol}
    
    if 'ε' in first[symbol]:  # Already computed
        return first[symbol]
    
    for production in grammar[symbol]:
        for prod_symbol in production:
            prod_first = compute_first(prod_symbol)
            first[symbol].update(prod_first - {'ε'})
            if 'ε' not in prod_first:
                break
        else:
            first[symbol].add('ε')
    
    return first[symbol]

# Compute the First sets for all non-terminals
for non_terminal in grammar:
    compute_first(non_terminal)

# Print the First sets
for non_terminal, first_set in first.items():
    print(f"First({non_terminal}) = {{ {', '.join(first_set)} }}")