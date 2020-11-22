'''
Script simples para sortear quem irá colocar a mesa no almoço
'''
from random import shuffle

# Lista com os nomes.
familia = ['Beatriz', 'Raquel', 'Sofia', 'Rafael', 'Camila', 'Flavia']

while True:
    #Menu básico do script
    print('''
    1 - Sortear
    2 - Sair
    ''')
    sorteio = int(input())
    if sorteio == 1:
        print(f'BOTAR A MESA')
        print(f'-=' * 8)
        # Embaralho os nomes da lista
        shuffle(familia)
        # Pego o primeiro elemento da lista após ser embaralhada
        print(familia[0])
    else:
        break
        
