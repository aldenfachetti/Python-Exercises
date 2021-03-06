'''
Autor: Alden Merlin Fachetti Barbosa

Dizemos que um inteiro positivo n é perfeito se for igual à soma de seus divisores positivos diferentes de n.

Exemplo: 6 é perfeito, pois 1+2+3 = 6.

Dado um inteiro positivo n, verificar se n é perfeito.
'''

def main():
    '''
    Programa que lê um inteiro positivos n e verifica e imprime uma
    mensagem indicando se n é perfeito.
    '''

    print("Determina se um número n é perfeito\n")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    soma = 0

    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor # soma = soma + divisor

    if n == soma:
        print("O numero %d é perfeito" %(n))
    else:
        print("O numero %d nao é perfeito\n" %(n))

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()
