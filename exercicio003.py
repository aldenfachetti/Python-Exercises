"""
Autor: Alden Merlin Fachetti Barbosa

Faça um programa que tem como dados de entrada o código de região de localização do cliente, o nome do cliente, o número de peças vendidas e o nome do vendedor, calcule e informe o valor do frete, a comissão do vendedor e o lucro obtido com a venda
"""

cod_regiao = int(input('Digite o codigo de regiao/localizacao do cliente:\nCodigo 1 - SUL\nCodigo 2 - NORTE\nCodigo 3 - LESTE\nCodigo 4 - OESTE\n'))
nome_cliente = str(input('Digite o nome do cliente: '))
num_pecas_vendidas = int(input('Digite o numero de pecas vendidas: '))
nome_vendedor = str(input('Digite o nome do vendedor: '))

valor_por_peca = 7.00
custo_total = valor_por_peca * num_pecas_vendidas
valor_total_venda = custo_total * 1.50
desconto = 6.5 / 100
comissao_vendedor = float(valor_total_venda * (1 - desconto))
lucro = float(valor_total_venda - custo_total - comissao_vendedor)
valor_frete = 0

if cod_regiao == 1:
    if valor_frete < 1000:
        valor_frete = 1.00
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
    if valor_frete >= 1000:
        valor_frete = 0.9
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
        
elif cod_regiao == 2:
    if valor_frete < 1000:
        valor_frete = 1.10
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
    if valor_frete >= 1000:
        valor_frete = 1.0
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
        
elif cod_regiao == 3:
    if valor_frete < 1000:
        valor_frete = 1.15
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
    if valor_frete >= 1000:
        valor_frete = 1.10
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
        
else:
    if valor_frete < 1000:
        valor_frete = 1.20
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
    if valor_frete >= 1000:
        valor_frete = 1.15
        print("Cliente "+ str(nome_cliente) + ", o valor do frete = " + str(valor_frete) + "\nVendedor " + str(nome_vendedor) + ", sua comissao = " + str(comissao_vendedor) + "\nO seu lucro obtido foi = " + str(lucro))
