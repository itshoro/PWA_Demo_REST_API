from flask import Flask
from flask_restful import Api, Resource, reqparse

imgs = [
    {
        "id"   : 42,
        "data" : "Some Data",
        "type" : ["Test"],
        "url"  : "127.0.0.1"
    }
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
        parser.add_argument("type")
        parser.add_argument("url")

        args = parser.parse_args()

        for img in imgs:
            if (id == img["id"]):
                img["data"] = args["data"]
                img["type"] = args["type"]
                img["url"] = args["url"]
                return img, 200

        img = {
            "id"   : id,
            "data" : args["data"],
            "type" : args["type"],
            "url"  : args["url"]
        }
        imgs.append(img)
        return img, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("data")
        parser.add_argument("type")
        parser.add_argument("url")

        args = parser.parse_args()

        for img in imgs:
            if (id == img["id"]):
                return "Image with Id {} already exists".format(id), 400

        img = {
            "id"   : id,
            "data" : args["data"],
            "type" : args["type"],
            "url"  : args["url"]
        }
        imgs.append(img)
        return img, 201

    def delete(self, id):
        self.imgs = [img for img in imgs if img["id"] != id]
        return "Image with Id {} is deleted.".format(id), 200

app = Flask(__name__)
api = Api(app)

api.add_resource(Image, "/imgs/<int:id>")
app.run()