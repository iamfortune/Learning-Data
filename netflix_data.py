# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!

# Load the CSV and store as a variable 
netflix_df = pd.read_csv("netflix_data.csv")

# Filter the data and remove the tv and store as var
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Investigate the Netflix movie data, keeping only the columns and save as new var 
netflix_movies = netflix_df[["title", "country", "genre", "release_year", "duration"]]

# Filter the movies with duration less than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]

# Create colors list object as empty 
colors = []
# LOOP 
for label, row in netflix_movies.iterrows():
    if row["genre"] == "Children":
        colors.append('red')
    elif row["genre"] == "Documentaries":
        colors.append("blue")
    elif row["genre"] == "Stand-Up":
        colors.append("yellow")
    elif row["genre"] == "Other":
        colors.append("black")
    else:
        colors.append("green")

# Creating a scatter plot of movies of year release against duration and colors for the c
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)
plt.xlabel("Release Year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")

plt.show()

answer = "yes"
print("Are we certain that movies are getting shorter?", answer)
