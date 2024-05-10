alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'

def gerador():

    contador = [0]

    def incrementador():

        contador[0] += 1
        return contador[0]

    return incrementador

# Chama a função gerador uma vez antes do loop iniciar
funcao_gerador = gerador()

def transformador(frase):

    cifrada = ''

    for carac in frase:

        if carac in alfabeto_original:
            index_carac = alfabeto_original.index(carac)

            # Chama a função de incremento
            num = funcao_gerador()

            index_novo = (index_carac + num) % len(alfabeto_original)
            carac_cifra = alfabeto_original[index_novo]
            cifrada += carac_cifra

        else:

            cifrada += carac

    return cifrada

frase = input('FRASE: ')
frase_modificada = transformador(frase.lower())
print(frase_modificada)
