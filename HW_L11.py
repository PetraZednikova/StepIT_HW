# Task 3: Dictionary App

from collections import deque, Counter

class DictionaryApp:
    def __init__(self):
        self.dictionary = {}
        self.request_counter = Counter()

    def add_word(self, word, translations):
        self.dictionary[word] = set(translations)

    def get_translations(self, word):
        self.request_counter[word] += 1
        return self.dictionary.get(word, set())

    def delete_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]

    def top_words(self, most_popular=True):
        return self.request_counter.most_common(10 if most_popular else None)

if __name__ == "__main__":
    dictionary = DictionaryApp()
    dictionary.add_word("hello", ["Ahoj"])
    dictionary.add_word("car", ["auto"])
    print(dictionary.get_translations("hello"))
    print(dictionary.get_translations("car"))
