
class ContadorCaracteres:

    def __init__(self, frase):
        self.frase = frase
        self.contagem = {}

    def contar_caracteres(self):
        # Itera sobre cada caractere na frase
        for char in self.frase:
            # Se o caractere já estiver na contagem, incrementa o contador
            if char in self.contagem:
                self.contagem[char] += 1
            # Se o caractere não estiver na contagem, adiciona ao dicionário com contagem 1
            else:
                self.contagem[char] = 1

    def informar_contagem(self):
        # Imprime a contagem de caracteres
        for char, count in self.contagem.items():
            print(f"{count} {char}")

# Exemplo de uso da classe
frase = "Oiiiooiio oiiviuebdfsnr vui"
contador = ContadorCaracteres(frase)
contador.contar_caracteres()
contador.informar_contagem()
