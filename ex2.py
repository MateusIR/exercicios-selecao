texto = input("insira um texto:")
contador = 0
for letra in texto:
    if letra.lower() == 'a':
        contador = contador + 1
if contador != 0:
    print(f'\nletra "a" apareceu {contador} vezes')
else:
    print('\nletra "a" não apareceu')