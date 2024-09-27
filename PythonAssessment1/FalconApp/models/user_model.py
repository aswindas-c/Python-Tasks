import falcon

from .mongodb_model import MongoDBModel
class User:
    def create_user(self,name,email,age):
        if not name or not email or age is None:
            raise falcon.HTTPBadRequest("Missing required fields : Name, email, and age are required")

        #Validate Email
        if "@" not in email:
            raise falcon.HTTPBadRequest("Invalid email")
        try:
            age = int(age)
        except ValueError:
            raise falcon.HTTPBadRequest("Age should be digit")
        model = MongoDBModel()
        collection = model.get_collection()
        if collection.find_one({'email': email}):
            raise falcon.HTTPBadRequest("Email already exists")
        data = self.convert_to_dict(name, email, age)
        if data is not None:
            collection.insert_one(data)

    @staticmethod
    def convert_to_dict(name, email, age):
        return {'name': name, 'email': email, 'age': age}

    @classmethod
    def find_by_email(cls,email):
        model = MongoDBModel()
        collection = model.get_collection()
        return collection.find_one({'email': email},{'_id': 0})