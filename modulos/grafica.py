from stop_words import get_stop_words #The words we want to ignore
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def grafica(comentarios,stop_words2):
    stop_words_es = get_stop_words('es') #Spanish StopWords
    stop_words_es.remove('estados')
    stop_words_es.remove('estado')
    stop_words =stop_words_es + stop_words2
    mx_mask = np.array(Image.open('modulos/amlo_2.png'))
    amlo_wc = WordCloud(background_color='white', max_words=500, mask=mx_mask,
          stopwords=stop_words,colormap='inferno')

    amlo_wc.generate(comentarios)

    # display the word cloud
    fig = plt.figure()
    fig.set_figwidth(1.5) # set width
    fig.set_figheight(2) # set height

    plt.imshow(amlo_wc, interpolation='spline36')
    plt.axis('off')
    plt.savefig("myimage.png",dpi=1200)
    #plt.show()