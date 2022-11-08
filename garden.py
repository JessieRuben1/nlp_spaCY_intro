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
catch = "caught catching catch"
# Creating a Doc object.
nlp_practice = nlp(sing)
nlp_practice2 = nlp(catch)
# Printing the lemmatized version of the words in the string.
print([word.lemma_ for word in nlp_practice])
print([word2.lemma_ for word2 in nlp_practice2])

# Creating a string.
gardenpathSentences = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

# Creating a Doc object.
nlp_priyanka = nlp(gardenpathSentences)
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


#Note:
    # Spacy returns the base word. it changes 'sang' to 'sing', and removes the 'ing' from 'singing'.
    # I don't know if this is done because of the first word in the list is 'sang'. After removing the word 'sing'
    # and replacing it with 'sung' the results are slightly the same.
    
    #With the 'catch' variable spacy changed every word to 'catch'.