'Задание №1'

from string import whitespace

def string_processing(text, *args, **kwargs):

    for symbol in text:
        if symbol in whitespace:
            raise ValueError('Warning ! Special symbol!')
    result = text.upper()
    
    return result

if __name__ == "__main__":
    try:
        print(string_processing('abc'))
        print(string_processing('a\nbc'))

    except ValueError as error:
    	print('string_processing return :', error)
