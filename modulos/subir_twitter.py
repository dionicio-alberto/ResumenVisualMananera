from io import BytesIO
from PIL import Image
import tweepy
from modulos.keys import *
from datetime import date
from datetime import datetime

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage


def subir_imagen(a):
    img = Image.open(a)

    # Do something to the image...

    # Save image in-memory
    b = BytesIO()
    img.save(b, "PNG")
    b.seek(0)

    # Setup Tweepy API
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(key=access_token, secret=access_token_secret)
    api = tweepy.API(auth)
        # Upload media to Twitter APIv1.1
    ret = api.media_upload(filename="dummy_string", file=b)
    return(ret.media_id_string)

def enviar_tweet_presidente(id):
    client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret)
    texto = f'''Estas fueron los temas de los que hablo el presidente en la mañanera del dia de hoy {current_date_format(datetime.now())}
#Mexico #Presidente #Mañanera #AMLO #Conferencia #Preguntas #Resumen #Visual'''
    response = client.create_tweet(media_ids=[id],text=texto)
    print(f"https://twitter.com/user/status/{response.data['id']}")
    
def enviar_tweet_preguntas(id):
    client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret)
    texto = f'''Estos fueron los temas sobre los cuales fue cuestionado el presidente @lopezobrador_ por los periodistas el dia de hoy {current_date_format(datetime.now())}
#Mexico #Presidente #Mañanera #AMLO #Conferencia #Preguntas #Resumen #Visual'''
    response = client.create_tweet(media_ids=[id],text=texto)
    print(f"https://twitter.com/user/status/{response.data['id']}")