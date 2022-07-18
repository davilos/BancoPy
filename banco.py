from typing import List, Union, Optional
from time import sleep

from models.conta import Conta
from models.cliente import Cliente

contas: List[Conta] = list()


def main() -> None:
    menu()


def menu() -> None:
    print('\033[1;97m-='*40)
    print(" ATM ".center(80, '-'))
    print('-='*40)
    print("Geek Bank".center(80, '-'))
    print('-=\033[m'*40)

    print('Seleciona uma opção no menu:')
    print(
        '1 - Criar conta\n2 - Efetuar saque\n3 - Efetuar depósito\n'
        '4 - Efetuar transferência\n5 - Listar contas\n6 - Sair do sistema'
    )

    opcao: int = int(input())

    def switch(op: int) -> None:
        sw = {
            1: criar_conta,
            2: efetuar_saque_ou_deposito,
            3: efetuar_saque_ou_deposito,
            4: efetuar_transferencia,
            5: listar_contas,
            6: sair
        }
        try:
            return sw[op]()
        except KeyError:
            print('\033[31mOpção inválida!\033[m')
            sleep(2)
            menu()
        except TypeError:
            efetuar_saque_ou_deposito(op)
    switch(opcao)


def criar_conta() -> None:
    print('Informe os dados do cliente:')

    clt: Cliente = Cliente(
        input('Nome do cliente: '),
        input('Email do cliente: '),
        input('CPF do cliente: '),
        input('Data de nascimento do cliente: ')
    )

    cnt: Conta = Conta(clt)
    contas.append(cnt)

    print('Conta criada com sucesso.\nDados da conta:')
    print('-='*20)
    print(cnt)
    print(cnt.cliente)
    print('-='*20)
    sleep(2)
    menu()


def efetuar_saque_ou_deposito(opc: int) -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Optional[Conta] = buscar_conta_por_numero(numero)

        if conta:
            if opc == 2:
                valor_s: float = float(input('Informe o valor do saque: '))
                conta.sacar(valor_s)
            else:
                valor_d: float = float(input('Informe o valor do depósito: '))
                conta.depositar(valor_d)
        else:
            print(
                f'\033[31mNão foi encontrada a conta com número {numero}\033[m'
            )
    else:
        print('\033[31mAinda não existem contas cadastradas!\033[m')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))
        conta_o: Optional[Conta] = buscar_conta_por_numero(numero_o)

        numero_d: int = int(input('Informe o número da conta de destino: '))
        conta_d: Optional[Conta] = buscar_conta_por_numero(numero_d)

        if conta_o and conta_d:
            valor: float = float(input('Informe o valor da transferência: '))
            conta_o.transferir(conta_d, valor)
        else:
            print('\033[31mUma ou duas contas não foram encontradas!\033[m')
    else:
        print('\033[31mAinda não existem contas cadastradas!\033[m')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('-='*20)
        print('Listagem de contas'.center(40, '-'))

        for conta in contas:
            print(conta)
            print('-='*20)
            sleep(1)
    else:
        print('\033[31mAinda não existem contas cadastradas!\033[m')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Union[Conta, None]:
    c: Union[Conta, None] = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


def sair():
    print('Volte sempre!')
    sleep(2)
    exit(0)


if __name__ == '__main__':
    main()
