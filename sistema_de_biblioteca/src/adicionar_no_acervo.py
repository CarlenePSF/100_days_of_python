import streamlit as st
import ast


def salvar_livros(livros):
    """Função para salvar os livros em um arquivo tipo .py
    :param livros: nome do livro
    :return: None
    """
    with open('data.py', 'w') as arquivo_py:
        arquivo_py.write(f"acervo_livros = {repr(livros)}")



def carregar_livros():
    """Função para carregar os livros contidos no arquivo .py
    :return: list
    """
    try:
        with open('data.py', 'r') as arquivo_py:
            conteudo = arquivo_py.read()
            if conteudo:
                return ast.literal_eval(conteudo.split('=')[1].strip())
    except FileNotFoundError:
        return []
    return []


#
def adicionar_livro(titulo, autor, paginas):
    """Função para adicionar um novo livro
    :param titulo: str
    :param autor: str
    :param paginas: int
    :return: None
    """
    livros = carregar_livros()
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas
    }
    livros.append(novo_livro)
    salvar_livros(livros)



def main():
    """
    programa main que inicializa página do stream lit
    :return: None
    """
    # Interface Streamlit
    st.title("Gerenciador de Livros")

    st.header("Adicionar um novo livro")
    titulo = st.text_input("Título do livro")
    autor = st.text_input("Autor do livro")
    paginas = st.text_input("Número de páginas")

    if st.button("Adicionar Livro"):
        if titulo and autor and paginas:
            adicionar_livro(titulo, autor, paginas)
            st.success(f"Livro '{titulo}' adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

    st.header("Livros no acervo ")

    livros = carregar_livros()

    if livros:
        for livro in livros:
            st.write(f"**Título**: {livro['titulo']}")
            st.write(f"**Autor**: {livro['autor']}")
            st.write(f"**Páginas**: {livro['paginas']}")
            st.write("---")
    else:
        st.info("Nenhum livro adicionado ainda.")


if __name__ == "__main__":
    main()
