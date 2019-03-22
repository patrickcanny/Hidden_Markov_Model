'''
tools.py

helpful stuff for data processing
'''

class FileTools():
    def __init__(self):
        pass

    def processFile(self, filename):
        fileToProcess = open(filename)
        tokenizedFile = []
        for line in fileToProcess:
            # grab all individual words in a line
            tokens = processLine(line).split()
            tokenizedFile.append(tokens)
        return tokenizedFile

    def processLine(self, line):
        # convert lines into common form
        line = line.rstrip().lower()
        punctuation = string.punctuation
        line = line.translate(str.maketrans('', '', punctuation))
        return line

