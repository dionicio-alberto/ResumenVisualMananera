
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def grafica_presidente(comentarios,stop_words):
    mx_mask = np.array(Image.open('modulos/amlo_2.png'))
    amlo_wc = WordCloud(background_color='white', max_words=500, mask=mx_mask,
          stopwords=stop_words,colormap='inferno')

    amlo_wc.generate(comentarios)

    # display the word cloud
    fig = plt.figure()
    fig.set_figwidth(0.75) # set width
    fig.set_figheight(1) # set height

    plt.imshow(amlo_wc, interpolation='spline36')
    plt.axis('off')
    nombre = "myimage.png"
    plt.savefig(nombre,dpi=1200)
    #plt.show()
    return nombre
    

def grafica_preguntas(comentarios,stop_words):
    mx_mask = np.array(Image.open('modulos/ask_1.png'))
    amlo_wc = WordCloud(background_color='white', max_words=500, mask=mx_mask,
          stopwords=stop_words,colormap='inferno')

    amlo_wc.generate(comentarios)

    # display the word cloud
    fig = plt.figure()
    fig.set_figwidth(0.75) # set width
    fig.set_figheight(1) # set height

    plt.imshow(amlo_wc, interpolation='spline36')
    plt.axis('off')
    nombre = "myimage1.png"
    plt.savefig(nombre,dpi=1200)
    #plt.show()
    return nombre