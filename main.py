import modulos.urls as url
import modulos.discurso as ds
import modulos.grafica as gr


stop_words2 = ["pues", "bueno", "si", "año", "mil", "millones","va","aqui","ahora","pesos", "ciento", "El", "En","PRESIDENTE",
              "ANDRÉS", "MANUEL", "LÓPEZ", "OBRADOR","Entonces",'tres','así','voy','ver','además','voy','llego','aunque','puede',
              "toda","aquí",'vamos','dos','ahí','cómo','Pregunta','caso']

if __name__ == '__main__':
    a = url.url_dia()
    print(a)
    b = ds.comentarios_presidente(a)
    gr.grafica(b,stop_words2)
    print('La imagen se obtuvo con exito')
