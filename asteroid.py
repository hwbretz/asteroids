from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        rot_1 = pygame.math.Vector2(rand_angle)
        rot_2 = pygame.math.Vector2(-rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_ast_2 = Asteroid(self.position.x,self.position.y,new_radius)

        new_ast_1.velocity = pygame.Vector2(rot_1 * 1.2)
        new_ast_2.velocity = pygame.Vector2(rot_2 * 1.2)



    
        
