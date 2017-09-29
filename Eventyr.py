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
    windowheight = 600 #declaires window height
    windowtitle = "Eventyr" #declaires window's name
    pygame.display.set_caption(windowtitle) #sets the title to the window
    window = pygame.display.set_mode ((windowwidth,windowheight), pygame.HWSURFACE|pygame.DOUBLEBUF)#sets the actual window

#implements fps
def fpscounter():
    global currentsecond, currentframe, FPS #sets variables

    if currentsecond == time.strftime("%S"): #gets the current time
        currentframe += 1
    else:
        FPS = currentframe
        currentframe = 0
        currentsecond = time.time.strftime("%S")

create_window()#actually creates window

on = True #creates a variable that runs as long as the program is running

#how it knows when to turn off
while on: #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    #Graphics
    window.fill((0, 0, 0)) #sets background to black



    pygame.display.update() #continually updates window

pygame.quit #ends pygame
sys.exit #ends program