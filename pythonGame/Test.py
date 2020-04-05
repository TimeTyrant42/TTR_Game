import pygame, sys, random

pygame.init()

## Functions and classes

## Variables

clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(pygame.display.list_modes()[-1])

radius = 50
whiteTrainImg = pygame.image.load('Ticket To Ride Assets\White\TrainCard_White.png')
blackTrainImg = pygame.image.load('Ticket To Ride Assets\Black\TrainCard_Black.png')

# create the surface that will contain the circle image.
# circle will be drawn on its center, so surface width and height is 2*radius
surface1 = pygame.Surface((2*radius, 2*radius))
surface2 = pygame.Surface((2*radius, 2*radius))
# Let's also paint the surface GREEN so you see its corners behind the circle

# draw the circle on the surface instead of screen

# Last but not the least, create a companion rect, based on surface's size
# A rect is just a tool to define width, height and position at the same time
rect1 = surface1.get_rect()
rect2 = surface1.get_rect()

# rect now has same width and height as the surface,
# It's positioned at (0, 0) so let's move it to desired initial position

rect1.x = 0  # instead of SCRENRECT.centerx, so it stays longer on screen
rect1.y = SCREEN.get_rect().centery
rect2.x = 0  # instead of SCRENRECT.centerx, so it stays longer on screen
rect2.y = SCREEN.get_rect().centery -300
# The surface (and our friend the rect) is set up and ready to be used on screen


## Main loop

running = True

while running:
    #Quit event etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running= False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                running= False

    if rect1.x < 10:
        rect1.x += 1
        rect2.x += 1
      #   print(pygame.time.get_ticks())

    else:

        rect1.x = rect1.x
        while rect2.y < rect1.y:
            if pygame.time.get_ticks() % 514 == 0:
              print(rect2.y)
              rect2.y +=1

    SCREEN.fill((0, 0, 0))

    # and now we blit the pre-drawn circle onto the screen,
    # using rect as coordinates
    SCREEN.blit(whiteTrainImg, rect1)
    SCREEN.blit(blackTrainImg, rect2)

    pygame.display.update()
    clock.tick(3)
