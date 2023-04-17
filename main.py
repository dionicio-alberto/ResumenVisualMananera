import modulos.urls as url
import modulos.discurso as ds
import modulos.grafica as gr
import modulos.subir_twitter as tw
from os import remove
from stop_words import get_stop_words #The words we want to ignore

stop_words_es = get_stop_words('es') #Spanish StopWords
stop_words_es.remove('estados')
stop_words_es.remove('estado')

    
stop_words2 = ["pues", "bueno", "si", "año", "mil", "millones","va","aqui","ahora","pesos", "ciento", "El", "En","PRESIDENTE",
              "ANDRÉS", "MANUEL", "LÓPEZ", "OBRADOR","Entonces",'tres','así','voy','ver','además','voy','llego','aunque','puede',
              "toda","aquí",'vamos','dos','ahí','cómo','Pregunta','caso',
              'INTERVENCIóN','INTERLOCUTOR','INTERLOCUTORA','inaudible',
              'gracias','comentarle']
stop_words =stop_words_es + stop_words2

if __name__ == '__main__':
    a = url.url_dia()
    data = ds.obtencion_comentarios(a)
    b = ds.comentarios_presidente(data)
    c = gr.grafica_presidente(b,stop_words)
    
    b1 = ds.comentarios_pyi(data)
    d = gr.grafica_preguntas(b1,stop_words)
    
    e = tw.subir_imagen(c)
    f = tw.enviar_tweet_presidente(e)
    
    g = tw.subir_imagen(d)
    h = tw.enviar_tweet_presidente(g)
    remove(d)
    remove(c)
