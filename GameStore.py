import webbrowser
from ulti import *

op = saldo = nsaldo = start = 0

start_menu()

while op != 5:  # [ 2 ] MENU
    cabeçalho('      \033[31mGAME STORE ZINFEX\033[m')
    cabeçalho(f'      \033[32mSeu saldo: R${nsaldo:.2f}\033[m')
    print('        \033[31mMENU PRODUTO\033[m')
    print('[ 1 ] Comprar jogos \033[32mXBOX ONE\033[m')
    print('[ 2 ] Comprar \033[36mGIFT CARDS\033[m')
    print('[ 3 ] Comprar jogos \033[34mPS4 e PS5\033[m')
    print('[ 4 ] Depositar saldo')
    print('[ 5 ] Fechar')
    op = leiaint('Escolha sua opção: ')
    clear()

    if op == 1:  # ------ [ 2.1 ] XBOX------
        print('   \033[32mJOGOS XBOX ONE\033[m')
        print('[ 1 ] Forza Horizon 5  [R$249,00] ')
        print('[ 2 ] Red Dead Redemption 2 [R$249,95]')
        print('[ 3 ] Far Cry 6 [R$279,95]')
        print('[ 4 ] Voltar')
        op1 = leiaint('Escolha o jogo para a compra: ')
        if op1 == 1:
            if nsaldo < 249.00:
                clear()
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                cobrar(249)
                webbrowser.open(
                    'https://www.xbox.com/pt-br/games/store/forza-horizon-5-edicao-padrao/9nkx70bbcdrn')
        elif op1 == 2:
            if nsaldo < 249.95:
                clear()
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                cobrar(249.95)
                webbrowser.open(
                    'https://www.xbox.com/pt-br/games/store/red-dead-redemption-2/9n2zdn7nwqkv')
        elif op1 == 3:
            if nsaldo < 279.95:
                clear()
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                cobrar(279.95)
                webbrowser.open('https://www.xbox.com/pt-BR/games/far-cry-6')
        elif op1 == 4:
            clear()
        else:
            clear()
            print('\033[31mOpção inválida!, Tente novamente\033[m')

    elif op == 2:  # ----- [ 2.1 ] GIFT CARD------
        print('   \033[36mGIFT CARDS\033[m')
        print('[ 1 ] Xbox Live Gold')
        print('[ 2 ] PlayStation Store (Desenvolvimento)')
        print('[ 3 ] Steam Gift Card (Desenvolvimento)')
        print('[ 4 ] Voltar')
        op2 = leiaint('Escolha o Gift Card para a compra: ')
        if op2 == 1:
            valor = int(
                leiafloat('Digite o valor do Gift Card que deseja comprar: R$'))
            if nsaldo < valor:
                clear()
                print('\033[31mSaldo insuficiente\033[m')
            elif valor == 5:
                cobrar(5)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266963/gift-card-xbox-5-reais-codigo-digital')
            elif valor == 10:
                cobrar(10)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266964/gift-card-xbox-10-reais-codigo-digital')
            elif valor == 20:
                cobrar(20)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266969/gift-card-xbox-20-reais-codigo-digital')
            elif valor == 25:
                cobrar(25)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266970/gift-card-xbox-25-reais-codigo-digital')
            elif valor == 40:
                cobrar(40)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266971/gift-card-xbox-40-reais-codigo-digital')
            elif valor == 50:
                cobrar(50)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266930/gift-card-xbox-50-reais-codigo-digital')
            elif valor == 60:
                cobrar(60)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266972/gift-card-xbox-60-reais-codigo-digital')
            elif valor == 100:
                cobrar(100)
                webbrowser.open(
                    'https://www.kabum.com.br/produto/266928/gift-card-xbox-100-reais-codigo-digital')
            else:
                print('\033[31mEste valor não está disponível\033[m')
        if op2 == 4:
            clear()

    elif op == 3:  # ------ [ 2.1 ] PS4-----
        print('   \033[34mJOGOS PS4 e PS5\033[m')
        print('[ 1 ] God of War Ragnarok [R$349,90]')
        print('[ 2 ] Grand Theft Auto V [R$R$299,90]')
        print('[ 3 ] Spider-Man: Miles Morales [R$R$99,80]')
        print('[ 4 ] Voltar')
        op3 = leiaint('Escolha o jogo que deseja comprar: ')
        if op3 == 1:
            if nsaldo < 349.90:
                clear()
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                cobrar(349.90)
                webbrowser.open(
                    'https://www.playstation.com/pt-br/games/god-of-war-ragnarok/')
        elif op3 == 2:
            if nsaldo < 299.90:
                clear()
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                cobrar(299.90)
                webbrowser.open(
                    'https://store.playstation.com/pt-br/product/UP1004-PPSA03420_00-GTAVCROSSGENBUND')
        elif op3 == 3:
            if nsaldo < 99.80:
                clear()
                print('\033[31mSaldo Insuficiente\033[m')
            else:
                cobrar(99.80)
                webbrowser.open(
                    'https://www.playstation.com/pt-br/games/marvels-spider-man-miles-morales/')
        elif op3 == 4:
            clear()
        else:
            clear()
            print('\033[31mOpção inválida!, Tente novamente\033[m')

    elif op == 4:  # ---- [ 2.1 ] DEPOSITAR----
        saldo = leiafloat('Quanto você deseja depositar no app? R$')
        nsaldo += saldo
        print(f'\033[32mVocê depositou R${saldo:.2f}\033[m')

    elif op != 5:
        print('\033[31mOpção inválida!, Tente novamente\033[m')
