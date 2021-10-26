'''
Autor: Alden Merlin Fachetti Barbosa

1º) Faça um programa que receba a idade, a altura e o peso de 30 pessoas, calcule e mostre:
  a) a quantidade de pessoas com idade superior a 50 anos;
  b) a média das alturas das pessoas com idade entre 10 e 20 anos;
  c) a porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
'''

qtdIdadePessoasSuperior50 = 0
mediaAlturasPessoas = 0
qtdIdadePessoasEntre10e20 = 0 
qtdPesoMenor40 = 0

i = 0

while i < 5:
    idade = int(input("Digite a idade da pessoa: "))
    altura = float(input("Digite a altura da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    print("\n")
    
    if(idade > 50):
        qtdIdadePessoasSuperior50 += 1
    if idade > 10 and idade < 20:
        mediaAlturasPessoas += altura
        qtdIdadePessoasEntre10e20 += 1
    if qtdPesoMenor40 < 40:
        qtdPesoMenor40 += 1
    i += 1

print("A quantidade de pessoas com idade superior a 50 anos: ", qtdIdadePessoasSuperior50)
print("A média das alturas das pessoas com idade entre 10 e 20 anos: ", mediaAlturasPessoas/qtdIdadePessoasEntre10e20)
print("A porcentagem de pessoas com peso inferior a 40 quilos: ", qtdPesoMenor40/5)

