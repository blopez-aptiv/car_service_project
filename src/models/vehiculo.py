class Vehiculo:
    _id_vehiculo = int
    _id_tipo     = int
    _ruedas      = int
    _color       = str
    _modelo      = str
    
    def __init__(self) -> None:
        pass
    
    @property
    def id_vehiculo(self):
        return self._id_vehiculo
    
    @id_vehiculo.setter
    def id_vehiculo(self, id_vehiculo):
        self._id_vehiculo = id_vehiculo
        
    @property
    def id_tipo(self):
        return self._id_tipo
    
    @id_tipo.setter
    def id_tipo(self, id_tipo):
        self._id_tipo = id_tipo
        
    @property
    def ruedas(self):
        return self._ruedas
    
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
        
    @property
    def modelo (self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
        
    