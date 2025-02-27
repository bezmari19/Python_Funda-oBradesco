soma = 0
media = 0
quantidade = 0
valor = float(input('Digite um valor aqui:'))

while (valor > 0.0):
    soma = soma + valor
    quantidade = quantidade + 1
    #Entrada de valores
    valor = float(input('Digite um valor aqui:'))

#Caso Digite um valor negativo o laço encerra
media = soma / quantidade
print('\n Total da Soma:', soma)
print('\n Qunatidade de valores digitados:', quantidade)
print('\n Média dos valores:', media)