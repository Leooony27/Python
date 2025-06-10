class Cores:
    PRETO = "\033[30m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"
    RESETAR = "\033[0m"

    @staticmethod
    def colorir(texto, cor):
        """Retorna o texto formatado com a cor especificada."""
        return f"{cor}{texto}{Cores.RESETAR}"

    @staticmethod
    def texto_colorido(texto, cor):
        """Imprime o texto na cor especificada."""
        print(Cores.colorir(texto, cor))

    @staticmethod
    def gerar_cor_aleatoria():
        """Gera uma cor ANSI aleatória."""
        import random
        cor_aleatoria = random.randint(30, 37)
        return f"\033[{cor_aleatoria}m"


# Exemplo de uso
if __name__ == "__main__":
    Cores.texto_colorido("Texto em vermelho!", Cores.VERMELHO)
    Cores.texto_colorido("Texto em verde!", Cores.VERDE)
    Cores.texto_colorido("Texto em azul!", Cores.AZUL)

    cor_aleatoria = Cores.gerar_cor_aleatoria()
    print(f"{cor_aleatoria}Texto em cor aleatória!{Cores.RESETAR}")
