# A program which uses NLP similarity analysis to recommend a movie from a list based on matching descriptions to
# the description of a movie that was previously watched.

import spacy

def recommendation(last_movie):
    # Load spacy model
    nlp = spacy.load('en_core_web_md')

    # Declare variables
    movie_list = {}
    recommendation_id = None
    top_score = 0

    # Read in the movie list
    with open('./movies.txt', 'r') as movies:
        for movie in movies:
            movie_id, description = movie.partition(" :")[::2]
            movie_list[movie_id] = description.strip("\n")
    movies.close()

    # Apply NLP to movie_description parameter
    last_movie_title, last_movie_description = last_movie.partition(" :")[::2]
    nlp_movie_description = nlp(last_movie_description)

    for movie_id, description in movie_list.items():
        # Check you're not recommending the same movie, i.e. where similarity score is 1
        if not (nlp(description).similarity(nlp_movie_description) == 1):
            # Calculate similarity score
            similarity_score = nlp(description).similarity(nlp_movie_description)

            # Recommend the movie by default if no movie has yet been selected
            if recommendation_id == None:
                recommendation_id = movie_id
                top_score = similarity_score

            # Compare similarity score to current recommendation and replace if necessary
            elif (similarity_score > top_score):
                recommendation_id = movie_id
                top_score = similarity_score
    
    # Return the movie id and score, or None if no match found (i.e. score = 0)
    if (top_score == 0):
        return None
    else:
        top_score = round(top_score * 100)
        return (f"{recommendation_id}\nMatch: {top_score}%")


# ========= Main body of code ==============

last_movie = '''
    Planet Hulk :Will he save their world or destroy it?
    When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into 
    space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is 
    sold into slavery and trained as a gladiator."
'''
suggestion = recommendation(last_movie)

# Print results
if suggestion is None:
    print("Sorry, no suitable recommendations found based on the last film you watched.")
else:
    print("Based on the last film you watched, we recommend: " + suggestion)