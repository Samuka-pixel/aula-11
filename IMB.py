from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def calcular_bmi():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        bmi = peso / (altura ** 2)
        resultado = f"BMI: {bmi:.2f} - {classificar_bmi(bmi)}"
        label_resultado.config(text=resultado)
        atualizar_imagem(bmi)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def classificar_bmi(bmi):
    if bmi < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= bmi < 25:
        return "Peso normal"
    elif 25 <= bmi < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def atualizar_imagem(bmi):
    if bmi < 18.5:
        caminho_imagem = "baixo_peso.png"
    elif 18.5 <= bmi < 25:
        caminho_imagem = "peso_normal.png"
    elif 25 <= bmi < 30:
        caminho_imagem = "sobrepeso.png"
    else:
        caminho_imagem = "obesidade.png"

    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((150, 150), Image.Resampling.LANCZOS)
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.config(image=imagem_tk)
    label_imagem.image = imagem_tk

janela = Tk()
janela.title("Calculadora de BMI")

Label(janela, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_peso = Entry(janela)
entrada_peso.grid(row=0, column=1, padx=10, pady=5)

Label(janela, text="Altura (m):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada_altura = Entry(janela)
entrada_altura.grid(row=1, column=1, padx=10, pady=5)

botao_calcular = Button(janela, text="Calcular BMI", command=calcular_bmi)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = Label(janela, text="BMI: ")
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

label_imagem = Label(janela)
label_imagem.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()
