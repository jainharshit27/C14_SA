import pygame, pymunk
import pymunk.pygame_util

class Arrow:
    def __init__(self,x,y):
        vs = [(-80, 0), (0, 2), (2, 0), (0, -2)]
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.shape = pymunk.Poly(self.body, vs)
        self.shape.density = 0.1
        self.body.position = x,y  # This is changed
        space.add(self.body, self.shape)
    
    def power(self, start, end):
        diff = end - start
        power = min(diff, 1000) * 13.5
        impulse = (power*1, 0)
        self.body.body_type = pymunk.Body.DYNAMIC
        self.body.apply_impulse_at_world_point(impulse, self.body.position)

#Create class Target:
    #Create special method __init__(self) and add the creation of target in it like following.
        #vs = [(1, -80), (1, 80), (-1, 80), (-1, -80)]
        #self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)          #Add self to all values to indicate objects
        #self.shape = pymunk.Poly(self.body, vs)
        #self.body.position = 600,400
        #space.add(self.body, self.shape)

    #Create method draw(self, image) and move the code which adds ropes and target here.
        #screen.blit(rope_img, (round(self.body.position.x-5), 0))
        #screen.blit(rope_img, (round(self.body.position.x-20), 0))
        #screen.blit(image, (round(self.body.position.x-15), round(self.body.position.y-80)))
        
def powerbar(ticks):
    current_time = ticks
    diff = current_time - start_time
    power = min(diff, 1000)
    h = power / 2
    pygame.draw.line(screen, pygame.Color("red"), (650, 550), (650, 550 - h), 10)

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

#background
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (width, height))

#archer
archer = pygame.image.load("bow.png")
archer = pygame.transform.scale(archer, (100,150))

#Remove Target creation from below and call Target class instead of this like target = Target()
vs_rect = [(1, -80), (1, 80), (-1, 80), (-1, -80)]
target_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
target_shape = pymunk.Poly(target_body, vs_rect)
target_body.position = 600,400
space.add(target_body, target_shape)     

target_image = pygame.image.load("target.png")
target_image = pygame.transform.scale(target_image, (25,160))
rope_img = pygame.image.load("rope.png")
rope_img = pygame.transform.scale(rope_img, (25,400))
    
#Arrow
arrow = Arrow(130,85)
flying_arrows = []

while True:
    screen.blit(bg, (0,0))
    screen.blit(archer, (25,40))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_time = pygame.time.get_ticks()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                end_time = pygame.time.get_ticks()
            
                arrow.power(start_time, end_time)
                flying_arrows.append(arrow.body)
                
                arrow = Arrow(130,85)
    
    if pygame.mouse.get_pressed()[0]:
        powerbar(pygame.time.get_ticks())

    space.debug_draw(draw_options)
    
    #call target.draw(target_image) here
    
    #space reload
    space.step(1/60)
    pygame.display.update()
    clock.tick(60)
