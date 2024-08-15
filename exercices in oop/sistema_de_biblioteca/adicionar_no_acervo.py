import streamlit as st
import ast

# Função para salvar os livros em um arquivo .py
def salvar_livros(livros):
    with open('data.py', 'w') as arquivo_py:
        arquivo_py.write(f"livros = {repr(livros)}")

# Função para carregar os livros do arquivo .py
def carregar_livros():
    try:
        with open('data.py', 'r') as arquivo_py:
            conteudo = arquivo_py.read()
            if conteudo:
                return ast.literal_eval(conteudo.split('=')[1].strip())
    except FileNotFoundError:
        return []
    return []

# Função para adicionar um novo livro
def adicionar_livro(titulo, autor, paginas):
    livros = carregar_livros()
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas
    }
    livros.append(novo_livro)
    salvar_livros(livros)




def main():
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
