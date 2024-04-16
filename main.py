import pygame
import button
import random

pygame.init()

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Falling Blocks")


#frame rate
clock = pygame.time.Clock()
FPS = 60

#colours
colors = [(58,123,170), (125,143,174), (161,180,193), (240,185,185), (255,255,255), (255,209,89), (0,0,0)]

#create class for squares
class Square(pygame.sprite.Sprite):
  def __init__(self, col, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50, 50))
    self.image.fill(col)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.vel = 5
    self.cleared = False

  def update(self,squares,Button):
    self.rect.move_ip(0, self.vel)
    #check if sprite has been cleared
    if self.cleared:
      self.vel = 10
      if self.rect.top > SCREEN_HEIGHT:
        self.kill()

    #check if sprite has collided

    elif len(pygame.sprite.spritecollide(self,squares,False)) >= 2: 
        self.vel = 0

    elif self.rect.bottom > SCREEN_HEIGHT:
      self.vel = 0

    #check if sprite is in the button
    if pygame.Rect.colliderect(self.rect, Button):
      self.kill()
    


def main():

  #Clear Button Image
  clearImage = pygame.image.load("Assets/Button.png").convert()

  #create sprite group for squares
  squares = pygame.sprite.Group()
  

  clear = button.Button(SCREEN_WIDTH-clearImage.get_width()-10,10,clearImage,1)
  

  #game loop
  run = True
  while run:

    clock.tick(FPS)

    #update background
    screen.fill((1,32,54))

    #update sprite group
    squares.update(squares, clear.rect)

    #draw sprite group
    squares.draw(screen)

    
    if clear.draw(screen):
      for x in squares:
        x.cleared = True

    #print(squares)




    #event handler
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        #get mouse coordinates
        pos = pygame.mouse.get_pos()
        #create square
        square = Square(random.choice(colors), pos[0], pos[1])
        squares.add(square)
      #quit program
      if event.type == pygame.QUIT:
        run = False

    #update display

    pygame.display.flip()

  pygame.quit()


if __name__ == "__main__":
  main()