# Write a program to implement Type Conversion.
class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_counter = 0
        self.instructions = []
        self.label_counter = 0

    def generate_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter - 1}"

    def generate_label(self):
        self.label_counter += 1
        return f"L{self.label_counter - 1}"

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def generate_code(self, ast):
        self.visit(ast)
        return self.instructions

    def visit(self, node):
        if isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, Num):
            return node.value
        elif isinstance(node, Variable):
            return node.name
        elif isinstance(node, TypeConversion):
            return self.visit_type_conversion(node)

    def visit_binop(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        result = self.generate_temp()
        self.add_instruction(f"{result} = {left} {node.op} {right}")
        return result

    def visit_type_conversion(self, node):
        operand = self.visit(node.operand)
        result = self.generate_temp()
        self.add_instruction(f"{result} = ({node.target_type}) {operand}")
        return result

class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

class TypeConversion(ASTNode):
    def __init__(self, operand, target_type):
        self.operand = operand
        self.target_type = target_type

# Example usage
if __name__ == "__main__":
    # Constructing AST for the expression: (3 + 5.0) * 2 + (7 - 2.5)
    ast = BinOp(
        left=BinOp(
            left=BinOp(left=Num(3), op='+', right=TypeConversion(Num(5.0), "int")),
            op='*',
            right=Num(2)
        ),
        op='+',
        right=BinOp(left=Num(7), op='-', right=TypeConversion(Num(2.5), "int"))
    )

    # Generate intermediate code
    generator = IntermediateCodeGenerator()
    intermediate_code = generator.generate_code(ast)

    # Print intermediate code, skipping the first instruction
    for instruction in intermediate_code[1:]:
        print(instruction)