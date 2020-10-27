from ahorcado import Ahorcado
from partida_repo import PartidaRepositorio


class Menu():
    def menu_juego(self):
        print("\nBIENVENIDO AL JUEGO DEL AHORCADO!")
        print("\nSeleccione el modo de juego que desea jugar.")
        print("\n1. Partida para un jugador")
        print("2. Partida para 2 jugadores")
        return int(input("\nElija una opción: "))


if __name__ == '__main__':
    menu = Menu()
    servicios = Ahorcado()
    while True:
        seleccion = menu.menu_juego()
        if seleccion == 1:
            servicios.un_jugador()
        if seleccion == 2:
            servicios.dos_jugadores()
            print("\nHistroial de partida: ", PartidaRepositorio.repo_partida)
