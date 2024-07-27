# Write a program to implement Follow of grammar.

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

# Initialize the Follow sets
follow = {non_terminal: set() for non_terminal in grammar}
start_symbol = 'S'
follow[start_symbol].add('$')  # End-of-input marker

# Function to compute the Follow sets
def compute_follow():
    changed = True
    while changed:
        changed = False
        for non_terminal in grammar:
            for production in grammar[non_terminal]:
                follow_temp = follow[non_terminal].copy()
                for symbol in reversed(production):
                    if symbol in grammar:  # Non-terminal
                        if follow[symbol].update(follow_temp):
                            changed = True
                        if 'ε' in first[symbol]:
                            follow_temp.update(first[symbol] - {'ε'})
                        else:
                            follow_temp = first[symbol]
                    else:  # Terminal
                        follow_temp = {symbol}

# Compute the Follow sets
compute_follow()

# Print the Follow sets
for non_terminal, follow_set in follow.items():
    print(f"Follow({non_terminal}) = {{ {', '.join(follow_set)} }}")