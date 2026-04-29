import pygame, random
from persistence import save_score
from ui import game_over_screen

WIDTH, HEIGHT = 400, 600

LEFT_BOUND = 50
RIGHT_BOUND = 350

# 🔥 ENEMY ФОНДЫ ТОЛЫҚ ЖОЮ
def remove_enemy_background(img):
    img = img.convert_alpha()
    w, h = img.get_size()

    for x in range(w):
        for y in range(h):
            r, g, b, a = img.get_at((x, y))

            # ақ + сұр + ашық фон толық кетеді
            if r > 180 and g > 180 and b > 180:
                img.set_at((x, y), (0, 0, 0, 0))

    return img


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # ===== LOAD =====
    road = pygame.image.load("assets/road.png").convert()
    road = pygame.transform.scale(road, (WIDTH, HEIGHT))

    # ❗ PLAYER untouched
    player_img = pygame.image.load("assets/car.png").convert_alpha()

    # ❗ ONLY enemy fix
    enemy_img = pygame.image.load("assets/enemy.png")
    enemy_img = remove_enemy_background(enemy_img)

    player_img = pygame.transform.scale(player_img, (50, 90))
    enemy_img = pygame.transform.scale(enemy_img, (50, 90))

    road_y = 0

    player = pygame.Rect(180, 500, 50, 90)

    enemies = []
    spawn_timer = 0

    speed = 5
    score = 0

    font = pygame.font.SysFont(None, 30)

    while True:
        # ===== ROAD =====
        road_y += speed
        if road_y >= HEIGHT:
            road_y = 0

        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y - HEIGHT))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # ===== INPUT =====
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= 6
        if keys[pygame.K_RIGHT]:
            player.x += 6

        # ===== ЖОЛДАН ШЫҚПАУ =====
        if player.x < LEFT_BOUND:
            player.x = LEFT_BOUND
        if player.x > RIGHT_BOUND - 50:
            player.x = RIGHT_BOUND - 50

        # ===== SPAWN =====
        spawn_timer += 1
        if spawn_timer > 60:
            x = random.randint(LEFT_BOUND, RIGHT_BOUND - 50)
            enemies.append(pygame.Rect(x, -100, 50, 90))
            spawn_timer = 0

        # ===== ENEMY =====
        for e in enemies:
            e.y += speed

            if player.colliderect(e):
                save_score(score)

                action = game_over_screen(score)

                if action == "retry":
                    run_game()
                else:
                    return

        # ===== DRAW =====
        screen.blit(player_img, (player.x, player.y))

        for e in enemies:
            screen.blit(enemy_img, (e.x, e.y))

        # ===== SCORE =====
        score += 1

        txt = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(txt, (10, 10))

        # difficulty өседі
        if score % 300 == 0:
            speed += 1

        pygame.display.flip()
        clock.tick(60)