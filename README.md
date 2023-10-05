# coleta_tweepy_v.1

Código para coleta de Tweets

Coletando Tweets usando a API v1.1 do Twitter com Python
Introdução:

Este tutorial mostrará como coletar tweets usando a API v1.1 do Twitter com a ajuda da biblioteca TwitterAPI em Python. Os tweets coletados serão salvos em um arquivo CSV.
Pré-requisitos:

    Uma conta no portal de desenvolvedores do Twitter.
    Chaves de acesso da API do Twitter (Consumer Key, Consumer Secret, Access Token, Access Token Secret).
    Python instalado em sua máquina.
    Bibliotecas TwitterAPI e pandas instaladas. Você pode instalá-las usando pip:

    bash

    pip install TwitterAPI pandas

Passos:
1. Configuração das Credenciais:

Substitua os placeholders 'aqui' pelas suas chaves de acesso da API do Twitter.

python

consumer_key = 'SUA_CONSUMER_KEY'
consumer_secret = 'SUA_CONSUMER_SECRET'
access_token_key = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

2. Configuração da API:

Inicialize a API do Twitter usando suas credenciais.

python

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

3. Definindo o Termo de Busca:

Substitua 'TERMO DE BUSCA' pelo termo ou hashtag que você deseja pesquisar.

python

termo_de_busca = 'SEU_TERMO_DE_BUSCA'

4. Definindo Parâmetros da Busca:

Estes parâmetros determinam como a busca será realizada. Você pode ajustar o número de tweets retornados, o idioma e o tipo de resultado.

python

params = {
    ...
}

5. Fazendo a Requisição:

Solicite os tweets usando a API.

python

r = api.request('search/tweets', params)

6. Processando os Tweets:

O código verifica se a requisição foi bem-sucedida e, em seguida, processa cada tweet retornado. Ele extrai informações relevantes, como texto, ID, data de criação, informações do usuário, hashtags, menções, links e, se disponível, a URL da imagem associada ao tweet.
7. Salvando os Dados:

Os tweets processados são salvos em um DataFrame do pandas e, em seguida, exportados para um arquivo CSV.

python

df_tweets.to_csv('tweets.csv', index=False)

Conclusão:
