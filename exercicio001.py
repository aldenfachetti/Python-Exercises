"""author: Gabriel Danius Fachetti Barbosa
#Um endocrinologista deseja controlar a saúde de seus pacientes e,
para isso, utiliza o Índice de Massa Corpórea (IMC). Sabendo-se que o IMC
é calculado através da seguinte fórmula: IMC = peso/(altura)2 ,
em que: peso é dado em Kg e altura é dada em metros. Escreva um programa que,
tendo como informação de entrada o peso e a altura,
apresenta o IMC da pessoa e sua faixa de risco, baseando-se na seguinte tabela:"""

#IMC        	                  Faixa de Risco
#Abaixo de 20	                 Abaixo do peso
#A partir de 20 até 25	     Normal	                 
#Acima de 25 até 30                  Excesso de Peso	                 
#Acima de 30 até 35                   Obesidade
#Acima de 35                            Obesidade mórbida

#Peso/Altura = IMC e Faixa de Risco

peso = float(input('Informe seu peso: (KG) '))
altura = float(input('Informe sua altura: (m) '))
imc = peso / (altura*altura)

print('O seu IMC é de: (:.2f)'. format(imc))
if imc < 20:
    print('Faixa de Peso: Abaixo do Peso')
elif 20 <= 25 > imc:
    print('Faixa de Peso: Normal')
elif 25 >= 30 > imc:
    print('Excesso de Peso')
elif 30 <= 35 > imc:
    print('Obesidade')
elif 35 < imc:
    print('Obesidade mórbida')





