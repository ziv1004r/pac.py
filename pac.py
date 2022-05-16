from ast import If
from calendar import c
from turtle import color
import pygame
 
#basic for game
WINDOW_W = 1300
WINDOW_H = 500
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
pygame.init()

#basic
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("PAC - MAN --> made by ziv") 

bk = pygame.image.load("pacpage.png")
bk = pygame.transform.scale(bk,(WINDOW_W,WINDOW_H))

pac = pygame.image.load("PACLOL right.png")
pac = pygame.transform.scale(pac,(30,30))

enemy1 = pygame.image.load("enemypac.png")
enemy1 = pygame.transform.scale(enemy1,(30,30))

candy_pick = pygame.image.load("candy.png")
candy_pick = pygame.transform.scale(candy_pick,(15,15))

over = pygame.image.load("game-over.jpg")
over = pygame.transform.scale(bk,(WINDOW_W,WINDOW_H))

clock = pygame.time.Clock()

#x and y
pac_x = WINDOW_W -585
pac_y = WINDOW_H - 380
candy_y = 30
candy_x = 30
x_step = 7
y_step = 7
pac_x_step = 15
enemy1_x = WINDOW_W / 2 
enemy1_y = WINDOW_H / 2 -66

#score
score = 0
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score P:' + str(score), True, (255, 255, 0))

#score1
score1 = 0
myfont1 = pygame.font.SysFont('Comic Sans MS', 30)
textsurface1 = myfont.render('Score E:' + str(score), True, (202,225,255))



      
play = True
while play:
  #blit 
  screen.blit(bk,(0,0))
  screen.blit(textsurface,(10,20))
  screen.blit(textsurface1,(1100,20))
  screen.blit(pac,(pac_x,pac_y))
  screen.blit(enemy1,(enemy1_x,enemy1_y))
  #print candy
  for candy in range(5):
   screen.blit(candy_pick,(candy_x,candy_y)) 
   candy_x += 10

 
