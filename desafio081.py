cont = 0
lista = []
while True:
    n = int(input('Digite um número: '))
    if n.alphanumeric():
        continue
    else:

        print('Isso não é um número, tente novamente!')

    cont += 1
    lista.append(n)
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print(f'Você digitou {cont} números e a lista em ordem decrescente é {sorted(lista, reverse=True)}')
if n == 5:
    print('O número 5 foi digitado!')
else:        
    print('O número 5 não foi digitado!')