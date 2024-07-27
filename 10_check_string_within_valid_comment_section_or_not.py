# Write a program to check whether a given string is within valid comment section or not.
def is_within_comment(code, target_string):
    in_single_line_comment = False
    in_multi_line_comment = False
    target_found = False

    lines = code.split('\n')
    for line in lines:
        i = 0
        while i < len(line):
            if in_single_line_comment:
                if line[i] == '\n':
                    in_single_line_comment = False
                i += 1
                continue

            if in_multi_line_comment:
                if line[i:i+2] == '*/':
                    in_multi_line_comment = False
                    i += 2
                else:
                    i += 1
                continue

            if line[i:i+2] == '//':
                in_single_line_comment = True
                i += 2
                continue

            if line[i:i+2] == '/*':
                in_multi_line_comment = True
                i += 2
                continue

            i += 1

        if in_single_line_comment or in_multi_line_comment:
            if target_string in line:
                target_found = True

    return target_found

# Example usage
code = """
// This is a single line comment
int main() {
    /* This is a 
    multi-line comment */
    printf("Hello, World!"); // Another comment
}
"""
target_string = "multi-line comment"
print(is_within_comment(code, target_string))  # Output: True