import pygame, sys, time, random
pygame.init()

#creates defalt values for FPS counter
currentsecond = 0
currentframe = 0
FPS = 0

#sets up display window
def create_window():
    global window, windowheight, windowtitle, windowwidth #sets variable names for the display size/title
    windowwidth = 800 #declaires window width
    windowheight = 608 #declaires window height
    windowtitle = "Eventyr" #declaires window's name
    pygame.display.set_caption(windowtitle) #sets the title to the window
    window = pygame.display.set_mode ((windowwidth,windowheight), pygame.HWSURFACE|pygame.DOUBLEBUF)#sets the actual window

#counts the fps
def fpscounter():
    global currentsecond, currentframe, FPS #sets variables

    if currentsecond == time.strftime("%S"): #aka if the time in game is equal to the real time in second
        currentframe += 1 #counts the frames in the second
    else: #calculates the fps in that second when the seconds changes
        FPS = currentframe #sets FPS to how many frames were acheived in that second
        currentframe = 0 #resets the variable so that it can count the FPS in the next second
        currentsecond = time.strftime("%S")

create_window()#actually creates the  window

on = True #creates a variable that runs as long as the program is running

#how it knows when to turn off
while on: #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

#Render Colors
class Color:
    Black = (0, 0, 0)
    Grey1 = (107, 107, 107)
    Grey2 = (145, 145, 145)
    Grey3 = (164, 164, 164)
    Grey4 = (183, 183, 183)
    Grey5 = (195, 195, 195)
    Grey6 = (218, 218, 218)
    White = (255, 255, 255)

    Brown = (149, 96, 17)
    LightBrown = (206, 133, 43)
    Pale = (239, 191, 127)

    Pink1 = (254, 158, 204)

    Red1 = (175, 1, 36)

    Orange1 = (248, 146, 33)

    Yellow1 = (255, 242, 0)
    DarkSand = (249, 251, 155)
    LightSand = (252, 254, 180)

    Green1 = (64, 64, 0)
    Green2 = (78, 185, 66)
    Green3 = (164, 210, 23)
    Green4 = (163, 233, 84)
    Green5 = (196, 236, 74)

    Blue1 = (0, 36, 72)
    Blue2 = (66, 139, 174)
    Blue3 = (104, 167, 198)
    Blue4 = (136, 186, 210)
    Blue5 = (89, 172, 255)
    Blue6= (224, 237, 243)

    Purple1 = (91, 40, 91)
    Purple2 = (177, 84, 177)
    Purple3 = (188, 179, 225)

#Graphics
window.fill(Color.Black) #sets background to black

pygame.display.update() #continually updates window

pygame.quit #ends pygame
sys.exit #ends program
