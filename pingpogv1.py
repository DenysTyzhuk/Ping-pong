from pygame import *
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS= 60
game = True
back = (124, 252, 0)
window.fill(back)

class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player1(GameSprite):
   #метод для управления 2м игрком стрелками клавиатуры
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

class Player2(GameSprite):
   #метод для управления 2м игрком стрелками клавиатуры
   def update_r(self):
       keys = key.get_pressed()
       if keys[W] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[W] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

#racket1 = (img_racket, 5, win_height - 100, 80, 100, 10) !!!!!!!!
#racket2 = (img_racket, 5, win_height - 100, 80, 100, 10) !!!!!!!!

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
