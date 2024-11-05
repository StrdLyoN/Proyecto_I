import pandas as pd
import streamlit as st

df = pd.read_csv('./music_project_en.csv')

print(df.head(10))
print()
print(df.info())
print()
print(df.columns)
print()

print('Bucle en los encabezados poniendo todo en minúsculas')
df.columns = [col.lower() for col in df.columns]
print(df.columns)
print()

print('Bucle en los encabezados eliminando los espacios')
df.columns = df.columns.str.strip() 
print(df.columns)
print()

print('Cambiar el nombre de la columna')
columns_new = {'userid': 'user_id'}
df.rename(columns = columns_new, inplace = True)
print(df.columns)
print()

print('Calcular el número de valores ausentes')
print(df.isna().sum())
print()

print('Bucle en los encabezados reemplazando los valores ausentes con unknown')
columns_to_replace = ['track', 'artist', 'genre']
for col in columns_to_replace :
    df[col].fillna('unknow',inplace=True)
print()

print('Contar valores ausentes')
print(df.isna().sum())
print()

print('Contar duplicados explícitos')
print(df.duplicated().sum())
print()

print('Eliminar duplicados explícitos')
df = df.drop_duplicates()

print('Comprobar de nuevo si hay duplicados')
print(df.duplicated().sum())
print()

print('Inspeccionar los nombres de géneros únicos')
print(df['genre'].unique())
print()

print('Función para reemplazar duplicados implícitos')
def replace_wrong_genres(wrong_genres, correct_genre):
    columns = df['genre']
    for wrong_genre in wrong_genres:
        columns.replace(wrong_genre, correct_genre,inplace=True)
    return columns
print()

print('Eliminar duplicados implícitos')
duplicates = ['hip','hop','hip-hop']
genre = 'hiphop'
df['genre'] = replace_wrong_genres(duplicates, genre) 
print()

print(df)
print()

print('Contar las canciones reproducidas en cada ciudad')
print(df.groupby(by='city')['track'].count())
print()

print('Calcular las canciones reproducidas en cada uno de los tres días')
print(df.groupby(by='day')['track'].count())
print()

print('Declara la función number_tracks() con dos parámetros: day= y city=.')
def number_tracks(day, city):
    filtered_by_day = df[df['day'] == day]
    filtered_by_city = filtered_by_day[filtered_by_day['city'] == city]
    tracks_played = filtered_by_city['user_id'].count()
    return tracks_played
print()

print('El número de canciones reproducidas en Springfield el lunes')
print(number_tracks("Monday", "Springfield"))
print()

print('El número de canciones reproducidas en Shelbyville el lunes')
print(number_tracks("Monday","Shelbyville"))
print()

print('El número de canciones reproducidas en Springfield el miércoles')
print(number_tracks("Wednesday", "Springfield"))
print()

print('El número de canciones reproducidas en Shelbyville el miércoles')
print(number_tracks("Wednesday", "Shelbyville") )
print()

print('El número de canciones reproducidas en Springfield el viernes')
print(number_tracks("Friday", "Springfield"))
print()

print('El número de canciones reproducidas en Shelbyville el viernes')
print(number_tracks("Friday", "Shelbyville"))
print()

print('')
print()
print()