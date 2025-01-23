
from elasticsearch import Elasticsearch


def conectar_elasticsearch(usuario, senha):
    return Elasticsearch(
        "http://localhost:9200",
        basic_auth=(usuario, senha)
    )
