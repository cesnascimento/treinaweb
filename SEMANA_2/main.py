from cachorro import Cachorro
from gato import Gato
from animal import Animal
from dono import Dono

lista_cachorro = list()
lista_gato = list()

while True:
    print(20*'-')
    print('1. Cadastrar usuário')
    print('2. Cadastrar cachorro')
    print('3. Cadastrar gato')
    print('4. Listar cachorros')
    print('5. Listar gatos')
    print('6. Brincar com cachorros')
    print('7. Brincar com gatos')
    print('8. Sair')
    print(20*'-')
    opcao = int(input('Escolha a opção: '))
    global dono

    if opcao == 1:
        nome_usuario = input('Digite o nome do usuário: ')
        dono = Dono(nome_usuario)
    elif opcao == 2:
        nome_cachorro = input('Digite o nome do cachorro: ')
        idade_cachorro = input('Digite a idade do cachorro: ')
        cor_cachorro = input('Digite a cor do cachorro: ')
        qtd_brinquedos_cachorro = input('Digite a quantidade de brinquedos do cachorro: ')
        cachorro = Cachorro(nome_cachorro, idade_cachorro, cor_cachorro, qtd_brinquedos_cachorro)
        lista_cachorro.append(cachorro)
        print(lista_cachorro[0])
    elif opcao == 3:
        nome_gato = input('Digite o nome do gato: ')
        idade_gato = input('Digite a idade do gato: ')
        cor_gato = input('Digite a cor do gato: ')
        qtd_bolinhas_gato = input('Digite a quantidade de brinquedos do gato: ')
        gato = Gato(nome_gato, idade_gato, cor_gato, qtd_bolinhas_gato)
        lista_gato.append(gato)
        print(lista_gato)
    elif opcao == 4:
        for cachorro in lista_cachorro:
            print(cachorro)
    elif opcao == 5:
        for gato in lista_gato:
            print(gato)
    
    else:
        break