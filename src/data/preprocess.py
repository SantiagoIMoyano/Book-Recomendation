def filter_ratings_by_book_count(df_ratings, min_book_count):
    book_counts = df_ratings.groupby('isbn')['rating'].count()
    books_to_keep = book_counts[book_counts >= min_book_count].index
    df_books_filtered = df_ratings[df_ratings['isbn'].isin(books_to_keep)]
    return df_books_filtered, books_to_keep

def filter_ratings_by_user_count(df_ratings, df_books_filtered, min_user_count):
    user_counts = df_ratings.groupby('user')['rating'].count()
    users_to_keep = user_counts[user_counts >= min_user_count].index
    df_ratings_filtered = df_books_filtered[df_books_filtered['user'].isin(users_to_keep)]
    return df_ratings_filtered

def preprocess_data(df_books, df_ratings, min_book_count, min_user_count):
    df_books_filtered, books_to_keep = filter_ratings_by_book_count(
        df_ratings, min_book_count
    )

    df_ratings_filtered = filter_ratings_by_user_count(
        df_ratings, df_books_filtered, min_user_count
    )

    df_books_filtered = df_books[df_books['isbn'].isin(books_to_keep)]

    return df_books_filtered, df_ratings_filtered