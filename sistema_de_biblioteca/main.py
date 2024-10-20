"""
Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro.
Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível.
"""
from sistema_de_biblioteca.src.data import acervo_livros
from sistema_de_biblioteca.src.pessoa import Aluno
from sistema_de_biblioteca.src.livro import Livro

acervo = list()

for index in range(len(acervo_livros)):
    titulo = acervo_livros[index]['titulo']
    autor = acervo_livros[index]['autor']
    numero_de_paginas = acervo_livros[index]['paginas']
    acervo.append(Livro(titulo, autor, numero_de_paginas))



# carregando os objetos para o nosso sistema - acervo de livros
livro_1 = acervo[0]
livro_2 = acervo[1]
livro_3 = acervo[2]
livro_4 = acervo[3]
livro_5 = acervo[4]


# um aluno que chega ao Balcao de empréstimos
aluno = Aluno(
    "Angela",
    25,
    'Baker-street 33, 000-000 England'
)

# Verificando a disponibilidade dos títulos

for i in range(len(acervo)):
    acervo[i].esta_disponivel(acervo[i].titulo)
print('\n')


# solicita o emprestimo de dois livros
aluno.emprestimos(livro_1.titulo)
livro_1.emprestimo(aluno.nome)

aluno.emprestimos(livro_2.titulo)
livro_2.emprestimo(aluno.nome)

print(f'{aluno.nome} possui {aluno.numero_de_emprestimos} empréstimos : {aluno.livros_sob_emprestimo}')


# o Aluno faz uma devolução
aluno.devolucao(aluno.livros_sob_emprestimo.index(livro_1.titulo))
livro_1.devolucao()

# checando que o livro agora está "disponível"
livro_1.esta_disponivel(livro_1.titulo)

# verificando quantos empréstimos a estudante ainda tem
print(f'{aluno.nome} possui {aluno.numero_de_emprestimos} empréstimos : {aluno.livros_sob_emprestimo}')
