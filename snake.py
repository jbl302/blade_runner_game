import pygame
from sys import exit
import time
from random import randint,choice

# from pygame.sprite import _Group


class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    player_walk_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
    player_walk_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_walk_2.png").convert_alpha()
    self.player_walk = [player_walk_1,player_walk_2]
    self.player_index = 0
    self.player_jump = pygame.image.load("UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha()
    self.image = self.player_walk[self.player_index]
    self.rect = self.image.get_rect(midbottom = (80,300))
    self.gravity = 0
    self.jump_sound = pygame.mixer.Sound("UltimatePygameIntro-main/audio/jump.mp3")
    self.jump_sound.set_volume(.1)
    
  def player_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and self.rect.bottom>=300:
      self.jump_sound.play()
      self.gravity = -20
      # print('in key_press')
  def gravity_apply(self):
    self.gravity+=1
    self.rect.y +=self.gravity
    
    if self.rect.bottom>=300:
      self.rect.bottom = 300
  def update(self):
    # print('inside player')
    self.player_input()
    self.gravity_apply()
    self.animation_player()
    
  def animation_player(self):
    if self.rect.bottom==300:
      # print('animation inside')
      self.player_index +=.1
      if self.player_index>len(self.player_walk):self.player_index=0
      self.image = self.player_walk[int(self.player_index)]
    else:
      self.image = self.player_jump

class obstacles(pygame.sprite.Sprite):
  def __init__(self,type):
    super().__init__()
    
    if type == 'fly':
      fly_frame1 = pygame.image.load("UltimatePygameIntro-main/graphics/Fly/Fly1.png")
      fly_frame2 = pygame.image.load("UltimatePygameIntro-main/graphics/Fly/Fly2.png")
      self.frame = [fly_frame1,fly_frame2]
      y_pos = 200
    else:
      snail_frame1= pygame.image.load("D:/move_game/UltimatePygameIntro-main/graphics/snail/snail1.png").convert_alpha()
      snail_frame2= pygame.image.load("D:/move_game/UltimatePygameIntro-main/graphics/snail/snail2.png").convert_alpha()
      self.frame = [snail_frame1,snail_frame2]
      y_pos = 300
    
    self.animation_index = 0   
    self.image = self.frame[self.animation_index]
    self.rect = self.image.get_rect(midbottom = (randint(900,1000),y_pos))
    
  def obstacle_animation(self):
       self.animation_index +=.1
       if self.animation_index>len(self.frame):self.animation_index = 0
       self.image = self.frame[int(self.animation_index)]
    
  def update(self):
      # print('inside update')
      self.rect.x -=6
      self.obstacle_animation()
  
  def destroy(self):
    if self.rect<-100:
      self.kill()       
  
def player_animation():
  global player_index,player_surf
  if player_rect.bottom == 300: #walk
    player_index+=.1
    if player_index>len(player_walk): player_index=0
    player_surf = player_walk[int(player_index)]
  else:
    player_surf = player_jump
def obstacle_movement(obstacle_list):
  # print('in loop')
  if obstacle_list:
    for obstacle_rect in obstacle_list:

      obstacle_rect.x-=4
      if obstacle_rect.bottom ==300:
        screen.blit(snail_surf,obstacle_rect)
      else:
        screen.blit(fly_surf,obstacle_rect)
    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle_rect.x > -100] # only copy those obstacle which are in the screen 
    return obstacle_list
  else:
    return []

def collsions(player,obstacle):
  if obstacle:
    for obstacle_rect in obstacle:
      if player.colliderect(obstacle_rect): 
        return False
  # print('shit')
  return True
def collsion_sprite():
  if pygame.sprite.spritecollide(player.sprite,obstacle_group,True):
    obstacle_group.empty()
    return False
  return True
  
def display_score():
  current_time = round(pygame.time.get_ticks()/250-start_time/250)
  score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
  score_rect = score_surf.get_rect(center = (400,100))
  screen.blit(score_surf,score_rect)
  return current_time
  
pygame.init() # Start the engine of a car
start_time = 0
# create a display service
screen = pygame.display.set_mode((700,400)) # ran for one frame
pygame.display.set_caption("BLADE_RUNNER")

# creating 60 fps max
clock = pygame.time.Clock()
bg_music = pygame.mixer.Sound("UltimatePygameIntro-main/audio/music.wav")
bg_music.play(loops = -1)
bg_music.set_volume(.5)

test_font = pygame.font.Font("D:/move_game/UltimatePygameIntro-main/font/Pixeltype.ttf",50)
sky_surface = pygame.image.load("D:/move_game/UltimatePygameIntro-main/graphics/Sky.png").convert() # A picure which is the content

