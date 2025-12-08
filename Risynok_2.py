import pygame
import math

# Цвета
RED = (255, 0, 0)
GREEN = (0, 100, 0)
LIGHT_GREEN1 = (0, 130, 0)
LIGHT_GREEN2 = (0, 160, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OAK = (120, 85, 60)
BROWN = (112, 91, 91)
FENCE_YELLOW = (204, 204, 0)


def apply_transform(points, x, y, scale):
    return [(x + px * scale, y + py * scale) for (px, py) in points]


def draw_sky(screen, x, y, scale):
    pygame.draw.rect(screen, (0, 255, 255), (x, y, int(600 * scale), int(120 * scale)))


def draw_fence(screen, x, y, scale):
    pygame.draw.rect(screen, FENCE_YELLOW, (x, y, int(600 * scale), int(330 * scale)))
    x1, y1 = x, y
    x2, y2 = x + int(600 * scale), y + int(330 * scale)
    N = 14
    pygame.draw.rect(screen, BLACK, (x1, y1, x2 - x1, y2 - y1), max(1, int(1 * scale)))
    h = (x2 - x1) // (N + 1)
    x_pos = x1 + h
    for _ in range(N):
        pygame.draw.line(screen, BLACK, (x_pos, y1), (x_pos, y2))
        x_pos += h


def draw_grass(screen, x, y, scale):
    pygame.draw.rect(screen, (0, 220, 100), (x, y, int(600 * scale), int(350 * scale)))


def draw_doghouse(screen, x, y, scale):
    wall1 = apply_transform([(370, 500), (480, 530), (480, 640), (370, 600)], x, y, scale)
    wall2 = apply_transform([(480, 530), (510, 495), (510, 590), (480, 640)], x, y, scale)
    roof = apply_transform([(370, 500), (430, 440), (470, 410), (510, 495), (480, 530)], x, y, scale)

    pygame.draw.polygon(screen, FENCE_YELLOW, wall1)
    pygame.draw.polygon(screen, FENCE_YELLOW, wall2)
    pygame.draw.polygon(screen, (200, 190, 0), roof)

    pointlist_house = apply_transform([
        (370, 500), (370, 600), (480, 640), (480, 530),
        (480, 640), (510, 590), (510, 495), (480, 530),
        (370, 500), (430, 440), (470, 410), (510, 495),
        (480, 530), (430, 440)
    ], x, y, scale)
    pygame.draw.lines(screen, BLACK, False, pointlist_house, max(1, int(1 * scale)))

    cx, cy = x + 420 * scale, y + 570 * scale
    r = 30 * scale
    pygame.draw.circle(screen, BLACK, (int(cx), int(cy)), max(1, int(r)))


def draw_chain(screen, x, y, scale):
    chain_parts = [
        (385, 590, 25, 10, 2),
        (385, 595, 10, 15, 0),
        (375, 605, 20, 15, 2),
        (365, 615, 20, 10, 2),
        (360, 620, 15, 12, 2),
        (338, 625, 30, 10, 2),
        (325, 627, 20, 10, 2),
        (318, 627, 12, 15, 2),
        (305, 635, 20, 10, 2),
    ]
    for px, py, w, h, width in chain_parts:
        rect = (x + px * scale, y + py * scale, w * scale, h * scale)
        pygame.draw.ellipse(screen, BLACK, rect, max(1, int(width * scale)))


def draw_dog(screen, x, y, scale):
    # Лапы
    pygame.draw.ellipse(screen, BROWN, (x + 20*scale, y + 700*scale, 50*scale, 25*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 110*scale, y + 715*scale, 50*scale, 25*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 245*scale, y + 675*scale, 40*scale, 20*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 175*scale, y + 645*scale, 40*scale, 20*scale))

    # Ноги
    pygame.draw.ellipse(screen, BROWN, (x + 50*scale, y + 595*scale, 40*scale, 115*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 135*scale, y + 610*scale, 40*scale, 115*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 270*scale, y + 625*scale, 20*scale, 60*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 200*scale, y + 595*scale, 20*scale, 60*scale))

    # Туловище
    pygame.draw.ellipse(screen, BROWN, (x + 165*scale, y + 560*scale, 55*scale, 65*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 230*scale, y + 585*scale, 55*scale, 60*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 180*scale, y + 560*scale, 90*scale, 55*scale))
    pygame.draw.ellipse(screen, BROWN, (x + 60*scale, y + 565*scale, 150*scale, 80*scale))

    # Голова
    pygame.draw.rect(screen, BROWN, (x + 61*scale, y + 530*scale, 90*scale, 90*scale))
    pygame.draw.lines(screen, BLACK, True, apply_transform(
        [(61, 530), (151, 530), (151, 620), (61, 620)], x, y, scale), max(1, int(1*scale)))

    # Уши
    pygame.draw.ellipse(screen, BROWN, (x + 48*scale, y + 530*scale, 25*scale, 30*scale))
    pygame.draw.ellipse(screen, BLACK, (x + 48*scale, y + 530*scale, 25*scale, 30*scale), max(1, int(1*scale)))
    pygame.draw.ellipse(screen, BROWN, (x + 138*scale, y + 530*scale, 25*scale, 30*scale))
    pygame.draw.ellipse(screen, BLACK, (x + 138*scale, y + 530*scale, 25*scale, 30*scale), max(1, int(1*scale)))

    # Глаза
    pygame.draw.ellipse(screen, WHITE, (x + 75*scale, y + 560*scale, 20*scale, 7*scale))
    pygame.draw.ellipse(screen, BLACK, (x + 75*scale, y + 560*scale, 20*scale, 7*scale), max(1, int(1*scale)))
    pygame.draw.circle(screen, BLACK, (x + 85*scale, y + 564*scale), max(1, int(4*scale)))

    pygame.draw.ellipse(screen, WHITE, (x + 116*scale, y + 560*scale, 20*scale, 7*scale))
    pygame.draw.ellipse(screen, BLACK, (x + 116*scale, y + 560*scale, 20*scale, 7*scale), max(1, int(1*scale)))
    pygame.draw.circle(screen, BLACK, (x + 126*scale, y + 564*scale), max(1, int(4*scale)))

    # Зубы
    tooth1 = apply_transform([(84, 582), (87, 593), (79, 598)], x, y, scale)
    pygame.draw.polygon(screen, WHITE, tooth1)
    pygame.draw.polygon(screen, BLACK, tooth1, max(1, int(1*scale)))

    tooth2 = apply_transform([(131, 598), (123, 593), (126, 583)], x, y, scale)
    pygame.draw.polygon(screen, WHITE, tooth2)
    pygame.draw.polygon(screen, BLACK, tooth2, max(1, int(1*scale)))

    # Рот
    arc_rect = (x + 75*scale, y + 590*scale, 60*scale, 35*scale)
    start = math.radians(0)
    stop = math.radians(180)
    pygame.draw.arc(screen, BLACK, arc_rect, start, stop, max(1, int(1*scale)))


# ======================
# ОСНОВНАЯ ФУНКЦИЯ
# ======================
def main():
    pygame.init()
    FPS = 30
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Custom Scene — Draw What You Want!")

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)  # чистый белый фон

        draw_doghouse(screen, 700, 200, 0.9)

        draw_sky(screen, 0, 0, 1.0)

        draw_grass(screen, 0, 120 + 330, 1.0)

        draw_fence(screen, 0, 120, 1.0)

        draw_doghouse(screen, 10, 40, 0.9)

        draw_doghouse(screen, 70, 180, 0.9)

        draw_chain(screen, 70, 180, 0.9)

        draw_chain(screen, 10, 40, 0.9)

        draw_dog(screen, 0, 80, 0.8)

        draw_dog(screen, 120, 420, 0.4)

        draw_dog(screen, 180, 500, 0.4)

        pygame.display.update()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
