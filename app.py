from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import random

imgs = [

]

class Image(Resource):
    def get(self, id):
        for img in imgs:
            if (id == img["id"]):
                return img, 200
        return "Image not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("data")
        parser.add_argument("name")

        args = parser.parse_args()

        for img in imgs:
            if (id == img["id"]):
                img["data"] = args["data"]
                img["name"] = args["name"]
                return img, 200

        img = {
            "id"   : id,
            "data" : args["data"],
            "name"  : args["name"]
        }
        imgs.append(img)
        return img, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("data")
        parser.add_argument("name")

        args = parser.parse_args()

        for img in imgs:
            if (id == img["id"]):
                return "Image with Id {} already exists".format(id), 400

        img = {
            "id"   : id,
            "data" : args["data"],
            "name"  : args["name"]
        }
        imgs.append(img)
        return img, 201

    def delete(self, id):
        self.imgs = [img for img in imgs if img["id"] != id]
        return "Image with Id {} is deleted.".format(id), 200

app = Flask(__name__)
api = Api(app)

api.add_resource(Image, "/api/<int:id>")
app.run(debug=True)