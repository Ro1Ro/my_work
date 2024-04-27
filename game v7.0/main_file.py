#import the module
import pygame
from tkinter import *
pygame.init()
import nps_move

#open window
screen = pygame.display.set_mode((900, 500))
#setting caption
pygame.display.set_caption("No name, I will rename later")
#more
in_home = 0

#delay setting
clock = pygame.time.Clock()

#setting coordinates
x = 70
y = 408

x_nps = 0
y_nps = 0
place_nps = 0

#and speed
speed = 15

#import image
npsWalkRight = [pygame.image.load('nps0.png'),
                pygame.image.load('nps1.png')]

npsStay = [pygame.image.load('nps2.png')]

npsWalkLeft = [pygame.image.load('nps3.png'),
               pygame.image.load('nps4.png')]

walkRight = [pygame.image.load('1.png'),
             pygame.image.load('2.png'),
             pygame.image.load('3.png'),
             pygame.image.load('4.png'),
             pygame.image.load('5.png'),
             pygame.image.load('6.png')]

walkLeft = [pygame.image.load('7.png'),
            pygame.image.load('8.png'),
            pygame.image.load('9.png'),
            pygame.image.load('10.png'),
            pygame.image.load('11.png'),
            pygame.image.load('12.png')]

playerStand = [pygame.image.load('0.png'),
               pygame.image.load('0.png')]

bg = [pygame.image.load('bg.png'),
      pygame.image.load('bg1.png'),
      pygame.image.load('bg2.png'),
      pygame.image.load('bg3.png')]
bg_1 = [pygame.image.load('bg2_1.png')]
book = pygame.image.load('book.png')
flower = pygame.image.load('flower.png')

#text
text = "Вы получили книгу"
text1 = "Вы получили цветок"
text2 = "Нажмите K для перехода на следующую локацию"
f = pygame.font.Font('19151.ttf', 30)

textForBook = f.render(text, 1, (47, 111, 157))
textForFlower = f.render(text1, 1, (47, 111, 157))
textForMess = f.render(text2, 1, (47, 111, 157))

#for move
frame_num = 0
lastMove = 0
animCount = 0

#for inventory
numberOfBooks = 0
numberOfFlowers = 0

#where
coord = [(50, y+8), (100, y+8), (250, y+8), (400, y+8)]
whereIsTheBook = [1, 0, 0, 0]
whereIsFlower = [1, 1, 1, 1]
#open inventory with 'l' and close on a cross
def importance_mess():
    if (x <= 10 or x >= 860) and frame_num != 88:
        pygame.draw.rect(screen, (0, 29, 42), (5, 10, 700, 50))
        pygame.draw.rect(screen, (255, 215, 0), (5, 10, 700, 50), 5)
        screen.blit(textForMess, (20, 20))
        pygame.display.update()
        pygame.time.wait(500)
    elif 549 <= x <= 550 and frame_num != 88 and frame_num == 2:
        pygame.draw.rect(screen, (0, 29, 42), (5, 10, 700, 50))
        pygame.draw.rect(screen, (255, 215, 0), (5, 10, 700, 50), 5)
        screen.blit(textForMess, (20, 20))
        pygame.display.update()
        pygame.time.wait(500)
    elif frame_num == 88 and x <= 10:
        pygame.draw.rect(screen, (0, 29, 42), (5, 10, 700, 50))
        pygame.draw.rect(screen, (255, 215, 0), (5, 10, 700, 50), 5)
        screen.blit(textForMess, (20, 20))
        pygame.display.update()
        pygame.time.wait(500)
def chainge_background():
    global x, frame_num, in_home
    if x >= 840 and x <= 870 and in_home != 1:
        x = 9
        if frame_num + 1 != len(bg):
            frame_num += 1
        else:
            frame_num = 0
    elif 8 <= x <= 11 and in_home != 1:
        x = 860
        if frame_num - 1 != -1:
            frame_num -= 1
        else:
            frame_num = len(bg) - 1
    elif 549 <= x <= 579 and frame_num == 2:
        in_home = 1
        frame_num = 88
        x = 9
        screen.blit(bg_1[0], (0, 0))
    elif 8 <= x <= 15 and frame_num == 88:
        in_home = 0
        x = 549
        frame_num = 2
    pygame.time.wait(90)
