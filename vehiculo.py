class Vehiculo:
    ruedas = int
    color  = str
    
    def __init__(self, ruedas, color) -> None:
        self.ruedas = ruedas
        self.color  = color