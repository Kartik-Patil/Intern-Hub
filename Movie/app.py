from flask import Flask, request, render_template
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Start the Flask app
app = Flask(__name__)

# 2. Load the datasets
movies = pd.read_csv(r'D:\Intern Hub\Movie\Data\movies.csv')
ratings = pd.read_csv(r'D:\Intern Hub\Movie\Data\rating.csv')

# 3. Clean and prepare the data
movie_ratings = pd.merge(ratings, movies, on='movieId')
movie_ratings['genres'] = movie_ratings['genres'].replace('(no genres listed)', 'Unknown')

user_item_matrix = movie_ratings.pivot_table(index='userId', columns='title', values='rating').fillna(0)

# 4. Content-based filtering using genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
movie_similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
movie_similarity_df = pd.DataFrame(movie_similarity, index=movies['title'], columns=movies['title'])

# 5. Genre-based recommendation function with exact genre match and debug prints
def recommend_by_genre(favorite_genres, num_recommendations=5):
    # Clean and normalize genres (removing extra spaces)
    favorite_genres = [genre.strip().lower() for genre in favorite_genres]
    
    # Split the genre column into a set of genres for each movie
    movies['genre_set'] = movies['genres'].apply(lambda x: set(x.lower().split('|')))
    
    # Debugging: Print out the first few genre sets and the user's favorite genres
    print("User's favorite genres:", favorite_genres)
    print("Sample genre sets in movies:\n", movies[['title', 'genre_set']].head())
    
    # Filter movies that match *all* favorite genres (exact match required)
    matching_movies = movies[movies['genre_set'].apply(
        lambda genre_set: all(genre in genre_set for genre in favorite_genres)
    )]
    
    # Debugging: Print out the filtered movies
    print(f"Movies matching genres {favorite_genres}:", matching_movies[['title', 'genre_set']].head())
    
    # Remove duplicates and return top recommended movies
    matching_movies = matching_movies.drop_duplicates(subset='title')
    return matching_movies['title'].head(num_recommendations).tolist()



# 6. Hybrid recommendation function combining content and collaborative filtering
def hybrid_recommendation(user_id, favorite_genres, num_recommendations=5):
    # Get genre-based recommendations
    genre_recommendations = recommend_by_genre(favorite_genres, num_recommendations * 2)  # Get extra genre recommendations
    
    # Collaborative filtering recommendations (based on user-item matrix)
    user_similarity = cosine_similarity(user_item_matrix)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
    
    # Get the most similar users to the input user
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]  # Skip self (first)
    collaborative_recommendations = user_item_matrix.loc[similar_users].mean(axis=0).sort_values(ascending=False)
    
    # Get the top collaborative recommendations
    collaborative_movies = collaborative_recommendations.head(num_recommendations).index.tolist()
    
    # Combine both genres-based and collaborative-based recommendations and drop duplicates using pd.concat
    final_recommendations = pd.concat([pd.Series(collaborative_movies), pd.Series(genre_recommendations)], ignore_index=True)
    final_recommendations = final_recommendations.drop_duplicates().head(num_recommendations)
    
    return final_recommendations.tolist()

# 7. Flask Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        favorite_genres = request.form['genres'].split(',')
        favorite_genres = [genre.strip() for genre in favorite_genres]
        
        recommended_movies = recommend_by_genre(favorite_genres)
        
        # Debugging: Print the recommended movies list before rendering
        print(f"Recommended movies to send to frontend: {recommended_movies}")
        
        return render_template('index.html', movies=recommended_movies)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
