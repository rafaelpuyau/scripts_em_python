'''
Script simples para colocar ordem no banho da criançada
'''
from random import shuffle

# Lista com nome das crianças
turminha = ['Beatriz', 'Raquel', 'Sofia']
# Embaralho a lista
shuffle(turminha)
print(f'ORDEM DO BANHO')
print(f'-=' * 8)
# Imprimir a ordem do banho da criançada
for ordem, nome in enumerate(turminha):
    print(f'{ordem+1}ª : {nome}')
