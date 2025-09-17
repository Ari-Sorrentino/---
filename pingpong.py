from pygame import *

main_win = display.set_mode((500, 500))
display.set_caption("ping-pong")

background = transform.scale(image.load("background.png"), (500, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def draw(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

game = True
finish = False
clock = time.Clock()

ball = GameSprite("heaviest_thing_ever.png", 200, 200, 3, 50, 50)
racket_l = Player("wooden_bat_l.png", 30, 200, 4, 150, 150)
racket_r = Player("wooden_bat_r.png", 420, 200, 4, 150, 150)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        main_win.blit(background, (0, 0))

        racket_l.update_l()
        racket_r.update_r()

        racket_l.draw()
        racket_r.draw()
        ball.draw()

    display.update()
    clock.tick(60)