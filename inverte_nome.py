'''
Script simples para inverter uma string
'''
nome = input('Qual seu nome? ')

# Uma string é uma cadeia de caracteres, assim
# basta usar o slice de string lendo a mesma de
# trás pra frente
print(nome[::-1].lower())
