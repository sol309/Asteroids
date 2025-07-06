# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot
def main():
   pygame.init()
   clock = pygame.time.Clock()
   dt = 0
   updateable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()
   AsteroidField.containers = updateable
   Shot.containers = (drawable, updateable, shots)
   Asteroid.containers = (updateable, drawable, asteroids)
   Player.containers = (updateable,drawable)
   field = AsteroidField()

   screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
   player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

   while(1):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return

       screen.fill("black")
       
       updateable.update(dt)

       for asteroid in asteroids:
           if asteroid.collisiondetection(player):
               print("Game Over!")
               sys.exit(0)

       for thing in drawable:
           thing.draw(screen)

       pygame.display.flip()
       dt = clock.tick(60)/1000
if __name__ == "__main__":
   main()
