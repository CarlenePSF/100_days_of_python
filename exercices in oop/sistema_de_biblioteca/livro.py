from datetime import datetime, timedelta


class Livro:
    def __init__(self, titulo, autor, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.disponibilidade = True

    def emprestimo(self, pessoa):
        self.disponibilidade = False
        data_devolucao = datetime.today() + timedelta(15)
        print(f"{self.titulo} está emprestado para {pessoa}. Devolver em {data_devolucao.date()}.")

        return self.disponibilidade

    def devolucao(self):
        self.disponibilidade = True
        return self.disponibilidade

    def esta_disponivel(self, titulo):
        if self.disponibilidade:
            print(f"O livro {titulo} está disponível.")
        else:
            print(f"O livro {titulo} está indisponível.")


# class AcademicoEstudos(Livro):
#     """
#     Herda de livro os mesmo atributos
#     """
#     def __init__(self, titulo, autor, numero_de_paginas):
#         super().__init__(titulo, autor, numero_de_paginas)
#         self.disponibilidade = True