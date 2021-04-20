# Multilingual

#### Two tiny Python classes to make multi-language support available for any project.

## Usage

Don't forget to add your strings to the `languages/main.yaml` file  
After that you can call those strings in your target language
```
from multilingual import Multilingual

if __name__ == '__main__':
    ml = Multilingual(target_language='fr')
    print(ml.get('contains'))
```

Output:
`contient`