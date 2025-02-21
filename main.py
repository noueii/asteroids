import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroid_group, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    asteroid_field = AsteroidField()

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in drawables:
            item.draw(screen)

        updatables.update(dt)

        for item in asteroid_group:
            if player.is_colliding(item):
                print("Game over!")
                return
            for shot in shots:
                if item.is_colliding(shot):
                    item.split()

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
