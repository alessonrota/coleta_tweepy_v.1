from TwitterAPI import TwitterAPI
import pandas as pd

# Credenciais da API do Twitter
consumer_key = 'aqui'
consumer_secret = 'aqui'
access_token_key = 'aqui'
access_token_secret = 'aqui'

# Configurar a API do Twitter
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# Termo de busca
termo_de_busca = 'TERMO DE BUSCA'

# Parâmetros da busca
params = {
    'q': termo_de_busca,
    'count': 100,  # Número de tweets a serem retornados (máximo: 100)
    'lang': 'pt',  # Idioma dos tweets a serem retornados
    'result_type': 'recent'  # Tipo de resultado (recente, popular ou misturado)
}

# Fazer a requisição dos tweets
r = api.request('search/tweets', params)

# Verificar se a requisição foi bem-sucedida
if r.status_code == 200:
    # Criar uma lista para armazenar os dados dos tweets
    tweets_data = []

    # Processar os tweets retornados
    for tweet in r:
        # Verificar se o tweet contém uma mídia de tipo "foto"
        if 'media' in tweet['entities']:
            for media in tweet['entities']['media']:
                if media['type'] == 'photo':
                    # Extrair o URL da imagem
                    image_url = media['media_url_https']
                    # Adicionar os dados do tweet e o URL da imagem à lista
                    tweet_data = {
                        'Texto': tweet.get('full_text', tweet['text']),
                        'ID': tweet['id'],
                        'Data de criação': tweet['created_at'],
                        'Usuário': tweet['user']['screen_name'],
                        'Nome': tweet['user']['name'],
                        'Localização': tweet['user']['location'],
                        'Seguidores': tweet['user']['followers_count'],
                        'Amigos': tweet['user']['friends_count'],
                        'Retweets': tweet['retweet_count'],
                        'Curtidas': tweet['favorite_count'],
                        'Língua': tweet['lang'],
                        'Coordenadas': tweet['coordinates'],
                        'Lugar': tweet['place'],
                        'Possível idioma': tweet['lang'],
                        'Possível idioma do dispositivo': tweet['source'].split('>')[1].split('<')[0] if tweet['source'] else None,
                        'Possível aplicativo': tweet['source'].split('rel="nofollow">')[1].split('</a>')[0] if tweet['source'] else None,
                        'Hashtags': [hashtag['text'] for hashtag in tweet['entities']['hashtags']],
                        'Menções de usuário': [user_mention['screen_name'] for user_mention in tweet['entities']['user_mentions']],
                        'Links': [url['expanded_url'] for url in tweet['entities']['urls']],
                        'URL da imagem': image_url,
                        'URL do tweet': f"https://twitter.com/{tweet['user']['screen_name']}/status/{tweet['id_str']}"
                    }
                    # Adicionar os dados do tweet à lista
                    tweets_data.append(tweet_data)
        else:
            # Adicionar os dados do tweet à lista sem URL da imagem
            tweet_data = {
                'Texto': tweet.get('full_text', tweet['text']),
                'ID': tweet['id'],
                'Data de criação': tweet['created_at'],
                'Usuário': tweet['user']['screen_name'],
                'Nome': tweet['user']['name'],
                'Localização': tweet['user']['location'],
                'Seguidores': tweet['user']['followers_count'],
                'Amigos': tweet['user']['friends_count'],
                'Retweets': tweet['retweet_count'],
                'Curtidas': tweet['favorite_count'],
                'Língua': tweet['lang'],
                'Coordenadas': tweet['coordinates'],
                'Lugar': tweet['place'],
                'Possível idioma': tweet['lang'],
                'Possível idioma do dispositivo': tweet['source'].split('>')[1].split('<')[0] if tweet['source'] else None,
                'Possível aplicativo': tweet['source'].split('rel="nofollow">')[1].split('</a>')[0] if tweet['source'] else None,
                'Hashtags': [hashtag['text'] for hashtag in tweet['entities']['hashtags']],
                'Menções de usuário': [user_mention['screen_name'] for user_mention in tweet['entities']['user_mentions']],
                'Links': [url['expanded_url'] for url in tweet['entities']['urls']],
                'URL da imagem': None,
                'URL do tweet': f"https://twitter.com/{tweet['user']['screen_name']}/status/{tweet['id_str']}"
            }
            # Adicionar os dados do tweet à lista
            tweets_data.append(tweet_data)

    # Criar o DataFrame com os dados dos tweets
    df_tweets = pd.DataFrame(tweets_data)

    # Salvar o DataFrame como arquivo CSV
    df_tweets.to_csv('tweets.csv', index=False)
else:
    print(f'Erro na requisição: {r.status_code}')
