import falcon
import json

from FalconApp.models.mongodb_model import MongoDBModel
from FalconApp.models.user_model import User


class PostRoute:
    def __init__(self):
        self.mongo_db = MongoDBModel()

    def on_post(self, req, resp):

        data = req.media
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')

        #Check for null value in input json
        if not name or not email or age is None:
            raise falcon.HTTPBadRequest('Missing required fields : Name, email, and age are required')

        #Validate Email
        if "@" not in email:
            raise falcon.HTTPBadRequest("Invalid email")

        # Check if email already exists in the database
        if self.mongo_db.collection.find_one({'email': email}):
            raise falcon.HTTPBadRequest("Email already exists")

        #Check if age is a digit
        try:
            age = int(age)
        except ValueError:
            raise falcon.HTTPBadRequest("Age should be digit")
        try:
            user = User(name,email,age)
            self.mongo_db.collection.insert_one(user.add_to_db())
            # Write user details to a JSON file
            try:
                with open('users.json', 'r') as f:
                    users = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                users = []

            users.append({'name': name, 'email': email, 'age': age})
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=4)
        except Exception as e:
            print(f"Exception : {e}")

        resp.media = {'Message': 'User added successfully'}