#color enemy
  #color left
  color_left_ene = screen.get_at((int(enemy1_x),int(enemy1_y + 15)))
  color_left_top_ene = screen.get_at((int(enemy1_x),int(enemy1_y + 7)))
  color_left_under_ene = screen.get_at((int(enemy1_x),int(enemy1_y + 22)))
  #color right
  color_right_ene = screen.get_at((int(enemy1_x + 30),int(enemy1_y + 15)))
  color_right_top_ene = screen.get_at((int(enemy1_x + 30),int(enemy1_y + 7)))
  color_right_under_ene = screen.get_at((int(enemy1_x + 30),int(enemy1_y + 22)))
  #color top
  color_top_ene = screen.get_at((int(enemy1_x + 15),int(enemy1_y)))
  color_top_left_ene = screen.get_at((int(enemy1_x + 7 ),int(enemy1_y)))
  color_top_right_ene = screen.get_at((int(enemy1_x + 22),int(enemy1_y)))
  # color under
  color_under_ene = screen.get_at((int(enemy1_x + 15),int(enemy1_y + 30)))
  color_under_right_ene = screen.get_at((int(enemy1_x + 22),int(enemy1_y + 30)))
  color_under_left_ene = screen.get_at((int(enemy1_x + 7),int(enemy1_y + 30)))
 
  #clicks 
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a]:
    if color_left_ene and color_left_top_ene and color_left_under_ene == (0,0,0,255):
      enemy1_x -= x_step
    elif color_left_ene and color_left_top_ene and color_left_under_ene == (244, 238, 66, 255):
      play = False


  if keys[pygame.K_d]:
    if color_right_top_ene and color_right_under_ene and color_right_ene == (0,0,0,255):
      enemy1_x += x_step

  if keys[pygame.K_w]:
    if color_top_ene and color_top_left_ene and color_top_right_ene == (0,0,0,255):
      enemy1_y -= y_step  

  if keys[pygame.K_s]:
    if color_under_ene and color_under_left_ene and color_under_right_ene == (0,0,0,255):
      enemy1_y += y_step 
    elif color_under_ene or color_under_right_ene or color_under_left_ene == (9, 0, 255, 255):
      pass



  for event in pygame.event.get():
  #color left
    color_left_ene = screen.get_at((int(enemy1_x),int(enemy1_y + 15)))
    color_left_top_ene = screen.get_at((int(enemy1_x),int(enemy1_y + 7)))
    color_left_under_ene = screen.get_at((int(enemy1_x),int(enemy1_y + 22)))
    #color right
    color_right_ene = screen.get_at((int(enemy1_x + 30),int(enemy1_y + 15)))
    color_right_top_ene = screen.get_at((int(enemy1_x + 30),int(enemy1_y + 7)))
    color_right_under_ene = screen.get_at((int(enemy1_x + 30),int(enemy1_y + 22)))
    #color top
    color_top_ene = screen.get_at((int(enemy1_x + 15),int(enemy1_y)))
    color_top_left_ene = screen.get_at((int(enemy1_x + 7 ),int(enemy1_y)))
    color_top_right_ene = screen.get_at((int(enemy1_x + 22),int(enemy1_y)))
    # color under
    color_under_ene = screen.get_at((int(enemy1_x + 15),int(enemy1_y + 30)))
    color_under_right_ene = screen.get_at((int(enemy1_x + 22),int(enemy1_y + 30)))
    color_under_left_ene = screen.get_at((int(enemy1_x + 7),int(enemy1_y + 30)))

    if event.type == pygame.QUIT:
      play = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        if color_left_ene and color_left_top_ene and color_left_under_ene == (0,0,0,255):
          enemy1_x -= x_step
        elif color_left_ene and color_left_top_ene and color_left_under_ene == (244, 238, 66, 255):
          play = False

      if event.key == pygame.K_d:
        if color_right_top_ene and color_right_under_ene and color_right_ene == (0,0,0,255):
          enemy1_x += x_step

      if event.key == pygame.K_w:
        if color_top_ene and color_top_left_ene and color_top_right_ene == (0,0,0,255):
          enemy1_y -= y_step

      if event.key == pygame.K_s:
        if color_under_ene and color_under_left_ene and color_under_right_ene == (0,0,0,255):
          enemy1_y += y_step 
        elif color_under_ene or color_under_right_ene or color_under_left_ene == (9, 0, 255, 255):
          pass

 

  #teleport
  if enemy1_x <= 31:
    enemy1_x = 1250
  if enemy1_x > WINDOW_W - 30:
    enemy1_x = 30




