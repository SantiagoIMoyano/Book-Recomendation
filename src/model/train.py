import os
import pickle

from src.model.architecture import build_model
from src.data.loader import download_data, load_books_data, load_ratings_data
from src.data.preprocess import preprocess_data


URL = "https://cdn.freecodecamp.org/project-data/books/book-crossings.zip"
DEST = "data/raw"
BOOKS_CSV = "BX-Books.csv"
RATINGS_CSV = "BX-Book-Ratings.csv"

def train_model(data_url, dest_dir, books_filename, ratings_filename, min_user_count, min_book_count, n_neighbors):
    download_data(data_url, dest_dir)

    books_path = os.path.join(dest_dir, books_filename)
    ratings_path = os.path.join(dest_dir, ratings_filename)

    df_books = load_books_data(books_path)
    df_ratings = load_ratings_data(ratings_path)

    df_books_filtered, df_ratings_filtered = preprocess_data(df_books, df_ratings, min_book_count, min_user_count)

    ratings_pivot = df_ratings_filtered.pivot_table(index='isbn', columns='user', values='rating').fillna(0)

    model = build_model(n_neighbors=n_neighbors)
    model.fit(ratings_pivot.values)

    os.makedirs("models", exist_ok=True)
    model_path = "models/nearest_neighbors_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    train_model(URL, DEST, BOOKS_CSV, RATINGS_CSV, 200, 100, 6)
    




