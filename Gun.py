   import math
import random
import pygame

FPS = 30
RED, WHITE, BLACK = 0xFF0000, 0xFFFFFF, 0x000000
WIDTH, HEIGHT = 800, 600
GAME_COLORS = [RED, 0x0000FF, 0xFFC91F, 0x00FF00, 0xFF03B8, 0x00FFCC]


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = False
        self.an = 0

    def fire2_start(self, event):
        self.f2_on = True

    def fire2_end(self, event):
        global balls
        new_ball = Ball(self.screen)
        new_ball.r += 5
        dx = event.pos[0] - new_ball.x
        dy = event.pos[1] - new_ball.y
        self.an = math.atan2(dy, dx)
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = False
        self.f2_power = 10

    def targetting(self, event):
        if event:
            dx = event.pos[0] - 20
            dy = event.pos[1] - 450
            self.an = math.atan2(dy, dx)

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, (0, 425, 40, 50))

    def power_up(self):
        if self.f2_on and self.f2_power < 100:
            self.f2_power += 1


class Ball:
    def __init__(self, screen, x=40, y=450):
        self.screen = screen
        self.x, self.y = x, y
        self.r = 10
        self.vx = self.vy = 0
        self.color = random.choice(GAME_COLORS)
        self.bounces = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Отскоки от стен
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx *= -1
            self.bounces += 1
        if self.x + self.r >= WIDTH:
            self.x = WIDTH - self.r
            self.vx *= -1
            self.bounces += 1
        if self.y - self.r <= 0:
            self.y = self.r
            self.vy *= -1
            self.bounces += 1
        if self.y + self.r >= HEIGHT:
            self.y = HEIGHT - self.r
            self.vy *= -1
            self.bounces += 1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.r)

    def hittest(self, obj):
        if not hasattr(obj, 'x') or not hasattr(obj, 'y') or not hasattr(obj, 'r'):
            return False
        dist = math.hypot(self.x - obj.x, self.y - obj.y)
        return dist <= self.r + obj.r

    def is_dead(self):
        return self.bounces >= 2


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.x = self.y = self.r = 0
        self.color = RED
        self.alive = True
        self.by_shot = False

    def set_pos(self, x, y, r):
        self.x, self.y, self.r = x, y, r
        self.alive = True
        self.by_shot = False

    def shrink(self):
        if self.alive and not self.by_shot:
            self.r -= 0.05
            if self.r <= 0:
                self.alive = False

    def draw(self):
        if self.alive and self.r > 0:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), int(self.r))


def spawn_targets(screen):
    t1 = Target(screen)
    r1 = random.randint(20, 40)
    x1 = random.randint(600, 780)
    y1 = random.randint(300, 550)
    t1.set_pos(x1, y1, r1)

    t2 = Target(screen)
    for _ in range(100):
        r2 = random.randint(20, 40)
        x2 = random.randint(600, 780)
        y2 = random.randint(300, 550)
        if math.hypot(x1 - x2, y1 - y2) > r1 + r2 + 10:
            t2.set_pos(x2, y2, r2)
            return [t1, t2]

    t2.set_pos(x1 - r1 - r2 - 30, y1, r2)
    return [t1, t2]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 72)

balls = []
gun = Gun(screen)
targets = spawn_targets(screen)
game_over = False
result = ""

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif not game_over and event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif not game_over and event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    if not game_over:
        gun.power_up()
        for b in balls:
            b.move()
            for t in targets:
                if b.hittest(t) and t.alive:
                    t.alive = False
                    t.by_shot = True
        balls = [b for b in balls if not b.is_dead()]
        for t in targets:
            t.shrink()

        if all(t.by_shot for t in targets):
            game_over = True
            result = "Победа!"
        elif any(not t.by_shot and not t.alive for t in targets):
            game_over = True
            result = "Проигрыш!"

    gun.draw()
    for t in targets:
        t.draw()
    for b in balls:
        b.draw()

    if game_over:
        text = font.render(result, True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
