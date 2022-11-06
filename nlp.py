# # Importing the spacy library.
import spacy

# It loads the small English model.
nlp = spacy.load('en_core_web_sm')

# Creating a string.
sample = u"Build your data science skills to launch an in-demand, valuable career in six months."

# Creating a Doc object.
doc = nlp(sample)

# Printing the text of each token in the doc.
[token.orth_ for token in doc]

# Printing the text of each token in the doc.
print([token.orth_ for token in doc if not token.is_punct | token.is_space])

# Printing all the stop words in the doc.
for word in doc:
    if word.is_stop == True:
        print(word)

# Creating a string.
sing = "sang singing sing"
# Creating a Doc object.
nlp_practice = nlp(sing)
# Printing the lemmatized version of the words in the string.
print([word.lemma_ for word in nlp_practice])

# Creating a string.
wiki_priyanka = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

# Creating a Doc object.
nlp_priyanka = nlp(wiki_priyanka)
# Printing the entities in the text.
print([(i, i.label_, i.label) for i in nlp_priyanka.ents])

# It creates a blank English model.
nlp = spacy.blank("en")

# Process the text
docs = nlp("I like tree kangaroos and narwhals.")

# Select the first token
first_token = docs[0]

# Print the first token's text
print(first_token.text)
