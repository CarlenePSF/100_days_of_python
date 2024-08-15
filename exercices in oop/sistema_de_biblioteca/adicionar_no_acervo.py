import ast


def salvar_livros(livros):
    with open('data.py', 'w') as arquivo_py:
        arquivo_py.write(f"livros = {livros}")


def carregar_livros():
    try:
        with open('data.py', 'r') as arquivo_py:
            conteudo = arquivo_py.read()
            if conteudo:
                return ast.literal_eval(conteudo.split('=')[1].strip())
    except FileNotFoundError:
        return []
    return []


def adicionar_livro(titulo, autor, paginas):
    livros = carregar_livros()
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas
    }
    livros.append(novo_livro)
    salvar_livros(livros)


def obter_dados_do_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    paginas = input("Número de páginas: ")
    return titulo, autor, paginas


def main():
    while True:
        print("\nAdicionar um novo livro")
        titulo, autor, paginas = obter_dados_do_livro()
        adicionar_livro(titulo, autor, paginas)

        continuar = input("Deseja adicionar outro livro? (s/n): ")
        if continuar.lower() != 's':
            break


if __name__ == "__main__":
    main()
