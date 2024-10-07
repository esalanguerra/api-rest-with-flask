# 1. Objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. Endpoints - /books
from flask import Flask
from .api import init_app as init_api


def create_app():
	app = Flask(__name__)
		
	init_api(app)
		
	return app

def create_app_wsgi():
    # workaround for Flask issue
    # that doesn't allow **config
    # to be passed to create_app
    # https://github.com/pallets/flask/issues/4170
    app = create_app()
    
    return app
