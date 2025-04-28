import os

def pda():
    initial_state = "q0"
    stack = []
    return initial_state, stack

def transitions(symbol, current_state, stack):
    if current_state == "q0":
        if symbol == "a":
            stack.append("A")
            return True
        elif symbol == "b":
            if len(stack) > 0:
                stack.pop()
                return True
            else:
                return False
        else:
            return False

def accept(string):
    state, stack = pda()
    for symbol in string:
        if not transitions(symbol, state, stack):
            return False
    return len(stack) == 0

def read_strings():
    script_path = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(script_path, "cadenas.txt")  # <- Renamed the file here if you want to change it

    with open(txt_path, "r") as file:
        return file.readlines()

def main():
    strings = read_strings()
    for line in strings:
        line = line.strip()
        if accept(line):
            print(f"The string '{line}' IS ACCEPTED by the PDA.")
        else:
            print(f"The string '{line}' IS REJECTED by the PDA.")

main()
