
# <h1 align=center> **PROYECTO INDIVIDUAL -  DTS06** </h1>

<h1 align=center> Data Engineering </h1>

**¡Hola, bienvenido!** mi nombre es *Franco Soto* y este es el mi proyecto individual, que forma parte de Henry Labs. 
## Objectivos del proyecto
+ Aplicar las **transformaciones** a los datasets
+ Realizar el **desarrollo de la API**
+ Hacer el **deployment** de la API
+ Un **video** de 5 minutos que sintetice el trabajo realizado

## Contextos
Para realizar este trabajo se utlizaron los datasets de las plataformas de Amazon Prime, Netflix, Disney Plus y Hulu. De los cuales se tenian que realizar las consignas del proyecto previamente mencionadas
<div>
<img src="https://i0.wp.com/codigoespagueti.com/wp-content/uploads/2020/07/Amazon-Prime-Video-Perfiles-Netflix-1.jpg?resize=1200%2C720&quality=80&ssl=1" width="230px">
<img src="https://i0.wp.com/frikispan.com/wp-content/uploads/2014/12/netflix-logo.png?resize=1200%2C720" width="230px">
<img src="https://tec.com.pe/wp-content/uploads/2021/11/logo-de-disney-plus-scaled-1.jpeg" width="230px">
<img src="https://www.streamingdigitally.com/wp-content/uploads/2022/12/hulu-featured-1-jpg-1200x720.webp" width="230px">

</div>

## Flujo de Trabajo

### Transformación:
Primero se importan los [datasets](/Datasets/) en Pandas, después se hacen las transformaciones que nos pideron en la consigna (no se hizo la limpieza ya que **solo** nos pedian esas 5 modificaciones a los datos, aqui el archivo [readme](https://github.com/HX-FNegrete/PI01-Data-Engineering/blob/main/README.md) del proyecto) y por último se exporta el dataframe como un csv para utilizar en la elaboración de la API.

### Desarrollo de la API:
Para la cración de la API se uso el archivo [main.py](/main.py), en donde se configuraron funciones para la creación de las consultas. En el script de la API se instancia de manera local, la API con tiene el [CSV](/plataformas.csv), previamente transformado, respondiendo las siguientes consultas:
+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
+ Película que más duró según año, plataforma y tipo de duración
+ Cantidad de series y películas por rating

Para revisar las consultas en la API, levantamos el Uvicorn de manera local desde la terminal con el comando: ***uvicorn main:app --reload***  para verificamos que todas las consultas funcionen

### Deployment:
Para hacer el deploy se utlizó el servicio de nube de [Deta](https://docs.deta.sh/docs/home/) la cual por el momento que hago este proyecto es gratuita. Se seguio casi a pie de la letra la documentación de FastAPI para hacer despliegues por Deta ([documentación](https://fastapi.tiangolo.com/deployment/deta/)). Con ello se logro presentar la API previamente desarrollada en FastAPI con el dominio de Deta ([ver](https://cbxopx.deta.dev/docs))


## Tecnologías Utilizadas
* [Pandas](https://pandas.pydata.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Deta](https://www.deta.sh/)

## Video en YouTube
Acá el video en YouTube explicando mi proyecto prevemente: (Haga click en la imagen)

[<img src=https://www.cinco8.com/wp-content/uploads/2020/08/404.png width = "200px">](https://www.youtube.com/watch?v=sqiuSpKkDHk)