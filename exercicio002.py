#Autor: Alden Merlin Fachetti Barbosa

#Escreva um programa que tendo como entrada o tipo do vôo (‘N’ para noturno / ‘D’ para diurno) e a quantidade de pessoas; calcula e mostra a tarifa e o total a pagar de acordo com as condições abaixo:

#Tipo de Vôo	Quantidade	    Tarifa
#Diurno	           <=50	           R$200,00
#Diurno	            >50	           R$120,00
#Noturno           <=50	           R$100,00
#Noturno            >50	           R$80,00

#Total a pagar = quantidade de pessoas x tarifa

tipo_voo = str(input("Escolha o tipo de voo (N = noturno | D = diurno): "))
qtde_pessoas = int(input("Entre com a quantidade de pessoas: "))
total_pagar: float = 0

if tipo_voo == 'D' and qtde_pessoas <= 50:
    total_pagar = qtde_pessoas * 200.00
    print("A tarifa total a pagar = R$" + str(total_pagar))

elif tipo_voo == 'D' and qtde_pessoas > 50:
    total_pagar = qtde_pessoas * 120.00
    print("A tarifa total a pagar = R$" + str(total_pagar))
    
elif tipo_voo == 'N' and qtde_pessoas <= 50:
    total_pagar = qtde_pessoas * 100.00
    print("A tarifa total a pagar = R$" + str(total_pagar))
    
elif tipo_voo == 'N' and qtde_pessoas > 50:
    total_pagar = qtde_pessoas * 80.00
    print("A tarifa total a pagar = R$" + str(total_pagar))
