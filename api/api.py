from flask import jsonify, request, Blueprint
from flask_restful import Api
from .resources import BookResource, BookItemResource


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)

def init_app(app):
    api.add_resource(BookResource, "/books/")
    api.add_resource(BookItemResource, "/books/<int:book_id>/")
    
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({ 'message': 'not found' }), 404
    
    app.register_error_handler(404, page_not_found)

    app.register_blueprint(bp)
