import pymysql
import os
import sys

from models.vehiculo import Vehiculo

class MySQL:
    def __init__(self) -> None:
        username   = os.environ['MYSQL_USERNAME']
        password   = os.environ['MYSQL_PASSWORD']
        mysql_db   = os.environ['MYSQL_DB']
        mysql_host = os.environ['MYSQL_HOST']
        
        self.mysql_connection = pymysql.connect(host= mysql_host, user=username, password=password, database=mysql_db, cursorclass=pymysql.cursors.DictCursor, autocommit=True)
        
    def obtener_tipo_vehiculo(self):
        try:
            with self.mysql_connection.cursor() as cursor:
                query = "SELECT id_tipo, descripcion \
                        FROM tipo_vehiculo;"
                        
                cursor.execute(query)
                return cursor.fetchall()
                        
        except pymysql.ProgrammingError as e:
            print(f"error al ejecutar la consulta {e}")
            sys.exit()
            
    def crear_vehiculo(self, tipo, color, n_ruedas, modelo, motor = 1):
        try:
            with self.mysql_connection.cursor() as cursor:
                query = "INSERT INTO vehiculo (`id_tipo`,`color`, `ruedas`, `modelo`)\
                        VALUES (%s, %s, %s, %s)"       
                cursor.execute(query, (tipo, color, n_ruedas, modelo))
                
                id_vehiculo = cursor.lastrowid
                query = "INSERT INTO carro (`id_carro`,`id_motor`)\
                        VALUES (%s, %s)"  
                
                cursor.execute(query, (id_vehiculo, motor))
                
        except pymysql.ProgrammingError as e:
            print(f"error al ejecutar la consulta {e}")
            sys.exit()
            
    def consultar_vehiculo(self):
        vehiculos = []
        try:
            with self.mysql_connection.cursor() as cursor:
                query = "SELECT id_vehiculo, id_tipo, color, ruedas, modelo  \
                        FROM vehiculo;"
                        
                cursor.execute(query)
                
                for row in cursor.fetchall():
                    vehiculo = Vehiculo()
                    vehiculo.id_vehiculo = row['id_vehiculo']
                    vehiculo.id_tipo     = row['id_tipo']
                    vehiculo.color       = row['color']
                    vehiculo.ruedas      = row['ruedas']
                    vehiculo.modelo      = row['modelo']
                    
                    vehiculos.append(vehiculo)
                        
            return vehiculos
        except pymysql.ProgrammingError as e:
            print(f"error al ejecutar la consulta {e}")
            sys.exit()
            
    def consultar_vehiculo_from_api(self):
        vehiculos = []
        try:
            with self.mysql_connection.cursor() as cursor:
                query = "SELECT id_vehiculo, id_tipo, color, ruedas, modelo  \
                        FROM vehiculo;"
                        
                cursor.execute(query)
                
                for row in cursor.fetchall():
                    vehiculos.append(row)
                        
            return vehiculos
        except pymysql.ProgrammingError as e:
            print(f"error al ejecutar la consulta {e}")
            sys.exit()
            
    def crear_cliente(self, role_id, password, nombre, apellido, telefono, correo, direccion, id_vehiculo, ultimo_servicio):
        try:
            with self.mysql_connection.cursor() as cursor:
                query = "INSERT INTO persona (id_role, contrasena, nombre, apellido, telefono, correo, direccion)\
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"       
                cursor.execute(query, (role_id, password, nombre, apellido, telefono, correo, direccion))
                
                id_persona = cursor.lastrowid
                query = "INSERT INTO cliente (id_cliente, id_vehiculo, ultimo_servicio )\
                        VALUES (%s, %s, %s)"  
                
                cursor.execute(query, (id_persona, id_vehiculo, ultimo_servicio))
                
        except pymysql.ProgrammingError as e:
            print(f"error al ejecutar la consulta {e}")
            sys.exit()
            
    def crear_cita(self, id_cliente, id_sucursal, fecha, id_vehiculo, id_estado_servicio, tipo_servicio_id):
        try:
            with self.mysql_connection.cursor() as cursor:
                query = "INSERT INTO servicio (id_vehiculo, id_estado_servicio, id_tipo_servicio  )\
                        VALUES (%s, %s, %s)"  
                
                cursor.execute(query, (id_vehiculo, id_estado_servicio, tipo_servicio_id))
                id_servicio = cursor.lastrowid
                
                query = "INSERT INTO cita (id_servicio, id_cliente, id_sucursal, fecha )\
                        VALUES (%s, %s, %s, %s)"       
                cursor.execute(query, (id_servicio, id_cliente, id_sucursal, fecha))
                
                
        except pymysql.ProgrammingError as e:
            print(f"error al ejecutar la consulta {e}")
            sys.exit()