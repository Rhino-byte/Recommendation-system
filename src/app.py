from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import pandas as pd
  


movies_df = pd.read_csv('movies.csv')  # Replace with the path to your MovieLens dataset
ratings_df = pd.read_csv('ratings.csv')  # Replace with the path to your MovieLens dataset

# Merged dataframe
merged_df = ratings_df.merge(movies_df, on='movieId')

# Generate a content-based similarity matrix using the 'genres' column
movies_df['genres'] = movies_df['genres'].fillna('')  # Handle missing values
vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))  # Genres are separated by '|'
genre_matrix = vectorizer.fit_transform(movies_df['genres'])

# Compute cosine similarity
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Map movie titles to indices for quick lookup
title_to_index = pd.Series(movies_df.index, index=movies_df['title']).to_dict()

app = Flask(__name__)
# Load SVD model and movies dataset
with open('svd_model.sav', 'rb') as f:
    svd_model = joblib.load(f)

# Create a dictionary to map movie titles to movieIds for fast lookup
title_to_id = pd.Series(movies_df['movieId'].values, index=movies_df['title']).to_dict()




@app.route('/')
def home():
    movies = list(zip(movies_df['movieId'], movies_df['title']))
    return render_template('index.html', movies=movies)

def get_similar_movies(movie_title, n=10):
    # Find the movie index using the title
    if movie_title not in title_to_index:
        raise ValueError("Movie not found in the dataset.")
    
    movie_idx = title_to_index[movie_title]
    sim_scores = list(enumerate(cosine_sim[movie_idx]))  # Get similarity scores for the movie
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Sort by similarity
    top_similar = sim_scores[1:n+1]  # Exclude the movie itself (index 0)

    # Get movie titles and IDs for the top similar movies
    similar_movies = [(movies_df.iloc[idx]['movieId'], movies_df.iloc[idx]['title'], score) 
                      for idx, score in top_similar]
    
    # Convert to rank and title format
    ranked_movies = [{"rank": idx + 1, "title": movie[1]} for idx, movie in enumerate(similar_movies)]
    return ranked_movies


@app.route('/similar-movies', methods=['POST'])
def similar_movies():
    try:
        # Get the movie title from the form
        movie_title = request.form['movie_title']

        # Optional: Log user_id (if provided)
        user_id = request.form.get('user_id')

        # Get the top similar movies
        ranked_movies = get_similar_movies(movie_title)
       
        return render_template('similar_movies.html', movies=ranked_movies, selected_movie=movie_title)
    except Exception as e:
        return render_template('error.html', message=str(e))
    
def get_top_n_recommendations(user_id, n=10):
    all_movie_ids = movies_df['movieId'].unique()
    predictions = [(movie_id, svd_model.predict(uid=user_id, iid=movie_id).est) for movie_id in all_movie_ids]
    predictions = sorted(predictions, key=lambda x: x[1], reverse=True)
    top_n = [(movie_id, movies_df.loc[movies_df['movieId'] == movie_id, 'title'].values[0]) for movie_id, _ in predictions[:n]]
    return top_n

@app.route('/top-n', methods=['POST'])
def top_n():
    try:
        user_id = int(request.form['user_id'])
        top_n_recommendations = get_top_n_recommendations(user_id)

        # Create ranked recommendations by manually adding ranks
        ranked_recommendations = []
        rank = 1  # Start the ranking at 1
        for movie_id, title in top_n_recommendations:
            ranked_recommendations.append((rank, movie_id, title))
            rank += 1  # Increment rank
        # print('Ranked recommendation',ranked_recommendations)
        return render_template('top_n.html',  recommendations=ranked_recommendations)
    except Exception as e:
        return render_template('error.html', message=str(e))



if __name__ == '__main__':
    app.run(debug=True)
  
  