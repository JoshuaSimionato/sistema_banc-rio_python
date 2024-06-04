saldo = 0
numero_saques = 0
limite = 500
lista_deposito = []
lista_saque = []
while True:
    print('='*25)
    print('  Olá, seja bem vindo !')
    print('''
        [0] Depositar
        [1] Sacar
        [2] Extrato
        [3] Sair
        ''')
    print('='*25)
    opcao = int(input('  Qual é sua opção? '))
    print('='*25)
    if opcao in [0, 1, 2, 3]:
        if opcao == 0:  #deposito
            while True:
                valor_deposito = float(input('Informe o valor do deposito R$'))
                if valor_deposito > 0:
                    print(f'\nO valor R${valor_deposito:.2f} foi depositado com sucesso.')
                    saldo += valor_deposito
                    lista_deposito.append(valor_deposito)
                else:
                    print(f'\nO valor R${valor_deposito:.2f} não pode ser depositado !')
                while True:
                    continuar2 = (input('\nDeseja continuar com deposito ? [S/N]')).upper()[0]
                    if continuar2 in ['N', 'S']:
                        break
                    else:
                        print('\nErro, digite sometente [S/N]')
                if continuar2 == 'N':
                    break
        elif opcao == 1: #saque
            while True:
                valor_saque = float(input('\nQual o valor que deseja sacar ? R$ '))
                if valor_saque < 0:
                    print('\nOperação falhou! O valor informado é inválido.')
                elif saldo >= valor_saque:
                    if numero_saques >= 3:
                        print('\nLimite de saques diários atingido. Você pode fazer até 3 saques diários por dia.')
                        break
                    else:
                        if valor_saque > limite: #limite do saque tem que ser até 500
                            print('\nEssa operação não pode ser realizada, o limite de saque é R$ 500.00')
                        else:
                            numero_saques += 1
                            saldo -= valor_saque
                            lista_saque.append(valor_saque)
                            print(f'\nSaque de R${valor_saque:.2f} realizado com sucesso')
                elif saldo < valor_saque:
                    print('\nOperação falhou! Você não tem saldo suficiente.')
                while True:
                    continuar3 = (input('\nDeseja continuar com o saque ? [S/N]')).upper()[0]
                    if continuar3 in ['N', 'S']:
                        break
                    else:
                        print('\nErro, digite somente [S/N]')
                if continuar3 == 'N':
                    break
        elif opcao == 2:  #Extrato
            if len(lista_deposito) == 0 and len(lista_saque) == 0:
                print('\n============= Extrato =============')
                print(f'Não foram realizadas movimentações.\nSaldo: R$ {saldo:.2f}')
            else:
                print('\n============= Extrato =============')
                print(f'{"Depósitos":<15}{"Saques":>9}')
                print('-' * 30)
                max_len = max(len(lista_deposito), len(lista_saque))
                for i in range(max_len):  # itera as duas listas
                    if i < len(lista_deposito):
                        print(f'R${lista_deposito[i]:<13.2f}', end=' ')
                    else:
                        print(f'{"":<15}', end=' ')
                    if i < len(lista_saque):
                        print(f'R${lista_saque[i]:<13.2f}')
                    else:
                        print('')
                print('-' * 30)
                print(f'Saldo atual: R${saldo:.2f}')
        elif opcao == 3:  #sair
            break

        else:   #quando usuario digita errado
            print('Erro, digite somente os digitos do menu !')

