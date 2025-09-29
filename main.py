import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.kill()
                    shot.kill()
                    if asteroid.radius > ASTEROID_MIN_RADIUS:
                        new_asteroids = asteroid.split()
                        for new_asteroid in new_asteroids:
                            asteroids.add(new_asteroid)
                            updatable.add(new_asteroid)
                            drawable.add(new_asteroid)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
        

if __name__ == "__main__":
    main()
