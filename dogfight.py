import pygame as pg
import numpy as np
import math

X = 0
Y = 1
RED = 0
BLUE = 1
V = 200 #pix/s
OMEGA = 180 #deg/s
M_LIFE = 1 #missile life in s
M_V = 1000 #px/s

black = (0,0,0)

def generate360(surf, perc):
    rotatedSurfaces = []
    
    for theta in range(0,360):
        rotated_image = pg.transform.rotate(surf, theta)
        
        orig_size = rotated_image.get_size()
        new_size = (int(orig_size[0] * float(perc/100)), int(orig_size[1] * float(perc/100)))
        scaled_img = pg.transform.scale(rotated_image, new_size)
        rotatedSurfaces.append(scaled_img)
        
    return rotatedSurfaces

pg.init()
redship_img = pg.image.load('gamefiles/redship.png')
redship = generate360(redship_img, 12)

blueship_img = pg.image.load('gamefiles/blueship.png')
blueship = generate360(blueship_img, 12)

missile_img = pg.image.load('gamefiles/missile.png')
missile = generate360(missile_img, 12)

ex1 = pg.image.load('gamefiles/ex1.gif')
ex1_r = ex1.get_rect()

ex2 = pg.image.load('gamefiles/ex2.gif')
ex2_r = ex2.get_rect()

ex3 = pg.image.load('gamefiles/ex3.gif')
ex3_r = ex3.get_rect()

ex4 = pg.image.load('gamefiles/ex4.gif')
ex4_r = ex4.get_rect()
scr = pg.display.set_mode((1000,1000))
scrrect = scr.get_rect()
scr.fill(black)

#Initialize time
dt = 0.01
t_start =  0.001 * pg.time.get_ticks()
t_prev = t_start

t_mis_r = 0
t_mis_b = 0

pos = np.array([[400, 500], [600, 500]]) #[x_red,y_red],[x_blue,y_blue]
vx_r, vy_r, vx_b, vy_b = -200, 0, 200, 0
v = np.array([[vx_r, vy_r],[vx_b, vy_b]])
rot = np.array([180, 0]) #red, blue

mis_coord = np.array([[0,0],[0,0]])
mis_rot = np.array([0,0])
v_mis = np.array([[0,0],[0,0]])

running = True
while running:
    t_run = 0.001 * pg.time.get_ticks() - t_start
    if t_run - t_prev >= dt:
        t_prev = t_run
        
        pos = pos + v * dt
        #for the corners
        pos[pos > 1000] = 0
        pos[pos < 0] = 1000
        
        red_rect = redship[int(rot[RED])].get_rect()
        blue_rect = blueship[int(rot[BLUE])].get_rect()
        
        red_rect.center = pos[RED]
        blue_rect.center = pos[BLUE]
        #keyboard controls for changing the rotation & direction
        pg.event.pump()
        keys = pg.key.get_pressed()
        
        pg.draw.rect(scr,black,scrrect)
        if keys[pg.K_ESCAPE]:
            running = False
        if keys[pg.K_a]:
            rot[RED] += OMEGA * dt
        if keys[pg.K_d]:
            rot[RED] -= OMEGA * dt
        if keys[pg.K_k]:
            rot[BLUE] += OMEGA * dt
        if keys[pg.K_SEMICOLON]:
            rot[BLUE] -= OMEGA * dt
        if keys[pg.K_s]:
            if t_mis_r > 1e-3:
                False
            else:
                t_mis_r = 1
                mis_coord[RED] = pos[RED]
                mis_rot[RED] = rot[RED]
                v_mis[RED] = np.array([M_V * math.cos(math.radians(-1 * mis_rot[RED])), M_V * math.sin(math.radians(-1 * mis_rot[RED]))])
                print(v_mis[RED])
                missile_red_rect = missile[int(mis_rot[RED])].get_rect()
                          
        if keys[pg.K_l]:
            if t_mis_b > 1e-3:
                False
            else:
                t_mis_b = 1
        
        if t_mis_r > 0:
            mis_coord[RED] = mis_coord[RED] + v_mis[RED] * dt
            missile_red_rect.center = mis_coord[RED]
            scr.blit(missile[mis_rot[RED]], missile_red_rect)
            t_mis_r -= dt

        rot[rot > 359] = 0
        rot[rot < 0] = 359
        
        vx_r, vy_r, vx_b, vy_b = V*math.cos(math.radians(-1 * rot[RED])), V*math.sin(math.radians(-1 * rot[RED])),V*math.cos(math.radians(-1 * rot[BLUE])), V*math.sin(math.radians(-1 * rot[BLUE]))
        
        v = np.array([[vx_r, vy_r],[vx_b, vy_b]])
        
        scr.blit(redship[rot[RED]], red_rect)
        scr.blit(blueship[rot[BLUE]], blue_rect)
        
        pg.display.flip()
    
pg.quit()