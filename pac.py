import pygame
 
WINDOW_W = 1336
WINDOW_H = 500
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
score = 0



pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("PAC - MAN --> ziv") 
bk = pygame.image.load("PACPAC.png")
bk = pygame.transform.scale(bk,(WINDOW_W,WINDOW_H))
pac = pygame.image.load("PACLOL.png")
pac = pygame.transform.scale(pac,(40,40))
clock = pygame.time.Clock()


pac_x = WINDOW_W /2
pac_y = WINDOW_H - 80

pac_x_step = 10
x_step = 10
play = True


myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score:', True, (255, 255, 255))
screen.blit(textsurface,(10,20))




while play:
  screen.blit(bk,(0,0))
  screen.blit(pac,(pac_x,pac_y))
  # pygame.draw.rect(screen,(24,116,205),((20,15),(1300,15)))
  # pygame.draw.rect(screen,(24,116,205),((20,480),(1300,480)))

  # pygame.draw.rect(screen,(24,116,205),((20,15),(20,200)))
  # pygame.draw.rect(screen,(24,116,205),((1315,15),(1315,200)))
  # pygame.draw.rect(screen,(24,116,205),((1315,270),(1315,480)))
  # pygame.draw.rect(screen,(24,116,205),((20,270),(20,480)))
  
  # pygame.draw.rect(screen,(24,116,205),((20,200),(150,20)))
  # pygame.draw.rect(screen,(24,116,205),((20,270),(150,20)))
  # pygame.draw.rect(screen,(24,116,205),((1165,270),(150,20)))
  # pygame.draw.rect(screen,(24,116,205),((1165,195),(150,20)))
  
  # pygame.draw.rect(screen,(24,116,205),((250,100),(70,250)))
  # pygame.draw.rect(screen,(24,116,205),((1000,100),(70,250)))

  event = 0
  num = 0
  if event.key == pygame.K_LEFT:
    event = 1
  if event.key == pygame.K_LEFT:
    event = 2
 

  pygame.display.flip()


  clock.tick(10)

pygame.quit()
