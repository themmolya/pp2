import pygame, random, json

WIDTH, HEIGHT = 600, 600
CELL = 20

def load_settings():
    with open("settings.json") as f:
        return json.load(f)

def save_score(score):
    try:
        with open("leaderboard.json") as f:
            data = json.load(f)
    except:
        data = []

    data.append(score)
    data = sorted(data, reverse=True)[:10]

    with open("leaderboard.json","w") as f:
        json.dump(data,f)

# ===== GAME OVER SCREEN =====
def game_over_screen(screen, score):
    font_big = pygame.font.SysFont(None, 60)
    font = pygame.font.SysFont(None, 40)

    retry_btn = pygame.Rect(200,300,200,60)
    quit_btn = pygame.Rect(200,380,200,60)

    while True:
        screen.fill((10,10,20))

        screen.blit(font_big.render("GAME OVER", True, (255,50,50)), (150,150))
        screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (230,220))

        pygame.draw.rect(screen,(0,200,0),retry_btn)
        screen.blit(font.render("RETRY", True,(0,0,0)),(240,315))

        pygame.draw.rect(screen,(200,0,0),quit_btn)
        screen.blit(font.render("QUIT", True,(0,0,0)),(250,395))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"
            if e.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.collidepoint(e.pos):
                    return "retry"
                if quit_btn.collidepoint(e.pos):
                    return "quit"

        pygame.display.flip()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    settings = load_settings()
    snake_color = settings["color"]

    snake = [(300,300)]
    dx,dy = CELL,0

    food = (random.randrange(0,WIDTH,CELL), random.randrange(0,HEIGHT,CELL))
    poison = None
    power = None
    power_type = None

    obstacles = []

    score = 0
    level = 1
    speed = 10
    shield = False

    font = pygame.font.SysFont(None,30)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT: dx,dy=-CELL,0
                if e.key == pygame.K_RIGHT: dx,dy=CELL,0
                if e.key == pygame.K_UP: dx,dy=0,-CELL
                if e.key == pygame.K_DOWN: dx,dy=0,CELL

        head = (snake[0][0]+dx, snake[0][1]+dy)

        # collision
        if head in snake or head in obstacles or not (0<=head[0]<WIDTH and 0<=head[1]<HEIGHT):
            if shield:
                shield = False
            else:
                save_score(score)
                action = game_over_screen(screen, score)
                if action == "retry":
                    return run_game()
                else:
                    return

        snake.insert(0,head)

        # food
        if head == food:
            score += 1
            food = (random.randrange(0,WIDTH,CELL), random.randrange(0,HEIGHT,CELL))

            if score % 3 == 0:
                poison = (random.randrange(0,WIDTH,CELL), random.randrange(0,HEIGHT,CELL))

            if score % 5 == 0:
                power = (random.randrange(0,WIDTH,CELL), random.randrange(0,HEIGHT,CELL))
                power_type = random.choice(["speed","slow","shield"])
        else:
            snake.pop()

        # poison
        if poison and head == poison:
            for _ in range(2):
                if len(snake)>1:
                    snake.pop()
            poison = None

        # power
        if power and head == power:
            if power_type == "speed":
                speed += 5
            elif power_type == "slow":
                speed = max(5, speed-5)
            elif power_type == "shield":
                shield = True
            power = None

        # obstacles
        if level >= 3 and len(obstacles)<5:
            obstacles.append((random.randrange(0,WIDTH,CELL), random.randrange(0,HEIGHT,CELL)))

        level = score//5 + 1

        # ===== КРАСИВЫЙ ФОН =====
        screen.fill((15,15,35))  # темный стиль

        # grid (optional)
        if settings["grid"]:
            for x in range(0,WIDTH,CELL):
                pygame.draw.line(screen,(40,40,60),(x,0),(x,HEIGHT))
            for y in range(0,HEIGHT,CELL):
                pygame.draw.line(screen,(40,40,60),(0,y),(WIDTH,y))

        # ===== SNAKE (красивый) =====
        for i, s in enumerate(snake):
            color = (0,255,0) if i == 0 else (0,200,0)
            pygame.draw.rect(screen,color,(*s,CELL,CELL), border_radius=6)

        # ===== FOOD (красивый) =====
        pygame.draw.circle(screen,(255,200,0),(food[0]+10, food[1]+10),10)

        # poison
        if poison:
            pygame.draw.circle(screen,(200,0,0),(poison[0]+10, poison[1]+10),10)

        # power
        if power:
            color = (0,0,255) if power_type=="speed" else (0,255,255) if power_type=="slow" else (255,0,255)
            pygame.draw.circle(screen,color,(power[0]+10, power[1]+10),10)

        # obstacles
        for o in obstacles:
            pygame.draw.rect(screen,(120,120,120),(*o,CELL,CELL), border_radius=4)

        # UI
        screen.blit(font.render(f"Score: {score}",True,(255,255,255)),(10,10))
        screen.blit(font.render(f"Level: {level}",True,(255,255,255)),(10,40))

        if shield:
            screen.blit(font.render("SHIELD",True,(0,255,255)),(10,70))

        pygame.display.flip()
        clock.tick(speed)