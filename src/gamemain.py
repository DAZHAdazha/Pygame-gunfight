import pygame
import pygame.freetype
import sys
import time

timer = -1
right = 1
left = 0
Yellow = 255, 255, 0
fps = 300
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
size = width, height = 1080, 800
jumpCount = 2
jumpCount2 = 2
stop = 0
stop2 = 0
gameOn = -1
keyUpdown = 0
keyUpdown2 = 0
textColor = 51, 172, 172
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.4)
font = pygame.font.Font("VideoTerminalScreen.ttf", 60)
texts = font.render("Single Player", True, textColor)
text = texts.get_rect()
texts2 = font.render("Multiple Player", True, textColor)
text2 = texts2.get_rect()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Warms")
icon = pygame.image.load("game.png")
pygame.display.set_icon(icon)
bloods = pygame.image.load("血.png")
blood = bloods.get_rect()
swordups = pygame.image.load("swordup.png")
swordup = swordups.get_rect()
sworddowns = pygame.image.load("sworddown.png")
sworddown = sworddowns.get_rect()
swordlefts = pygame.image.load("swordleft.png")
swordleft = swordlefts.get_rect()
swordrights = pygame.image.load("swordright.png")
swordright = swordrights.get_rect()
pistolrights = pygame.image.load("pistolright.png")
pistolright = pistolrights.get_rect()
pistollefts = pygame.image.load("pistolleft.png")
pistolleft = pistollefts.get_rect()
warmsright = pygame.image.load("warmsright.png")
warmsleft = pygame.image.load("warmsleft.png")
warmright = warmsright.get_rect()
warmleft = warmsleft.get_rect()
warmright = warmright.move(100, 100)
warms2right = pygame.image.load("warms2right.png")
warms2left = pygame.image.load("warms2left.png")
warm2right = warms2right.get_rect()
warm2left = warms2left.get_rect()
warm2left = warm2left.move(900, 100)
gameovers = pygame.image.load("gameover.jpg")
gameover = gameovers.get_rect()
fclock = pygame.time.Clock()
block = []
for i in range(5):
    block.append((100 + 200 * i, 300, 100, 20))
    block.append((100 + 200 * i, 500, 100, 20))
'moving blocks'
choiceCoor = (200, 400)
thriangleup = []
thriangledown = []
thriangleleft = []
thriangleright = []
text.center = (540, 400)
text2.center = (540, 600)

class WARMS:
    def __init__(self):
        self.direction = right
        self.alive = True


class Weapons:
    pass


class pis(Weapons):
    def __init__(self, bullets):
        self.bullets = bullets
        self.direction = right
        self.bullet = []
        self.coord = []
        self.hitdirection = []
        self.hitstatus = []
        for i in range(bullets):
            self.bullet.append(0)
            self.coord.append([])
            self.hitdirection.append(0)
            self.hitstatus.append(0)

    def check(self):
        num = ()
        for i in range(self.bullets):
            if self.bullet[i] < 1:  # 1 for left, 2 for right
                num += (i,)
        return num

    def skill(self):
        pass

    def shoot(self, coorx, coory, runs, direction):
        self.hitdirection = direction
        if self.direction == right:
            self.bullet[runs] = 2
            self.coord[runs] = [(coorx + 20, coory + 20, 8, 3)]  # (x,y,length, width)
        else:
            self.bullet[runs] = 1
            self.coord[runs] = [(coorx - 70, coory + 20, 8, 3)]

    def fly(self):
        for i in range(self.bullets):
            if self.bullet[i] == 1:
                temp = list(self.coord[i][0])
                temp[0] -= 2
                self.coord[i][0] = tuple(temp)
                if temp[0] <= 0 or self.hitstatus[i] == 1:
                    self.bullet[i] = 0
                    self.hitstatus[i] = 0
                else:
                    pygame.draw.rect(screen, Yellow, (self.coord[i][0]))
            if self.bullet[i] == 2:
                temp = list(self.coord[i][0])
                temp[0] += 2
                self.coord[i][0] = tuple(temp)
                if temp[0] >= 1080 or self.hitstatus[i] == 1:
                    self.bullet[i] = 0
                    self.hitstatus[i] = 0
                else:
                    pygame.draw.rect(screen, Yellow, (self.coord[i][0]))

    def hit(self, x, y, direction):
        for i in range(self.bullets):
            if self.coord[i]:
                if self.bullet[i]:
                    if self.coord[i][0][0] >= x and self.coord[i][0][0] <= x + 50 and self.coord[i][0][1] >= y and \
                            self.coord[i][0][1] <= y + 50:
                        self.hitstatus[i] = 1
                        return direction
        return -1


