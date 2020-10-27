from servicesPartidas import ServicesPartidas


class Ahorcado():
    def pedir_letras(self, partida):
        servicios = ServicesPartidas()
        seguir = True
        while seguir is True:
            try:
                let = str(input("Letra: "))
            except StopIteration:
                return
            if let == "salir":
                break
            result = servicios.intentar_letra(partida, let)
            print("\n", partida._palabra_aciertos)
            if result == "Gano":
                print("\nGANASTE! La palabra era: ", partida.palabra)
                return "Gano"
                seguir = False
            if result == "Perdio":
                print("\nPERDISTE! La palabra era: ", partida.palabra)
                return "Perdio"
                seguir = False

    def un_jugador(self):
        servicios = ServicesPartidas()
        nombre = str(input("Nombre: "))
        intentos = int(input("Dificultad: "))
        palabra = ""
        partida = servicios.iniciar_partida(nombre, intentos, palabra, "")
        self.pedir_letras(partida)
        return True

    def dos_jugadores(self):
        count = 0
        while count == 0:
            count += 1
            servicios = ServicesPartidas()
            n1 = str(input("\nIngrese el nombre del jugador 1: "))
            dif = int(input("Ingrese la dificultad: "))
            p1 = str(input("Palabra elegida por el jugador" +
                           " 2 para el jugador 1: "))
            t1 = str(input("Tipo de palabra: "))
            partida1 = servicios.iniciar_partida(n1, dif, p1, t1)
            resultado = self.pedir_letras(partida1)
            dic = {}
            dic[0] = {"JUGADOR 1": {"Nombre": n1.upper(),
                                    "Resultado": resultado.upper()}}
        if count == 1:
            n2 = str(input("\nIngrese el" +
                           " nombre del jugador 2: "))
            dif2 = int(input("Ingrese la dificultad: "))
            p2 = str(input("Palabra elegida por el jugador" +
                           " 1 para el jugador 2: "))
            t2 = str(input("Tipo de palabra: "))
            partida2 = servicios.iniciar_partida(n2, dif2, p2, t2)
            resultado2 = self.pedir_letras(partida2)
            dic[1] = {"JUGADOR 2": {"Nombre": n2.upper(),
                                    "Resultado": resultado2.upper()}}
            servicios.add_partida(dic)
        return True
