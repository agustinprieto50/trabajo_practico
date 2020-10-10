from palabras import RepositorioPalabras
import random

def func():
    repo = RepositorioPalabras.repo_palabras
    palabra, tipo = random.choice(list(repo.items()))
    return tipo

hola = func()
print(hola)

