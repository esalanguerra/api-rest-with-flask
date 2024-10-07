from flask import jsonify, request
from flask_restful import Resource
from .data import books


class BookResource(Resource):
    def __init__(self):
        self.books = books

    def get(self):
        return jsonify(self.books)
    
    def post(self):
        book = request.get_json()

        book = {
            'id': len(self.books) + 1,
            'title': book['title'],
            'author': book['author']
        }

        if not book['title']:
            return jsonify({ 'message': 'title is required' })
        
        if not book['author']:
            return jsonify({ 'message': 'author is required' })

        self.books.append(book)

        return jsonify({ 'message': 'ok' })
    
class BookItemResource(Resource):
    def __init__(self):
        self.books = books

    def get(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                return jsonify(book)
            
        return jsonify({ 'message': 'not found' })
    
    def patch(self, book_id):
        book = request.get_json()
        
        for index, book in enumerate(self.books):
            if book['id'] == book_id:
                self.books[index] = book
                return jsonify(book)
            
        return jsonify({ 'message': 'not found' })
    
    def delete(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                return jsonify({ 'message': 'deleted' })
            
        return jsonify({ 'message': 'not found' })
