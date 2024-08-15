"""
Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro.
Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível.
"""
from data import acervo_livros
from pessoa import Aluno
from livro import Livro

acervo = list()

for index in range(len(acervo_livros)):
    titulo = acervo_livros[index]['titulo']
    autor = acervo_livros[index]['autor']
    numero_de_paginas = acervo_livros[index]['paginas']
    acervo.append(Livro(titulo, autor, numero_de_paginas))



# Criando os objetos do nosso sistema - acervo de livros
livro_1 = acervo[0]
livro_2 = acervo[1]


# um aluno que chega ao Balcao de empréstimos
aluno = Aluno(
    "Angela",
    25,
    'Baker-street 33, 000-000 England'
)

# Verificando a disponibilidade dos títulos
livro_1.esta_disponivel(livro_1.titulo)
livro_2.esta_disponivel(livro_2.titulo)

# solicita o emprestimo de dois livros
aluno.emprestimos(livro_1.titulo)
livro_1.emprestimo(aluno.nome)

aluno.emprestimos(livro_2.titulo)
livro_2.emprestimo(aluno.nome)

print(f'{aluno.nome} possui {aluno.numero_de_emprestimos} empréstimos : {aluno.livros_sob_emprestimo}')



aluno.devolucao(aluno.livros_sob_emprestimo.index(livro_1.titulo))
livro_1.devolucao()
livro_1.esta_disponivel(livro_1.titulo)

print(f'{aluno.nome} possui {aluno.numero_de_emprestimos} empréstimos : {aluno.livros_sob_emprestimo}')
