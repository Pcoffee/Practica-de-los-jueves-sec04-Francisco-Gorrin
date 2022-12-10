#anagramas y tautograma

def run() :
    word_1= input('ingrese una palabra:')
    word_2= input('ingrese una palabra:')
    
    print(f' la palabra "{word_1}" es amagrama de "{word_2}? " {set(word_1) == set(word_2)}"')


if __name__ == '__main__':
    run()