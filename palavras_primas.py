'''
Palavras Primas

Contribuição de: Marianna Reis
Você está resolvendo este problema.

Este problema foi utilizado em 160 Dojo(s).

Um número primo é definido se ele possuir exatamente dois divisores: o número um e ele próprio. São exemplos de números primos: 2, 3, 5, 101, 367 e 523.

Neste problema, você deve ler uma palavra composta somente por letras [a-zA-Z]. Cada letra possui um valor específico, a vale 1, b vale 2 e assim por diante, até a letra z que vale 26. Do mesmo modo A vale 27, B vale 28, até a letra Z que vale 52.

Você precisa definir se cada palavra em um conjunto de palavras é prima ou não. Para ela ser prima, a soma dos valores de suas letras deve ser um número primo.

fonte http://dojopuzzles.com/problemas/exibe/palavras-primas/
'''

def pega_alfabeto():
    letras_minusculas =  [chr(i) for i in range(ord('a'), ord('z')+1)]
    letras_maiusculas =  [chr(i) for i in range(ord('A'), ord('Z')+1)]
    dict_alfabeto     = {}
    #
    for n, l in enumerate(letras_minusculas + letras_maiusculas, start=1):
        dict_alfabeto[l]=n
    return dict_alfabeto

def numero_primo(num):
    for i in range(2, num):
        i = num % i
        if i == num or i == 0:
            return False
    return True


def palavra_prima(palavra):
    soma = 0
    alfabeto = pega_alfabeto()
    retorno = 'A palavra ' +  palavra + '{0}'
    #
    for p in palavra:
        soma += alfabeto[p]
    print(soma)
    return  numero_primo(soma) and retorno.format(' é prima.') or retorno.format(' não é prima.')

def main():
    #
    print (palavra_prima('a'))

if __name__ == '__main__':
    main()

