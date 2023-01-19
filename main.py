#Importación de las librerías necesarias
from fastapi import FastAPI
import pandas as pd

#Colocar un título
app = FastAPI(title='Proyecto Individual')

#Crear la función para visualizar las primeras palabras del API
@app.get('/')
async def index():
    return {'Bienvenidos a mi primer experimento con FastAPI'}


#Función que devuelve la cantidad de veces que aoarece una keyword en el título de peliculas/series, por plataforma
@app.get('/get_word_count/({platform}, {keywords})')
async def get_word_count(plataform:str,keywords:str):
    #Se llama el csv por medio de https
    global df
    df = pd.read_csv('plataformas.csv') 
    #Selecionamos la primea letra y la ponemos en minúscula para segmentar por plataformas
    lower = plataform[:1].lower()
    #Se hace una máscara para trabajar con las columnas competentes
    mascara = df[['id','title']]
    #Se filtra según plataformas y por la keyword
    answer = mascara[mascara['id'].str.startswith(lower) & mascara['title'].str.contains(keywords)]
    #Se cuentan las filas
    return len(answer.index)



#Función que devuelve la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get('/get_score_count/({platform},{greater_than},{year})')
async def get_score_count(plataform:str,greater_than:int,year:int):
    #Se llama el csv por medio de https
    global df
    df = pd.read_csv('plataformas.csv') 
    #Selecionamos la primea letra y la ponemos en minúscula para segmentar por plataformas
    lower = plataform[:1].lower()
    #Se hace una máscara para trabajar con las columnas competentes
    mascara = df[['id','release_year','score','type']]
    #Se filtra según plataformas, puntaje mayor a y por el año
    answer = mascara[(mascara['id'].str.startswith(lower)) & (mascara['release_year'] == year) & (mascara['score']>greater_than) & (mascara['type'] == 'movie')]
    #Se cuentan las filas
    return len(answer.index)



#Función que devuelve la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get('/get_second_score/({plataform})')
async def get_second_score(plataform:str):
    #Se llama el csv por medio de https
    global df
    df = pd.read_csv('plataformas.csv') 
    #Selecionamos la primea letra y la ponemos en minúscula para segmentar por plataformas
    lower = plataform[:1].lower()
    #Se hace una máscara para trabajar con la columna competente
    mascara = df[['id','title','score','type']]
    #Se filtra según plataformas y por película
    filtro = mascara[(mascara['id'].str.startswith(lower)) & (mascara['type'] == 'movie')] 
    #Se orderna según orden alfabético y por mayor score
    answer = filtro.sort_values(by = ['score','title'], ascending=[False, True])
    #Se seleciona la segunda fila de la columna de "title"
    return answer.iloc[1,1]



#Función que devuelve la película que más duró según año, plataforma y tipo de duración
@app.get('/get_longest/({plataform},{duration_type},{year})')
async def get_longest(plataform:str,duration_type:str,year:int):
    #Se llama el csv por medio de https
    global df
    df = pd.read_csv('plataformas.csv') 
    #Selecionamos la primea letra y la ponemos en minúscula para segmentar por plataformas
    lower = plataform[:1].lower()
    #Se hace una máscara para trabajar con las columnas competentes
    mascara = df[['id','title','duration_int','duration_type','release_year']]
    #Se filtra según plataformas y por película
    filtro = mascara[(mascara['id'].str.startswith(lower)) & (mascara['duration_type'] == duration_type) & (mascara['release_year'] == year)]
    #Se orderna según la duracion de la película o serie 
    answer = filtro.sort_values('duration_int',ascending = False)
    #Se seleciona la primera fila de la columna de "title"
    return answer.iloc[0,1]



#Función que devuelve la cantidad de series y películas por rating
@app.get('/get_rating_count/({rating})')
async def get_rating_count(rating:str):
    #Se llama el csv por medio de https
    global df
    df = pd.read_csv('plataformas.csv') 
    #Se hace una mascara para trabajar con la columna competente
    mascara = df[['rating']]
    #Se filtra según el rating 
    answer = mascara[(mascara['rating'] == rating)]
    #Se cuentan las filas
    return len(answer.index)