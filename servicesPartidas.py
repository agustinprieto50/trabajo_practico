from partida import Partida
from palabras import RepositorioPalabras
import random


class ServicesPartidas():
    def iniciar_partida(self, nombre, intentos, palabra, tipo):
        if palabra == '' and tipo == '':
            word = self.get_random_palabra()
            partida = Partida(word.get('palabra'),
                              intentos, word.get("tipo_palabra"), nombre)
            return partida
        partida = Partida(palabra, intentos, tipo, nombre)
        return partida
    
    def get_random_palabra(self):
        repo = RepositorioPalabras.repo_palabras
        key, p = random.choice(list(repo.items()))
        return p


#     def intentos(self, palabra, dificultad):
#         intento = len(palabra) * dificultad
#         return intento

#     def add_partida(self, partida):
#         lastKey = -1
#         for key in PartidaRepositorio.repo_partida:
#             lastKey = key
#         new = (lastKey) + 1
#         PartidaRepositorio.repo_partida[new] = partida.__dict__
#         return new

#     def select_palabra():
#         repo = RepositorioPalabras.repo_palabras
#         palabra = random.choice(list(repo))
#         return palabra

#     def juego(palabra, dificultad):
#         intento = (int(len(palabra)) * int(dificultad))
#         contador = 0
#         gano = len(palabra)
#         acierto = 0
#         palabra_adivinada = list(palabra)
#         palabra_final = palabra
#         while contador < intento:
#             letra = str(input("Letra: "))
#             if letra in palabra:
#                 palabra_adivinada.insert(palabra.find(letra), letra)
#                 palabra_adivinada.pop(palabra.find(letra) + 1)
#                 print(palabra_adivinada)
#                 acierto += 1
#                 palabra = palabra.replace(letra, letra)
#                 print(palabra)

#             else:
#                 contador += 1

#             if acierto == gano:
#                 print("La palabra era " + palabra_final + ". Ganaste")
#                 break
#             if acierto != gano and contador == intento:
#                 print("La palabra era " + palabra_final + ". Perdiste")
#                 break
