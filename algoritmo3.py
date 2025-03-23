import os

def process_string_with_stack_trace(string):
    stack = []
    configurations = []
    remaining_input = string

    for i, symbol in enumerate(string):
        if symbol == 'a':
            stack.append('A')
        elif symbol == 'b':
            if stack:
                stack.pop()
            else:
                configurations.append(("q", remaining_input[i:], stack.copy()))
                return False, configurations
        else:
            configurations.append(("q", remaining_input[i:], stack.copy()))
            return False, configurations
        configurations.append(("q", remaining_input[i+1:], stack.copy()))

    accepted = len(stack) == 0
    if accepted:
        configurations.append(("q", "", stack.copy()))  # Final accepted state
    return accepted, configurations


# CODE 3 - Configuration tree ONLY for accepted strings
def read_strings():
    script_path = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(script_path, "cadenas.txt")
    with open(txt_path, "r") as file:
        return file.readlines()

print("\n========== CONFIGURATION TREES FOR ACCEPTED STRINGS ==========\n")

lines = read_strings()

for line in lines:
    line = line.strip()

    # Ignore headers or empty lines
    if line == "" or line.lower() in ["cadenas validas:", "cadenas inválidas:", "cadenas invalidas:"]:
        continue

    accepted, configurations = process_string_with_stack_trace(line)

    if accepted:
        print(f"STRING: '{line}' → ACCEPTED")
        print("Configuration tree of the PDA computation (state, remaining input, stack):")
        for i, (state, remaining, stack) in enumerate(configurations):
            print(f"  Step {i+1}: ({state}, {remaining if remaining != '' else 'ε'}, {stack if stack else 'ε'})")
        print("-" * 60)
