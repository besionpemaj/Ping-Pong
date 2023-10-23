from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        self.size_x=size_x
        self.size_y=size_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y < 495:
            self.rect.y += self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.y < 495:
            self.rect.y += self.speed
        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Ping Pong")
background=transform.scale(image.load("background.jpg"),(win_width,win_height))
racket1=Player("racket.png",30,200,50,150,5)
racket2=Player("racket.png",620,200,50,150,5)
ball=Player("tenis_ball.png",300,300,50,50,5)
game=True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
