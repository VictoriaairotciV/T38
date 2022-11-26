import spacy

nlp = spacy.load('en_core_web_sm')

# Page 3 example
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Page 5 example
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Page 6 example
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Observation:

# The language model appears to understand the concept of animals, as two
# animals are rated as more similar than an animal and a fruit.


tokens = nlp('horse car bike')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Observations on the simpler model

# The simpler model appears to lose some of the linguistic nuances of words,
# presumably because of the lower volume of data it was applied to.
