import pygame
import math
pygame.init()


screen = pygame.display.set_mode((792, 1072))
pygame.display.set_caption("Simplified Drawing")



WHITE = (255, 255, 255)
LIGHT_GRAY = (230, 230, 230)  # небо
GRAY = (220, 217, 214)   
SNOW = (255, 255, 255)        # снег
BLACK = (0, 0, 0)             # контурные линии
BROWN = (139, 115, 100)       # человек
GRAY = (190, 190, 190)        # животное
BLUE = (64, 224, 208 )          # рыбка
RED = (200, 0, 0)             # рыбка

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, GRAY, (0, 0, 792, 503))
    pygame.draw.rect(screen, GRAY, (0, 700, 792, 503))

    # ИГЛА
    pygame.draw.circle(screen, (GRAY), (250, 600), 172)
    pygame.draw.arc(screen, (BLACK), (76, 450, 348, 300), 0, math.pi, 1)
    pygame.draw.rect(screen, (WHITE), (0, 600, 500, 200))
    pygame.draw.line(screen, (BLACK), (76, 600), (425, 600), 1)
    pygame.draw.arc(screen, (BLACK), (85, 550, 331, 10),math.pi, 0,  1)
    pygame.draw.arc(screen, (BLACK), (114, 500, 270, 15),math.pi, 0,  1)
    pygame.draw.arc(screen, (BLACK), (166, 460, 165, 15),math.pi, 0,  1)
    pygame.draw.arc(screen, (BLACK), (240, 451, 5, 22),math.pi/2, 3*math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (300, 473, 9, 41), 3*math.pi/2, math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (230, 473, 9, 41),math.pi/2, 3*math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (180, 473, 9, 41),math.pi/2, 3*math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (150, 510, 9, 47),math.pi/2, 3*math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (200, 510, 9, 47),math.pi/2, 3*math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (260, 510, 9, 47), 3*math.pi/2, math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (330, 510, 9, 47), 3*math.pi/2, math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (370, 560, 9, 42), 3*math.pi/2, math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (300, 560, 9, 42), 3*math.pi/2, math.pi/2,  1)
    pygame.draw.arc(screen, (BLACK), (120, 560, 9, 42), math.pi/2,3*math.pi/2,   1)
    pygame.draw.arc(screen, (BLACK), (220, 560, 9, 42), math.pi/2,3*math.pi/2,   1)

    # Фон
    pygame.draw.rect(screen, LIGHT_GRAY, (0, 602, 792, 503))

    # котик
    oval_surf = pygame.Surface((60, 650), pygame.SRCALPHA)
    pygame.draw.ellipse(oval_surf, GRAY, (10, 20, 33, 140))
    rotated_oval = pygame.transform.rotate(oval_surf, 90)
    oval_rect = rotated_oval.get_rect(center=(510, 800))
    screen.blit(rotated_oval, oval_rect.topleft)

    tail_surf = pygame.Surface((30, 90), pygame.SRCALPHA)
    pygame.draw.ellipse(tail_surf, GRAY, (0, 0, 13, 70))
    rotated_tail = pygame.transform.rotate(tail_surf, 90)
    tail_rect = rotated_tail.get_rect()
    tail_rect.midleft = (190, 800)
    screen.blit(rotated_tail, tail_rect.topleft)

    ear_surf = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(ear_surf, GRAY, (0, 0, 20, 200))
    rotated_ear = pygame.transform.rotate(ear_surf, 120)
    ear_rect = rotated_ear.get_rect()
    ear_rect.center = (210, 808)
    screen.blit(rotated_ear, ear_rect.topleft)

    ear1_surf = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(ear1_surf, GRAY, (0, 0, 20, 200))
    rotated_ear1 = pygame.transform.rotate(ear1_surf, 240)
    ear1_rect = rotated_ear1.get_rect()
    ear1_rect.center = (342, 822)
    screen.blit(rotated_ear1, ear1_rect.topleft)
    pygame.display.flip()

    ear2_surf = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(ear2_surf, GRAY, (0, 0, 20, 200))
    rotated_ear2 = pygame.transform.rotate(ear2_surf, 270)
    ear2_rect = rotated_ear2.get_rect()
    ear2_rect.center = (345, 815)
    screen.blit(rotated_ear2, ear2_rect.topleft)
    pygame.display.flip()

    fish_surf = pygame.Surface((35, 150), pygame.SRCALPHA)
    pygame.draw.ellipse(fish_surf, BLUE, (1, 5, 15, 50))
    rotated_fish = pygame.transform.rotate(fish_surf, 90)
    fish_rect = rotated_fish.get_rect(center=(270, 780))
    screen.blit(rotated_fish, fish_rect.topleft)

    cx, cy = 209, 778
    fx, fy = cx - 5, cy + 12

    pygame.draw.polygon(screen, (0, 149, 240), [
        (fx, fy - 3),
        (fx + 20, fy - 9),
        (fx + 50, fy - 3)
    ])
    pygame.draw.polygon(screen, (0, 149, 240), [
        (fx, fy + 3),      
        (fx + 50, fy + 3),
        (fx + 20, fy + 9)
    ])

    pygame.draw.polygon(screen, (205, 92, 92), [(fx, fy), (fx - 8, fy - 5), (fx - 8, fy + 5)])
    pygame.draw.circle(screen, (0, 0, 0), (fx - 3, fy), 1)

    pygame.draw.circle(screen, GRAY, (240, 772), 23, 23)

    pygame.draw.circle(screen, WHITE, (232, 770), 5, 5)
    pygame.draw.circle(screen, WHITE, (250, 770), 5, 5)

    pygame.draw.circle(screen, BLACK, (234, 770), 2, 2)
    pygame.draw.circle(screen, BLACK, (252, 770), 2, 2)

    points = [
    (248, 742),   # вершина (вверху)
    (240, 750),   # левая нижняя
    (251, 752)    # правая нижняя
    ]
    pygame.draw.polygon(screen, GRAY, points)

    points = [
    (238, 742),   # вершина (вверху)
    (230, 750),   # левая нижняя
    (241, 752)    # правая нижняя
    ]
    pygame.draw.polygon(screen, GRAY, points)

    points = [
    (242, 778),   # вершина (вверху)
    (233, 782),   # левая нижняя
    (241, 788)    # правая нижняя
    ]
    pygame.draw.polygon(screen, BLACK, points)

    points = [
    (233, 790),   # вершина (вверху)
    (222, 789),   # левая нижняя
    (230, 795)    # правая нижняя
    ]
    pygame.draw.polygon(screen, WHITE, points)

    points = [
    (243, 790),   # вершина (вверху)
    (232, 789),   # левая нижняя
    (240, 795)    # правая нижняя
    ]
    pygame.draw.polygon(screen, WHITE, points)

    # Чувак
    px, py = 620, 700
    
    pygame.draw.ellipse(screen, (139, 115, 100), (px - 55, py + 10, 30, 50)) 
    pygame.draw.ellipse(screen, (139, 115, 100), (px + 35, py + 25, 30, 40)) 

    pygame.draw.circle(screen, (139, 115, 100), (px - 15, py + 115), 18) 
    pygame.draw.circle(screen, (139, 115, 100), (px + 35, py + 115), 18) 

    pygame.draw.polygon(screen, (139, 115, 100), [(px - 20, py + 40), (px + 40, py + 40), (px + 50, py + 110), (px - 30, py + 110)])
    
    pygame.draw.rect(screen, (90, 75, 65), (px - 30, py + 100, 80, 12))
    pygame.draw.rect(screen, (90, 75, 65), (px, py + 40, 20, 60))

    pygame.draw.circle(screen, (220, 220, 215), (px + 10, py), 35)
    pygame.draw.circle(screen, (235, 225, 225), (px + 10, py), 23)
    
    pygame.draw.line(screen, (50, 50, 50), (px, py - 5), (px + 8, py - 2), 2)
    pygame.draw.line(screen, (50, 50, 50), (px + 20, py - 5), (px + 12, py - 2), 2)
    pygame.draw.arc(screen, (50, 50, 50), (px, py + 5, 20, 10), 0.5, 2.6, 2)

    pygame.draw.line(screen, (BLACK), (579, 611), (579, 824), 1)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
