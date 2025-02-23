def linha(texto):
    tamanho = len(texto)
    print('\033[97;42m' + '-' * tamanho + '\033[0m')
    print('\033[97;42m' + texto + '\033[0m')
    print('\033[97;42m' + '-' * tamanho + '\033[0m')


def funcaoint(a):
    while True:
        linha('SISTEMA DE AJUDA PYTHON')
        receber = input(a)
        msg = f'Acessando o manual do comando "{receber}"'
        tamanho = len(msg)
        if receber == 'fim':
            break
        print('\033[97;44m' + '-' * tamanho + '\033[0m')

        # Exibe a mensagem com fundo azul
        print('\033[97;44m' + msg + '\033[0m')

        # Exibe os traços novamente com fundo azul
        print('\033[97;44m' + '-' * tamanho + '\033[0m')
        print('\033[30;47m')
        help(receber)
        print('\033[0m')
    print('-' * tamanho)



f = funcaoint('Funcao ou biblioteca: ')
