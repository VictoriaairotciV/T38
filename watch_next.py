import spacy

nlp = spacy.load('en_core_web_md')

class Movie(object):
    "Records the label and description of a movie."

    def __init__(self, label, description):
        self.label = label
        self.description = description


def load_movies():
    "Read the movies from the movies file."
    movies = []
    with open("movies.txt", "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            # Split the line into it's label and description.
            parts = line.split(" :")
            # Create a new movie and add it to the list.
            movie = Movie(parts[0], parts[1])
            movies.append(movie)

    return movies


movies = load_movies()


def recommend_movie(description):
    "Look for the most similar movie to the specified description."
    similarity = 0
    recommendation = None

    description_nlp = nlp(description)
    # For each movie, check the similarity of the descriptions.
    for movie in movies:
        value = nlp(movie.description).similarity(description_nlp)
        if value > similarity:
            recommendation = movie
            similarity = value
    return recommendation

description = """Will he save their world or destroy it? When the Hulk becomes too
dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him
into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land
on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

recommendation = recommend_movie(description)

print(f"Based on recently watching 'Planet Hulk', consider this:")
print(f"{recommendation.label}")
print(f"{recommendation.description}")
print()
