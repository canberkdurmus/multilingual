import os
import yaml
from translator import Translator


class Multilingual:
    def __init__(self, target_language='en'):
        # TODO: Add multilingual support for main.yaml file (set source language on initialization)
        # TODO: Automatically detect source word list file language

        self.target_language = target_language.lower()
        self.words = {}
        self.main_list = []
        self.path = 'languages/' + self.target_language + '.yaml'

        with open(r'languages/main.yaml') as file:
            self.main_list = file.read().split('\n')

        if os.path.isfile(self.path):
            self.read_language()
        else:
            self.generate()

    def generate(self):
        generated = {}
        tr = Translator(dst_lang=self.target_language)
        for word in self.main_list:
            generated[word] = tr.translate(word)
        with open(self.path, 'w') as file:
            yaml.dump(generated, file, allow_unicode=True)
        self.words = generated

    def read_language(self):
        with open(self.path) as file:
            self.words = yaml.load(file, Loader=yaml.FullLoader)

    def get(self, word):
        # TODO: translate the word at that moment if doesn't exist in the word list and cache it
        return self.words[word]
