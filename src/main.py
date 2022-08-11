# Main program
# Object oriented programing
#from carro import Carro
from libs.mysql import MySQL

if __name__ == '__main__':
    #carro = Carro('susuki swift', 'gray', 'susuki', 4)
    mysql = MySQL()
    print('conexion exitosa')
    #print(vars(carro))