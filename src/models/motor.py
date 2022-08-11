class Motor:
    cilindros     = int 
    tipo_motor    = str
    __temperatura  = float
    
    def __init__(self, cilindros, tipo_motor = 'gas') -> None:
        self.cilindros  = cilindros
        self.tipo_motor = tipo_motor
        self.__temperatura = 0
     
    @property    
    def temperatura(self):
        return self.__temperatura
        
    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura < 0:
            raise ValueError("No se puede asignar temperaturas negativas")
        
        self.__temperatura = temperatura