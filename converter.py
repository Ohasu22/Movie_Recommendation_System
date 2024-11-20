import pandas as pd

# Paths to the CSV files
credits_path = 'C:/Users/Ojas Gharde/Downloads/archive (1)/tmdb_5000_credits.csv'
movies_path = 'C:/Users/Ojas Gharde/Downloads/archive (1)/tmdb_5000_movies.csv'

# Load the CSV files into DataFrames
credits_df = pd.read_csv(credits_path)
movies_df = pd.read_csv(movies_path)

# Save DataFrames to pickle files
credits_df.to_pickle('tmdb_5000_credits.pkl')
movies_df.to_pickle('tmdb_5000_movies.pkl')

print("Files have been successfully converted to .pkl format.")
