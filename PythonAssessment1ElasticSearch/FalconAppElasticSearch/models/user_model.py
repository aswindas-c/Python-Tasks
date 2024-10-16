import falcon
import elasticsearch
from .elasticsearch_model import ElasticsearchModel
class User:
    def create_user(self, name, email, age):
        if not name or not email or age is None:
            raise falcon.HTTPBadRequest("Missing required fields : Name, email, and age are required")

        # Validate Email
        if "@" not in email:
            raise falcon.HTTPBadRequest("Invalid email")
        try:
            age = int(age)
        except ValueError:
            raise falcon.HTTPBadRequest("Age should be digit")
        model = ElasticsearchModel()
        es = model.get_es_client()
        index = model.get_index()
        if es.exists(index=index, id=email):
            raise falcon.HTTPBadRequest("Email already exists")
        data = self.convert_to_dict(name, email, age)
        if data is not None:
            es.index(index=index, id=email, body=data)

    @staticmethod
    def convert_to_dict(name, email, age):
        return {'name': name, 'email': email, 'age': age}

    @classmethod
    def find_by_email(cls, email):
        try:
            model = ElasticsearchModel()
            es = model.get_es_client()
            index = model.get_index()
            return es.get(index=index, id=email)['_source']
        except elasticsearch.NotFoundError:
            return None