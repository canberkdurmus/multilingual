from multilingual import Multilingual

if __name__ == '__main__':
    ml = Multilingual(target_language='fr')
    print(ml.main_list)
    print(ml.words)
    print(ml.get('words'))
