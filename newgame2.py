import pygame,sys,time,random
from pygame.locals import *
pygame.init()

mainClock=pygame.time.Clock()
W=1200
H=600

w=pygame.display.set_mode((W,H),0,32)
pygame.display.set_caption("artitin051")

Fps=100
gameoversound= pygame.mixer.Sound("gameover.wav")
pygame.mixer.music.load("background.mid")



playerimage=pygame.image.load("skier.png")
playerrect=playerimage.get_rect()
treeimge=pygame.image.load("tree.png")


red=(255,0,0)
green =(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
yellow = (255,255,0)
lightgreen=(127,255,0)
textcolor=black

treemax=40
treemin=10
treespeed=5

add_newtree_rate=6
player_move_rate=10

font = pygame.font.SysFont(None,48)

def terminate():
    pygame.quit()
    sys.exit()

def waitforplayertopresskey():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    terminate()   
                return
            
def plyerhittree(playerrect,trees):
    for t in trees:
        if playerrect.colliderect(t["rect"]):
            return True
        return False

def drawtext(text,font,surface,x,y):
    text1=font.render(text,2,textcolor)
    textrect=text1.get_rect()
    textrect.topleft=(x,y)
    surface.blit(text1, textrect)
    
w.fill(white)
drawtext('artitn051',font,w,W/3,H/3)
drawtext("PRESS ANY KEYS",font,w,W/4,H/4)
pygame.display.update()
waitforplayertopresskey()

topscore=0
while True:
    tree=[]
    scor=0
    playerrect.topleft=(W/2,H-50)
    moveup=moveleft=movedown=moveright=False
    reverscheat=slowcheat= False
    tree_add_c=0
    pygame.mixer.music.play(-1,0.0)
    while True:
        scor+=1
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    moveright=False
                    moveleft=True
                if event.key==K_RIGHT:
                    moveright=True
                    moveleft=False
                if event.key==K_UP:
                    moveup=True
                    movedown=False
                if event.key==K_DOWN:
                    moveup=False
                    movedown=True
            if event.type==KEYUP:
                if event.key==K_LEFT:
                    moveleft= False
                if event.key==K_RIGHT:
                    moveright=False
                if event.key==K_UP:
                    moveup = False
                if event.key==K_DOWN:
                    movedown=False
        tree_add_c+=1
        if tree_add_c == add_newtree_rate:
            tree_add_c =0
            treesize=random.randint(treemin,treemax)
            newtree={
                "rect":pygame.Rect(random.randint(0,W-treesize),0-treesize,treesize,treesize),
                "speed":treespeed,
                "surface":pygame.transform.scale(treeimge,(treesize,treesize)),
                }
            tree.append(newtree)
            
        if moveleft and playerrect.left > 0:
            playerrect.move_ip(-1 * player_move_rate, 0)
            
        if moveright and playerrect.right < W:
            playerrect.move_ip(player_move_rate, 0)

        if moveup and playerrect.top > 0:
            playerrect.move_ip(0,-1*player_move_rate)
            
        if movedown and playerrect.bottom < H:
            playerrect.move_ip(0,  player_move_rate)
    
        
        for t in tree:
            t['rect'].move_ip(0, t['speed'])
        for t in tree[:]:
            if t['rect'].top>H:
                tree.remove(t)
        w.fill(white)
        drawtext('score:%s'%(scor),font,w,50,0)
        drawtext('topscore: %s'%(topscore),font,w,50,60)
        w.blit(playerimage,playerrect)

        for t in tree:
            w.blit(t['surface'],t["rect"])
        pygame.display.update()
        
        if plyerhittree(playerrect,tree):
            if scor>topscore:
                topscor=scor
            break
        mainClock.tick(Fps)
    pygame.mixer.music.stop()
    gameoversound.play()
    drawtext('gameover',font,w,W/3,H/3)
    drawtext('play again',font,w,(W/3)-80,(H/3)+30)
    pygame.display.update()
    waitforplayertopresskey()
    gameoversound.stop()





        


           
