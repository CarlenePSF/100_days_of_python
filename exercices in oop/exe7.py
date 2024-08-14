"""
Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro.
Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível.
"""
from datetime import date, datetime, timedelta

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)
        self.numero_de_emprestimos = 0

    def emprestimos(self):
        pass
        # return self.numero_de_emprestimos = 0



class Livro:
    def __init__(self, titulo, autor, numero_de_paginas, editora):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.editora = editora
        self.disponibilidade = True

    def emprestimo(self, data_de_emprestimo):
        self.disponibilidade = False

        data_devolucao = datetime.strptime(str(data_de_emprestimo)) + timedelta(15)

        print(f"Devolução em {data_devolucao}")
        return self.disponibilidade

    def devolucao(self):
        self.disponibilidade = True
        return self.disponibilidade

    def disponibilidade(self):
        pass



class FiccaoCientifica(Livro):
    pass

class AcademicoEstudos(Livro):
    def __init__(self, titulo, autor, numero_de_paginas, editora):
        super().__init__(titulo, autor, numero_de_paginas, editora)
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.editora = editora
        self.disponibilidade = True




livro_1 = AcademicoEstudos(
    "Python programming: An introduction to computer science",
    "John Zelle",
    554,
    "Franklin Beedle"
)
aluno = Aluno("Angela", 25, 'Baker-street 33, 000-000 England')
print(aluno.nome)
print(livro_1.disponibilidade)


