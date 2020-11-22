'''
Uma nova forma de testar se um número é par ou não
'''

referencia = ('0', '2', '4', '6', '8')

num = input('Digite um número: ')

# Verifico se o último caracter está na tupla referencia
# e valido se é par ou não
if num[-1] in referencia:
    print('PAR')
else:
    print('ÍMPAR')
