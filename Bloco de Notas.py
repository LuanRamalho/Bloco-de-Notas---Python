import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Função para atualizar os contadores de linhas e caracteres
def atualizar_contadores(event=None):
    texto = text_area.get("1.0", "end-1c")  # Obtém o conteúdo da caixa de texto
    linhas = texto.splitlines()  # Separa o texto em linhas
    num_linhas = len(linhas)
    num_caracteres_com_espaco = len(texto)
    num_caracteres_sem_espaco = len(texto.replace(" ", ""))

    # Atualiza os rótulos com as contagens
    label_linhas.config(text=f"Linhas: {num_linhas}")
    label_caracteres_com_espaco.config(text=f"Caracteres (com espaços): {num_caracteres_com_espaco}")
    label_caracteres_sem_espaco.config(text=f"Caracteres (sem espaços): {num_caracteres_sem_espaco}")

    # Atualiza a posição do cursor
    atualizar_posicao_cursor()

# Função para atualizar a posição do cursor
def atualizar_posicao_cursor(event=None):
    linha, coluna = text_area.index(tk.INSERT).split(".")  # Obtém linha e coluna
    label_posicao_cursor.config(text=f"Linha: {linha}, Coluna: {int(coluna)+1}")  # Coluna é 0-based

# Função para salvar o conteúdo em um arquivo .txt
def salvar_arquivo():
    texto = text_area.get("1.0", "end-1c")
    if texto.strip() == "":
        messagebox.showwarning("Aviso", "O campo de texto está vazio.")
        return

    # Abre a caixa de diálogo para escolher onde salvar o arquivo
    caminho_arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        title="Salvar como"
    )
    
    if not caminho_arquivo:  # Se o usuário cancelar, o caminho será uma string vazia
        return

    try:
        with open(caminho_arquivo, "w") as file:
            file.write(texto)
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Bloco de Notas")
root.geometry("940x680")
root.config(bg="#2c3e50")

# Frame para os rótulos superiores
label_frame = tk.Frame(root, bg="#34495e")
label_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

# Configuração dos rótulos no frame
label_linhas = tk.Label(
    label_frame, text="Linhas: 0", font=("Arial", 12, "bold"),
    bg="#34495e", fg="#ecf0f1", anchor="w", width=15
)
label_linhas.pack(side="left", padx=5, pady=5)

label_caracteres_com_espaco = tk.Label(
    label_frame, text="Caracteres (com espaços): 0", font=("Arial", 12, "bold"),
    bg="#34495e", fg="#ecf0f1", anchor="w", width=25
)
label_caracteres_com_espaco.pack(side="left", padx=5, pady=5)

label_caracteres_sem_espaco = tk.Label(
    label_frame, text="Caracteres (sem espaços): 0", font=("Arial", 12, "bold"),
    bg="#34495e", fg="#ecf0f1", anchor="w", width=25
)
label_caracteres_sem_espaco.pack(side="left", padx=5, pady=5)

label_posicao_cursor = tk.Label(
    label_frame, text="Linha: 1, Coluna: 1", font=("Arial", 12, "bold"),
    bg="#34495e", fg="#ecf0f1", anchor="w", width=20
)
label_posicao_cursor.pack(side="right", padx=5, pady=5)

# Frame principal para área de texto
text_frame = tk.Frame(root, bg="#2c3e50")
text_frame.grid(row=1, column=0, padx=15, pady=10, sticky="nsew")

# Configuração da barra de rolagem
scrollbar = tk.Scrollbar(text_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Configuração da área de texto
text_area = tk.Text(
    text_frame, wrap=tk.WORD, font=("Arial", 14),
    bg="#ecf0f1", fg="#2c3e50", yscrollcommand=scrollbar.set
)
text_area.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text_area.yview)

# Atualizações automáticas
text_area.bind("<KeyRelease>", atualizar_contadores)
text_area.bind("<ButtonRelease-1>", atualizar_posicao_cursor)

# Botão para salvar
botao_salvar = tk.Button(
    root, text="Salvar", command=salvar_arquivo,
    font=("Arial", 14, "bold"), bg="#27ae60", fg="white",
    activebackground="#2ecc71", activeforeground="white",
    relief="raised", bd=3
)
botao_salvar.grid(row=2, column=0, pady=10, padx=15, sticky="nsew")

# Permite que os widgets se expandam ao redimensionar a janela
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Atualiza contadores no início
atualizar_contadores()

# Inicia o programa
root.mainloop()
