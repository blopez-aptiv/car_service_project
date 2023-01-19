from flask import Flask
from api import api

app = Flask(__name__)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
    #Cristian was here
    # mysql = MySQL()
    # print('conexion exitosa')
    
    # opcion = int(input(''' 
    #                    1. Crear vehiculo
    #                    2. Consulte vehiculo
    #                    3. Crear cliente
    #                    4. Crear cita
    #                    5. Consultar cita
    #                    opcion?: '''))
    
    # if opcion == 1:
    #     tipo_vehiculo = mysql.obtener_tipo_vehiculo()
    #     [print(f"{vehiculo.get('id_tipo', 1)}. {vehiculo['descripcion']}\n") for vehiculo in tipo_vehiculo]
        
    #     tipo  = int(input("tipo de vehiculo?: "))
    #     color = input('color?')
    #     n_ruedas = int(input("numero de ruedas?"))
    #     modelo = input("modelo?: ")
        
    #     mysql.crear_vehiculo(tipo, color, n_ruedas, modelo)
    # elif opcion == 2:
    #     vehiculos = mysql.consultar_vehiculo()
        
    #     for vehiculo in vehiculos:
    #         print(f"{vehiculo.id_vehiculo, vehiculo.modelo}")
        
    # elif opcion == 3:
    #     pass
    # elif opcion == 4:
    #     pass
    # elif opcion == 5:
    #     pass
    