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
        email_query = {'match': {'email.keyword': email}}
        response = es.search(index=index, query=email_query)
        email_exists = response['hits']['total']['value']
        if email_exists > 0:
            raise falcon.HTTPBadRequest("Email already exists")
        data = self.convert_to_dict(name, email, age)
        if data is not None:
            es.index(index=index, body=data)

    @staticmethod
    def convert_to_dict(name, email, age):
        return {'name': name, 'email': email, 'age': age}

    @classmethod
    def find_by_email(cls, email):
        model = ElasticsearchModel()
        es = model.get_es_client()
        index = model.get_index()
        search_query = {'match': {'email.keyword': email}}
        search_data = es.search(index=index, query=search_query)['hits']['hits']
        for data in search_data:
            return data['_source']
        else:
            return None