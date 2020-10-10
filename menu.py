from funciones import Functions


class Menu():
    def menu_juego(self):
        print("\n\n1. Partida para un jugador")
        print("2. Partida para 2 jugadores")
        return int(input("Elija una opción: "))


if __name__ == '__main__':
    menu = Menu()
    servicios = Functions()
    while True:
        seleccion = menu.menu_juego()
        if seleccion == 1:
            dificultad = int(input("Indique la dificultad: "))
            palabra_elegida = Functions.select_palabra()
            partida = Functions.juego(palabra_elegida, dificultad)
        if seleccion < 1 or seleccion > 4:
            break

    