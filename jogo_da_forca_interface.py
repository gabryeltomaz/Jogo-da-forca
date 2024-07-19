import tkinter as tk
from tkinter import messagebox
import random

# Lista de palavras para o jogo
palavras = ["cachorro", "gato", "cavalo", "pato", "tatu", "leao", "urso", "peixe"]

class ForcaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Forca")
        self.master.geometry("400x300")
        
        self.palavra_secreta = random.choice(palavras)
        self.letras_acertadas = ["_"] * len(self.palavra_secreta)
        self.letras_erradas = []
        self.tentativas = 6
        
        self.create_widgets()
        self.update_display()
        
    def create_widgets(self):
        self.rotulo_palavra = tk.Label(self.master, text="Palavra:", font=("Helvetica", 16))
        self.rotulo_palavra.pack(pady=10)
        
        self.display_palavra = tk.Label(self.master, text=" ".join(self.letras_acertadas), font=("Helvetica", 16))
        self.display_palavra.pack(pady=10)
        
        self.rotulo_tentativas = tk.Label(self.master, text=f"Tentativas restantes: {self.tentativas}", font=("Helvetica", 14))
        self.rotulo_tentativas.pack(pady=10)
        
        self.rotulo_letra = tk.Label(self.master, text="Digite uma letra:", font=("Helvetica", 14))
        self.rotulo_letra.pack(pady=5)
        
        self.entrada_letra = tk.Entry(self.master, font=("Helvetica", 14))
        self.entrada_letra.pack(pady=5)
        
        self.botao_adivinhar = tk.Button(self.master, text="Adivinhar", command=self.adivinhar_letra, font=("Helvetica", 14))
        self.botao_adivinhar.pack(pady=10)
        
        self.display_erradas = tk.Label(self.master, text="Letras erradas: " + ", ".join(self.letras_erradas), font=("Helvetica", 12))
        self.display_erradas.pack(pady=10)
    
    def update_display(self):
        self.display_palavra.config(text=" ".join(self.letras_acertadas))
        self.rotulo_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.display_erradas.config(text="Letras erradas: " + ", ".join(self.letras_erradas))
    
    def adivinhar_letra(self):
        letra = self.entrada_letra.get().lower()
        
        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Entrada invalida", "Por favor, digite uma letra valida.")
            return
        
        if letra in self.letras_acertadas or letra in self.letras_erradas:
            messagebox.showwarning("Letra ja tentada", "Você ja tentou essa letra tente outra.")
            return
        
        if letra in self.palavra_secreta:
            for index, char in enumerate(self.palavra_secreta):
                if char == letra:
                    self.letras_acertadas[index] = letra
        else:
            self.letras_erradas.append(letra)
            self.tentativas -= 1
        
        self.entrada_letra.delete(0, tk.END)
        self.update_display()
        
        if "_" not in self.letras_acertadas:
            messagebox.showinfo("Voce venceu!!", f"Parabéns! A palavra era: {self.palavra_secreta}")
            self.master.destroy()
        elif self.tentativas == 0:
            messagebox.showinfo("Voce perdeu!!", f"Que pena! A palavra era: {self.palavra_secreta}")
            self.master.destroy()

# Configuração da janela principal
root = tk.Tk()
app = ForcaGame(root)
root.mainloop()
