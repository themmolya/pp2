import pygame, json

WIDTH, HEIGHT = 600, 600

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 50)

    play_btn = pygame.Rect(200,250,200,60)
    quit_btn = pygame.Rect(200,330,200,60)

    while True:
        screen.fill((20,20,40))

        screen.blit(font.render("SNAKE GAME", True, (255,255,0)), (150,150))

        pygame.draw.rect(screen,(0,200,0),play_btn)
        screen.blit(font.render("PLAY", True,(0,0,0)),(250,260))

        pygame.draw.rect(screen,(200,0,0),quit_btn)
        screen.blit(font.render("QUIT", True,(0,0,0)),(250,340))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"
            if e.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(e.pos):
                    return "play"
                if quit_btn.collidepoint(e.pos):
                    return "quit"

        pygame.display.flip()