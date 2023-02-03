import os
import webbrowser
op = saldo = 0
while op != 5:          #MENU
    print('=-' * 15)
    print('         \033[31mLOJA ZINFE\033[m')
    print('=-' * 15)
    print('        \033[31mMENU PRODUTO\033[m')
    print('[ 1 ] Comprar jogos \033[32mXBOX ONE\033[m')          
    print('[ 2 ] Comprar \033[36mGIFT CARDS\033[m  (Desenvolvimento)')
    print('[ 3 ] Comprar jogos \033[34mPS4 e PS5\033[m')
    print('[ 4 ] Depositar saldo')
    print('[ 5 ] Fechar')
    op = int(input('Escolha sua opção: '))
    os.system('cls')
    if op == 1: #------XBOX------
        print('   \033[32mJOGOS XBOX ONE\033[m')
        print('[ 1 ] Forza Horizon 5  [R$249,00] ')
        print('[ 2 ] Red Dead Redemption 2 [R$249,95]')
        print('[ 3 ] Far Cry 6 [R$279,95]')
        print('[ 4 ] Voltar')
        op1 = int(input('Escolha o jogo para a compra: '))
        if op1 == 1:
            if saldo < 249.00:
                os.system('cls')
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                webbrowser.open('https://www.xbox.com/pt-br/games/store/forza-horizon-5-edicao-padrao/9nkx70bbcdrn')
                print('\033[32mCompra realizada com sucesso\033[m')
                print('\033[33mAbrindo navegador...\033[m')
        elif op1 == 2:
            if saldo < 249.95:
                os.system('cls')
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                webbrowser.open('https://www.xbox.com/pt-br/games/store/red-dead-redemption-2/9n2zdn7nwqkv')
                print('\033[32mCompra realizada com sucesso\033[m')
                print('\033[33mAbrindo navegador...\033[m')
        elif op1 == 3:
            if saldo < 279.95:
                os.system('cls')
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                webbrowser.open('https://www.xbox.com/pt-BR/games/far-cry-6')
                print('\033[32mCompra realizada com sucesso\033[m')
                print('\033[33mAbrindo navegador...\033[m')
        elif op1 == 4:
            os.system('cls')
        else:
            os.system('cls')
            print('\033[31mOpção inválida!, Tente novamente\033[m')
    elif op == 2: #-----GIFT CARD------
        os.system('cls')
        print('Em desenvolvimento')                       
    elif op == 3: #------PS4-----
        print('   \033[34mJOGOS PS4 e PS5\033[m')              
        print('[ 1 ] God of War Ragnarok [R$349,90]')
        print('[ 2 ] Grand Theft Auto V [R$R$299,90]')
        print('[ 3 ] Spider-Man: Miles Morales [R$R$99,80]')
        print('[ 4 ] Voltar')
        op3 = int(input('Escolha o jogo que deseja comprar: '))
        if op3 == 1:
            if saldo < 349.90:
                os.system('cls')
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                webbrowser.open('https://www.playstation.com/pt-br/games/god-of-war-ragnarok/')
                print('\033[32mCompra realizada com sucesso\033[m')
                print('\033[33mAbrindo navegador...\033[m')
        elif op3 == 2:
            if saldo < 299.90:
                os.system('cls')
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                webbrowser.open('https://store.playstation.com/pt-br/product/UP1004-PPSA03420_00-GTAVCROSSGENBUND')
                print('\033[32mCompra realizada com sucesso\033[m')
                print('\033[33mAbrindo navegador...\033[m')
        elif op3 == 3:
            if saldo < 99.80:
                os.system('cls')
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                webbrowser.open('https://www.playstation.com/pt-br/games/marvels-spider-man-miles-morales/')
                print('\033[32mCompra realizada com sucesso\033[m')
                print('\033[33mAbrindo navegador...\033[m')
        elif op3 == 4:
            os.system('cls')
        else:
            os.system('cls')
            print('\033[31mOpção inválida!, Tente novamente\033[m')
    elif op == 4: #----DEPOSITAR----
        saldo = float(input('Quanto você deseja depositar no app? R$'))
        print(f'\033[32mVocê depositou R${saldo:.2f}\033[m')
    elif op != 5:
        print('\033[31mOpção inválida!, Tente novamente\033[m')
