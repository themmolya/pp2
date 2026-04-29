import pygame

WIDTH, HEIGHT = 400, 600

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font_big = pygame.font.SysFont(None, 60)
    font = pygame.font.SysFont(None, 40)

    start_btn = pygame.Rect(120, 250, 160, 50)
    quit_btn = pygame.Rect(120, 320, 160, 50)

    while True:
        screen.fill((20,20,40))

        title = font_big.render("RACER", True, (255,255,0))
        screen.blit(title, (110,120))

        pygame.draw.rect(screen, (0,200,0), start_btn)
        screen.blit(font.render("START", True, (0,0,0)), (150,260))

        pygame.draw.rect(screen, (200,0,0), quit_btn)
        screen.blit(font.render("QUIT", True, (0,0,0)), (150,330))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    return "play"
                if quit_btn.collidepoint(event.pos):
                    return "quit"

        pygame.display.flip()


def game_over_screen(score):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font_big = pygame.font.SysFont(None, 60)
    font = pygame.font.SysFont(None, 40)

    retry_btn = pygame.Rect(120, 300, 160, 50)
    menu_btn = pygame.Rect(120, 370, 160, 50)

    while True:
        screen.fill((30,0,0))

        screen.blit(font_big.render("GAME OVER", True, (255,0,0)), (60,150))
        screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (130,230))

        pygame.draw.rect(screen, (0,200,0), retry_btn)
        screen.blit(font.render("RETRY", True, (0,0,0)), (150,310))

        pygame.draw.rect(screen, (200,200,0), menu_btn)
        screen.blit(font.render("MENU", True, (0,0,0)), (150,380))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.collidepoint(event.pos):
                    return "retry"
                if menu_btn.collidepoint(event.pos):
                    return "menu"

        pygame.display.flip()