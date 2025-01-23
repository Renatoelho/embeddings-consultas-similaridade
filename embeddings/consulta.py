
from utils.carregar_ambiente import carregar_ambiente
from utils.conectar_elasticsearch import conectar_elasticsearch
from utils.gerar_embedding import gerar_embedding


def consultar_documentos(es, api_key):
    termo = input("Digite o termo para buscar documentos similares: ")
    try:
        k = int(input("Quantos documentos similares deseja retornar? "))
    except ValueError:
        print("Entrada inválida! Retornando o padrão de 5 documentos.")
        k = 5

    embedding = gerar_embedding(termo, api_key)

    consulta = {
        "size": k,
        "_source": ["texto"],
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": embedding}
                }
            }
        }
    }

    resultados = es.search(index="embeddings", body=consulta)

    print("\nResultados encontrados:")
    for doc in resultados['hits']['hits']:
        texto = doc['_source']['texto']
        score = doc['_score']
        print(f"Texto: {texto}, Similaridade: {score}")

def main():
    usuario, senha, api_key = carregar_ambiente()
    es = conectar_elasticsearch(usuario, senha)
    consultar_documentos(es, api_key)


if __name__ == "__main__":
    main()
