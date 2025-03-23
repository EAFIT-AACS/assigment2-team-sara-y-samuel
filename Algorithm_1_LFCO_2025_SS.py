import random
import os

def generate_valid_string():
    n = random.randint(0, 5)
    string = 'a' * n + 'b' * n
    return string

def is_valid(string):
    counter = 0
    for c in string:
        if c == 'a':
            counter += 1
        elif c == 'b':
            if counter == 0:
                return False
            counter -= 1
    return counter == 0

def generate_invalid_String():
    while True:
        lenght = random.randint(1, 10)
        string = ''.join(random.choice(['a', 'b']) for _ in range(lenght))
        if not is_valid(string):
            return string

ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_txt = os.path.join(ruta_script, "cadenas.txt")

with open(ruta_txt, "w") as fil:
    for _ in range(5):
        cadena_valida = generate_valid_string()
        fil.write(cadena_valida + "\n")

    for _ in range(5):
        cadena_invalida = generate_invalid_String()
        fil.write(cadena_invalida + "\n")
