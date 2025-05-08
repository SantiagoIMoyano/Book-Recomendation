import pickle
import os

from src.data.loader import load_books_data, load_ratings_data
from src.data.preprocess import preprocess_data

MODEL_PATH = "models/nearest_neighbors_model.pkl"
RAW_DIR = "data/raw"
BOOKS_CSV = "BX-Books.csv"
RATINGS_CSV = "BX-Book-Ratings.csv"

def load_artifacts(model_path, raw_dir, books_file, ratings_file, min_book_count, min_user_count):
    with open(model_path, "rb") as f:
        nn_model = pickle.load(f)
    
    books_path   = os.path.join(raw_dir, books_file)
    ratings_path = os.path.join(raw_dir, ratings_file)
    df_books   = load_books_data(books_path)
    df_ratings = load_ratings_data(ratings_path)

    df_books_filtered, df_ratings_filtered = preprocess_data(df_books, df_ratings, min_book_count, min_user_count)

    ratings_matrix = df_ratings_filtered.pivot_table(index='isbn', columns='user', values='rating').fillna(0)

    return nn_model, df_books_filtered, ratings_matrix

def get_recommends(book):
    nn_model, df_books_filtered, ratings_matrix = load_artifacts(MODEL_PATH, RAW_DIR, BOOKS_CSV, RATINGS_CSV, 100, 200)
    
    isbn_query = df_books_filtered[df_books_filtered['title'] == book]['isbn'].values
    if isbn_query.size == 0:
        print("Title not found in the book set.")
        return []

    isbn = isbn_query[0]
    if isbn not in ratings_matrix.index:
        print("The book doesn't have enough reviews to be recommended.")
        return []
    
    vec = ratings_matrix.loc[isbn].values.reshape(1, -1)
    distances, indices = nn_model.kneighbors(vec, n_neighbors=6)

    neigh_idx = indices[0][1:]
    neigh_dist = distances[0][1:]
    neigh_isbns = ratings_matrix.index[neigh_idx]

    df_rec = df_books_filtered[df_books_filtered["isbn"].isin(neigh_isbns)].copy()
    df_rec["distance"] = df_rec["isbn"].apply(lambda x: float(neigh_dist[list(neigh_isbns).index(x)]))

    recs = df_rec[["title", "distance"]].values.tolist()
    return [book, recs]

    
