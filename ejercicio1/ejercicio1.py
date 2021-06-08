import nltk
from nltk.stem.snowball import SnowballStemmer
# nltk.download("punkt")
# nltk.download('stopwords')

listaRecurrente = {}

with open('stoplist.txt') as filterFile:
    stoplist = [line.lower().strip() for line in filterFile]
stoplist += ['.', '?', '-', ';', ':', ',', '\'', '\"', '!', '¿', '¡', '»', '(', ')', '«']


def readFile(name):
    f = open(name, "r", encoding='utf8')
    stemmer = SnowballStemmer('spanish')
    texto = f.read()
    palabras = nltk.word_tokenize(texto.lower())
    for token in palabras:
        word = stemmer.stem(token)
        if word not in stoplist:
            if listaRecurrente.get(word) is not None:
                listaRecurrente[word] = listaRecurrente.get(word) + 1
            else:
                listaRecurrente[word] = 1


readFile("libro1.txt")
readFile("libro2.txt")
readFile("libro3.txt")
readFile("libro4.txt")
readFile("libro5.txt")
readFile("libro6.txt")

listaRecurrente = sorted(listaRecurrente.items(), key=lambda x: x[1], reverse=True)

print(listaRecurrente)

file = open("freqWord.txt", "w", encoding='utf8')
for i in range(500):
    if listaRecurrente[i] is None:
        break
    else:
        file.write(listaRecurrente[i][0]+'\n')
