# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from circleshape import *
from player import *
from constants import *
def main():
   pygame.init()
   clock = pygame.time.Clock()
   dt = 0
   updateable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   Player.containers = (updateable,drawable)
   screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
   player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

   while(1):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return

       screen.fill("black")
       
       updateable.update(dt)

       for thing in drawable:
           thing.draw(screen)

       pygame.display.flip()
       dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
