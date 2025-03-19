import pandas as pd
import matplotlib.pyplot as plt

# Read the Netflix CSV into a DataFrame
netflix_df = pd.read_csv("data/netflix_data.csv")

# Subset the DataFrame for "Movie" type only
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter the data for movies released in the 1990s
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]
movies_1990s = subset[(subset["release_year"] < 2000)]

# Visualize the distribution of movie durations in the 1990s
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Filter for "Action" genre movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Count the number of short action movies
short_movie_count = (action_movies_1990s["duration"] < 90).sum()

print(f"Number of short action movies: {short_movie_count}")