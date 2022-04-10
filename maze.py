from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <=500:
            self.direction = 'right'
        if self.rect.x >= 600:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))    

#сцена
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#персонажи
player = Player("hero.png", 5, win_height - 80, 5)
monster = Enemy("cyborg.png", win_width - 80, 280, 2)
final = GameSprite("treasure.png", win_width - 120, win_height - 80, 0)

w1 = Wall(61, 61, 61, 90, 90, 20, 420)
w2 = Wall(61, 61, 61, 230, 0, 21, 100)
w3 = Wall(61, 61, 61, 200, 80, 50, 20)
w4 = Wall(61, 61, 61, 200, 100, 20, 120)
w5 = Wall(61, 61, 61, 200, 215, 125, 20)
w6 = Wall(61, 61, 61, 305, 235, 20, 75)
w7 = Wall(61, 61, 61, 195, 300, 130, 20)
w8 = Wall(61, 61, 61, 195, 320, 20, 90)
w9 = Wall(61, 61, 61, 195, 410, 135, 20)
w10 = Wall(61, 61, 61, 470, 80, 20, 420)
w11= Wall(61, 61, 61, 390, 80, 100, 20)
w12 = Wall(61, 61, 61, 220, 140, 60, 20)
w13 = Wall(61, 61, 61, 420, 440, 60, 20)
w14 = Wall(61, 61, 61, 420, 230, 50, 20)
w15 = Wall(61, 61, 61, 410, 150, 70, 20)

finish = False
game = True
clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font = font.SysFont('Arial', 36)
win = font.render('YOU WIN', True, (255, 215, 0))
win = font.render('YOU LOSE', True, (255, 0, 0))
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))

        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w14) or sprite.collide_rect(player, w15):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()   

    clock.tick(FPS) 
    display.update()       
