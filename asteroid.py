import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20,50)
        split1 = self.velocity.rotate(new_angle)
        split2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new1 = Asteroid(self.position.x, self.position.y, new_radius)
        new2 = Asteroid(self.position.x, self.position.y, new_radius)
        new1.velocity = split1 *1.2
        new2.velocity = split2 *1.2