class swords(Weapons):
    def __init__(self):
        self.skilltime = 1

    def skill(self):
        pass


sword = swords()
pistol = pis(5)
Warms = WARMS()
Warms2 = WARMS()
Warms.x_velocity = 0
Warms.x_acceleate = 0
Warms.y_velocity = 0
Warms.y_acceleate = 0
Warms.hit_buff = 0
Warms.out = 0
Warms2.x_velocity = 0
Warms2.x_acceleate = 0
Warms2.y_velocity = 0
Warms2.y_acceleate = 0
Warms2.hit_buff = 0
Warms2.out = 0
pygame.mixer.music.load("music4.wav")
while gameOn == -1:
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and choiceCoor[1] > 400:
                choiceCoor = list(choiceCoor)
                choiceCoor[1] = 400
                choiceCoor = tuple(choiceCoor)
            if event.key == pygame.K_DOWN and choiceCoor[1] == 400:
                choiceCoor = list(choiceCoor)
                choiceCoor[1] = 600
                choiceCoor = tuple(choiceCoor)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and choiceCoor[1] == 600:
                gameOn = 1
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (200, choiceCoor[1]), 10)
    screen.blit(texts, text)
    screen.blit(texts2, text2)
    pygame.display.update()
    fclock.tick(fps)
pygame.mixer.music.load("music1.wav")
BLOCK = [pygame.draw.rect(screen, WHITE, block[i]) for i in range(10)]
for i in range(27):
    thriangleup.append(((i * 40, 0), (40 + i * 40, 0), (40 * i + 20, 40)))
    thriangledown.append(((40 * i + 20, 760), (i * 40, 800), (40 + i * 40, 800)))
