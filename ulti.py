import os


def clear():
    """Limpa a tela do console."""
    os.system('cls')


def start_menu():
    """Exibe o menu inicial e aguarda a escolha do usuário."""
    while True:
        print("DIGITE:\n[ 1 ] PARA INCIAR\n[ 2 ] PARA FECHAR")
        start = leiaint('Sua opção: ')
        if start == 2:
            exit()
        clear()
        if start == 1:
            return
        print('\033[31mOpção inválida!, Tente novamente\033[m')


def cobrar(valor):
    """Cobrar valor do produto e tira do saldo do usuário 
        E imprimi a mensagem de compra"""
    global nsaldo
    nsaldo -= valor
    print(f'\033[32mCompra de R${valor:.2f} realizada com sucesso\033[m')
    print('\033[33mAbrindo navegador...\033[m')


def linha():
        print ("-" * 30)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close


def leiaint(msg):
    """LER PERGUNTAS INT"""
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um valor válido\033[m')
            continue


def leiafloat(txt):
    """LER PERGUNTAS FLOAT"""
    while True:
        try:
            n = float(input(txt))
            return n
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um valor válido\033[m')
            continue


def cabeçalho(txt):
    linha()
    print(txt.center(30))
    linha()
