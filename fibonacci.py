'''
Série de fibonacci em Python para testar o tempo de execução
'''
fibonacci = 1
last1 = 0
last2 = 1
print('Starting...')
print(f'{last1}')
for i in range(1_000_000):
    print(f'{fibonacci}')
    fibonacci = last1 + last2
    last1 = last2
    last2 = fibonacci
print('The End')
