
import openai


def gerar_embedding(texto, api_key):
    openai.api_key = api_key
    resposta = openai.Embedding.create(
        input=texto,
        model="text-embedding-ada-002"
    )
    return resposta["data"][0]["embedding"]
