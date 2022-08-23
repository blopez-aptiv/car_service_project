from flask import Flask
from api import api
#from libs.mysql import MySQL

app = Flask(__name__)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
    #mysql = MySQL()
    #print('conexion exitosa')
    
    #opcion = int(input(''' 
    #                   1. Crear vehiculo
    #                   2. Consulte vehiculo
    #                   3. Crear cliente
    #                   4. Crear cita
    #                   5. Consultar cita
    #                   opcion?: '''))
    
    #if opcion == 1:# Crear vehiculo
    #    tipo_vehiculo = mysql.obtener_tipo_vehiculo()
    #    [print(f"{vehiculo.get('id_tipo', 1)}. {vehiculo['descripcion']}\n") for vehiculo in tipo_vehiculo]
        
    #    tipo  = int(input("tipo de vehiculo?: "))
    #    color = input('color?')
    #    n_ruedas = int(input("numero de ruedas?"))
    #    modelo = input("modelo?: ")
        
    #    mysql.crear_vehiculo(tipo, color, n_ruedas, modelo)
    #elif opcion == 2:# Consultar vehiculo
    #    vehiculos = mysql.consultar_vehiculo()
        
    #    for vehiculo in vehiculos:
    #        print(f"{vehiculo.id_vehiculo, vehiculo.modelo}")
        
    #elif opcion == 3:# Crear cliente
        
    #    idcliente = input("ID cliente?: ")
    #    idvehiculo = input("ID vehiculo?: ")
        #ultimo_servicio = input("Ultimo servicio?: ")
        
    #    mysql.crear_cliente(idcliente, idvehiculo)
    #elif opcion == 4:# Crear cita
        
    #    servicio = int(input("ID servicio?: "))
    #    cliente = int(input("ID del cliente?: "))
    #    sucursal = int(input("ID Sucursal?: "))
        #fecha = input("Fecha de cita?: ")
        
    #    mysql.crear_cita(servicio, cliente, sucursal)
    #elif opcion == 5:# Consultar cita
    #    pass