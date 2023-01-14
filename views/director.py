from flask import request
from flask_restx import Resource, Namespace
from decorators import auth_required, admin_required
from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace("directors")
@directors_ns.route("/")
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all()
        return DirectorSchema(many=True).dump(directors), 200

    @admin_required
    def post(self):
        request_json = request.json
        director = director_service.create(request_json)
        return "", 201

@directors_ns.route("/<int:bid")
class DirectorView(Resource):
    @auth_required
    def get(self, bid):
        directors = director_service.get_one(bid)
        return DirectorSchema().dump(directors), 200

    @admin_required
    def put(self, rid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = rid
        director_service.update(request_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        director_service.delete(rid)
        return "", 204
