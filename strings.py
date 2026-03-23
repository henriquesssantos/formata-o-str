''' função replace
(troca de caracteres)

frase = "a tecnologia move mundo."

saida1 = frase.replace('a', 'A', 1)
print(saida1)

saida2 = frase.title()
print(saida2)

'''

''' round
(arredondamento de numeros)

valor_1 = 1150.96666
valor_2 = 1150.91111

valor_1 = round(valor_1 , 2)
valor_2 = round(valor_2 , 3)

print(valor_1 , valor_2)
'''

'''
string[start:stop]
exemplo:
'''
nome = "Henrique Fernandes"
print(len(nome)) #lê a quantidade de caracteres que possui a str informada.
print(nome[0:9])
print(nome[9:])
print(nome[::-1]) #Lê a str de trás para frente.
'''
vai printar meu nome a partir do caracter 0 até o final
Os numeros se referem a posição da letra, começando em zero, porem o ultimo vai ser -1, seguindo exemplo do meu nome que possui 8 caracteres
O print vai até 9, porem impreme até o 9.
'''

''' metodo count
Conta quantos caracteres especificos possui a str.
exemplo:
'''

contador = nome.count("e")
print(contador)