background_image_filename = 'background.png'
mouse_image_filename = 'hero.jpg'
bullet_image_filename = 'bullet.png'
enemy_image_filename = 'enemy.jpg'
#指定图像文件名称
 
import pygame #导入pygame库
from sys import exit #向sys模块借一个exit函数用来退出程序
from random import randint #引入随机数

#定义一个Bullet类，封装子弹的数据和方法
class Bullet(object):
    def __init__(self):
        self.x = 0
        self.y = -100
        self.speed = 600
        self.image = pygame.image.load(bullet_image_filename).convert_alpha()
        self.active = False

    def move(self, passed_time_second):
        if self.y < 0:
            self.active = False
        else:
            self.y -= self.speed*passed_time_second

    def restart(self):
        self.active = True
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width()/2
        self.y = mouseY - self.image.get_width()/2

class Enemy(object):#定义一个Enemy类，封装敌机的数据和方法
    def restart(self):
        self.x = randint(-30,400)
        self.y = randint(-100, -50)
        self.speed = randint(100,400)
        self.active = True
    def __init__(self):
        self.restart()
        self.active = False
        self.image = pygame.image.load(enemy_image_filename).convert_alpha()

    def move(self, passed_time_second):
        if self.y < 650:
            self.y += self.speed*passed_time_second
        else:
            self.active = False
   
pygame.init() #初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((480, 650), 0, 32)
#创建了一个窗口
pygame.display.set_caption("PlaneFight!")
#设置窗口标题
pygame.mouse.set_visible(False)
 
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像
bullet = []
for i in range(6):#子弹总数量
    bullet.append(Bullet())
interval_bullet = 25 #发射子弹的帧数间隔
index_bullet = 0 #初始化子弹坐标
enemy = []
for i in range(10):#敌机总数量
    enemy.append(Enemy())
interval_enemy = 100 #敌机出现的间隔
index_enemy = 0 #初始化敌机坐标
clock = pygame.time.Clock()
while True:
#游戏主循环
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()
    time_passed = clock.tick(100)
    time_passed_second = time_passed/1000.0
    screen.blit(background, (0,0))
    #将背景图画上去
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置

    interval_bullet -= 1
    if interval_bullet <= 0:
        interval_bullet = 25
        bullet[index_bullet].restart()#重置子弹
        index_bullet = (index_bullet + 1) % 6 #循环递增
    def checkHit(enemy,bullet):
        if enemy.x < bullet.x < enemy.x + enemy.image.get_width() \
           and enemy.y < bullet.y < enemy.y + enemy.image.get_height():
            enemy.active = False
            bullet.active = False
            return True
        else:
            return False
    
    for b in bullet:
        if b.active:
            b.move(time_passed_second)#移动子弹
            for e in enemy:
                if e.active:
                    checkHit(e,b)
            screen.blit(b.image, (b.x, b.y))#显示子弹

    interval_enemy -= 1
    if interval_enemy <= 0:
        interval_enemy = randint(30,100)
        enemy[index_enemy].restart() #重置飞机
        index_enemy = (index_enemy + 1) % 10 #循环递增
    for e in enemy:
        if e.active:
            e.move(time_passed_second) #移动敌机
            screen.blit(e.image, (e.x, e.y)) #显示敌机
        
    
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
 
    #screen.blit(bullet.image, (bullet.x, bullet.y))
    screen.blit(mouse_cursor, (x, y))
    #把各个元素画上去
 
    pygame.display.update()
    #刷新一下画面
