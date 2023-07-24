print('Menu')
menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
=> """

saldo = 0
limite = 500
extrato = '' 
numero_saque = 0
limite_saque = 3

while True: 
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito:'))
        
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou: O valor informado é invalido.')
    
        
    elif opcao == 's':
 
        valor = float(input('Informe o valor do saque:'))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saque >= limite_saque
        
        if saldo_excedido:
            print('Operação falhou! Voce não possui saldo suficiente.')
            
        elif limite_excedido:
            print('Operação falhou! Seu limite esta excedido.')
            
        elif saque_excedido:
            print('Operação falhou! Seu número de saque está excedido.')
            
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numero_saque += 1
        else: 
            print('Operação falhou! Informe um valor válido!')
            
    
    elif opcao == 'e':
        print('\n***************EXTRATO***************\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('*****************************************')
        
    elif opcao == 'q':
        print('Sair')
        break
    else: print('Operação inválida, favor selecionar a operação desejada.')