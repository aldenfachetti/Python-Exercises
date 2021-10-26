#Autor: Alden Merlin Fachetti Barbosa

altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em Kg): "))
 
imc = peso / altura**2
#imc = peso/(altura * altura) 
 
if imc < 20:
	print("Abaixo do peso")
elif imc >= 20 and imc <= 25:
	print("Normal")
elif imc > 25 and imc <= 30:
	print("Excesso de Peso")
elif imc > 30 and imc <= 35:
	print("Obesidade")
else:
	print("Obesidade mórbida")
	
print("Seu IMC é: " + str(imc))
