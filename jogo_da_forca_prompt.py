import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "forca", "desafio", "desenvolvimento"]

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras)
letras_acertadas = ["_"] * len(palavra_secreta)
letras_erradas = []
tentativas = 6

print("Bem-vindo ao jogo da Forca!")
print("Adivinhe a palavra:")
print(" ".join(letras_acertadas))

while tentativas > 0 and "_" in letras_acertadas:
    letra = input("Digite uma letra: ").lower()
    
    if len(letra) != 1:
        print("Por favor, digite apenas uma letra.")
        continue

    if letra in letras_acertadas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra_secreta:
        for index, char in enumerate(palavra_secreta):
            if char == letra:
                letras_acertadas[index] = letra
        print("Boa! Você acertou uma letra.")
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")

    print("Palavra: " + " ".join(letras_acertadas))
    print("Letras erradas: " + ", ".join(letras_erradas))

if "_" not in letras_acertadas:
    print("Parabéns! Você ganhou! A palavra era:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
