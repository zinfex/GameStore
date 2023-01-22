import webbrowser

print('=-' * 15)
print('         \033[31mLOJA ZINFE\033[m')
print('=-' * 15)

print('   \033[31mTABELA DE PRODUTOS\033[m')
print('[ 1 ] Comprar jogos \033[32mXBOX ONE\033[m')
print('[ 2 ] Comprar \033[36mGIFT CARDS\033[m')
print('[ 3 ] Comprar jogos \033[34mPS4 e PS5\033[m')
op = int(input('Escolha sua opção: '))

if op == 1:
    print('   \033[32mJOGOS XBOX ONE\033[m')

elif op == 2:
    print('   \033[36mGIFT CARDS\033[m')
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
elif op == 3:
    print('   \033[34mJOGOS PS4 e PS5\033[m')
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
else:
    print('\033[31mOpção inválida!, Tente novamente\033[m')

