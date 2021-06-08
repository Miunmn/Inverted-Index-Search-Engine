import nltk
from nltk.stem.snowball import SnowballStemmer
# nltk.download("punkt")
# nltk.download('stopwords')


def stoplistInitilizer(filename):
    with open(filename) as filterFile:
        stoplist = [line.lower().strip() for line in filterFile]
    stoplist += ['.', '?', '-', ';', ':', ',', '\'', '\"', '!', '¿', '¡', '»', '(', ')', '«']
    return stoplist


def readFile(listaRecurrente, name, stoplist):
    f = open(name, "r", encoding='utf8')
    stemmer = SnowballStemmer('spanish')
    texto = f.read()
    palabras = nltk.word_tokenize(texto.lower())
    for token in palabras:
        word = stemmer.stem(token)
        if word not in stoplist:
            if listaRecurrente.get(word) is not None:
                if name not in listaRecurrente[word][1]:
                    listaRecurrente[word][1].append(name)
                listaRecurrente[word][0] = listaRecurrente[word][0]  + 1
            else:
                listaRecurrente[word] = [1,[name]]


def readAllFiles(listaRecurrente, libros,stoplist):
    for libro in libros:
        readFile(listaRecurrente,libro,stoplist)


def printelemensinlist(lista):
    string = ""
    for i in range(len(lista)):
        string =  string + lista[i]
        if i != len(lista)-1:
            string = string + ","
    return string


def solve():
    listaRecurrente = {}
    stoplistfilename = 'stoplist.txt'
    libros = ["libro1.txt", "libro2.txt", "libro3.txt", "libro4.txt", "libro5.txt", "libro6.txt"]
    stoplist = stoplistInitilizer(stoplistfilename)

    readAllFiles(listaRecurrente,libros,stoplist)

    listaRecurrente = sorted(listaRecurrente.items(), key=lambda x: x[1], reverse=True)

    del listaRecurrente[500:]

    listaRecurrente.sort(key=lambda tup: tup[0])

    file = open("freqWord.txt", "w", encoding='utf8')
    for i in range(500):
        if listaRecurrente[i] is None:
            break
        else:
            file.write(listaRecurrente[i][0]+':'+ printelemensinlist(listaRecurrente[i][1][1])+'\n')


def L(search_word):
    stemmer = SnowballStemmer('spanish')
    cut_word = search_word.lower()
    cut_word = stemmer.stem(cut_word)
    with open("freqWord.txt", "r", encoding='utf8') as file:
        for line in file:
            word = line.split(':')
            if word[0] == cut_word:
                return word[1].rstrip('\n').split(',')


if __name__ == "__main__":
    solve()
    print(L("Frodo"))
