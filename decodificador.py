def decodificar(frase_codificada):

    alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'
    contador = 0
    frase_decodificada = ''

    for carac in frase_codificada:

        if carac in alfabeto_original:

            contador += 1
            index_carac = alfabeto_original.index(carac)
            index_novo = (index_carac - contador) % len(alfabeto_original)
            carac_decifrado = alfabeto_original[index_novo]
            frase_decodificada += carac_decifrado

        else:

            frase_decodificada += carac

    return frase_decodificada


frase_codificada = str(input('FRASE:  '))
frase_decodificada = decodificar(frase_codificada.lower())
print("Mensagem decodificada:", frase_decodificada)
