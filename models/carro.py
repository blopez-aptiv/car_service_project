from vehiculo import Vehiculo
from motor import Motor

class Carro(Vehiculo):
    modelo = str
    marca  = str
    _motor = None
    
    def __init__(self, modelo, color, marca, ruedas):
        self.modelo = modelo
        self.color  = color
        self.marca  = marca
        self._motor = Motor(4)
        self.ruedas = ruedas
    