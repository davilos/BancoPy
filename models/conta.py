from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:

    codigo: int = 1001

    def __init__(self, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self) -> str:
        return f'Número da conta: {self.numero}\nCliente: {self.cliente.nome}' \
         f'\nSaldo total: {formata_float_str_moeda(self.saldo_total)}'

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self) -> float:
        return self.saldo + self.limite

    def depositar(self, valor_depositar: float) -> None:
        if valor_depositar > 0:
            self.saldo += valor_depositar
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!')
        else:
            print('\033[31mErro ao efetuar depósito. Tente novamente.\033[m')

    def sacar(self, valor_sacar: float) -> None:
        if 0 < valor_sacar <= self.saldo_total:
            if self.saldo >= valor_sacar:
                self.saldo -= valor_sacar
                self.saldo_total = self._calcula_saldo_total
            else:
                restante_saque: float = self.saldo - valor_sacar
                self.limite += restante_saque
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso!')
        else:
            print('\033[31mErro ao efetuar saque. Tente novamente.\033[m')

    def transferir(self, destino, valor_transferir: float) -> None:
        if 0 < valor_transferir <= self.saldo_total:
            if self.saldo >= valor_transferir:
                self.saldo -= valor_transferir
                self.saldo_total = self._calcula_saldo_total
                destino.saldo += valor_transferir
                destino.saldo_total = destino._calcula_saldo_total
            else:
                restante_transferencia: float = self.saldo - valor_transferir
                self.limite += restante_transferencia
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                destino.saldo += valor_transferir
                destino.saldo_total = destino._calcula_saldo_total
            print(
                f'Transferência para {destino.cliente.nome} '
                'efetuada com sucesso!'
            )
        else:
            print(
                '\033[31mTransferência não realizada. Tente novamente!\033[m'
            )
