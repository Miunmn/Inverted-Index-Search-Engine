
def readfile(filename):
    file = open(filename, encoding='utf8')
    read = file.read()
    file.seek(0)   
    line = 1
    for word in read:
        if word == '\n':
            line += 1
    print("Number of lines in file is: ", line)

    array = []
    for i in range(line):
        array.append(file.readline())

    return array

def invertedindex(array,line):
    dict = {}    
    for i in range(line):
        check = array[i].lower()
        for item in tokens_without_sw:
            if item in check:
                if item not in dict:
                    dict[item] = []
    
                if item in dict:
                    dict[item].append(i+1)
  
if __name__ == "__main__":
    readfile()
