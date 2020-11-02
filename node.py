import pygame
import colors


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row*width
        self.y = col*width
        self.color = colors.WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == colors.CYAN

    def is_open(self):
        return self.color == colors.GREEN

    def is_barrier(self):
        return self.color == colors.BLACK

    def is_start(self):
        return self.color == colors.BLUE

    def is_end(self):
        return self.color == colors.RED

    def erase(self):
        self.color = colors.WHITE

    def make_closed(self):
        self.color = colors.CYAN

    def make_open(self):
        self.color = colors.GREEN

    def make_barrier(self):
        self.color = colors.BLACK

    def make_start(self):
        self.color = colors.BLUE

    def make_end(self):
        self.color = colors.RED

    def make_path(self):
        self.color = colors.PURPLE

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
