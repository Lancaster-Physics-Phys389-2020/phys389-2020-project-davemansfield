import numpy as np 
import pygame
from simplePendulum import *

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
black = pygame.Color(0,0,0)

class PendulumAnimation(pygame.sprite.Sprite):
    def __init__(self,length,bobPostion):
        self.length=length
        self.bobPostion=bobPostion

        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((length*2,length*2)).convert() #surface big enough to fit swing
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.topleft=(length,length)
        self.image_center=(self.rect.width//2,self.rect.height//2)
        self._render()
    
    def _render(self):
        self.image.fill(white)
        pygame.draw.aaline(self.image,black,self.image_center,self.bobPostion,True)
        pygame.draw.circle(self.image,red,self.bobPostion,3)

    def update(self,angle):
        x=np.sin(angle)*self.length
        y=np.cos(angle)*self.length
        self.bobPostion=(int(round(x)),int(round(y)))
        self._render()
        


def main():
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption('Pendulum')

    background=pygame.Surface(screen.get_size())
    background=background.convert()
    background.fill(white)

    clock=pygame.time.Clock()
    #Pendulum(self,length,mass,initialAngle,steps,timestep)
    po=Pendulum(150,3.0,90.0,100.0,0.001)
    XY=(int(round(po.xi)),int(round(po.yi)))
    pa=PendulumAnimation(po.length,XY)

    free_group=pygame.sprite.RenderPlain(pa) #-- needed for double pendulum
    screen.blit(background,(0,0))
    pygame.display.flip()
    running=True
    while running:
        for i in range (0,po.n-1):
            free_group.update(po.theta[i])
            screen.blit(background,(0,0))
            free_group.draw(screen)
            pygame.display.flip()
            po.calculateNextStep(i)
        running=False
            

main()