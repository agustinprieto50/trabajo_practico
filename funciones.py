from palabras import RepositorioPalabras
import random


class Functions():

    def intentos(self, palabra, dificultad):
        intento = len(palabra) * dificultad
        return intento

    def un_jugador(self):
        repo = RepositorioPalabras.repo_palabras
        palabra = random.choice(list(repo.items()))
        return palabra


def juego(palabra, dificultad):
    intento = (int(len(palabra)) * int(dificultad))
    contador = 0
    gano = len(palabra)
    acierto = 0
    adivinanza = []
    while contador < intento:
        letra = str(input("Letra: "))
        for i in palabra:
            if i == letra:
                print(letra)
                acierto += 1
                adivinanza[i] = palabra[i]
                print(adivinanza)
            else:
                contador + 1

        if acierto == gano:
            print("La palabra era " + palabra + ". Ganaste")
            break


repo = RepositorioPalabras.repo_palabras
palabra = random.choice(list(repo))
game = juego(palabra, 100)
