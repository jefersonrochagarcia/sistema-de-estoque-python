import tkinter as tk
from tkinter import messagebox

# Dados de usuários
usuarios = [
    {"id": 1, "nome": "Administrador", "login": "admin", "senha": "123", "nivel": "administrador"},
    {"id": 2, "nome": "Operador", "login": "operador", "senha": "456", "nivel": "operador"}
]

# Dados de produtos
produtos = []

# Estilo global
FONTE_TITULO = ("Helvetica", 16, "bold")
FONTE_PADRAO = ("Helvetica", 12)
COR_FUNDO = "#f0f8ff"
COR_BOTAO = "#4CAF50"
COR_BOTAO_LISTA = "#2196F3"
COR_TEXTO_BOTAO = "white"

# Cadastro de produto
def cadastrar_produto():
    cadastro = tk.Toplevel(bg=COR_FUNDO)
    cadastro.title("Cadastro de Produto")

    campos = {}
    for campo in ["Nome", "Código", "Categoria", "Tamanho", "Quantidade", "Preço"]:
        tk.Label(cadastro, text=f"{campo}:", font=FONTE_PADRAO, bg=COR_FUNDO).pack(pady=2)
        entrada = tk.Entry(cadastro, font=FONTE_PADRAO)
        entrada.pack(pady=2)
        campos[campo] = entrada

    def salvar():
        try:
            produto = {
                "nome": campos["Nome"].get(),
                "codigo": campos["Código"].get(),
                "categoria": campos["Categoria"].get(),
                "tamanho": campos["Tamanho"].get(),
                "quantidade": int(campos["Quantidade"].get()),
                "preco": float(campos["Preço"].get())
            }
            produtos.append(produto)
            messagebox.showinfo("Sucesso", "✅ Produto cadastrado com sucesso!")
            cadastro.destroy()
        except ValueError:
            messagebox.showerror("Erro", "⚠️ Verifique os campos numéricos.")

    tk.Button(cadastro, text="Salvar", font=FONTE_PADRAO, bg=COR_BOTAO, fg=COR_TEXTO_BOTAO,
              height=2, width=20, command=salvar).pack(pady=10)

# Listagem de produtos
def listar_produtos():
    lista = tk.Toplevel(bg=COR_FUNDO)
    lista.title("Lista de Produtos")

    if not produtos:
        tk.Label(lista, text="⚠️ Nenhum produto cadastrado.", font=FONTE_PADRAO, bg=COR_FUNDO).pack(pady=10)
        return

    for i, p in enumerate(produtos, start=1):
        texto = (
            f"🔹 Produto {i}\n"
            f"  Nome: {p['nome']}\n"
            f"  Código: {p['codigo']}\n"
            f"  Categoria: {p['categoria']}\n"
            f"  Tamanho: {p['tamanho']}\n"
            f"  Quantidade: {p['quantidade']}\n"
            f"  Preço: R$ {p['preco']:.2f}\n"
            f"----------------------------------"
        )
        tk.Label(lista, text=texto, justify="left", font=FONTE_PADRAO, bg=COR_FUNDO).pack(anchor="w", padx=10, pady=5)

# Menu principal
def abrir_menu(nivel_acesso):
    menu = tk.Tk()
    menu.title("Sistema de Estoque")
    menu.configure(bg=COR_FUNDO)

    tk.Label(menu, text=f"Nível de acesso: {nivel_acesso}", font=FONTE_TITULO, bg=COR_FUNDO).pack(pady=10)

    tk.Button(menu, text="📦 Cadastrar Produto", font=FONTE_PADRAO, bg=COR_BOTAO, fg=COR_TEXTO_BOTAO,
              height=2, width=25, command=cadastrar_produto).pack(pady=10)

    tk.Button(menu, text="📋 Listar Produtos", font=FONTE_PADRAO, bg=COR_BOTAO_LISTA, fg=COR_TEXTO_BOTAO,
              height=2, width=25, command=listar_produtos).pack(pady=10)

    menu.mainloop()

# Função de login
def verificar_login():
    login = entrada_login.get()
    senha = entrada_senha.get()
    for usuario in usuarios:
        if usuario["login"] == login and usuario["senha"] == senha:
            messagebox.showinfo("Login", f"✅ Bem-vindo(a), {usuario['nome']}!")
            janela_login.destroy()
            abrir_menu(usuario["nivel"])
            return
    messagebox.showerror("Erro", "❌ Login ou senha incorretos.")

# Tela de login
janela_login = tk.Tk()
janela_login.title("Login do Sistema")
janela_login.configure(bg=COR_FUNDO)

tk.Label(janela_login, text="Login:", font=FONTE_PADRAO, bg=COR_FUNDO).pack(pady=5)
entrada_login = tk.Entry(janela_login, font=FONTE_PADRAO)
entrada_login.pack(pady=5)

tk.Label(janela_login, text="Senha:", font=FONTE_PADRAO, bg=COR_FUNDO).pack(pady=5)
entrada_senha = tk.Entry(janela_login, show="*", font=FONTE_PADRAO)
entrada_senha.pack(pady=5)

tk.Button(janela_login, text="Entrar", font=FONTE_PADRAO, bg="#FF5722", fg="white",
          height=2, width=20, command=verificar_login).pack(pady=15)

janela_login.mainloop()
