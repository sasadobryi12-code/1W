import pygame
import math

# Инициализация цветов
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


def draw_sky(screen):
    pygame.draw.rect(screen, (0, 255, 255), (0, 0, 600, 120))


def draw_fence(screen):
    # Основной забор
    pygame.draw.rect(screen, FENCE_YELLOW, (0, 120, 600, 330))
    # Полосы забора
    x1, y1 = 0, 120
    x2, y2 = 600, 450
    N = 14
    pygame.draw.rect(screen, BLACK, (x1, y1, x2 - x1, y2 - y1), 1)
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for _ in range(N):
        pygame.draw.line(screen, BLACK, (x, y1), (x, y2))
        x += h


def draw_grass(screen):
    pygame.draw.rect(screen, (0, 220, 100), (0, 450, 600, 350))



def draw_doghouse(screen):
    # Стены будки
    pygame.draw.polygon(screen, FENCE_YELLOW, [(370, 500), (480, 530), (480, 640), (370, 600)])
    pygame.draw.polygon(screen, FENCE_YELLOW, [(480, 530), (510, 495), (510, 590), (480, 640)])
    pygame.draw.polygon(screen, (200, 190, 0), [(370, 500), (430, 440), (470, 410), (510, 495), (480, 530)])
    
    pointlist_house = [
        (370, 500),(370, 600),(480, 640),(480, 530),(480, 640), (510, 590),(510, 495),
        (480, 530),(370, 500), (430, 440), (470, 410), (510, 495), (480, 530), (430, 440)]
    pygame.draw.lines(screen, (0, 0 , 0), False, pointlist_house, 1)
    pygame.draw.circle(screen, (0,0,0), (420, 570), 30)


def draw_chain(screen):
    # Цепь — серия эллипсов
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
    for x, y, w, h, width in chain_parts:
        pygame.draw.ellipse(screen, BLACK, (x, y, w, h), width)



def draw_dog(screen):
    # Лапы
    pygame.draw.ellipse(screen, BROWN, (20, 700, 50, 25))   # Правая передняя
    pygame.draw.ellipse(screen, BROWN, (110, 715, 50, 25))  # Левая передняя
    pygame.draw.ellipse(screen, BROWN, (245, 675, 40, 20))  # Левая задняя
    pygame.draw.ellipse(screen, BROWN, (175, 645, 40, 20))  # Правая задняя

    # Ноги
    pygame.draw.ellipse(screen, BROWN, (50, 595, 40, 115))
    pygame.draw.ellipse(screen, BROWN, (135, 610, 40, 115))
    pygame.draw.ellipse(screen, BROWN, (270, 625, 20, 60))
    pygame.draw.ellipse(screen, BROWN, (200, 595, 20, 60))

    # Туловище
    pygame.draw.ellipse(screen, BROWN, (165, 560, 55, 65))
    pygame.draw.ellipse(screen, BROWN, (230, 585, 55, 60))
    pygame.draw.ellipse(screen, BROWN, (180, 560, 90, 55))
    pygame.draw.ellipse(screen, BROWN, (60, 565, 150, 80))

    # Голова
    pygame.draw.rect(screen, BROWN, (61, 530, 90, 90))
    pygame.draw.lines(screen, BLACK, True, [(61, 530), (151, 530), (151, 620), (61, 620)], 1)

    # Уши
    pygame.draw.ellipse(screen, BROWN, (48, 530, 25, 30))
    pygame.draw.ellipse(screen, BLACK, (48, 530, 25, 30), 1)
    pygame.draw.ellipse(screen, BROWN, (138, 530, 25, 30))
    pygame.draw.ellipse(screen, BLACK, (138, 530, 25, 30), 1)

    # Глаза
    pygame.draw.ellipse(screen, WHITE, (75, 560, 20, 7))
    pygame.draw.ellipse(screen, BLACK, (75, 560, 20, 7), 1)
    pygame.draw.circle(screen, BLACK, (85, 564), 4)

    pygame.draw.ellipse(screen, WHITE, (116, 560, 20, 7))
    pygame.draw.ellipse(screen, BLACK, (116, 560, 20, 7), 1)
    pygame.draw.circle(screen, BLACK, (126, 564), 4)

    # Зубы
    pygame.draw.polygon(screen, WHITE, [(84, 582), (87, 593), (79, 598)])
    pygame.draw.polygon(screen, BLACK, [(83, 582), (88, 593), (78, 598)], 1)
    pygame.draw.polygon(screen, WHITE, [(131, 598), (123, 593), (126, 583)])
    pygame.draw.polygon(screen, BLACK, [(131, 598), (122, 593), (126, 583)], 1)

    # Рот
    start = math.radians(0)
    stop = math.radians(180)
    pygame.draw.arc(screen, BLACK, (75, 590, 60, 35), start, stop, 1)


def draw_scene(screen):
    draw_sky(screen)
    draw_fence(screen)
    draw_grass(screen)
    draw_doghouse(screen)
    draw_chain(screen)
    draw_dog(screen)


def main():
    pygame.init()
    FPS = 30
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Pygame Scene")

    draw_scene(screen)
    pygame.display.update()

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
