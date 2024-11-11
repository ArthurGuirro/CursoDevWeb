frase = input("Digite uma frase: ").lower()  

def contar_caracteres(frase):
    contagem = {}
    for char in frase:
        if char != " ": 
            contagem[char] = contagem.get(char, 0) + 1

    return contagem

contagem_caracteres = contar_caracteres(frase)
print("\nCaracteres repetidos:")

for char, qtd in contagem_caracteres.items():
    if qtd > 1:
        print(f"{char}: {qtd} vezes")
