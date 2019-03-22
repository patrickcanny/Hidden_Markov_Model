'''
EECS738 - Machine Learning
@file: hmm.py
'''
from tools import FileTools

class HMM():

    def __init__(self, filename):
        self.filename = filename
        self.file = FileTools.processFile(filename)
        self.transition_matrix = {}
        self.first_words = {}
        self.second_words = {}

    def updateDict(target, key, val):
        if key not in target:
            target[key] = []
        target[key].append(value)

    def determineProbability(wordList):
        prob_dict = {}
        n_words = len(wordList)
        for word in wordList:
            prob_dict[word] = prob_dict.get(word, 0) + 1
        for key, count in prob_dict.items():
            prob_dict[key] = count / n_words
        return prob_dict

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
                    self.first_words = self.first_words.get(token, 0) + 1
                else:
                    previous_token = line[i-1]
                    if i == len(line - 1):
                        updateDict(self.transition_matrix, (previous_token, token), 'END')
                    if i == 1:
                        updateDict(self.second_words, previous_token, token)
                    else:
                        prev_previous_token = tokens[i-2]
                        updateDict(self.transition_matrix, (prev_previous_token, previous_token), token)

    def normalize_distributions(self):
        total_word_count = sum(self.first_words.values())
        for key, value in self.first_words.items():
            self.first_words[key] = value/total_word_count
        for prev_word, next_wordList in self.second_words.items():
            second_words[prev_word] = determineProbability(next_wordList)
        for word_combo, next_wordList in self.transition_matrix.items():
            transition_matrix[word_combo] = determineProbability(next_wordList)

    def predict(self):
        pass

    def generate():
        for i in range(number_of_sentences):
            # Sentence array
            sentence = []
            # Initial word
            word0 = sample_word(initial_word)
            sentence.append(word0)
            # Second word
            word1 = sample_word(second_word[word0])
            sentence.append(word1)
            # Subsequent words untill END
            while True:
                word2 = sample_word(transitions[(word0, word1)])
                if word2 == 'END':
                    break
                sentence.append(word2)
                word0 = word1
                word1 = word2
            print(' '.join(sentence))