def inventory():
    global root, numberOfBooks, numberOfFlowers
    def booky():
        global root
        root.destroy()
        root = Tk()
        root.title('Book')
        root.geometry('250x200+200+100')
        left = Button(root, text = '<==')
        right = Button(root, text = '==>')
        menu = Button(root, text = 'menu')
        left.place(relx = 0.25, rely = 0.75)
        menu.place(relx = 0.41, rely = 0.75)
        right.place(relx = 0.60, rely = 0.75)
        root.mainloop()
    def menu():
        global root
        root.destroy()
        root = Tk()
        root.title('Menu')
        root.geometry('250x200+200+100')
        m = Button(root, text = '         Exit          ', command = des)
        i = Button(root, text = '     Inventory   ', command = inventory)
        c = Button(root, text = '         Craft       ', command = craft)
        s = Button(root, text = '        Shop        ', command = shop)
        i.place(relx = 0.33, rely = 0.05)
        c.place(relx = 0.33, rely = 0.3)
        s.place(relx = 0.33, rely = 0.55)
        m.place(relx = 0.33, rely = 0.8)
        root.mainloop()
    def inventory():
        global root
        root.destroy()
        root = Tk()
        root.geometry('250x200+200+100')
        root.title('Inventory')
        book_t = Button(root, text = f'    Books: {numberOfBooks}  ', command = booky)
        flower_t = Button(root, text = f'   Flowers: {numberOfFlowers}')
        m = Button(root, text = '     Menu     ', command = menu)
        book_t.place(relx = 0.35, rely = 0.05)
        flower_t.place(relx = 0.35, rely = 0.25)
        m.place(relx = 0.35, rely = 0.45)
        root.mainloop()
    def craft():
        global root
        root.destroy()
        root = Tk()

        f_top = Frame(root)
        f_bot = Frame(root)
        f_3 = Frame(root)
        f_top.pack()
        f_bot.pack()
        f_3.pack()
        def sel():
            selection = "You selected the option " + var.get() + " and this " + li.get()
            label.config(text = selection)
        var = StringVar()
        var.set('None')
        li = StringVar()
        li.set('None')
        R1 = Radiobutton(f_top, text = 'option 1', variable = var, value = 'soup', command = sel)
        R1.pack(side = LEFT)
        R2 = Radiobutton(f_bot, text = 'option 2', variable = var, value = 'pour', command = sel)
        R2.pack(side = LEFT)
        R3 = Radiobutton(f_3, text = 'option 3', variable = var, value = 'fork', command = sel)
        R3.pack(side = LEFT)
        R1_1 = Radiobutton(f_top, text = 'option 1_1', variable = li, value = 'no soup', command = sel)
        R1_1.pack(side = LEFT)
        R2_1 = Radiobutton(f_bot, text = 'option 2_1', variable = li, value = 'no pour', command = sel)
        R2_1.pack(side = LEFT)
        R3_1 = Radiobutton(f_3, text = 'option 3_1', variable = li, value = 'no fork', command = sel)
        R3_1.pack(side = LEFT)
        
        label = Label(root)
        label.pack()
        
        root.geometry('250x200+200+100')
        root.title('Craft')
        m = Button(root, text = 'Menu', command = menu)
        m.pack()
        root.mainloop()
    def shop():
        global root
        root.destroy()
        root = Tk()
        root.geometry('250x200+200+100')
        root.title('Shop')
        m = Button(root, text = 'Menu', command = menu)
        m.pack()
        root.mainloop()
    def des():
        global root
        root.destroy()
    root = Tk()
    root.geometry('250x200+200+100')
    m = Button(root, text = '         Exit          ', command = des)
    i = Button(root, text = '     Inventory   ', command = inventory)
    c = Button(root, text = '         Craft       ', command = craft)
    s = Button(root, text = '        Shop        ', command = shop)
    i.place(relx = 0.33, rely = 0.05)
    c.place(relx = 0.33, rely = 0.3)
    s.place(relx = 0.33, rely = 0.55)
    m.place(relx = 0.33, rely = 0.8)
    root.mainloop()

#function for animatoin
def drawWindow():
    global animCount, lastMove
    
    #backgound setting
    if frame_num != 88:
        screen.blit(bg[frame_num], (0, 0))
    else:
        screen.blit(bg_1[0], (0, 0))
    if frame_num != 88 and whereIsTheBook[frame_num]:
    	screen.blit(book, (475, y+8))
    if frame_num != 88 and whereIsFlower[frame_num]:
        screen.blit(flower, coord[frame_num])

    #animation
    if animCount + 1 >= 25:
        animCount = 0
    
    if left:
        #delivery by 3 for the delay of animation
        screen.blit(walkLeft[int(animCount//5)], (x, y))
        animCount += 1
        lastMove = 1
        
    #it's too
    elif right:
        screen.blit(walkRight[int(animCount//5)], (x, y))
        animCount += 1
        lastMove = 0
        
    else:
        screen.blit(playerStand[lastMove], (x, y))
        
    pygame.display.update()

#change the background
def stop_go():
    global x, frame_num
    if x > 860:
        x = 860
    elif x < 10:
        x = 10

run = True
while run:
    clock.tick(30)
    
    #security quit
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            run = False

    #which buttons are pressed 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
        left = False
        right = True
        stop_go()
        importance_mess()
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
        left = True
        right = False
        stop_go()
        importance_mess()
    else:
        left = False
        right = False
        animCount = 0
    if keys[pygame.K_k]:
        chainge_background()

    #open inventory
    if keys[pygame.K_l]:
        inventory()

    #collect object
    if frame_num != 88 and keys[pygame.K_SPACE] and 420 < x < 500 and whereIsTheBook[frame_num] != 0:
        whereIsTheBook[frame_num] = 0
        numberOfBooks += 1
        pygame.draw.rect(screen, (0, 29, 42), (5, 10, 300, 50))
        pygame.draw.rect(screen, (255, 215, 0), (5, 10, 300, 50), 5)
        screen.blit(textForBook, (20, 20))
        pygame.display.update()
        pygame.time.wait(900)
    elif frame_num != 88 and keys[pygame.K_SPACE] and coord[frame_num][0] - 30 < x < coord[frame_num][0] + 30 and whereIsFlower[frame_num] != 0:
        whereIsFlower[frame_num] = 0
        numberOfFlowers += 1
        pygame.draw.rect(screen, (0, 29, 42), (5, 10, 300, 50))
        pygame.draw.rect(screen, (255, 215, 0), (5, 10, 300, 50), 5)
        screen.blit(textForFlower, (20, 20))
        pygame.display.update()
        pygame.time.wait(900)

    drawWindow()
    
pygame.quit()
