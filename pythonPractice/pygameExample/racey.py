import pygame

pygame.init()
display_width = 800
display_height = 600
black = (0,0,0) #colors made with rgb values
white = (250,255,255)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((display_width,display_height)) #width and height as tuple
pygame.display.set_caption('A bit Racey') #window title
clock = pygame.time.Clock() #tracks specific game clock

carImg = pygame.image.load('racecar.png') #load an image(use gimp transparent)

def car(x,y):
    gameDisplay.blit(carImg, (x,y)) #blit draws img

x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

while not crashed:
    for event in pygame.event.get(): #tracks all events occuring
        if event.type == pygame.QUIT:
            crashed = True
        #print(event)

    gameDisplay.fill(white) #background color
    car(x,y)
    pygame.display.update() #updates display
    clock.tick(60) #frames per second

pygame.quit()
quit()
