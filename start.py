import pygame
import sys
import os
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("black"))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    running = True
    all_sprites = pygame.sprite.Group()
    arrow = pygame.sprite.Sprite(all_sprites)
    arrow.image = load_image('arrow.png', -1)
    arrow.rect = arrow.image.get_rect()
    arrow.rect.x = 20
    arrow.rect.y = 30

    image = pygame.sprite.Sprite(all_sprites)
    image.image = load_image('start.jpg')
    image.rect = arrow.image.get_rect()
    image.rect.x = 350
    image.rect.y = 400
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("PACMAN", 1, (123, 104, 238))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2 - 250
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        menu = font.render("PLAY", 1, (100, 255, 255))
        screen.blit(menu, (text_x + 30, text_y + 100))
        exit = font.render("EXIT", 1, (100, 255, 255))
        screen.blit(exit, (text_x + 33, text_y + 200))
        pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if arrow.rect.y < 50:
                        arrow.rect.y += 100
                elif event.key == pygame.K_UP:
                    if arrow.rect.y > 105:
                        arrow.rect.y -= 100
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()




def terminate():
    pygame.quit()
    sys.exit()


start_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
