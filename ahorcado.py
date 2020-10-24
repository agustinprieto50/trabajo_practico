from servicesPartidas import ServicesPartidas
import sys


class Ahorcado():
    def pedir_letras():
        pass

    def un_jugador(self):
        servicios = ServicesPartidas()
        nombre = str(input("Nombre: "))
        intentos = int(input("Dificultad: "))
        palabra = ""
        partida = servicios.iniciar_partida(nombre, intentos, palabra, "")
        while partida._palabra != partida._palabra_aciertos:
            let = str(input("Letra: "))
            if let == "salir":
                break
            servicios.intentar_letra(partida, let)
            print(partida._palabra_aciertos)
            if partida._intentos == 0:
                break
        if partida._palabra == partida._palabra_aciertos:
            print("Gano. La palabra era ", partida._palabra)
            return True
        print("Perdio. La palabra era ", partida._palabra)
        return True
        

    def dos_jugadores(self):
        n1 = str(input("Ingrese el nombre del jugador 1: "))
        p1 = str(input("Palabra elegida por el jugador 2 para el jugador 1: "))
        t1 = str(input("Tipo de palabra: "))
        dif = int(input("Ingrese la dificultad: "))

        


        
