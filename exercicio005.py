'''
Autor: Alden Merlin Fachetti Barbosa

2º) Elabore um programa que calcule e apresente a soma dos inteiros existentes entre dois valores lidos.
    Considere que o segundo número lido deve ser maior que o primeiro número lido.
'''

while True:
  num1 = int(input('Entre com o valor inicial: '))
  num2 = int(input('Entre com o valor final: '))
  #Grava 2 números inteiros nos endereços das variaveis em questão, na ordem em que foram informados
  
  if num2 < num1:
    print("\nO valor final TEM que ser MAIOR que o valor inicial.\nExecute de novo o programa.")
    
    break #Finaliza o programa

  else:
    soma = 0 #Soma será a variável usada para somar os números do intervalo
    i = 0 #i é o contador do for

    for i in range (num1, num2, 1):
      #O primeiro número a ser somado é num1. Enquanto i (valor inicial num1) não chegar a num2, continuará somando
      soma += i; #soma = soma + i
      #Quando chegarmos aqui, i é maior que num2 e por tanto, não está em nosso intervalo

    print("\nA soma do intervalo entre ", num1, " e ", num2, " = ", (soma - num1))
    #Imprime o resultado da soma do intervalo [num1,num2]

    break #Finaliza o programa
  