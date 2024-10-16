from elasticsearch import Elasticsearch

class ElasticsearchModel:
    def __init__(self):
        self.es = Elasticsearch(
            [{'scheme': 'http', 'host': 'localhost', 'port': 9200}],
            http_auth=('elastic', 'FWs4SNLeyn8wATslm+GX')
        )
        self.index = 'users'
        self.create_index()

    def get_index(self):
        return self.index

    def get_es_client(self):
        return self.es

    def create_index(self):
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index)
