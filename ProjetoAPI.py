num = int(input('Digite um número para calcular a tabuada: '))
multiplicacao = 0
print(f'A TABUADA DO {num}:')
i = 1
for i in range(1, 11, 1):
    print(i)
    multiplicacao = i * num
    print(multiplicacao)