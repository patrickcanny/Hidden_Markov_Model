'''
tools.py

helpful stuff for data processing
'''
import string
import numpy as np

class FileTools():
    def __init__(self):
        pass

    def processFile(self, filename):
        fileToProcess = open(filename)
        tokenizedFile = []
        for line in fileToProcess:
            # grab all individual words in a line
            tokens = self.processLine(line).split()
            tokenizedFile.append(tokens)
        return tokenizedFile

    def processLine(self, line):
        # convert lines into common form
        line = line.rstrip().lower()
        punctuation = string.punctuation
        line = line.translate(str.maketrans('', '', punctuation))
        return line

class DictTools():
    def __init__(self):
        pass

    def updateDict(self,target, key, val):
        if key not in target:
            target[key] = []
        target[key].append(val)

    def determineProbability(self, wordList):
        prob_dict = {}
        n_words = len(wordList)
        for word in wordList:
            prob_dict[word] = prob_dict.get(word, 0) + 1
        for key, count in prob_dict.items():
            prob_dict[key] = count / n_words
        return prob_dict

    def sample_word(self, dictionary):
        p0 = np.random.random()
        cum = 0
        for key, value in dictionary.items():
            cum += value
            if p0 < cum:
                return key
        assert(False)


