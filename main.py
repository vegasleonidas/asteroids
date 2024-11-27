import sys
import pygame
from asteroidfield import AsteroidField
from player import *
from asteroid import Asteroid
from constants import *
from shot import Shot

def main():
   
   print("Starting asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")   

   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   all_shots = pygame.sprite.Group()

   Player.containers = (updatable, drawable)
   Asteroid.containers = (asteroids, updatable, drawable)
   AsteroidField.containers = (updatable,)
   Shot.containers = (all_shots, updatable, drawable)

   pygame.init()
   clock = pygame.time.Clock()
   dt = 0
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   asteroid_field = AsteroidField()

   #Player object
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   while True:
      for event in pygame.event.get():
    	   if event.type == pygame.QUIT:
            return
      #fill black background
      screen.fill(pygame.Color('black'))

      #Update all sprites
      for item in updatable:
         item.update(dt)
      
      #Checking for collisions
      for item in asteroids:
         if item.collision(player) == True:
            print("Game over!")
            sys.exit()

      for item in asteroids:
         for shot in all_shots:
            if item.collision(shot) == True:
               item.split()
               shot.kill()          
            
      
      #draw screen
      for item in drawable:
         item.draw(screen)
      #reset display
      pygame.display.flip()
      dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

