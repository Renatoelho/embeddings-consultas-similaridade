import os

from dotenv import load_dotenv


def carregar_ambiente():
    load_dotenv()
    usuario_elastic = os.getenv("USUARIO_ELASTIC")
    senha_elastic = os.getenv("SENHA_ELASTIC")
    api_key_openai = os.getenv("API_KEY_OPENAI")
    return usuario_elastic, senha_elastic, api_key_openai
