import falcon
import json

from FalconApp.models.mongodb_model import MongoDBModel
from FalconApp.models.user_model import User


class MainController:
    def __init__(self):
        self.mongo_db = MongoDBModel()

    @staticmethod
    def on_post(req, resp):

        data = req.media
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')
        user = User().create_user(name,email,age)
        # Write user details to a JSON file
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            users = []

        users.append({'name': name, 'email': email, 'age': age})
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
        resp.media = {'Message': 'User added successfully'}

    @staticmethod
    def on_get(req,resp,email):
        if email is None:
            raise falcon.HTTPBadRequest("Enter email")
        if "@" not in email:
            raise falcon.HTTPBadRequest("Invalid email")

        user = User().find_by_email(email)

        if user:
            resp.media = user
            resp.status = falcon.HTTP_200
        else:
            resp.media = {'Message': 'User not exist'}
            resp.status = falcon.HTTP_404