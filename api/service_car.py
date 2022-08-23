from flask import request, current_app as app
from flask_restx import Namespace, Resource, fields

from libs.mysql import MySQL

namespace = Namespace('service', description='')
mysql = MySQL()

carro_modelo = namespace.inherit('crea_carro',
{
    "tipo": fields.Integer(description='1. carro, 2. motocicleta, 3. automovil de 3 ruedas', required=True),
    "color": fields.String(description='azul, gris, blanco, negro', required=True),
    "n_ruedas": fields.Integer(description='numero de ruedas', required=True),
    "modelo": fields.String(description='modelo', required=True),
})

persona_modelo = namespace.inherit('persona',
{
    "role_id": fields.Integer(description='1. empleado, 2. cliente', required=True),
    "password": fields.String(description='', required=True),
    "nombre": fields.String(description='', required=True),
    "apellido": fields.String(description='', required=True),
    "telefono": fields.String(description='', required=True),
    "correo": fields.String(description='', required=True),
    "direccion": fields.String(description='', required=True),
    "id_vehiculo": fields.Integer(description='', required=True),
    "ultimo_servicio": fields.Date(description='AAAA-MM-DD HH', required=True),
})

cita_modelo = namespace.inherit('cita',
{
    "id_cliente": fields.Integer(description='', required=True),
    "id_sucursal": fields.Integer(description='', required=True),
    "fecha": fields.Date(description='AAAA-MM-DD HH', required=True),
    "id_vehiculo": fields.Integer(description='', required=True),
    "id_estado_servicio": fields.Integer(description='', required=True),
    "tipo_servicio_id": fields.Integer(description='', required=True),
})

@namespace.route('crea_carro')
class crea_carro(Resource):
    @namespace.expect(carro_modelo, validate=True)
    @namespace.response(code=200, description='Registro exitoso')
    @namespace.response(code=400, description='Peticion invalida')
    @namespace.response(code=500, description='Error interno en el servidor')
    def post(self):
        app.logger.info(f"json = {request}")
        tipo     = request.json['tipo']
        color    = request.json['color']
        n_ruedas = request.json['n_ruedas']
        modelo   = request.json['modelo']
        
        mysql.crear_vehiculo(tipo, color, n_ruedas, modelo)

@namespace.route('obtener_vehiculo')
class obtener_vehiculo(Resource):
    @namespace.response(code=200, description='Registro exitoso')
    @namespace.response(code=400, description='Peticion invalida')
    @namespace.response(code=500, description='Error interno en el servidor')
    def get(self):
        
        vehiculos = mysql.consultar_vehiculo_from_api()        
        return vehiculos

@namespace.route('crea_cliente')
class crea_cliente(Resource):
    @namespace.expect(persona_modelo, validate=True)
    @namespace.response(code=200, description='Registro exitoso')
    @namespace.response(code=400, description='Peticion invalida')
    @namespace.response(code=500, description='Error interno en el servidor')
    def post(self):
        app.logger.info(f"json = {request.json}")
        role_id     = request.json['role_id']
        password    = request.json['password']
        nombre      = request.json['nombre']
        apellido    = request.json['apellido']
        telefono    = request.json['telefono']
        correo      = request.json['correo']
        direccion   = request.json['direccion']
        id_vehiculo = request.json['id_vehiculo']
        ultimo_servicio = request.json['ultimo_servicio']
        
        mysql.crear_cliente(role_id, password, nombre, apellido, telefono, correo, direccion, id_vehiculo, ultimo_servicio)
        
        return "Creacion exitosa de cliente"
    
@namespace.route('/crea_cita')
class crea_cita(Resource):
    @namespace.expect(cita_modelo, validate=True)
    @namespace.response(code=200, description='Registro exitoso')
    @namespace.response(code=400, description='Peticion invalida')
    @namespace.response(code=500, description='Error interno en el servidor')
    def post(self):
        app.logger.info(f"json = {request.json}")
        id_cliente     = request.json['id_cliente']
        id_sucursal    = request.json['id_sucursal']
        fecha          = request.json['fecha']
        id_vehiculo    = request.json['id_vehiculo']
        id_estado_servicio = request.json['id_estado_servicio']
        tipo_servicio_id = request.json['tipo_servicio_id']
        
        mysql.crear_cita(id_cliente, id_sucursal, fecha, id_vehiculo, id_estado_servicio, tipo_servicio_id)#
        
        return  "Creacion exitosa de cita"
    
@namespace.route('obtener_cita')
class obtener_vehiculo(Resource):
    @namespace.response(code=200, description='Registro exitoso')
    @namespace.response(code=400, description='Peticion invalida')
    @namespace.response(code=500, description='Error interno en el servidor')
    def get(self):
        
        citas = mysql.consultar_cita()        
        return citas