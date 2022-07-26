class Motor:
    cilindros     = int 
    tipo_motor    = str
    _temperatura  = float
    
    def __init__(self, cilindros, tipo_motor = 'gas') -> None:
        self.cilindros  = cilindros
        self.tipo_motor = tipo_motor