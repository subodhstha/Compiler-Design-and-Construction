# Write a program to check whether a given identifier is valid or not.
import keyword

def is_valid_identifier(identifier):
    if not identifier:
        return False

    if not (identifier[0].isalpha() or identifier[0] == '_'):
        return False

    if not all(char.isalnum() or char == '_' for char in identifier[1:]):
        return False

    if keyword.iskeyword(identifier):
        return False

    return True

# Example usage
if __name__ == "__main__":
    test_identifiers = [
        "valid_identifier",
        "_valid_identifier",
        "1_invalid_identifier",
        "invalid-identifier",
        "for",
        "while",
        "anotherValid123"
    ]

    for identifier in test_identifiers:
        print(f"'{identifier}': {'Valid' if is_valid_identifier(identifier) else 'Invalid'}")