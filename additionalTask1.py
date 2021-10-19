import pygame
import random

width, height = 320, 300
FPS = 60

if __name__ == '__main__':
    pygame.init()
    size = width, height
    pygame.display.set_caption('Смайлик')
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 128))
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 280)
    emoji = font.render(f'=-(', True,
                        (255, 255, 255))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                emoji = font.render(f'=-(', True,
                                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        screen.blit(emoji, (20, 20))
        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()
