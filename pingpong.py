from pygame import *

win = display.set_mode((1200, 563))
display.set_caption('ping-pong')
biha = transform.scale(image.load('fon.jpg'), (1200, 563))

speed_x = 7
speed_y = 7

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 563 - 150:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 563 - 150:
            self.rect.y += self.speed

racket_1 = Player('racket.png', 45, 200, 170, 150, 10)
racket_2 = Player('racket.png', 970, 200, 170, 150, 10)
ball = Player('ball.png', 550, 250, 60, 60, 20)

font.init()
font = font.SysFont('Arial', 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

game = True
finish = False

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        win.blit(biha, (0,0))
        racket_2.reset()
        racket_2.update_r()
        racket_1.reset()
        racket_1.update_l()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 563 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1
        
        if ball.rect.x < 0:
            finish = True
            win.blit(lose1, (550, 250))
            game = True

        if ball.rect.x > 1200:
            finish = True
            win.blit(lose2, (550, 250))
            game = True

    display.update()
    time.delay(50)