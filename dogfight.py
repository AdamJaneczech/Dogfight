import pygame as pg

def rotateSurface(surf):
    rotatedSurfaces = []
    for theta in range(0,359):
        rotated_image = pg.transform.rotate(surf, theta)
        rotatedSurfaces.append(rotated_image.get_rect())
    return rotatedSurfaces

pg.init()
scr = pg.display.set_mode((1000,1000))
redship_img = pg.transform.scalepg.image.load('gamefiles/redship.png')
redship_r = redship_img.get_rect()
blueship_img = pg.image.load('gamefiles/redship.png')
blueship_r = blueship_img.get_rect()
missile_img = pg.image.load('gamefiles/redship.png')
missile_r = missile_img.get_rect()
ex1 = pg.image.load('gamefiles/redship.png')
ex1_r = ex1.get_rect()
ex2 = pg.image.load('gamefiles/redship.png')
ex2_r = ex2.get_rect()
ex3 = pg.image.load('gamefiles/redship.png')
ex3_r = ex3.get_rect()
ex4 = pg.image.load('gamefiles/redship.png')
ex4_r = ex4.get_rect()

rotated_image = pg.transform.rotate(redship_img, 45)
scr.fill((0, 0, 0))

# Draw the rotated image at the center of the screen
image_rect = rotated_image.get_rect(center=(400, 300))
scr.blit(rotated_image, image_rect.topleft)

# Update the display
pg.display.flip()
while True:
    pg.display.flip()
pg.quit()