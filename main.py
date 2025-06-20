#import pygame, so we can use thier library
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # groups for tracking objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfields = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Shot.containers = (shot_group,updateable, drawable)
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)

    # make objects and draw to screen

    player_sprite = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #player_sprite.draw(screen)  

    asteroid_sprites = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        #updateable.update(dt)

        for upd in updateable:
            upd.update(dt)
        for ast in asteroids:
            if ast.collision(player_sprite):
                print("Game over!")
                exit(0)
        for can_draw in drawable:
            can_draw.draw(screen)
        
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
