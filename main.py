#!/usr/bin/env python3
import pygame

from board import Board

def main():
    pygame.init()
    # largest screen size that is a multiple of 480
    scailing_factor = 1
    for size in pygame.display.get_desktop_sizes():
        scailing_factor = max(scailing_factor, min(size) // 480)

    screen = pygame.display.set_mode((scailing_factor*480,scailing_factor*480))
    clock = pygame.time.Clock()
    running = True

    board = Board(scailing_factor)

    x1, x2, y1, y2 = None, None, None, None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if x1 == None:
                        x1 = event.pos[0] // (60 * scailing_factor)
                        y1 = event.pos[1] // (60 * scailing_factor)
                    else:
                        x2 = event.pos[0] // (60 * scailing_factor)
                        y2 = event.pos[1] // (60 * scailing_factor)
                        board.move(x1, y1, x2, y2)
                        x1, y1 = None, None


        screen.fill("black")

        board.draw(screen)

        pygame.display.flip()

        # 60 fps limit
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
