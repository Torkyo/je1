import pygame
import random
import time

pygame.init()

icone = pygame.image.load("spriteJE/livro4.png")
pygame.display.set_caption("Game Educacional")
pygame.display.set_icon(icone)
largura = 800
altura = 480
display = pygame.display.set_mode((largura,altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("spriteJE/fundo.jpg")
avatar = pygame.image.load("spriteJE/estudante.png")
livros = pygame.image.load("spriteJE/livro.png")


preto = (0, 0, 0)
branco = (255, 255, 255)


def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf", 120)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    jogo()

def dead():
    pygame.mixer.music.stop()
    message_display("Game Over!")

def pontuação(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios: "+str(desvios), True, preto)
    display.blit(texto, (340, 0))

def jogo():
    pygame.mixer.music.load("spriteJE/musica_game.mp3")
    pygame.mixer.music.play(-1)

    avatar_eixo_x = largura * 0.40
    avatar_eixo_y = altura * 0.6
    avatar_largura = 124
    avatar_altura = 139
    movimento_x = 0

    livro_eixo_x = largura * 0.40
    livro_eixo_y = -80
    livro_largura = 20
    livro_altura = 66
    velocidade = 6

    desvios = 0


    while True:
        for evento in pygame.event.get():
             if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimento_x = -8
                elif evento.key == pygame.K_RIGHT:
                    movimento_x = 8
             if evento.type == pygame.KEYUP:
                movimento_x = 0

        display.blit(fundo, (0, 0))

        avatar_eixo_x = avatar_eixo_x + movimento_x
        if avatar_eixo_x < 0:
            avatar_eixo_x = 0 
        elif avatar_eixo_x > 620:
            avatar_eixo_x = 620
        display.blit(avatar, (avatar_eixo_x,avatar_eixo_y))
    
        display.blit(livros, (livro_eixo_x, livro_eixo_y))
        livro_eixo_y = livro_eixo_y + velocidade
        if livro_eixo_y > altura :
            livro_eixo_y = -80
            velocidade += + 0.5
            livro_eixo_x = random.randrange(0, largura-60)
            desvios = desvios + 1

        if avatar_eixo_y < livro_eixo_y + livro_altura:
            if avatar_eixo_x < livro_eixo_x and avatar_eixo_x + avatar_largura > livro_eixo_x or livro_eixo_x + livro_largura > avatar_eixo_x and livro_eixo_x < avatar_eixo_x + avatar_largura:
                dead()

        pontuação(desvios)
        pygame.display.update()
        fps.tick(64)

jogo()




