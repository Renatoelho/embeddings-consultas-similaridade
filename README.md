# Criando um Gerenciador de Contexto com Embeddings e Elasticsearch

Neste vídeo, você aprenderá como trabalhar com **embeddings** e criar um gerenciador de contexto para suas aplicações de **Inteligência Artificial**. Vou mostrar como converter textos simples em representações matemáticas usando a **API da OpenAI**, armazená-los no **Elasticsearch** e consultá-los de forma eficiente para compor **prompts** ou gerar insights. Além disso, explicarei como configurar o ambiente de desenvolvimento em **Python**, incluindo o uso de variáveis de ambiente e bibliotecas essenciais, como openia, dotenv e Elasticsearch. Você verá como implementar a gravação de documentos (individuais e em lote), configurar corretamente o mapeamento do Elasticsearch para armazenar embeddings e realizar consultas por **similaridade**. Este vídeo é ideal para quem deseja explorar aplicações práticas de embeddings e otimizar fluxos de trabalho de IA.

<!--
https://www.youtube.com/@renato-coelho
-->

## Apresentação em Vídeo

<p align="center">
  <a href="https://youtu.be/5AHtITcSCKw" target="_blank"><img src="imagens/thumbnail/thumbnail-embeddings-01.png" alt="Vídeo de apresentação"></a>
</p>

![YouTube Video Views](https://img.shields.io/youtube/views/5AHtITcSCKw) ![YouTube Video Likes](https://img.shields.io/youtube/likes/5AHtITcSCKw)


### Requisitos

+ ![Python](https://img.shields.io/badge/Python-3.9%2B-E3E3E3)

+ ![OpenAI](https://img.shields.io/badge/OpenAI-API-E3E3E3)

+ ![Docker](https://img.shields.io/badge/Docker-27.4.1-E3E3E3)

+ ![Docker-compose](https://img.shields.io/badge/Docker--compose-1.25.0-E3E3E3)

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E3E3E3)

## Deploy da aplicação

### Clonando o repositório

```bash
git clone https://github.com/Renatoelho/embeddings-consultas-similaridade.git embeddings-consultas-similaridade
```

### Configurando o Elasticsearch e o ambiente Python

+ Acesse o diretório do projeto:

```bash
cd embeddings-consultas-similaridade/
```

+ Execute o comando para subir o Elasticsearch:

```bash
docker compose -p embeddings -f docker-compose.yaml up -d
```

> ***OBS.:*** Para acessar o Kibana (Interface de gerenciamento do Elasticsearch), utilize o endereço: [http://localhost:5601](http://localhost:5601) e as credenciais estão no arquivo: [docker-compose.yaml](docker-compose.yaml).

+ Configure o ambiente Python:

```bash
cd embeddings/
```

```bash
python3.9 -m venv .venv \
  source .venv/bin/activate \
  pip install -U pip setuptools wheel --no-cache-dir \
  pip install -r requirements.txt --no-cache-dir \
  export PYTHONPATH=$(pwd)/utils
```

+ Crie o arquivo `.env` com a seguinte estrutura dentro do diretório `embeddings`:

```text
USUARIO_ELASTIC=elastic
SENHA_ELASTIC=dRWbd49Fg9QSMpdeg
API_KEY_OPENAI=<Sua Chave da OpenIA>
```

# Referências

Vector embeddings, **OpenIA Platform.** Disponível em: <https://platform.openai.com/docs/guides/embeddings/>. Acesso em: 20 jan. 2025.

Dense vector field type, **elastic.** Disponível em: <https://www.elastic.co/guide/en/elasticsearch/reference/current/dense-vector.html>. Acesso em: 20 jan. 2025.

What are word embeddings?, **elastic.** Disponível em: <https://www.elastic.co/what-is/word-embedding>. Acesso em: 20 jan. 2025.
