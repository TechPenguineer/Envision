from numpy.core.numeric import indices
import pygame,os,math,sys
from pygame.constants import FULLSCREEN, KEYDOWN, K_v, RESIZABLE
from pygame.threads import FINISH
from pygame.version import ver
from arrays.cube_array import cube_projection_matrix,points
from functions.colour_manager import enviroment_colour,grid_colour,object_border,vertex_colour,fps_counter_colour,options_panel_colour
from math import *
from configs.viewport_conf import *
import numpy as np
isRun = True
angle = 0
pygame.init() 
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

WIDTH,HEIGHT = (info.current_w,info.current_h-55)
while isRun:
    
    HEIGHT_PANEL = info.current_h
    window = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE, pygame.DOUBLEBUF,pygame.HWSURFACE,pygame.HWACCEL)
    pygame.init()
    circle_pos = [WIDTH/2,HEIGHT/2]
    
    clock.tick(76)
    scale = 100
    pygame.init()
    infoObject = pygame.display.Info()
    pygame.display.set_caption("Envision")
    window.fill(enviroment_colour)
    
    # COUNT FPS DISPLAY
    baseFont = pygame.font.SysFont("Arial", 48)
    text = baseFont.render("FPS", True, fps_counter_colour)
    def connect_points(i,j, points):
          pygame.draw.line(window,object_border,(points[i][0], points[i][1]),(points[j][0], points[j][1]), 3)
    
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
    projected_points = [
       [n, n] for n in range(len(points))
    ]    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        if event.type == pygame.K_ESCAPE:
            isRun = False     
    
    
    keyState = pygame.key.get_pressed()
    if(KEYDOWN == K_v):
        view_vertex=False
    
    i = 0
     
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3,1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        pygame.event.pump() 
        projected2d = np.dot(cube_projection_matrix, rotated2d) 
        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y= int(projected2d[1][0] * scale) + circle_pos[1] 
        projected_points[i] = [x,y]
        if view_vertex == True:
            pygame.draw.circle(window, vertex_colour, (x,y), 5)
        i+=1
        
    if view_edges == True:
      for p in range(len(cube_projection_matrix)+1):
          connect_points(p, (p+1) % 4, projected_points)
          connect_points(p+4, ((p+1) % 4) + 4, projected_points)
          connect_points(p, (p+4), projected_points)   

    # CREATE VIEWPORT OPTION DISPLAYS
    class viewVerts:
        def __init__(self,  image, position, callback):
            self.image = sys.path.append(os.path.abspath('../icons/view_verticies_ico.png'))
    # CREATE SURFACES
    infoWindow = pygame.display.Info()
    options_panel = pygame.Surface([300,HEIGHT_PANEL])
    options_panel.fill(options_panel_colour)
    window.blit(options_panel, [WIDTH-300,0])
    pygame.display.flip()
    

pygame.display.quit()
pygame.display.init()
pygame.quit()