from carro import Carro

if __name__ == '__main__':
    carro = Carro('susuki swift', 'gray', 'susuki', 4)
    carro._motor.temperatura = -10
    print(carro._motor.temperatura)