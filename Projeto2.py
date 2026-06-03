saldo = float(input('Digite seu saldo inicial: '))

while True:
    opcoes = input('Digite uma opção: "Ver saldo", "Depositar dinheiro", "Sacar dinheiro", "sair": ')

    if opcoes == "Ver saldo":
        print(f'Seu saldo é R$ {saldo:.2f}')

    elif opcoes == "Depositar dinheiro":
        valor = float(input('Digite quanto você quer depositar: '))
        saldo += valor
        print(f'Seu saldo atual é R$ {saldo:.2f}')

    elif opcoes == "Sacar dinheiro":
        sacar = float(input('Quanto você quer sacar?: '))

        if sacar > saldo:
            print('Saldo insuficiente')
            continue

        saldo -= sacar
        print(f'Seu saldo atual é R$ {saldo:.2f}')

    elif opcoes == "sair":
        print('Encerrando programa')
        break

    else:
        print('Opção inválida')