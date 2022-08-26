from sqlite3 import Cursor
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
            
    
