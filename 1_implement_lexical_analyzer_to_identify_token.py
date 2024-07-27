# Write a program to implement Lexical Analyzer to identify token.

keywords = {"if", "else", "while", "do", "break", "continue", "int", "double", "float", "return", "char", "case", "sizeof", "long", "short", "typedef", "switch", "unsigned", "void", "static", "struct", "goto"}
operators = {'+', '-', '*', '/', '>', '<', '=', '>=', '<=', '==', '!='}
delimiters = {' ', ',', ';', '(', ')', '[', ']', '{', '}', '\n'}

def is_delimiter(char):
    return char in delimiters

def is_operator(char):
    return char in operators

def is_keyword(word):
    return word in keywords

def is_identifier(word):
    return word.isidentifier() and not is_keyword(word)

def is_number(word):
    return word.isdigit()

def lexical_analyzer(input_string):
    tokens = []
    current_token = ""
    for char in input_string:
        if is_delimiter(char) or is_operator(char):
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if not is_delimiter(char):
                tokens.append(char)
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)

    for token in tokens:
        if is_keyword(token):
            print(f"{token} : Keyword")
        elif is_identifier(token):
            print(f"{token} : Identifier")
        elif is_number(token):
            print(f"{token} : Number")
        elif is_operator(token):
            print(f"{token} : Operator")
        elif is_delimiter(token):
            print(f"{token} : Delimiter")
        else:
            print(f"{token} : Unknown")

# Take input from user
input_string = input("Enter a string to analyze: ")
lexical_analyzer(input_string)