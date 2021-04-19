import os
import yaml
from translate import Translator


class Multilingual:
    def __init__(self, target_language='en'):
        self.target_language = target_language.lower()
        self.words = {}
        self.main_list = []
        self.path = 'languages/' + self.target_language + '.yaml'

        with open(r'languages/main.yaml') as file:
            self.main_list = file.read().split('\n')

        if os.path.isfile(self.path):
            print(self.path)
            self.read_language()
        else:
            self.generate()

    def generate(self):
        generated = {}
        tr = Translator(to_lang=self.target_language)
        for word in self.main_list:
            generated[word] = tr.translate(word)
        with open(self.path, 'w') as file:
            self.words = yaml.dump(generated, file)

    def read_language(self):
        with open(self.path) as file:
            self.words = yaml.load(file, Loader=yaml.FullLoader)

    def get(self, word):
        return self.words[word]


"""
- generate languages -> check target language at the initiation, if doesn't exist, generate it from main file and save
- use multilingual -> get some string by string id, if id is not valid return none
"""
