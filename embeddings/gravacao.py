
from utils.carregar_ambiente import carregar_ambiente
from utils.conectar_elasticsearch import conectar_elasticsearch
from utils.gerar_embedding import gerar_embedding

def gravar_documento(es, api_key):
    texto = input("Digite o texto para ser gravado: ")
    embedding = gerar_embedding(texto, api_key)

    documento = {
        "texto": texto,
        "embedding": embedding
    }

    es.index(index="embeddings", document=documento)
    print("Documento armazenado com sucesso!")

def gravar_lista_documentos(es, api_key):
    arquivo = input("Digite o nome do arquivo com os textos (um por linha): ")

    try:
        with open(arquivo, "r") as file:
            linhas = file.readlines()

        for texto in linhas:
            texto = texto.strip()
            if texto:
                embedding = gerar_embedding(texto, api_key)
                documento = {
                    "texto": texto,
                    "embedding": embedding
                }
                es.index(index="embeddings", document=documento)
        print("Todos os documentos foram armazenados com sucesso!")

    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado!")


def main():
    usuario, senha, api_key = carregar_ambiente()
    es = conectar_elasticsearch(usuario, senha)

    print("\nEscolha uma opção:")
    print("1. Gravar um único documento")
    print("2. Gravar uma lista de documentos")
    print("3. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        gravar_documento(es, api_key)
    elif opcao == "2":
        gravar_lista_documentos(es, api_key)
    else:
        print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
