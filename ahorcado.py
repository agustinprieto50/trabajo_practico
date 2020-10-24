from servicesPartidas import ServicesPartidas


class Ahorcado():
    def pedir_letras(self, partida):
        servicios = ServicesPartidas()
        seguir = True
        while seguir is True:
            let = str(input("Letra: "))
            if let == "salir":
                break
            servicios.intentar_letra(partida, let)
            print(partida._palabra_aciertos)
            if partida._palabra == partida._palabra_aciertos:
                seguir = False

    def un_jugador(self):
        servicios = ServicesPartidas()
        nombre = str(input("Nombre: "))
        intentos = int(input("Dificultad: "))
        palabra = ""
        partida = servicios.iniciar_partida(nombre, intentos, palabra, "")
        self.pedir_letras(partida)
        if partida._palabra == partida._palabra_aciertos:
            print("Gano. La palabra era ", partida._palabra)
            return True
        else:
            print("Perdio. La palabra era ", partida._palabra)
            return True

    def dos_jugadores(self):
        count = 0
        while count == 0:
            count += 1
            servicios = ServicesPartidas()
            n1 = str(input("Ingrese el nombre del jugador 1: "))
            dif = int(input("Ingrese la dificultad: "))
            p1 = str(input("Palabra elegida por el jugador 2 para el jugador 1: "))
            t1 = str(input("Tipo de palabra: "))
            partida1 = servicios.iniciar_partida(n1, dif, p1, t1)
            self.pedir_letras(partida1)
            if partida1._palabra == partida1._palabra_aciertos:
                print("Gano. La palabra era ", partida1._palabra)
            else:
                print("Perdio. La palabra era ", partida1._palabra)
        if count == 1:
            n2 = str(input("Ingrese el nombre del jugador 2: "))
            dif2 = int(input("Ingrese la dificultad: "))
            p2 = str(input("Palabra elegida por el jugador 1 para el jugador 2: "))
            t2 = str(input("Tipo de palabra: "))
            partida2 = servicios.iniciar_partida(n2, dif2, p2, t2)
            self.pedir_letras(partida2)
            if partida2._palabra == partida2._palabra_aciertos:
                print("Gano. La palabra era ", partida2._palabra)
            else:
                print("Perdio. La palabra era ", partida2._palabra)
        return True
