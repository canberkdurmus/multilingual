import requests


class Translator:
    def __init__(self, dst_lang, src_lang='en'):
        self.src_lang = src_lang
        self.dst_lan = dst_lang
        self.lang_pair = self.src_lang.upper() + '|' + self.dst_lan.upper()
        self.base_url = 'https://api.mymemory.translated.net/get'

    def translate(self, word):
        params = {'q': word, 'langpair': self.lang_pair}
        r = requests.get(url=self.base_url, params=params).json()
        return r['responseData']['translatedText']


if __name__ == '__main__':
    tr = Translator('it')
    print(tr.translate('hello'))
