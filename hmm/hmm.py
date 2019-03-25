'''
EECS738 - Machine Learning
@file: hmm.py
'''
from tools import FileTools, DictTools
import numpy as np

class HMM():
    def __init__(self, filename):
        self.filename = filename
        self.dt = DictTools()
        ft = FileTools()
        self.file = ft.processFile(filename)
        self.transition_matrix = {}
        self.first_words = {}
        self.second_words = {}

    def train(self):
        print('Training on: {}'.format(self.filename))
        self.build_matricies()
        self.normalize_distributions()
        print('Done Training on: {}'.format(self.filename))

    def build_matricies(self):
        for line in self.file:
            for i in range(len(line)):
                token = line[i]
                if i == 0:
                    self.first_words[token] = self.first_words.get(token, 0) + 1
                else:
                    previous_token = line[i-1]
                    if i == len(line) - 1:
                        self.dt.updateDict(self.transition_matrix, (previous_token, token), 'END')
                    if i == 1:
                        self.dt.updateDict(self.second_words, previous_token, token)
                    else:
                        prev_previous_token = line[i-2]
                        self.dt.updateDict(self.transition_matrix, (prev_previous_token, previous_token), token)

    def normalize_distributions(self):
        total_word_count = sum(self.first_words.values())
        for key, value in self.first_words.items():
            self.first_words[key] = value/total_word_count
        for prev_word, next_wordList in self.second_words.items():
            self.second_words[prev_word] = self.dt.determineProbability(next_wordList)
        for word_combo, next_wordList in self.transition_matrix.items():
            self.transition_matrix[word_combo] = self.dt.determineProbability(next_wordList)

    def predict(self):
        pass

    def generate(self, number_of_sentences, starter_sentence = ''):
        for i in range(number_of_sentences):
            # Sentence array with starter sentence
            sentence = starter_sentence.split()
            # Initial word
            if len(sentence) == 0:
                word0 = self.dt.sample_word(self.first_words)
                sentence.append(word0)
                # Second word
                word1 = self.dt.sample_word(self.second_words[word0])
                sentence.append(word1)
            elif len(sentence) == 1:
                word0 = sentence
                word1 = self.dt.sample_word(self.second_words[word0])
            else:
                word0 = sentence[len(sentence)-2]
                word1 = sentence[len(sentence)-1]
             
            # Subsequent words untill END
            while True:
                try:
                    word2 = self.dt.sample_word(self.transition_matrix[(word0, word1)])
                except KeyError as e:
                    print("[ERROR]: The word(s) is/are not among the words used in the trained model.")
                    print("Try different words or a larger training set")
                    return
                if word2 == 'END':
                    break
                sentence.append(word2)
                word0 = word1
                word1 = word2
            print(' '.join(sentence))


