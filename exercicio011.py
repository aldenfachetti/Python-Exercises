'''
Autor: Alden Merlin Fachetti Barbosa

Dados o número n de alunos de uma turma de Introdução aos Autômatos a Pilha (MAC 414) e suas notas da
primeira prova, determinar a maior e a menor nota obtidas por essa turma (Nota máxima = 100 e nota mínima = 0).
'''

def main():
    '''
    Programa que lê um número inteiro positivo n e uma sequência
    de n notas (número inteiros entre 0 e 100) e imprime
    a maior e a menor nota.
    '''

    print("Cálculo da maior da menor nota\n");

    # leia o número de notas
    n = int(input("Digite o número de notas: "))

    # inicialize o contador de notas lidas
    i = 0

    # inicialize o candidato a maior nota
    maior_nota = -1

    # inicialize o candidato a menor nota
    menor_nota = 101

    # determine a maior e menor nota
    while i < n:
        # leia a próxima nota
        nota = int(input("Digite uma nota (inteiro de 0 a 100): "))
        i = i + 1

        # determine a menor nota lida até agora
        if nota < menor_nota:
            menor_nota = nota

        # determine a maior nota lida até agora
        if nota > maior_nota:
            maior_nota = nota


    print("A maior nota foi", maior_nota)
    print("A menor nota foi", menor_nota)


# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()
