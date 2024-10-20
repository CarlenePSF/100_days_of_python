from datetime import datetime, timedelta


class Livro:
    """
    This is a conceptual class representation for the books ina library

        :param titulo: the title of the book
        :type titulo: str
        :param autor: who wrote the book, defaults to None
        :type autor: str, optional
        :param numero_de_paginas: number of pages
        :type numero_de_paginas: str, optional
    """
    def __init__(self, titulo, autor, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.disponibilidade = True

    def emprestimo(self, pessoa):
        """

        :param pessoa:
        :return:
        """
        self.disponibilidade = False
        data_devolucao = datetime.today() + timedelta(15)
        print(f"{self.titulo} está emprestado para {pessoa}. Devolver em {data_devolucao.date()}.")

        return self.disponibilidade

    def devolucao(self):
        """

        :return:
        """
        self.disponibilidade = True
        return self.disponibilidade

    def esta_disponivel(self, titulo):
        """

        :param titulo:
        :return:
        """
        if self.disponibilidade:
            print(f"O livro {titulo} está disponível.")
        else:
            print(f"O livro {titulo} está indisponível.")