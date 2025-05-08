import requests
import os
import zipfile
import pandas as pd

def download_data(url: str, dest: str) -> None:
    if not os.path.exists(dest):
        os.makedirs(dest)

    response = requests.get(url)
    zip_path = os.path.join(dest, 'data.zip')

    with open(zip_path, 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest)

    os.remove(zip_path)

def load_books_data(file_path: str):
    return pd.read_csv(file_path,
                       encoding="ISO-8859-1",
                       sep=";",
                       header=0,
                       names=['isbn', 'title', 'author'],
                       usecols=['isbn', 'title', 'author'],
                       dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

def load_ratings_data(file_path: str):
    return pd.read_csv(file_path,
                       encoding="ISO-8859-1",
                       sep=";",
                       header=0,
                       names=['user', 'isbn', 'rating'],
                       usecols=['user', 'isbn', 'rating'],
                       dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})