while gameOn == 1:
    if timer >= 0:
        timer += 1
    if timer == 300:
        timer = -1
    Warms.change = 0
    screen.fill(BLACK)
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    if stop == 1:
        jumpCount = 2
    if stop2 == 1:
        jumpCount2 = 2
    stop = 0
    stop2 = 0
    if Warms2.hit_buff != 0:
        Warms2.x_acceleate = Warms2.hit_buff
        if Warms2.hit_buff > 0:
            Warms2.hit_buff -= 1
        else:
                Warms2.hit_buff += 1
    if Warms.hit_buff != 0:
        Warms.x_acceleate = Warms.hit_buff
        if Warms.hit_buff > 0:
            Warms.hit_buff -= 1
        else:
            Warms.hit_buff += 1
    if Warms.x_acceleate != 0:
        Warms.x_velocity = Warms.x_acceleate + Warms.x_velocity
        Warms.x_acceleate = 0
    if Warms.y_acceleate != 0:
        Warms.y_velocity = Warms.y_acceleate + Warms.y_velocity
        Warms.y_acceleate = 0
    if Warms2.x_acceleate != 0:
        Warms2.x_velocity = Warms2.x_acceleate + Warms2.x_velocity
        Warms2.x_acceleate = 0
    if Warms2.y_acceleate != 0:
        Warms2.y_velocity = Warms2.y_acceleate + Warms2.y_velocity
        Warms2.y_acceleate = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Warms.x_velocity = 1
                if Warms.direction == left:
                    Warms.direction = right
            if event.key == pygame.K_d:
                Warms2.x_velocity = 1
                if Warms2.direction == left:
                    Warms2.direction = right
            if event.key == pygame.K_LEFT:
                Warms.x_velocity = -1
                if Warms.direction == right:
                    Warms.direction = left
            if event.key == pygame.K_a:
                Warms2.x_velocity = -1
                if Warms2.direction == right:
                    Warms2.direction = left
            if event.key == pygame.K_UP and jumpCount > 0 and keyUpdown == 0:
                keyUpdown = 1
                Warms.y_velocity = -4
                if jumpCount > 0:
                    jumpCount -= 1
            if event.key == pygame.K_w and jumpCount2 > 0 and keyUpdown2 == 0:
                keyUpdown2 = 1
                Warms2.y_velocity = -4
                if jumpCount2 > 0:
                    jumpCount2 -= 1
            if event.key == pygame.K_DOWN:
                Warms.y_velocity = 1
            if event.key == pygame.K_s:
                Warms2.y_velocity = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Warms.x_velocity = 0
            if event.key == pygame.K_d:
                Warms2.x_velocity = 0
            if event.key == pygame.K_LEFT:
                Warms.x_velocity = 0
            if event.key == pygame.K_a:
                Warms2.x_velocity = 0
            if event.key == pygame.K_UP:
                keyUpdown = 0
                Warms.y_velocity = 0
            if event.key == pygame.K_w:
                keyUpdown2 = 0
                Warms2.y_velocity = 0
            if event.key == pygame.K_DOWN:
                Warms.y_velocity = 0
            if event.key == pygame.K_s:
                Warms2.y_velocity = 0
            if event.key == pygame.K_g:
                if timer == -1:
                    if Warms2.direction == right:  # change!!!
                        if warmright.left + 25 >= warm2left.right and warmright.left + 25 <= warm2left.right + 200 and \
                                warm2left.top + 15 <= warmright.top + 25 and warm2left.top + 40 >= warmright.top + 25:
                            Warms.hit_buff = 2
                            warmright = warmright.move(80, 0)
                        warm2lef = warm2left.move(40, 0)
                        Warms2.hit_buff = 2
                    else:
                        if warmright.left + 25 >= warm2left.left - 200 and warmright.left + 25 <= warm2left.right and \
                                warm2left.top + 15 <= warmright.top + 25 and warm2left.top + 40 >= warmright.top + 25:
                            Warms.hit_buff = -2
                            warmright = warmright.move(-80, 0)
                        warm2lef = warm2left.move(- 40, 0)
                        Warms2.hit_buff = -2
                    timer = 0
            if event.key == pygame.K_l:
                pistol.direction = Warms.direction
                if pistol.check():
                    if pistol.direction == right:
                        warmright = warmright.move(-5, 0)
                    else:
                        warmright = warmright.move(5, 0)
                    pistol.shoot(warmright.right, warmright.top, pistol.check()[0], Warms.direction)
    if Warms.x_velocity > 0:
        warmright = warmright.move(Warms.x_velocity, 0)
    if Warms.x_velocity < 0:
        warmright = warmright.move(Warms.x_velocity, 0)
    if Warms.y_velocity > 0 and warmright.bottom <= 800:
        warmright = warmright.move(0, Warms.y_velocity)
    if Warms.y_velocity < 0 and warmright.top >= 0:
        warmright = warmright.move(0, Warms.y_velocity)
    if Warms2.x_velocity > 0:
        warm2left = warm2left.move(Warms2.x_velocity, 0)
    if Warms2.x_velocity < 0:
        warm2left = warm2left .move(Warms2.x_velocity, 0)
    if Warms2.y_velocity > 0 and warm2left.bottom <= 800:
        warm2left = warm2left.move(0, Warms2.y_velocity)
    if Warms2.y_velocity and warm2left.top >= 0:
        warm2left = warm2left.move(0, Warms2.y_velocity)
    for a in BLOCK:
        if (warmright.left + warmright.right) / 2 >= a.left \
            and (warmright.left + warmright.right) / 2 <= a.right and \
                warmright.bottom == a.top:
            stop = 1
        if (warm2left.left + warm2left.right) / 2 >= a.left and (
                warm2left.left + warm2left.right) / 2 <= a.right and warm2left.bottom == a.top:
            stop2 = 1
    if stop == 0:
        warmright = warmright.move(0, 1)
    if stop2 == 0:
        warm2left = warm2left.move(0, 1)
    for i in range(10):
        pygame.draw.rect(screen, WHITE, block[i])
    for i in range(27):
        pygame.draw.polygon(screen, RED, thriangleup[i])
        pygame.draw.polygon(screen, RED, thriangledown[i])
    pistol.fly()
    hitstatu = pistol.hit(warm2left.left, warm2left.top, pistol.hitdirection)
    if hitstatu == right:
        warm2left = warm2left.move(50, 0)
        Warms2.hit_buff = 2
    if hitstatu == left:
        warm2left = warm2left.move(-50, 0)
        Warms2.hit_buff = -2
    if (warmright.left < 0) or (warmright.right > 1080):
        if Warms.out == 0:
            Warms.out = 1
            now = int(time.time()*1000)
    else:
        Warms.out = 0
        now = 0
    if (warm2left.left < 0) or (warm2left.right > 1080):
        if Warms2.out == 0:
            Warms2.out = 1
            now2 = int(time.time()*1000)
    else:
        Warms2.out = 0
        now2 = 0

    warmleft.top = warmright.top
    warmleft.left = warmright.left
    warm2right.top = warm2left.top
    warm2right.left = warm2left.left
    if Warms2.direction == right:
        screen.blit(warms2right, warm2right)
        swordright.top = warm2left.top - 15
        swordright.left = warm2left.left + 25
        screen.blit(swordrights, swordright)
    else:
        screen.blit(warms2left, warm2left)
        swordleft.top = warm2left.top - 13
        swordleft.left = warm2left.left - 75
        screen.blit(swordlefts, swordleft)
    if Warms.direction == right:
        screen.blit(warmsright, warmright)
        pistolright.top = warmright.top + 10
        pistolright.left = warmright.right - 17
        screen.blit(pistolrights, pistolright)
    else:
        screen.blit(warmsleft, warmleft)
        pistolleft.top = warmright.top + 10
        pistolleft.left = warmright.left - 23
        screen.blit(pistollefts, pistolleft)
    if (warmright.top <= 40 or warmright.bottom >= 760):
        Warms.alive = 0
        blood.move_ip(warmright.left, warmright.top + 48)
    if (warm2left.top <= 40 or warm2left.bottom >= 760):
        Warms2.alive = 0
        blood.move_ip(warm2left.left, warm2left.top + 48)
    if Warms.alive == 0 or Warms2.alive == 0:
        pygame.mixer.music.load("music3.wav")
        pygame.mixer.music.play()
        gameOn = 0
        screen.blit(bloods, blood)
        pygame.display.update()
        gameover.move_ip(250, 160)
        screen.blit(gameovers, gameover)

    present = int(time.time()*1000)
    if now != 0:
        if (2000 - present + now) < 0:
            Warms.alive = 0
            time_texts = font.render( '0ms', True, textColor)
        else:
            time_texts = font.render(str((2000 - present + now)) + 'ms', True, textColor)
        time_text = time_texts.get_rect()
        time_text.center = (100, 80)
        screen.blit(time_texts, time_text)

    present2 = int(time.time() * 1000)
    if now2 != 0:
        if (2000 - present2 + now2) < 0:
            Warms2.alive = 0
            time_texts2 = font.render('0ms', True, textColor)
        else:
            time_texts2 = font.render(str((2000 - present2 + now2)) + 'ms', True, textColor)
        time_text2 = time_texts2.get_rect()
        time_text2.center = (980, 80)
        screen.blit(time_texts2, time_text2)


    pygame.display.update()
    fclock.tick(fps)
time.sleep(2)
screen.fill(BLACK)
texts3 = font.render("YOU WIN!", True, textColor)
text3 = texts3.get_rect()
text3.center = (580, 200)
screen.blit(texts3, text3)
if Warms2.alive == 0:
    warmwins = pygame.image.load("warmwin.png")
    warmwin = warmwins.get_rect()
    warmwin.move(540, 300)
    screen.blit(warmwins, warmwin)
else:
    warm2wins = pygame.image.load("warm2win.png")
    warm2win = warm2wins.get_rect()
    warm2win.move(540, 300)
    screen.blit(warm2wins, warm2win)
pygame.display.update()
time.sleep(3)
