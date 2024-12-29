class TicTacToe:
    def __init__(self):
        self.tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.turno = 0

    def imprimirTablero(self):
        print("\n")
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                print(self.tablero[i][j], end=" | ")
            print("\n-----------")

    def movimiento(self, simbolo, x,y):
        self.tablero[x-1][y-1] = simbolo
    

    def WhoWin(self):
        ganador = ""
        # Revisamos las filas
        for i in range(len(self.tablero)):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] and self.tablero[i][0] != "-":
                ganador = self.tablero[i][0]
        
        # Revisamos las columnas
        for j in range(len(self.tablero[0])):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] and self.tablero[0][j] != "-":
                ganador = self.tablero[0][j]
        
        # Revisamos las diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] and self.tablero[0][0] != "-":
            ganador = self.tablero[0][0]
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] and self.tablero[0][2] != "-":
            ganador = self.tablero[0][2]
            
        return ganador


    def IsFull(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.tablero[i][j] == "-":
                    return False
        return True 
    
    def IsTerminal(self):
        if self.WhoWin() != "" or self.IsFull():
            return True
        else:
            return False
    
    def jugadorTurno(self):
        if self.turno % 2 == 0:
            jugador = "X"
        else:
            jugador = "O"
        return jugador
    
    def juego(self):
        turno = 0
        print(self.WhoWin())
        while not self.IsTerminal():
            simbolo = self.jugadorTurno()
            print("Turno de: ", simbolo, end="")
            self.imprimirTablero()
            x = int(input("X: "))
            y = int(input("Y: "))
            self.movimiento(simbolo,x,y)
            self.turno += 1

def run():
    juego = TicTacToe()
    juego.juego()

if __name__ == '__main__':
    run()