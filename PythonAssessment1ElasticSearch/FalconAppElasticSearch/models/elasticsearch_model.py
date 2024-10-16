from elasticsearch import Elasticsearch

class ElasticsearchModel:
    def __init__(self):
        self.es = Elasticsearch(
            [{'scheme': 'http', 'host': 'localhost', 'port': 9200}],
            http_auth=('elastic', 'FWs4SNLeyn8wATslm+GX')
        )
        self.index = 'falcon_index'
        self.create_index()  # Create the index when the class is instantiated

    def get_index(self):
        return self.index

    def get_es_client(self):
        return self.es

    def create_index(self):
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index)

    def add_document(self, doc_id, document):
        self.es.index(index=self.index, id=doc_id, body=document)

    def get_document(self, doc_id):
        return self.es.get(index=self.index, id=doc_id)['_source']

    def document_exists(self, doc_id):
        return self.es.exists(index=self.index, id=doc_id)
