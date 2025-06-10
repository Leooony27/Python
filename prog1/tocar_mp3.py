import pygame
import os
import sys

def tocar_mp3(caminho_arquivo):
    if os.path.isfile(caminho_arquivo):
        # Inicializa o mixer do pygame
        pygame.mixer.init()
        
        # Inicializa o pygame
        pygame.init()
        
        # Cria uma janela (necessária para capturar eventos)
        screen = pygame.display.set_mode((300, 100))
        pygame.display.set_caption('Tocando Música')

        # Carrega e toca o arquivo MP3
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()

        print(f"Tocando: {caminho_arquivo}")
        print("Pressione 'p' para parar a música.")

        while True:
            # Espera um evento
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Pressione 'p' para parar
                        pygame.mixer.music.stop()
                        print("Música parada.")
                        pygame.quit()
                        return
    else:
        print("Arquivo não encontrado! Verifique o caminho.")

# Solicitar o caminho do arquivo MP3
caminho_do_mp3 = input("Digite o caminho do arquivo MP3: ")
tocar_mp3(caminho_do_mp3)
