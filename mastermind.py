import random
from colored import fg, attr
class Mastermind:
    COLORES = {"R": fg("red"), "B": fg("blue"), "G": fg("green"), "Y": fg("yellow")}
    ColorCorrecto = fg("green") + "O" + attr("reset")
    ColorDesubicado = fg("yellow") + "O" + attr("reset")
    def mostrar(self):
        for fila in self.tablero:
            adivinanza = " ".join([self.COLORES.get(color, '') + 'O' + attr('reset') for color in fila[:4]])
            indicaciones = " ".join(fila[4])
            print(f"{adivinanza} | {indicaciones}")
       
    def __init__(self):
        self.tablero = [[' ']*4 + [' '] for _ in range(12)]     
    def actualizar(self, turno, adivinanza, indicaciones):
        self.tablero[turno][:4] = adivinanza
        self.tablero[turno][4] = indicaciones

class CreadorCodigo:
    def __init__(self, colores):
        self.colores = colores
        self.codigo_secreto = self.crear_codigo_secreto()
    def crear_codigo_secreto(self):
        return [random.choice(self.colores) for _ in range(4)]
    def ObtenerIndicaciones(self, adivinanza):
        indicaciones = []
        CopiaCodigoColoresSecreto = self.codigo_secreto[:]
        for i in range(4):
            if adivinanza[i] == CopiaCodigoColoresSecreto[i]:
                indicaciones.append(Mastermind.ColorCorrecto)
                CopiaCodigoColoresSecreto[i] = None 
        for i in range(4):
            if adivinanza[i] in CopiaCodigoColoresSecreto:
                indicaciones.append(Mastermind.ColorDesubicado)
                CopiaCodigoColoresSecreto[CopiaCodigoColoresSecreto.index(adivinanza[i])] = None
        return indicaciones
    
class AdivinadorDeJuego:
    def __init__(self, colores):
            self.colores = colores
            
    def HacerAdivinanaza(self):
            adivinanza = input("Agregue su adivinanza de colores:").upper()
            while len(adivinanza) != 4 or any(c not in self.colores for c in adivinanza):
             adivinanza = input("Adivinaza incorrecta").upper()
            return list(adivinanza)

def JugarMatermind():
            colores = ["R", "B", "G", "Y"]
            tablero = Mastermind()
            creador__codigo = CreadorCodigo(colores)
            adivinador__codigo = AdivinadorDeJuego(colores)
            
            for turno in range(12):
                tablero.mostrar()
                adivinanza = adivinador__codigo.HacerAdivinanaza()
                indicaciones = creador__codigo.ObtenerIndicaciones(adivinanza)
            tablero.actualizar(turno, adivinanza, indicaciones)
            
            if all(f == Mastermind.ColorCorrecto for f in indicaciones):
                print("Colores adivinados!")
                return
            print(f"Juego terminado, los colores eran {''.join(creador__codigo.codigo_secreto)}")
   
JugarMatermind() 
        


