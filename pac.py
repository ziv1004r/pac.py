from ast import If
from calendar import c
from tkinter.tix import IMAGE
from turtle import color, left, right
from winsound import PlaySound
import pygame
import time
import cv2 as cv
import mediapipe as mp
import time

#basic for game
WINDOW_W = 1300
WINDOW_H = 500
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
pygame.init()

#ai
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

#basic
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("PAC - MAN --> made by @itzhak.ziv ") 

#BK
bk = pygame.image.load("pacpage.png")
bk = pygame.transform.scale(bk,(WINDOW_W,WINDOW_H))

#PAC
pac = pygame.image.load("PACLOL right.png")
pac = pygame.transform.scale(pac,(30,30))
#ENEMY
enemy1 = pygame.image.load("enemypac.png")
enemy1 = pygame.transform.scale(enemy1,(30,30))

#CANDY 
candy_pick = pygame.image.load("candy.png")
candy_pick = pygame.transform.scale(candy_pick,(15,15))


#WIN-LOSE
over = pygame.image.load("gamelose.png")
over = pygame.transform.scale(over,(400, 200))

won = pygame.image.load("won.png")
won = pygame.transform.scale(won,(400,200))

clock = pygame.time.Clock()

#x and y
pac_x = WINDOW_W -585
pac_y = WINDOW_H - 380
x_step = 6
y_step = 6

enemy1_x = WINDOW_W / 2 
enemy1_y = WINDOW_H / 2

bot1_x = 300 
bot1_2_y = 20
bot2_x = WINDOW_W - 310
bot3_4_x = 65
bot3_y = 20
bot4_y = WINDOW_H - 50
bot5_6_x = WINDOW_W // 2 + 20

candy1_2x = 120
candy1_y = 50
candy2_y = WINDOW_H - 70
candy3_4x = WINDOW_W - 130




#score for player
score = 0
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score P:' + str(score), True, (255, 255, 0))

#score1 for enemy
score1 = 0
myfont1 = pygame.font.SysFont('Comic Sans MS', 30)
textsurface1 = myfont.render('Score E:' + str(score1), True, (202,225,255))
 

cap = cv.VideoCapture(0)

def bilt():
  global pac_y, pac_x , bot1_x , bot1_2_y , bot2_x ,textsurface, textsurface1
  screen.blit(bk,(0,0))
  screen.blit(pac,(pac_x,pac_y))
  screen.blit(textsurface,(10,250))
  screen.blit(textsurface1,(1100,250))
  screen.blit(textsurface2,(590,200))

  screen.blit(enemy1,(bot1_x,bot1_2_y))
  screen.blit(enemy1,(bot2_x,bot1_2_y))

  screen.blit(enemy1,(bot3_4_x,bot3_y))
  screen.blit(enemy1,(bot3_4_x,bot4_y))

  screen.blit(enemy1,(bot5_6_x,bot3_y))
  screen.blit(enemy1,(bot5_6_x,bot4_y))

  if can1 == 0 :
    screen.blit(candy_pick,(candy1_2x,candy1_y))
  if can2 == 0 :
    screen.blit(candy_pick,(candy1_2x,candy2_y))
  if can3 == 0 :
    screen.blit(candy_pick,(candy3_4x,candy1_y))
  if can4 == 0 :
    screen.blit(candy_pick,(candy3_4x,candy2_y))

