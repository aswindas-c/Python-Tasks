import falcon

from FalconApp.models.mongodb_model import MongoDBModel

class GetRoute:
    def __init__(self):
        self.mongo_db = MongoDBModel()

    def on_get(self,req,resp,email):
        if email is None:
            raise falcon.HTTPBadRequest("Enter email")
        if "@" not in email:
            raise falcon.HTTPBadRequest("Invalid email")
        user = self.mongo_db.collection.find_one({'email': email},{'_id': 0})
        if user:
            resp.media = user
            resp.status = falcon.HTTP_200
        else:
            resp.media = {'Message': 'User not exist'}
            resp.status = falcon.HTTP_404