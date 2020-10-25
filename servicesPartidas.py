from partida import Partida
from palabras import RepositorioPalabras
from partida_repo import PartidaRepositorio
import random


class ServicesPartidas():

    # Crea una instancia de la clase partida
    def iniciar_partida(self, nombre, intentos, palabra, tipo):
        if palabra == '' and tipo == '':
            word = self.get_random_palabra()
            partida = Partida(word.get('palabra'),
                              intentos, word.get("tipo_palabra"), nombre)
            return partida
        partida = Partida(palabra, intentos, tipo, nombre)
        return partida

    # Devuelve una palabra al azar del repositorio de palabras
    def get_random_palabra(self):
        repo = RepositorioPalabras.repo_palabras
        key, p = random.choice(list(repo.items()))
        return p

    def intentar_letra(self, partida, letra):
        letter = letra.upper()
        if partida._intentos == 0:
            raise ValueError("Error")
        while partida._intentos > 0 and \
                (partida._palabra != partida._palabra_aciertos):
            for i in range(len(partida._palabra)):
                if partida._palabra[i] == letter:
                    partida._palabra_aciertos[i] = letter
            print(partida._palabra_aciertos)
            partida._intentos -= 1
            if (partida._palabra_aciertos != partida._palabra
               and partida._intentos > 0):
                return "Continua"
            if (partida._palabra_aciertos == partida._palabra
               and partida._intentos > 0):
                break
        if partida._palabra_aciertos == partida._palabra:
            return "Gano"
        return "Perdio"

    def add_partida(self, partida):
        lastKey = -1
        for key in PartidaRepositorio.repo_partida:
            lastKey = key
        new = (lastKey) + 1
        PartidaRepositorio.repo_partida[new] = partida.__dict__
        return new
