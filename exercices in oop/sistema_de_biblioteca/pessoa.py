class Pessoa:
    # pessoa tem atributo, mas não tem métodos.
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
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


class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)
        self.em_aula = False

    def esta_em_aula(self):
        self.em_aula = True
        return self.em_aula


class Servidor(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)
        self.aposentado = False
        self.ativo = True
        self.de_ferias = False

    def esta_trabalhando(self):
        return self.ativo

    def pedir_ferias(self):
        self.de_ferias = True
        return self.de_ferias


class Professor(Pessoa, Servidor):
    def __init__(self, nome, idade, endereco, aposentado, ativo, de_ferias):
        super().__init__(nome, idade, endereco)
        super().__init__(aposentado, ativo, de_ferias)
        self.dando_aula = False

    def dando_aula(self):
        self.dando_aula = True
        return self.dando_aula