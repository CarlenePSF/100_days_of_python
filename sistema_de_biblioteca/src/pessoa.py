class Pessoa:
    """This is a conceptual class representation of a user of the library

    :param nome: o nome do usuário
    :type nome: str
    :param idade: age of the person, defaults to None
    :type idade: str, optional
    :param endereco: his/her adress, defaults to None
    :type endereco: str, optional
    """

    # pessoa tem atributo, mas não tem métodos.
    def __init__(self, nome, idade=None, endereco=None):
        """Constructor method"""
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.numero_de_emprestimos = 0
        self.livros_sob_emprestimo = list()

    def emprestimos(self, titulo):
        """

        :param titulo: O título do livro
        :return: the number of books
        """
        self.numero_de_emprestimos += 1
        self.livros_sob_emprestimo.append(titulo)
        return self.numero_de_emprestimos

    def devolucao(self, titulo):
        """

        :param titulo:
        :return:
        """
        self.numero_de_emprestimos -= 1
        self.livros_sob_emprestimo.pop(titulo)
        return self.numero_de_emprestimos


class Aluno(Pessoa):
    """
    Classe Student
    """
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)
        self.numero_de_emprestimos = 0
        self.livros_sob_emprestimo = list()
        self.em_aula = False

    def esta_em_aula(self):
        self.em_aula = True
        return self.em_aula


class Servidor(Pessoa):
    """
    Class Servidor
    """
    def __init__(self, nome, idade, endereco):
        """

        :param nome:
        :param idade:
        :param endereco:
        """
        super().__init__(nome, idade, endereco)
        self.aposentado = False
        self.ativo = True
        self.de_ferias = False

    def esta_trabalhando(self):
        """

        :return:
        """
        return self.ativo

    def pedir_ferias(self):
        """

        :return:
        """
        self.de_ferias = True
        return self.de_ferias


class Professor(Pessoa):
    """
    class professor/teacher
    """
    def __init__(self, nome, idade, endereco):
        """

        :param nome:
        :param idade:
        :param endereco:
        """
        super().__init__(nome, idade, endereco)
        self.dando_aula = False

    def dando_aula(self):
        """

        :return:
        """
        self.dando_aula = True
        return self.dando_aula