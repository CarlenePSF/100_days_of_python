class Pessoa:
    # pessoa tem atributo, mas não tem métodos.
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


class Aluno(Pessoa):
    """
    Herda de Pessoa os mesmo atributos
    """
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)
        self.numero_de_emprestimos = 0
        self.livros_sob_emprestimo = list()

    def emprestimos(self, titulo):
        self.numero_de_emprestimos += 1
        self.livros_sob_emprestimo.append(titulo)
        return self.numero_de_emprestimos

    def devolucao(self, titulo):
        self.numero_de_emprestimos -= 1
        self.livros_sob_emprestimo.pop(titulo)
        return self.numero_de_emprestimos