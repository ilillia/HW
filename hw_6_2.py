'Задание №2'

from string import whitespace

class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol

def string_processing(text, *args, **kwargs):
    
    for symbol in text:
        if symbol in whitespace:
            raise WhitespaceError(text.find(symbol), repr(symbol))
    result = text.upper()
    return result

def main():
    try:
        print(string_processing('UnDetected'))
        print(string_processing('''Un
Detected'''))

    except WhitespaceError as error:
        print('Detected whitespace symbol : position = {}, symbol = {}'.format(error.position, error.symbol))

if __name__ == "__main__":
    main()
    
