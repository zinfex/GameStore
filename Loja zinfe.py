import os
import webbrowser
op = 0
while op != 4:
    print('=-' * 15)
    print('         \033[31mLOJA ZINFE\033[m')
    print('=-' * 15)
    print('   \033[31mTABELA DE PRODUTOS\033[m')
    print('[ 1 ] Comprar jogos \033[32mXBOX ONE\033[m')          #MENU
    print('[ 2 ] Comprar \033[36mGIFT CARDS\033[m')
    print('[ 3 ] Comprar jogos \033[34mPS4 e PS5\033[m')
    print('[ 4 ] Sair')
    op = int(input('Escolha sua opção: '))
    os.system('cls')
    if op == 1:
        print('   \033[32mJOGOS XBOX ONE\033[m')                   #XBOX
        print('[ 1 ] Forza Horzin 5')
        print('[ 2 ] Red Dead Redemption 2')
        print('[ 3 ] Far Cry 6')
        op1 = int(input('Escolha o jogo para a compra: '))
        if op1 == 1:
            webbrowser.open('https://www.xbox.com/pt-br/games/store/forza-horizon-5-edicao-padrao/9nkx70bbcdrn')
        elif op1 == 2:
            webbrowser.open('https://www.xbox.com/pt-br/games/store/red-dead-redemption-2/9n2zdn7nwqkv')
        elif op1 == 3:
            webbrowser.open('https://www.xbox.com/pt-BR/games/far-cry-6')
        print('\033[33mAbrindo navegador...\033[m')
        exit()
    elif op == 2:
        print('   \033[36mGIFT CARDS\033[m')                       #GIFT CARD
        print('[ 1 ] Xbox Live Gold')
        print('[ 2 ] PlayStation Store')
        print('[ 3 ] Steam Gift Card')
        op2 = int(input('Escolha o Gift Card para a compra: '))
        if op2 == 1:
            valor = int(input('Digite o valor do Gift Card que deseja comprar: R$'))
            if valor == 5:
                webbrowser.open('https://www.kabum.com.br/produto/266963/gift-card-xbox-5-reais-codigo-digital')
            elif valor == 10:
                webbrowser.open('https://www.kabum.com.br/produto/266964/gift-card-xbox-10-reais-codigo-digital')
            elif valor == 20:
                webbrowser.open('https://www.kabum.com.br/produto/266969/gift-card-xbox-20-reais-codigo-digital')
            elif valor == 25:
                webbrowser.open('https://www.kabum.com.br/produto/266970/gift-card-xbox-25-reais-codigo-digital')
            elif valor == 40:
                webbrowser.open('https://www.kabum.com.br/produto/266971/gift-card-xbox-40-reais-codigo-digital')
            elif valor == 50:
                webbrowser.open('https://www.kabum.com.br/produto/266930/gift-card-xbox-50-reais-codigo-digital')
            elif valor == 60:
                webbrowser.open('https://www.kabum.com.br/produto/266972/gift-card-xbox-60-reais-codigo-digital')
            elif valor == 100:
                webbrowser.open('https://www.kabum.com.br/produto/266928/gift-card-xbox-100-reais-codigo-digital')
            elif valor == 200:
                webbrowser.open('https://www.kabum.com.br/produto/266929/gift-card-xbox-200-reais-codigo-digital')
            else:
                print('\033[31mEste valor não está disponível\033[m')
                exit()
    elif op == 3:
        print('   \033[34mJOGOS PS4 e PS5\033[m')               #PS4
        print('[ 1 ] God of War Ragnarok')
        print('[ 2 ] Grand Theft Auto V')
        print('[ 3 ] Spider-Man: Miles Morales')
        op3 = int(input('Escolha o jogo que deseja comprar: '))
        if op3 == 1:
            webbrowser.open('https://www.playstation.com/pt-br/games/god-of-war-ragnarok/')
        if op3 == 2:
            webbrowser.open('https://store.playstation.com/pt-br/product/UP1004-PPSA03420_00-GTAVCROSSGENBUND')
        if op3 == 3:
            webbrowser.open('https://www.playstation.com/pt-br/games/marvels-spider-man-miles-morales/')
        print('\033[33mAbrindo navegador...\033[m')
        exit()
    elif op != 4:
        print('\033[31mOpção inválida!, Tente novamente\033[m')
