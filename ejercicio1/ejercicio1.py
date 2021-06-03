import nltk
from nltk.corpus import stopwords
nltk.download("punkt")
nltk.download('stopwords')

texto = "Hola mi amor. Aqui estoy en los causas de UTEC aprendiendo indice invertido"
palabras = nltk.word_tokenize(texto.lower())
print(palabras)


with open('stoplist.txt') as file:
    stoplist = [line.lower().strip() for line in file]
stoplist += ['.','?','-','hola']

palabras_limpias = palabras[:]
for token in palabras:
    if token in stoplist:
        palabras_limpias.remove(token)
print(palabras)
print(palabras_limpias)


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["program", "programs", "programer", "programing", "programers"]
for w in words:
    print(w, " =>", stemmer.stem(w))

######
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('spanish')
words = ["amor", "amaras", "amores"]
for w in words:
    print(w, " =>", stemmer.stem(w))

stemmer = SnowballStemmer('spanish')
for w in palabras_limpias:
    print(w, " =>", stemmer.stem(w))