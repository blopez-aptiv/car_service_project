from flask import url_for
from flask_restx import Api

from .service_car import namespace as service_car_namespace

class ApiSwaggerFix(Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)
    
api = ApiSwaggerFix(
    title = 'Servicio de carro',
    version = '0.1',
    descripcion = 'Curso de python QTC 2022'
)

api.add_namespace(service_car_namespace)