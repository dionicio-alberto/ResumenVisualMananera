import requests as rq
from bs4 import BeautifulSoup


def obtencion_comentarios(url):
    website_url= rq.get(url).text
    soup = BeautifulSoup(website_url,'html.parser')
    data = [element.text for element in soup.find_all('p')]
    return(data)

def comentarios_presidente(data):
    comentarios_amlo = []
    guardar_amlo = False
    for element in data: #Para todos los elementos de la lista
        if element[0:5]==element[0:5].upper(): # Verificar si empieza con mayuscula
           
            if element[0:5]=='PRESI': #Si empieza a hablar amlo 
                guardar_amlo = True
            else:
                guardar_amlo = False

        if guardar_amlo: comentarios_amlo.append(element)

    comentarios_amlo = str(comentarios_amlo)
    return(comentarios_amlo)

def comentarios_pyi(data):
    comentarios_pyi = []
    guardar_otros = False, False
    for element in data: #Para todos los elementos de la lista
        
        if element[0:5]==element[0:5].upper(): # Verificar si empieza con mayuscula
           
            if element[0:5]=='PREGU' or element[0:5]=='INTER': #Si empieza a hablar amlo 
                guardar_otros = True
            else:
                guardar_otros = False
            
        if guardar_otros: comentarios_pyi.append(element)

    comentarios_pyi = str(comentarios_pyi)
    return(comentarios_pyi)