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


def convert_image(image, x, y):
    image1 = pygame.transform.scale(image, (x, y))
    return image1


def terminate():
    pygame.quit()
    sys.exit()


def nast():
    screen.fill((0, 0, 0))
    print(1)


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
        font = pygame.font.SysFont("comicsansms", 50)
        text = font.render("PACMAN", 1, (123, 104, 238))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2 - 250
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        menu = font.render("PLAY", 1, (100, 255, 255))
        screen.blit(menu, (text_x + 30, text_y + 100))
        settings = font.render("SETTINGS", 1, (100, 255, 255))
        screen.blit(settings, (text_x + 33, text_y + 200))
        exit = font.render("EXIT", 1, (100, 255, 255))
        screen.blit(exit, (text_x + 33, text_y + 300))
        pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if arrow.rect.y < 150:
                        arrow.rect.y += 100
                elif event.key == pygame.K_UP:
                    if arrow.rect.y > 105:
                        arrow.rect.y -= 100
                elif event.key == pygame.K_RETURN:
                    if arrow.rect.y == 30:
                        return
                    elif arrow.rect.y == 130:
                        nast()
                        running = False
                    elif arrow.rect.y == 230:
                        terminate()
                    print(arrow.rect.y)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()


class Pacman:
    def __init__(self, x, y):
        self.all_sprites = pygame.sprite.Group()
        self.pac = pygame.sprite.Sprite(self.all_sprites)
        self.pac.image = convert_image(load_image('pacman.png', -1), 20, 20)
        self.pac.rect = self.pac.image.get_rect()
        self.pac.rect.x = x
        self.pac.rect.y = y
        self.pac.rect.x += 2
        self.moveUp = self.moveLeft = self.moveDown = self.moveRight = False
        self.direction = 0
        self.speed = 5

    def move(self, event):
        if event.key == pygame.K_UP:
            self.pac.rect.y -= 2
            self.direction = 0
        elif event.key == pygame.K_DOWN:
            self.pac.rect.y += 2
            self.direction = 1
        elif event.key == pygame.K_RIGHT:
            self.pac.rect.x += 2
            self.direction = 2
        elif event.key == pygame.K_LEFT:
            self.pac.rect.x -= 2
            self.direction = 3

    def return_direction(self):
        return self.direction

    def update(self):
        self.all_sprites.update()
        self.all_sprites.draw(screen)



start_screen()
FPS = 60
clock = pygame.time.Clock()
running = True
screen.fill((0, 0, 0))
print(1)
pacman = Pacman(50, 50)
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            screen.fill((0, 0, 0))
            pacman.move(event)
        pacman.update()
    pygame.display.flip()
