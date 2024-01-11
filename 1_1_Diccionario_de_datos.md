<center><img src="img/logo.jpg" alt="Data Warehouse Process"></center>

----

<br>

# <center>  DICCIONARIO DE DATOS
---

## Indice

## Índice
- <!-- omit in toc -->
  - [Google Maps](#google-maps)
  - [Business](#business)
  - [Reviews](#reviews)
  - [Yelp](#yelp)
  - [Business Yelp](#business-yelp)
  - [Reviews Yelp](#reviews-yelp)

---

## Google Maps

## Business

## Reviews

---

# Yelp

## Business Yelp

- **id_business:** STRING, identificador único del negocio (restaurante).

- **name:** STRING, nombre del negocio.

- **state:** STRING, estado en el que se encuentra el negocio.

- **latitude:** FLOAT, coordenada de latitud del negocio.

- **longitude:** FLOAT, coordenada de longitud del negocio.

- **categories:** STRING, categorías o tipo de negocio.

- **stars:** FLOAT, clasificación o calificación del negocio.

- **review_count:** INTEGER, cantidad de revisiones o comentarios recibidos por el negocio.

- **hours:** STRING, horarios de atención del negocio.

## Reviews Yelp

- **id_review:** INTEGER, identificador único de la review (reseña).

- **user_id:** STRING, identificador único del usuario que realizó la review (reseña).

- **id_business:** INTEGER, identificador único del negocio al que se refiere la review (reseña).

- **stars:** INTEGER, calificación o puntuación asignada al negocio.

- **text:** STRING, opinión o texto de la review (reseña).

- **date:** DATE, fecha en que se realizó la review (reseña).

- **hour:** TIME, hora en que se realizó la review (reseña).

# Google 

## Business Google

- **name:** STRING, nombre del negocio.

- **gmap_id:** STRING, ID de Google Maps asociado al lugar.

- **latitude:** FLOAT, coordenada de latitud del negocio.

- **longitude:** FLOAT, coordenada de longitud del negocio.

- **avg_rating:** FLOAT, Calificación promedio del lugar.

- **num_of_reviews:** INTEGER, Número de revisiones o reseñas del lugar.

- **hour:** TIME, hora en que se realizó la review (reseña).

- **state:** STRING, estado en el que se encuentra el negocio.

- **category:** STRING, categorías o tipo de negocio.

## Reviews Google

- **user_id:** FLOAT, identificador único del usuario que realizó la review (reseña).

- **name:** STRING, nombre del negocio.

- **rating:** FLOAT, Calificación proporcionada por el usuario.

- **text:** STRING, Comentario o texto asociado a la calificación.

- **gmap_id:** STRING, ID de Google Maps asociado al lugar.

- **hour:** TIME, hora en que se realizó la review (reseña).

- **date:** DATE, fecha en que se realizó la review (reseña).
