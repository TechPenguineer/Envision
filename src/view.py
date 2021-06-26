import pygame,os,math
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.version import ver
from arrays.cube_array import cube_projection_matrix,points
from functions.colour_manager import enviroment_colour,grid_colour,object_border,vertex_colour
from math import *
from functions.connect_points import *
import numpy as np
isRun = True
angle = 0
while isRun:

    clock = pygame.time.Clock()
    clock.tick(60)
    WIDTH,HEIGHT = (700,700)
    scale = 100
    circle_pos = [WIDTH/2,HEIGHT/2]
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    infoObject = pygame.display.Info()
    window = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE,pygame.OPENGL)
    pygame.display.set_caption("Envision")
    window.fill(enviroment_colour)
    
    
    
    rotation_z = np.matrix([
         [cos(angle), -sin(angle), 0],
         [sin(angle), cos(angle), 0],
         [0,0,1]
    ])    
    rotation_y = np.matrix([    
          [cos(angle), 0, sin(angle)],
          [0,1,0],
          [-sin(angle), 0, cos(angle)],
    ])
    rotation_x = np.matrix([    
          [1,0,0],
          [0, cos(angle), -sin(angle)],
          [0, sin(angle), 0, cos(angle)],
    ])
    angle += 0.01
    
    
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3,1)))
        rotated2d = np.dot(rotation_y, rotated2d)

        projected2d = np.dot(cube_projection_matrix, rotated2d)
        
        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y= int(projected2d[1][0] * scale) + circle_pos[1]
        
        projected_points[i]
        pygame.draw.circle(window, vertex_colour, (x,y), 5)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        if event.type == pygame.K_ESCAPE:
            isRun = False
    pygame.display.flip()

pygame.display.quit()
pygame.display.init()
pygame.quit()