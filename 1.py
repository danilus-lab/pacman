import pygame
import sys
import os


class Board:
    def __init__(self, width, height):
        self.k = 0
        self.width = width
        self.height = height
        self.baord = [[0] * width for i in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(self.height):
            for y in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + y * self.cell_size,
                                                           self.top + x * self.cell_size,
                                                           self.cell_size, self.cell_size), 3)
                if self.baord[x][y] == 2:
                    pygame.draw.ellipse(screen, (255, 0, 0), (self.left + 2 +
                                                             (y) * self.cell_size ,
                                                             self.top + 2 + x * self.cell_size, 26, 26),
                                       2)
                elif self.baord[x][y] == 1:
                    pygame.draw.line(screen, (0, 0, 255), (
                        self.left + 2 + y * self.cell_size, self.top + 2 + x * self.cell_size),
                                     (self.left - 4 + (y + 1) * self.cell_size,
                                      self.top - 3 + (x + 1) * self.cell_size,),
                                     2)
                    pygame.draw.line(screen, (0, 0, 255), (
                        self.left - 5 + (y + 1) * self.cell_size, self.top + 2 + x * self.cell_size),
                                     (self.left + 3 + y * self.cell_size,
                                      self.top - 3 + (x + 1) * self.cell_size), 2)

    def get_cell(self, mouse_pos):  # возвращает координаты мыши
        cell = (mouse_pos[0] - self.left) // self.cell_size, (
                mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell[0] < self.width and 0 <= cell[1] < self.height:
            return cell
        return None

    def on_click(self, cell_coords):  # изменяет поле по координатам
        if cell_coords:
            if self.baord[cell_coords[1]][cell_coords[0]] == 0:
                self.k += 1
                if self.k % 2 == 1:
                    self.baord[cell_coords[1]][cell_coords[0]] = 1
                else:
                    self.baord[cell_coords[1]][cell_coords[0]] = 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)



pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
board = Board(20, 20)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()