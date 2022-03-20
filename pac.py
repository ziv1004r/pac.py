from ast import If
from turtle import color
import pygame
 
WINDOW_W = 1300
WINDOW_H = 500
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
score = 0



pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("PAC - MAN --> ziv") 
bk = pygame.image.load("PACPAC.png")
bk = pygame.transform.scale(bk,(WINDOW_W,WINDOW_H))
pac = pygame.image.load("PACLOL.png")
pac = pygame.transform.scale(pac,(30,30))
clock = pygame.time.Clock()


pac_x = WINDOW_W /2
pac_y = WINDOW_H - 80

pac_x_step = 10
x_step = 7
play = True

y_step = 7

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score:', True, (255, 255, 255))
screen.blit(textsurface,(10,20))
vector1 = False
vector2 = False
vector3 = False
vector4 = False


while play:
  screen.blit(bk,(0,0))
  screen.blit(pac,(pac_x,pac_y))
  color_left = screen.get_at((int(pac_x),int(pac_y + 15)))
  color_right = screen.get_at((int(pac_x + 30),int(pac_y + 15)))
  color_top = screen.get_at((int(pac_x + 15),int(pac_y)))
  color_under = screen.get_at((int(pac_x + 15),int(pac_y - 32)))
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    if color_left == (0,0,1,255):
      pac_x -= x_step
    else:
      print('The color is not black here')

  if keys[pygame.K_RIGHT]:
    if color_right == (0,0,1,255):
      pac_x += x_step

  if keys[pygame.K_UP]:
    if color_top == (0,0,1,255):
      pac_y -= y_step  

  if keys[pygame.K_DOWN]:
    if color_under == (0,0,1,255):
      pac_y += y_step 



  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:

        if color_left == (0,0,1,255):
          pac_x -= x_step
        else:
          print('The color is not black here')

      if event.key == pygame.K_RIGHT:
        if color_right == (0,0,1,255):
          pac_x += x_step

      if event.key == pygame.K_UP:
        if color_top == (0,0,1,255):
          pac_y -= y_step

      if event.key == pygame.K_DOWN:
        if color_under == (0,0,1,255):
          pac_y += y_step 


  if pac_x <= 30:
    pac_x = WINDOW_W - 30
  if pac_x > WINDOW_W - 30:
    pac_x = + 30
  pygame.display.flip()


  clock.tick(10)

pygame.quit()
