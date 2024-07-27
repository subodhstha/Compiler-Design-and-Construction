# Write a program to implement Final code generation.
# Define the intermediate code as a list of tuples
intermediate_code = [
    ('t1', '=', '10', '-', '4'),
    ('t2', '=', '5', '*', 't1'),
    ('t3', '=', '3', '+', 't2')
]

def generate_assembly(intermediate_code):
    assembly_code = []
    for instruction in intermediate_code:
        if instruction[1] == '=':
            dest = instruction[0]
            op1 = instruction[2]
            operator = instruction[3]
            op2 = instruction[4]
            
            if operator == '+':
                assembly_code.append(f'MOV R1, {op1}')
                assembly_code.append(f'ADD R1, {op2}')
                assembly_code.append(f'MOV {dest}, R1')
            elif operator == '-':
                assembly_code.append(f'MOV R1, {op1}')
                assembly_code.append(f'SUB R1, {op2}')
                assembly_code.append(f'MOV {dest}, R1')
            elif operator == '*':
                assembly_code.append(f'MOV R1, {op1}')
                assembly_code.append(f'MUL R1, {op2}')
                assembly_code.append(f'MOV {dest}, R1')
            elif operator == '/':
                assembly_code.append(f'MOV R1, {op1}')
                assembly_code.append(f'DIV R1, {op2}')
                assembly_code.append(f'MOV {dest}, R1')
    
    return assembly_code

# Generate the assembly code
assembly_code = generate_assembly(intermediate_code)

# Print the assembly code
for line in assembly_code:
    print(line)