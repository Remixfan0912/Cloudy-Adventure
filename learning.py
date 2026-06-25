import pygame
import os

pygame.init()

running = True
fps = 60

WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WIDTH = 500
HEIGHT = 600


#* 管理時間
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("第一個遊戲")

#* 載入圖片
player_img = pygame.image.load(os.path.join("img", "player.jpg")).convert()
poop_img = pygame.image.load(os.path.join("img", "poop.png")).convert()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #* 設定image，以transform將圖片修至正常大小
        self.image = pygame.transform.scale(player_img, (player_img.get_size()[0]/5, player_img.get_size()[1]/5))
        #* 設置color_key，讓該顏色溶於背景
        self.image.set_colorkey(WHITE)
        #* 填滿image
        # self.image.fill(GREEN)
        #* rect : 框出image、定位rect的(x,y)在遊戲視窗
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed = 3
        self.radius = (self.rect.centery - self.rect.y) - 5
        # local_center = (self.rect.width // 2, self.rect.height // 2)
        # pygame.draw.circle(self.image, GREEN, local_center, self.radius)
    
    def update(self):
        #* 偵測鍵盤上的按鍵是否被按下 : Tuple的[bool]，以鍵盤編號作為index
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed
    
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Obj(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #* 設定image，以transform將圖片修至正常大小
        self.image = pygame.transform.scale(poop_img, (poop_img.get_size()[0]/3, poop_img.get_size()[1]/3))
        self.image.set_colorkey(WHITE)
        #* 填滿image
        # self.image.fill(BLACK)
        #* rect : 框出image、定位rect的(x,y)在遊戲視窗
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT-50)
         # 將 self.rect.center 改成圖片內部的中心點
        self.radius = self.rect.height / 7
        # local_center = (self.rect.width // 2, self.rect.height // 2)
        # pygame.draw.circle(self.image, GREEN, local_center, self.radius)

all_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
obj_sprite = pygame.sprite.Group()

player1 = Player()
obj1 = Obj()
player_sprite.add(player1)
obj_sprite.add(obj1)

all_sprite.add(player1)
all_sprite.add(obj1)

while running:
    #! clock.tick限定電腦在一秒內能執行"幾次"迴圈
    clock.tick(fps)
    
    #* 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #* 事件更新
    #! 會去執行所有sprite的update函式
    all_sprite.update()
    hits = pygame.sprite.spritecollide(player1, obj_sprite, True, pygame.sprite.collide_circle)
    # if hits:
    #     running = False
    
    #* 畫面渲染
    screen.fill(BLACK)
    #! 畫出所有sprite在screen上
    all_sprite.draw(screen)

    
    #* 畫面更新
    pygame.display.update()
    
    
pygame.quit()