gnd_surface = pygame.image.load("D:/move_game/UltimatePygameIntro-main/graphics/ground.png").convert()

# score_surf = test_font.render("SMOOTH MACHINE",False,(64,64,64))
# score_rect = score_surf.get_rect(center = (400,100))
# snail_image = pygame.image.load("spritesheet.png").convert_alpha()
snail_frame1= pygame.image.load("D:/move_game/UltimatePygameIntro-main/graphics/snail/snail1.png").convert_alpha()
snail_frame2= pygame.image.load("D:/move_game/UltimatePygameIntro-main/graphics/snail/snail2.png").convert_alpha()
snail_frame = [snail_frame1,snail_frame2]
snail_index = 0
snail_surf = snail_frame[snail_index]
# snail_rect = snail_surf.get_rect(snail_surf)


fly_frame1 = pygame.image.load("UltimatePygameIntro-main/graphics/Fly/Fly1.png")
fly_frame2 = pygame.image.load("UltimatePygameIntro-main/graphics/Fly/Fly2.png")
fly_frame = [fly_frame1,fly_frame2]
fly_index = 0
fly_surf = fly_frame[fly_index]
# fly_rect = fly_surf.get_rect(fly_surf)

obstacle_group = pygame.sprite.Group()

player = pygame.sprite.GroupSingle()
player.add(Player())
player_walk_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load("UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (100,300)) # creating a rectangle around player and also point fo control

player_stand = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (350,200))

game_active = False
gravity = 0
score = 0

obstacle_list = []
#timer
obstacle_timer = pygame.USEREVENT+1 #custom user event
pygame.time.set_timer(obstacle_timer,950)

snail_timer = pygame.USEREVENT+2
pygame.time.set_timer(snail_timer,500)

fly_timer = pygame.USEREVENT+3
pygame.time.set_timer(fly_timer,150)

while True:
  for event in pygame.event.get(): # event loop
    if event.type == pygame.QUIT:
        pygame.quit() # opposite of init 
        exit() 
    if game_active:
      
      # closes any running program
      if event.type == obstacle_timer:
        obstacle_group.add(obstacles(choice(['fly','snail','snail'])))
        
        # print(randint(0,1))
        # if randint(0,2):
        #   obstacle_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
        # else:
        #   obstacle_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),200)))
        # obstacle_list = obstacle_movement(obstacle_list)

      # if event.type == pygame.KEYDOWN:
      #   if event.key == pygame.K_SPACE: gravity = -20
          # print('jump')
        
      # if event.type == pygame.MOUSEBUTTONDOWN:
      #   if player_rect.collidepoint(event.pos):gravity = -20
          # print('jump')
      
      # if event.type == snail_timer:
      #   if snail_index == 0: snail_index =1
      #   else: snail_index = 0
      #   snail_surf = snail_frame[snail_index]
      
      # if event.type == fly_timer:
        
      #   if fly_index == 0: fly_index = 1
      #   else: fly_index = 0
      #   fly_surf = fly_frame[fly_index]
      
          
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_active = True
        start_time = pygame.time.get_ticks()
    
  if game_active:   
      screen.blit(sky_surface,(0,0)) # put surface over other surface ,
      screen.blit(gnd_surface,(0,300))
      
      # gravity+=1
      # player_rect.y+=gravity
      # obstacle_list = obstacle_movement(obstacle_list)
      
      #obstacle movement
      # if player_rect.bottom >= 300:player_rect.bottom =  300# Acting like collison with the floor
      # screen.blit(player_surf,player_rect)
      game_active = collsion_sprite()
      
      player.draw(screen)
      player_animation()
      player.update()
      
      obstacle_group.draw(screen)  
      obstacle_group.update()
        # pygme.quit() # opposite of init 
        # exit() # closes any running program
      score = max(display_score(),score)
  else: # intro screen
    obstacle_list.clear()
    player_rect.midbottom = (60,300)
    gravity = 0
    screen.fill((50, 121, 168))
    screen.blit(player_stand,player_stand_rect)
    title = test_font.render("Cutie runner",False,(154, 168, 50))
    title_rect = title.get_rect(center = (350,100))
    instruction = test_font.render("To Start Press Space",False,(50, 168, 121))
    instruction_rect = instruction.get_rect(center = (350,320))
    score_surf = test_font.render(f'Max Score:{score}',False,(154, 168, 50))
    score_rect = score_surf.get_rect(center = (350,320))
    if score == 0: screen.blit(instruction,instruction_rect)
    else: screen.blit(score_surf,score_rect)
    screen.blit(title,title_rect)
    
      
           

  pygame.display.update()# anything drawn is updated to the screen
  clock.tick(60) # while loop should not run more than 60 times per second