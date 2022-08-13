import json


class Letter_converter:
    
    def __init__(self, filename='turkish_alphabet.json'):
        
        self.alphabet = self.read_alphabet(filename)

    def read_alphabet(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                db = json.load(f)
        except:
            raise Exception("Error occured while reading file.")
        try:
            alphabet_dict = db['alphabet']
        except:
            raise Exception("'alphabet' couldn't find while reading file.")
        return alphabet_dict
        
    def turkish_upper_case_to_title(self, word, upper_to_lower = False):
        
        if upper_to_lower is True:
            first_c = ''
            
        else:
            first_c = word[0]
            word = word[1:]
        
        for c in word:
            if c in self.alphabet:
                word = word.replace(c, self.alphabet[c])
        word = word.lower()
        result = first_c + word
        return result


obj = Letter_converter()
print(obj.turkish_upper_case_to_title('ŞANLIURFA', upper_to_lower=False))