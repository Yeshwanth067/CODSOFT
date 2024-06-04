import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset: users' movie ratings
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Movie1': [5, 4, 1, 0, 3],
    'Movie2': [4, 5, 2, 1, 0],
    'Movie3': [1, 0, 5, 4, 3],
    'Movie4': [0, 2, 4, 5, 1],
    'Movie5': [3, 0, 1, 0, 5]
}

df = pd.DataFrame(data)
df.set_index('User', inplace=True)
print("User-Movie Ratings Matrix:")
print(df)

# Calculate user similarity matrix using cosine similarity
similarity_matrix = cosine_similarity(df)
similarity_df = pd.DataFrame(similarity_matrix, index=df.index, columns=df.index)
print("\nUser Similarity Matrix:")
print(similarity_df)

def get_recommendations(user, df, similarity_df):
    # Get the ratings of the target user
    user_ratings = df.loc[user]
    # Get the indices of the movies the user hasn't rated yet
    unrated_movies = user_ratings[user_ratings == 0].index
    
    # Calculate weighted sum of ratings for each unrated movie
    recommendations = {}
    for movie in unrated_movies:
        weighted_sum = 0
        similarity_sum = 0
        for other_user in df.index:
            if other_user != user and df.loc[other_user, movie] > 0:
                similarity = similarity_df.loc[user, other_user]
                weighted_sum += similarity * df.loc[other_user, movie]
                similarity_sum += similarity
        if similarity_sum > 0:
            recommendations[movie] = weighted_sum / similarity_sum
    
    # Sort the recommendations by score in descending order
    recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return recommendations

# Get recommendations for User1
user = 'User1'
recommendations = get_recommendations(user, df, similarity_df)
print(f"\nRecommendations for {user}:")
for movie, score in recommendations:
    print(f"{movie}: {score:.2f}")
