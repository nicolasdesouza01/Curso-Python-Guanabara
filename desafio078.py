valor = []
for c in range (0, 5):
    valor.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} na posição ', end='')
for i, v in enumerate(valor):                          
    if v == max(valor):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(valor)} na posição ', end='')
for i, v in enumerate(valor):
    if v == min(valor):
        print(f'{i}... ', end='')