bot_step = 4
plus = 0 
min = 0
def plusY():
  #bot way
  global min , plus , bot1_2_y , bot3_4_x , bot5_6_x , bot_step
  bot1_2_y += bot_step
  bot3_4_x += bot_step
  bot5_6_x += bot_step
  if   370< bot1_2_y >400:
    bot1_2_y = 20
  if 600 < bot3_4_x <(WINDOW_W//2 - 30 ):
    bot3_4_x = 65
  if 1200 < bot5_6_x <1230:
    bot5_6_x = WINDOW_W//2 + 20

can1 = 0
can2 = 0
can3 = 0
can4 = 0

def get_candys():
  # get candy or nah
  global can1 , can2 , can3 ,can4 , score
  if (pac_x -  candy1_2x) < 30 and ( pac_y - candy1_y) < 30 and can1 == 0 :
    score  += 2
    can1 = 1
    print("yay i got")

  elif (pac_x -  candy1_2x) < 30 and ( candy2_y -pac_y ) < 30 and can2 == 0:
    score += 2
    can2 = 2
    print("yay i got2")

  elif ( candy3_4x - pac_x ) < 30 and ( pac_y - candy1_y) < 30 and can3 == 0:
    score += 2
    can3 = 3
    print("yay i got3")
  
  elif (candy3_4x -  pac_x) < 30 and ( candy2_y - pac_y) < 30 and can4 == 0 :
    score += 2
    can4 = 4
    print("yay i got4")

level = 1
play = True
while play:
  #blit
  myfont = pygame.font.SysFont('Comic Sans MS', 30)
  textsurface = myfont.render('Score P:' + str(round(score)), True, (255, 255, 0)) 
  myfont1 = pygame.font.SysFont('Comic Sans MS', 30)
  textsurface1 = myfont.render('Score E:' + str(score1), True, (202,225,255))
  myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
  textsurface2 = myfont.render('LEVEL:' + str(level), True, (255,225,255))
  bilt()

  #calling def
  plusY()
  get_candys()

  #close the window
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

  #who won
  if score1 == 6 :
    screen.blit(over,(450, 200))
  elif score == 8 :
    screen.blit(won,(450,200))

 #color player
  #color left
  color_left = screen.get_at((int(pac_x +2),int(pac_y + 15)))
  color_left_top = screen.get_at((int(pac_x),int(pac_y + 7)))
  color_left_under = screen.get_at((int(pac_x ),int(pac_y + 22)))
  #color right
  color_right = screen.get_at((int(pac_x + 32),int(pac_y + 15)))
  color_right_top = screen.get_at((int(pac_x + 30),int(pac_y + 7)))
  color_right_under = screen.get_at((int(pac_x + 30),int(pac_y + 22)))
  #color top
  color_top = screen.get_at((int(pac_x + 15),int(pac_y+2)))
  color_top_left = screen.get_at((int(pac_x + 7 ),int(pac_y)))
  color_top_right = screen.get_at((int(pac_x + 22),int(pac_y)))
  # color under
  color_under = screen.get_at((int(pac_x + 15),int(pac_y + 32)))
  color_under_right = screen.get_at((int(pac_x + 22),int(pac_y + 30)))
  color_under_left = screen.get_at((int(pac_x + 7),int(pac_y + 30)))
  
  #camera
  ret, frame = cap.read(0)
  RGB_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  results = hands.process(RGB_image)
  multiLandMarks = results.multi_hand_landmarks
  
  if not ret:
   print("Can't receive frame (stream end?). Exiting ...")
   break

  if color_right_top and color_right_under and color_right ==  (112, 201, 194, 255) :
    score1 = score1 + 2
    pac_x = WINDOW_W -585
    pac_y = WINDOW_H - 380
  elif  color_left and color_left_top and color_left_under ==  (112, 201, 194, 255):
    score1 = score1 + 2
    pac_x = WINDOW_W -585
    pac_y = WINDOW_H - 380
  elif color_top and color_top_left and color_top_right ==  (112, 201, 194, 255):
    score1 = score1 + 2
    pac_x = WINDOW_W - 585
    pac_y = WINDOW_H - 380
  elif color_under and color_under_left and color_under_right == (112, 201, 194, 255):
    score1 = score1 + 2
    pac_x = WINDOW_W -585
    pac_y = WINDOW_H - 380

  if multiLandMarks:
    index_finger_x = multiLandMarks[0].landmark[8].x
    index_finger_y = multiLandMarks[0].landmark[8].y
    index_finger_y5 = multiLandMarks[0].landmark[5].y
    close1 = index_finger_y < index_finger_y5 

    index_finger_y12 = multiLandMarks[0].landmark[12].y
    index_finger_y9 = multiLandMarks[0].landmark[9].y
    close2 = index_finger_y12 < index_finger_y9

    index_finger_y16 = multiLandMarks[0].landmark[16].y
    index_finger_y13 = multiLandMarks[0].landmark[13].y
    close3 = index_finger_y16 > index_finger_y13

    index_finger_y20 = multiLandMarks[0].landmark[20].y
    index_finger_y17 = multiLandMarks[0].landmark[17].y
    close4 = index_finger_y20 < index_finger_y17

    if (close1 and close2 and close3 and close4 == True) and (score1 == 6):
      score = 0 
      score1 = 0
      level = 1
      pac_x = WINDOW_W -585
      pac_y = WINDOW_H - 380
      can1 = 0
      can2 = 0
      can3 = 0
      can4 = 0 
      bot_step = 4

    elif (close1 and close2 and close3 and close4 == True) and (score == 8):
      pac_x = WINDOW_W -585
      pac_y = WINDOW_H - 380
      level += 1
      can1 = 0
      can2 = 0
      can3 = 0
      can4 = 0
      score = 0
      bot_step += 2

    if (index_finger_x < 0.25 and score1 != 6 )and (index_finger_x < 0.25 and score != 8):
      pac = pygame.image.load("PACLOL right.png")
      pac = pygame.transform.scale(pac,(30,30))
      screen.blit(pac,(pac_x,pac_y))
      print(color_right)
      if color_right_top and color_right_under and color_right == (0,0,0,255):
        pac_x += x_step
        if pac_x > WINDOW_W - 50:
         pac_x = 30


    elif (index_finger_x > 0.75 and score1 != 6) and (index_finger_x > 0.75 and score !=8):
      pac = pygame.image.load("PACLOL left.png")
      pac = pygame.transform.scale(pac,(30,30))
      screen.blit(pac,(pac_x,pac_y))
      if color_left and color_left_top and color_left_under == (0,0,0,255):
        pac_x -= x_step
        if pac_x <= 31:
          pac_x = 1250


    elif (0.5 > index_finger_y and score1 != 6 ) and (0.5 > index_finger_y and score != 8) :
      pac = pygame.image.load("PACLOL top.png")
      pac = pygame.transform.scale(pac,(30,30))
      cv.putText(frame, 'up', (100,100),cv.FONT_HERSHEY_SIMPLEX,3, (255, 0, 0), 2 , cv.LINE_AA)
      if color_top and color_top_left and color_top_right == (0,0,0,255):
        pac_y -= y_step

    elif (0.5< index_finger_y and score1 != 6) and (0.5 < index_finger_y and score != 8):
      pac = pygame.image.load("PACLOLunder.png")
      pac = pygame.transform.scale(pac,(30,30))
      cv.putText(frame, 'down', (100,100),cv.FONT_HERSHEY_SIMPLEX,3, (255, 0, 0), 2 , cv.LINE_AA)
      if color_under and color_under_left and color_under_right == (0,0,0,255):
        pac_y += y_step 
      elif color_under or color_under_right or color_under_left == (9, 0, 255, 255):
        pass


    for handLms in multiLandMarks:
      mpDraw.draw_landmarks(frame, handLms, mp_Hands.HAND_CONNECTIONS)
    
      
  cv.imshow('frame',frame)  
  if cv.waitKey(1) == ord('q'):
    break
  

  
  pygame.display.flip()
cap.release()
cv.destroyAllWindows()
clock.tick(10)
pygame.quit()

