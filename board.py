import pygame
import os
from default_board import default_board


class Board:
    def __init__(self, scailing_factor):
        # King: K, queen: Q, rook: R, bishop: B, knight: N, pawn: P
        self.board = default_board
        self.scailing_factor = scailing_factor
        self.turn = "w"

    def move(self, x1, y1, x2, y2):
        if self.turn != self.board[y1][x1][1]:
            print("Can't move enemy piece")
            return
        if self.turn == self.board[y2][x2][1]:
            print("Can't kill your own piece")
            return
        # TODO: handle en passant
        if self.board[y1][x1][0] == "P":
            if self.turn == "w":
                other = "b"
                sign = -1
                n = 6
            else:
                other = "w"
                sign = 1
                n = 1
            if self.board[y2][x2][1] == other:
                if x1 == x2 or abs(x1 - x2) != 1 or y1 + 1 * sign != y2:
                    print("Invalid move")
                    return
            else:
                if y1 + 1 * sign != y2:
                    if (
                        y1 + 2 * sign != y2
                        or y1 != n
                        or self.board[y1 + sign][x1][1] != ""
                    ):
                        print("Invalid move")
                        return
        if self.board[y1][x1][0] == "N":
            if (not (abs(x1 - x2) == 2 and abs(y1 - y2) == 1)) and (
                not (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
            ):
                print("Invalid move")
                return
        if self.board[y1][x1][0] == "B":
            if abs(x1 - x2) != abs(y1 - y2):
                print("Invalid move")
                return
            dx = (x2 - x1) // abs(x2 - x1)
            dy = (y2 - y1) // abs(y2 - y1)
            x, y = x1, y1
            while x != x2 - dx:
                x += dx
                y += dy
                if self.board[y][x][1] != "":
                    print("Invalid move")
                    return
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = ("", "")
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"

    def draw(self, screen):
        sf = self.scailing_factor
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(
                        screen,
                        (240, 215, 180),
                        (sf * x * 60, sf * y * 60, sf * 60, sf * 60),
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        (180, 135, 100),
                        (sf * x * 60, sf * y * 60, sf * 60, sf * 60),
                    )
                if self.board[y][x] != ("", ""):
                    image = pygame.image.load(
                        os.path.join("pieces", f"{''.join(self.board[y][x])}.png")
                    )
                    image = pygame.transform.smoothscale(image, (sf * 60, sf * 60))
                    screen.blit(image, (sf * x * 60, sf * y * 60))
