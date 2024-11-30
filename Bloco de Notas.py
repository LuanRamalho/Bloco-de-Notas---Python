import tkinter as tk
from tkinter import messagebox

# Função para atualizar o contador de linhas e caracteres
def atualizar_contadores():
    texto = text_area.get("1.0", "end-1c")  # Obtém o conteúdo da caixa de texto
    linhas = texto.splitlines()  # Separa o texto em linhas
    num_linhas = len(linhas)
    num_caracteres_com_espaco = len(texto)
    num_caracteres_sem_espaco = len(texto.replace(" ", ""))

    # Atualiza os rótulos com as contagens
    label_linhas.config(text=f"Linhas: {num_linhas}")
    label_caracteres_com_espaco.config(text=f"Caracteres (com espaços): {num_caracteres_com_espaco}")
    label_caracteres_sem_espaco.config(text=f"Caracteres (sem espaços): {num_caracteres_sem_espaco}")

# Função para salvar o conteúdo em um arquivo .txt
def salvar_arquivo():
    texto = text_area.get("1.0", "end-1c")
    if texto.strip() == "":
        messagebox.showwarning("Aviso", "O campo de texto está vazio.")
        return
    try:
        with open("bloco_de_notas.txt", "w") as file:
            file.write(texto)
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Bloco de Notas Colorido")
root.geometry("940x680")
root.config(bg="#2c3e50")

# Configuração da caixa de texto (Text Area)
text_area = tk.Text(
    root, wrap=tk.WORD, width=60, height=20,
    font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50",
    highlightbackground="#2980b9", highlightthickness=2
)
text_area.grid(row=0, column=1, padx=15, pady=15)
text_area.bind("<KeyRelease>", lambda event: atualizar_contadores())  # Atualiza contadores ao digitar

# Configuração do contador de linhas (Label)
label_linhas = tk.Label(
    root, text="Linhas: 0", font=("Arial", 12, "bold"),
    bg="#2c3e50", fg="#ecf0f1", anchor="w"
)
label_linhas.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

# Configuração do contador de caracteres com e sem espaços (Labels)
label_caracteres_com_espaco = tk.Label(
    root, text="Caracteres (com espaços): 0", font=("Arial", 12, "bold"),
    bg="#2c3e50", fg="#ecf0f1", anchor="w"
)
label_caracteres_com_espaco.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

label_caracteres_sem_espaco = tk.Label(
    root, text="Caracteres (sem espaços): 0", font=("Arial", 12, "bold"),
    bg="#2c3e50", fg="#ecf0f1", anchor="w"
)
label_caracteres_sem_espaco.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

# Botão para salvar o arquivo
botao_salvar = tk.Button(
    root, text="Salvar", command=salvar_arquivo,
    font=("Arial", 14, "bold"), bg="#27ae60", fg="white",
    activebackground="#2ecc71", activeforeground="white",
    relief="raised", bd=3
)
botao_salvar.grid(row=3, column=1, pady=20, padx=15)

# Adiciona uma moldura decorativa
moldura = tk.Frame(root, bg="#16a085", width=10, height=500)
moldura.grid(row=0, column=2, rowspan=4, sticky="ns")

# Inicia o programa
root.mainloop()
