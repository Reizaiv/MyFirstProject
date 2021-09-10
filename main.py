"""

Este programa es la plantilla principal de ejecucion.

"""
import TicTacToe as ttt
from MyMainPackage.SubPackage import mysubscript
mysubscript.sub_report()


KEEP = True
while KEEP:
    MARCADOR = ttt.players_choice()
    TABLERO = []
    GANADOR = False
    while not GANADOR:
        FIGURA, POSICION = ttt.player_input(MARCADOR)
        TABLERO = ttt.place_holder(FIGURA, POSICION, TABLERO)
        BOARD = ttt.display_board(TABLERO)
        GANADOR = ttt.check_victory(BOARD, FIGURA)
        MARCADOR = ttt.player_turn(MARCADOR)

    KEEP = ttt.keep_playing()
