from passlib.hash import pbkdf2_sha256 as cryp


class Nome:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    @property
    def mostra_cpf(self):
        return f'Nome: {self.__nome} CPF: {self.__cpf}'


class Banco(Nome):

    def __init__(self, nome, sobrenome, cpf, numero, saldo, limite, senha):
        super().__init__(nome, sobrenome, cpf)
        self._destino__limite = limite
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__senha = cryp.hash(senha, rounds=2000000, salt_size=16)

    def verifica_senha(self, senha):
        if len(self.__senha) >= 5:
            if cryp.verify(senha, self.__senha):
                return True
            return False
        else:
            print('Senha precisa ter no mínimo 5 caracteres')

    def mostrar_cliente(self):
        return f'Cliente: {self.__nome} Número da conta: {self.__numero}'

    def mostrar_saldo(self):
        return f'O saldo de {self.__nome} é de R${self.__saldo}'

    def mostrar_limite(self):
        return f'O limite de {self.__nome} é de R${self.__limite}'

    def extrato(self):
        return f'O cliente {self.__nome}, Número da conta: {self.__numero} possui saldo de {self.__saldo} e limite de {self.__limite}'

    def depositar(self, valor):
        if self.verifica_senha(self.__senha) is True:
            if valor > 0:
                self.__saldo += valor
            else:
                print('Valor precisar ser maior que zero.')

    def sacar(self, valor):
        if self.verifica_senha(self.__senha) is True:
            if valor <= 10:
                print('Valor insuficiente, o valor de saque deve ser superior à R$10,00.')
            else:
                if self.__saldo >= valor:
                    self.__saldo -= valor
                    print("Saque feito com sucesso.")

    def transf(self, valor, destino):
        if self.verifica_senha(self.__senha) is True:
            if valor < self.__saldo:
                if valor > 0:
                    self.__saldo -= 1.05 * valor  # 5% de imposto por transferência
                    if valor < self._destino__limite:
                        destino.__saldo += valor
                        print('Transferência feito com sucesso.')
        else:
            print('Senha incorreta.')


