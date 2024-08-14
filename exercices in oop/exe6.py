"""
6. Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o número da conta,
nome do titular e saldo. Adicione métodos para realizar depósitos e saques.


"""

class ContaBancaria:
    def __init__(self, nome_titular, numero_da_conta):
        self.nome_titular = nome_titular
        self.numero_da_conta = numero_da_conta
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo


cliente_1 = ContaBancaria('Jack', "001")
print(f'Cliente:{cliente_1.nome_titular}')
print("Saldo atual:", cliente_1.saldo)

deseja_depositar = True

while deseja_depositar:
    quantia = float(input("Digite o quantia para deposito: "))
    cliente_1.depositar(quantia)
    print("Saldo após depósito:", cliente_1.saldo)
    novo_deposito = input('Deseja fazer outro deposito (S/N)?').lower()
    if novo_deposito == 'n':
        deseja_depositar = False
        print("Fim da transação. Novo saldo :", cliente_1.saldo)