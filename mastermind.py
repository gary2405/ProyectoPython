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
        self.codigosecret = self.crearcodigosecret()
    def crearcodigosecret(self):
         return [random.choice(self.colores) for _ in range(4)]
    def obtenerIndicaciones(self, adivinanza):
        indicaciones = []
        CopiaCodColoresSecreto = self.codigosecret[:]
        for i in range(4):
            if adivinanza[i] == CopiaCodColoresSecreto[i]:
                indicaciones.append(Mastermind.ColorCorrecto)
                CopiaCodColoresSecreto[i] = None
        for i in range(4):
            if adivinanza[i] in CopiaCodColoresSecreto:
                indicaciones.append(Mastermind.ColorDesubicado)
                CopiaCodColoresSecreto[CopiaCodColoresSecreto.index(adivinanza[i])] = None
        return indicaciones
class AdivinadorDeJuego:
    def __init__(self, colores):
        self.colores = colores
    def HacerAdivinanza(self):
        estrategia = input("Elige la estrategia de adivinanza: aleatoria (A) o fuerza bruta (F): ").upper()
        while estrategia not in ["A", "F"]:
            estrategia = input("Opción inválida, elige A para aleatoria o F para fuerza bruta: ").upper()
        if estrategia == "A":
            return self.adivinanzaAzar()
        elif estrategia == "F":
            return self.adivinanzaConFuerzabruta()
    def adivinanzaAzar(self):
        return [random.choice(self.colores) for _ in range(4)]
    def adivinanzaConFuerzabruta(self):
        combinaciones = [[a, b, c, d] for a in self.colores for b in self.colores for c in self.colores for d in self.colores]
        return random.choice(combinaciones)
    
def jugarMastermind():
    colores = ["R", "B", "G", "Y"]
    tablero = Mastermind()
    opcion = input("¿Quieres ser el creador del código (Maker) o el adivinador del código (Breaker)? (M/B): ").upper()
    while opcion not in ["M", "B"]:
        opcion = input("Opción inválida, elige M para Maker o B para Breaker: ").upper()
    if opcion == "M":
        CodigoDeJugador = input("Ingresa tu código de 4 colores: ").upper()
        while len(CodigoDeJugador) != 4 or any(c not in colores for c in CodigoDeJugador):
            CodigoDeJugador = input("Código incorrecto, intente de nuevo: ").upper()
        creador_codigo = CreadorCodigo(colores)
        creador_codigo.codigosecret = list(CodigoDeJugador)
    else:
        creador_codigo = CreadorCodigo(colores)
    adivinador_codigo = AdivinadorDeJuego(colores)
    for turno in range(12):
        tablero.mostrar()
        adivinanza = adivinador_codigo.HacerAdivinanza()
        indicaciones = creador_codigo.obtenerIndicaciones(adivinanza)
        tablero.actualizar(turno, adivinanza, indicaciones)
        if all(f == Mastermind.ColorCorrecto for f in indicaciones):
            tablero.mostrar()
            print("Colores adivinados!!")
            return
        tablero.mostrar()
        print(f"El juego ha terminado, los colores eran {''.join(creador_codigo.codigosecret)}")
jugarMastermind()








