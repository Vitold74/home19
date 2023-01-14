from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace("genres")
@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        genre = genre_service.get_all()
        return GenreSchema(many=True).dump(genre), 200

    def post(self):
        request_json = request.json
        genre = genre_service.create(request_json)
        return "", 201
@genres_ns.route("/<int:bid")
class GenresView(Resource):
    def get(self, bid):
        genre = genre_service.get_one(bid)
        return GenreSchema().dump(genre), 200
    def put(self, rid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = rid

        genre_service.update(request_json)
        return "", 204

    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204