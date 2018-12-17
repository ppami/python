import nltk
#nltk.download()
from nltk.corpus import udhr
from nltk import wordpunct_tokenize as wptk
from nltk.corpus import stopwords as sw

text = udhr.raw()

def probability_of_language(text):
    probability = {}
    tokens = wptk(text)
    words = [word.lower() for word in tokens]

    for language in sw.fileids():
        sw_np = set(sw.words(language))
        words_np = set(words)
        common = words_np.intersection(sw_np)

        probability[language] = len(common)

    return probability

def language_detection(text):
    checker = probability_of_language(text)
    largest_prob = max(checker, key=checker.get)
    return largest_prob

whatlanguage = language_detection(text)
print(whatlanguage)