#color player
  #color left
  color_left = screen.get_at((int(pac_x),int(pac_y + 15)))
  color_left_top = screen.get_at((int(pac_x),int(pac_y + 7)))
  color_left_under = screen.get_at((int(pac_x),int(pac_y + 22)))
  #color right
  color_right = screen.get_at((int(pac_x + 30),int(pac_y + 15)))
  color_right_top = screen.get_at((int(pac_x + 30),int(pac_y + 7)))
  color_right_under = screen.get_at((int(pac_x + 30),int(pac_y + 22)))
  #color top
  color_top = screen.get_at((int(pac_x + 15),int(pac_y)))
  color_top_left = screen.get_at((int(pac_x + 7 ),int(pac_y)))
  color_top_right = screen.get_at((int(pac_x + 22),int(pac_y)))
  # color under
  color_under = screen.get_at((int(pac_x + 15),int(pac_y + 30)))
  color_under_right = screen.get_at((int(pac_x + 22),int(pac_y + 30)))
  color_under_left = screen.get_at((int(pac_x + 7),int(pac_y + 30)))

  #clicks player
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    pac = pygame.image.load("PACLOL left.png")
    pac = pygame.transform.scale(pac,(30,30))
    screen.blit(pac,(pac_x,pac_y))
    if color_left and color_left_top and color_left_under == (0,0,0,255):
      pac_x -= x_step
    print(color_left)
  if keys[pygame.K_RIGHT]:
    pac = pygame.image.load("PACLOL right.png")
    pac = pygame.transform.scale(pac,(30,30))
    screen.blit(pac,(pac_x,pac_y))
    if color_right_top and color_right_under and color_right == (0,0,0,255):
      pac_x += x_step
    elif color_left and color_left_top and color_left_under == (112, 201, 194, 255):
      play = False 


  if keys[pygame.K_UP]:
    pac = pygame.image.load("PACLOL top.png")
    pac = pygame.transform.scale(pac,(30,30))
    screen.blit(pac,(pac_x,pac_y))
    if color_top and color_top_left and color_top_right == (0,0,0,255):
      pac_y -= y_step 
    elif color_left and color_left_top and color_left_under == (112, 201, 194, 255):
      play = False 

  if keys[pygame.K_DOWN]:
    pac = pygame.image.load("PACLOLunder.png")
    pac = pygame.transform.scale(pac,(30,30))
    screen.blit(pac,(pac_x,pac_y))
    if color_under and color_under_left and color_under_right == (0,0,0,255):
      pac_y += y_step 
    elif color_under or color_under_right or color_under_left == (9, 0, 255, 255):
      pass
    elif color_left and color_left_top and color_left_under == (112, 201, 194, 255):
      play = False



  for event in pygame.event.get():
    #color left
    color_left = screen.get_at((int(pac_x),int(pac_y + 15)))
    color_left_top = screen.get_at((int(pac_x),int(pac_y + 7)))
    color_left_under = screen.get_at((int(pac_x),int(pac_y + 22)))
    #color right
    color_right = screen.get_at((int(pac_x + 30),int(pac_y + 15)))
    color_right_top = screen.get_at((int(pac_x + 30),int(pac_y + 7)))
    color_right_under = screen.get_at((int(pac_x + 30),int(pac_y + 22)))
    #color top
    color_top = screen.get_at((int(pac_x + 15),int(pac_y)))
    color_top_left = screen.get_at((int(pac_x + 7 ),int(pac_y)))
    color_top_right = screen.get_at((int(pac_x + 22),int(pac_y)))
    # color under
    color_under = screen.get_at((int(pac_x + 15),int(pac_y + 30)))
    color_under_right = screen.get_at((int(pac_x + 22),int(pac_y + 30)))
    color_under_left = screen.get_at((int(pac_x + 7),int(pac_y + 30)))

    if event.type == pygame.QUIT:
      play = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        pac = pygame.image.load("PACLOL left.png")
        pac = pygame.transform.scale(pac,(30,30))
        screen.blit(pac,(pac_x,pac_y))
        if color_left and color_left_top and color_left_under == (0,0,0,255):
          pac_x -= x_step
        elif color_left and color_left_top and color_left_under == (112, 201, 194, 255):
          play = False

      if event.key == pygame.K_RIGHT:
        pac = pygame.image.load("PACLOL right.png")
        pac = pygame.transform.scale(pac,(30,30))
        screen.blit(pac,(pac_x,pac_y))
        if color_right_top and color_right_under and color_right == (0,0,0,255):
          pac_x += x_step
        elif color_left and color_left_top and color_left_under == (112, 201, 194, 255):
          play = False

      if event.key == pygame.K_UP:
        pac = pygame.image.load("PACLOL top.png")
        pac = pygame.transform.scale(pac,(30,30))
        screen.blit(pac,(pac_x,pac_y))
        if color_top and color_top_left and color_top_right == (0,0,0,255):
          pac_y -= y_step
        elif color_left and color_left_top and color_left_under == (112, 201, 194, 255):
          play = False

      if event.key == pygame.K_DOWN:
        pac = pygame.image.load("PACLOLunder.png")
        pac = pygame.transform.scale(pac,(30,30))
        screen.blit(pac,(pac_x,pac_y))
        if color_under and color_under_left and color_under_right == (0,0,0,255):
          pac_y += y_step 
        elif color_under or color_under_right or color_under_left == (9, 0, 255, 255):
          pass
        elif color_left and color_left_top and color_left_under == (112, 201, 194, 255):
          play = False
 

  #teleport
  if pac_x <= 31:
    pac_x = 1250
  if pac_x > WINDOW_W - 30:
    pac_x = 30
  pygame.display.flip()


  clock.tick(10)
pygame.quit()
