palavra = input("Digite uma palavra: ").lower()
vogais = 0
consoantes = 0

for letra in palavra:
    if letra.isalpha():  # Verifica se é uma letra
        if letra in "aeiou":
            vogais += 1
        else:
            consoantes += 1

print(f"A palavra contém {vogais} vogais e {consoantes} consoantes.")
