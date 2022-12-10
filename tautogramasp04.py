#anagramas y tautograma

def verifica_tautograma(p):
    return len({i[0] for i in p}) == 1


if __name__ == '__main__':
    txt = input('oracion:').lower().split()
    repuesta = verifica_tautograma(txt)

    print(repuesta)