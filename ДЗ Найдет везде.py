import string
from collections import Counter

class WordsFinder:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for self.file_num in self.file_name:
            with open(self.file_num, encoding='utf8') as file:
                table = str.maketrans(".", "!", string.punctuation)
                line = file.read().translate(table).split()
                for j in range(len(line)):
                    line[j] = line[j].lower()
                    all_words[self.file_num] = line
        return all_words

    def find(self, word):
        find_in = {}
        for self.file_num in self.file_name:
            for key, value in self.get_all_words().items():
                word = word.upper()
                if word in [x.upper() for x in value]:
                    find_in[key] = (value.index(word.lower()) + 1)
            return find_in

    def count(self, word):
        count_in = {}
        for self.file_num in self.file_name:
            for key, value in self.get_all_words().items():
                word = word.upper()
                if word in [x.upper() for x in value]:
                    count_in[key] = value.count(word.lower())
            return count_in

finder2 = WordsFinder(['Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt',
                       'Mother Goose - Monday’s Child.txt'])
print(finder2.get_all_words())
print(finder2.find('the'))
print(finder2.count('the'))
