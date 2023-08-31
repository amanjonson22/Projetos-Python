def criar_usuário():
    usuário = input('Qual seu nome de usuário? ')
    senha = input('Qual sua senha? ')
    conta = []
    conta.append(usuário)
    conta.append(senha)
    print(f'Seu usuário é: {conta[0]}. Sua senha é: {conta[1]}')
    return conta

def extrato():
    return 'Gastos:\n - Livraria Curitiba.....R$59.90\n - McDonalds.....R$78.33\n - Supermercado Oba.....R$347.98'

def limite():
    return 'Seu limite restante é:\n R$347.14'

def acessar_conta():
    print('Escolha: \n - Ver extrato (extrato) \n - Ver limite do cartão de crédito (limite)\n - Sair(sair)')
    resposta = 0
    while resposta != 'sair':
        resposta = input('O que você deseja? \n').lower()
        if resposta == 'extrato':
            print(extrato())
        if resposta == 'limite':
            print(limite())
        if resposta == 'sair':
            return 4

def login(conta):
    tentativa_login = 0
    while tentativa_login <=3:
        usuário = input('Digite seu usuário: ')
        senha = input('Digite sua senha: ')
        if conta[0] == usuário and conta[1] == senha:
            tentativa_login = 4
            acessar_conta()
        else:
            if conta[0] != usuário:
                print('Seu usuário está errado, tente novamente')
            if conta[1] != senha:
                print('Sua senha está errada, tente novamente')
            tentativa_login += 1


print('Bem-vindo ao Banco MasterX')
acesso = 0
while acesso != 'sair':
    acesso = input('O que você deseja?\n Criar conta(criar)\n Login(login)\n Sair(sair)\n').lower()
    if acesso == 'criar':
       conta = criar_usuário()
    if acesso == 'login':
        login(conta)
print('Até breve')
