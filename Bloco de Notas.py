import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Função para atualizar os contadores de linhas, caracteres e números das linhas
def atualizar_contadores(event=None):
    texto = text_area.get("1.0", "end-1c")  # Obtém o conteúdo da caixa de texto
    linhas = texto.splitlines()  # Separa o texto em linhas
    num_linhas = len(linhas)
    num_caracteres_com_espaco = len(texto)
    num_caracteres_sem_espaco = len(texto.replace(" ", ""))

    # Atualiza os rótulos com as contagens
    label_caracteres_com_espaco.config(text=f"Caracteres (com espaços): {num_caracteres_com_espaco}")
    label_caracteres_sem_espaco.config(text=f"Caracteres (sem espaços): {num_caracteres_sem_espaco}")

    # Atualiza os números de linha
    atualizar_numeros_linhas()

# Função para exibir os números das linhas
def atualizar_numeros_linhas():
    texto_linhas = ""
    for i in range(1, int(text_area.index("end").split(".")[0])):
        texto_linhas += f"{i}\n"
    linha_numbers.config(state="normal")
    linha_numbers.delete("1.0", "end")
    linha_numbers.insert("1.0", texto_linhas)
    linha_numbers.config(state="disabled")

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
root.title("Bloco de Notas Colorido")
root.geometry("940x680")
root.config(bg="#2c3e50")

# Frame para a numeração de linhas e a área de texto
text_frame = tk.Frame(root, bg="#2c3e50")
text_frame.grid(row=0, column=1, padx=15, pady=15)

# Configuração da numeração de linhas
linha_numbers = tk.Text(
    text_frame, width=4, height=20, font=("Arial", 14),
    bg="#bdc3c7", fg="#2c3e50", state="disabled"
)
linha_numbers.pack(side="left", fill="y")

# Configuração da caixa de texto (Text Area)
text_area = tk.Text(
    text_frame, wrap=tk.WORD, width=60, height=20,
    font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50",
    highlightbackground="#2980b9", highlightthickness=2
)
text_area.pack(side="right", fill="both", expand=True)
text_area.bind("<KeyRelease>", atualizar_contadores)  # Atualiza contadores e números de linha ao digitar

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

# Inicializa os números de linha
atualizar_numeros_linhas()

# Inicia o programa
root.mainloop()
