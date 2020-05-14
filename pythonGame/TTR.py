from typing import Any
from random import *
import pygame
import math
import sys

import switch as switch

from Background import Background
from Edge import Edge
from City import City
from Card import Card
from Player import Player
from Track import Track

pygame.init()

# sets the window size to 800x600px
display_width = 1920
display_height = 1080

# easy access to colors
black = (0, 0, 0)
grey = (139, 139, 139)
darkGrey = (47, 79, 79)
white = (255, 255, 255)
yellow = (255, 255, 0)
pink = (255, 102, 178)
red = (255, 0, 0)
darkRed = (139, 0, 0)
orange = (255, 128, 0)
green = (0, 255, 0)
darkGreen = (0, 139, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 139)

# makes the screen as wide and tall as above variables, makes a white background, adds TTR title, and starts a clock
screen = pygame.display.set_mode([display_width, display_height], pygame.FULLSCREEN)
pygame.display.set_caption("Ticket To Ride")
clock = pygame.time.Clock()

# loads images to act as the static cards
whiteTrainImg = pygame.image.load('Ticket To Ride Assets\White\TrainCard_White.png')
pinkTrainImg = pygame.image.load('Ticket To Ride Assets\Pink\TrainCard_Pink.png')
redTrainImg = pygame.image.load('Ticket To Ride Assets\Red\TrainCard_Red.png')
orangeTrainImg = pygame.image.load('Ticket To Ride Assets\Orange\TrainCard_Orange.png')
yellowTrainImg = pygame.image.load('Ticket To Ride Assets\Yellow\TrainCard_Yellow.png')
greenTrainImg = pygame.image.load('Ticket To Ride Assets\Green\TrainCard_Green.png')
blueTrainImg = pygame.image.load('Ticket To Ride Assets\Blue\TrainCard_Blue.png')
blackTrainImg = pygame.image.load('Ticket To Ride Assets\Black\TrainCard_Black.png')

# loads images to act as the moving cards
whiteMovingCardImg = pygame.image.load('Ticket To Ride Assets\White\RotatedCard_White.png')
pinkMovingImg = pygame.image.load('Ticket To Ride Assets\Pink\RotatedCard_Pink.png')
redMovingImg = pygame.image.load('Ticket To Ride Assets\Red\RotatedCard_Red.png')
orangeMovingImg = pygame.image.load('Ticket To Ride Assets\Orange\RotatedCard_Orange.png')
yellowMovingImg = pygame.image.load('Ticket To Ride Assets\Yellow\RotatedCard_Yellow.png')
greenMovingImg = pygame.image.load('Ticket To Ride Assets\Green\RotatedCard_Green.png')

# loads images to act as the draw deck
whiteDeckImg = pygame.image.load('Ticket To Ride Assets\White\WhiteDeck.png')
pinkDeckImg = pygame.image.load('Ticket To Ride Assets\Pink\PinkDeck.png')
redDeckImg = pygame.image.load('Ticket To Ride Assets\Red\RedDeck.png')
orangeDeckImg = pygame.image.load('Ticket To Ride Assets\Orange\OrangeDeck.png')
yellowDeckImg = pygame.image.load('Ticket To Ride Assets\Yellow\YellowDeck.png')
greenDeckImg = pygame.image.load('Ticket To Ride Assets\Green\GreenDeck.png')
blueDeckImg = pygame.image.load('Ticket To Ride Assets\Blue\BlueDeck.png')
blackDeckImg = pygame.image.load('Ticket To Ride Assets\Black\BlackDeck.png')

# loads images of the train tracks
blankTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Blank.png')
redTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Red.png')
orangeTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Orange.png')
yellowTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Yellow.png')
greenTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Green.png')
blueTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Blue.png')
pinkTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Pink.png')
whiteTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_White.png')
blackTrack = pygame.image.load('Ticket To Ride Assets\Tracks\Filled\Track_Black.png')

# loads images of the occupied train tracks
redTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_Red.png')
orangeTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_Orange.png')
yellowTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_Yellow.png')
greenTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_Green.png')
blueTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_Blue.png')
pinkTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_Pink.png')
whiteTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_White.png')
blackTrackOcc = pygame.image.load('Ticket To Ride Assets\Tracks\Occupied\Track_Black.png')

human = Player()
bot = Player()

screen.blit(blackTrainImg, (display_width * 0.05, display_height * 0.9))
screen.blit(whiteTrainImg, (display_width * 0.15, display_height * 0.9))

BackGround = Background('Ticket To Ride Assets\BackGrounds\Background.png', [0, 0])
TitleScreenImg = Background('Ticket To Ride Assets\BackGrounds\TitleScreen.png', [0, 0])

##numNodes = input('How many cities?')
'''
cityConnection = ([[-1, Edge(3, 'black'), -1, Edge(5, 'white'), Edge(2,  'black'), -1, -1],
                   [Edge(3, 'black'), -1, Edge(4, 'white'), -1, -1, -1, -1],
                   [-1, Edge(4, 'white'), -1, Edge(6, 'black'), -1, Edge(4, 'black'), -1],
                   [Edge(5, 'white'), -1, Edge(6, 'black'), -1, -1, -1, Edge(3, 'white')],
                   [Edge(2, 'black'), -1, -1, -1, -1, Edge(3, 'white'), Edge(3, 'white')],
                   [-1, -1, Edge(4, 'black'), -1, Edge(3, 'white'), -1, Edge(2, 'black')],
                   [-1, -1, -1, Edge(3, 'white'), Edge(3, 'white'), Edge(2, 'black'), -1]])
'''

cityNames = ['Washington', 'Montana', 'New York', 'Texas', 'Colorado', 'Kansas', 'Oklahoma']


# numNodes = input('How many cities?')
# cityNames = ['Los Angeles', 'Seattle', 'New York', 'Dallas', 'Salt Lake', 'Milwaukee', 'Chicago']
# cities = [City(1, 2, 'Los Angeles', red), City(3, 4, 'Seattle', blue), City(5, 6, 'New York', green),

def quitGame():
    pygame.quit()
    quit()


# Draws the surface where the text will be written
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# makes a button with message,font size,x,y,width,height,inactive and active color and the action
def button(msg, fs, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.Font('freesansbold.ttf', fs)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x + (w / 2), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def strToObj(name):
    return eval(name)


def titleScreen():
    #   print(pygame.font.get_fonts())
    start = True
    screen.fill(white)
    screen.blit(TitleScreenImg.image, TitleScreenImg.rect)

    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
        button("Start Train-ing", 20, display_width * 0.45, display_height * 0.4, 200, 75, green, darkGreen, gameLoop)
        button("Settings", 20, display_width * 0.45, display_height * 0.5, 200, 75, blue, darkBlue, settings)
        button("Quit", 20, display_width * 0.45, display_height * 0.6, 200, 75, red, darkRed, quitGame)

        pygame.display.update()
        clock.tick(60)


colors = ["white", "pink", "red", "orange", "yellow", "green", "blue", "black"]
chosenColors = ["white", "black"]

def settings():
    screen.fill(white)
    screen.blit(BackGround.image, BackGround.rect)
    pygame.draw.rect(screen, grey, (display_width * 0.075, display_height * 0.15, 1550, 200), 0)
    for j in range(0, len(chosenColors), 1):
        pygame.draw.rect(screen, darkBlue, (display_width * (colors.index(chosenColors[j])+1) / 10 - 6, display_height * 0.2 - 6, 110, 110), 11)

    running = True

    global whiteDeck1, pinkDeck1, redDeck1, orangeDeck1, yellowDeck1, greenDeck1, blueDeck1, blackDeck1

    while running:

        whiteDeck1 = pygame.draw.rect(screen, white, (display_width * 0.1, display_height * 0.2, 100, 100), 0)
        pinkDeck1 = pygame.draw.rect(screen, pink, (display_width * 0.2, display_height * 0.2, 100, 100), 0)
        redDeck1 = pygame.draw.rect(screen, red, (display_width * 0.3, display_height * 0.2, 100, 100), 0)
        orangeDeck1 = pygame.draw.rect(screen, orange, (display_width * 0.4, display_height * 0.2, 100, 100), 0)
        yellowDeck1 = pygame.draw.rect(screen, yellow, (display_width * 0.5, display_height * 0.2, 100, 100), 0)
        greenDeck1 = pygame.draw.rect(screen, green, (display_width * 0.6, display_height * 0.2, 100, 100), 0)
        blueDeck1 = pygame.draw.rect(screen, blue, (display_width * 0.7, display_height * 0.2, 100, 100), 0)
        blackDeck1 = pygame.draw.rect(screen, black, (display_width * 0.8, display_height * 0.2, 100, 100), 0)

        button("Play Game", 20, display_width * 0.45, display_height * 0.4, 200, 75, blue, darkBlue, titleScreen)
        button("Quit", 20, display_width * 0.45, display_height * 0.6, 200, 75, red, darkRed, quitGame)

        for event in pygame.event.get():
            for j in range(0, len(chosenColors), 1):
                print(chosenColors[j])
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in range(0, len(colors), 1):
                    colorDeck = switchDeck(colors[i])
                    if strToObj(colorDeck).collidepoint(pos):
                        if chosenColors.__contains__(colors[i]):
                            chosenColors.remove(colors[i])
                            pygame.draw.rect(screen, grey,
                                             (display_width * (i + 1) / 10 - 6, display_height * 0.2 - 6, 110, 110), 11)
                        else:
                            chosenColors.append(colors[i])
                            pygame.draw.rect(screen, darkBlue,
                                             (display_width * (i + 1) / 10 - 6, display_height * 0.2 - 6, 110, 110), 11)

            pygame.display.update()
        clock.tick(60)





def switchDeck(color):
    return {
        'white': lambda: 'whiteDeck1',
        'pink': lambda: 'pinkDeck1',
        'red': lambda: 'redDeck1',
        'orange': lambda: 'orangeDeck1',
        'yellow': lambda: 'yellowDeck1',
        'green': lambda: 'greenDeck1',
        'blue': lambda: 'blueDeck1',
        'black': lambda: 'blackDeck1',
    }.get(color, lambda: None)()


def drawHand(color):
    print('added ' + color + ' card to your hand')
    human.handCards.append(Card(color, randint(1, 10)))
    screen.blit(globals()[color + 'TrainImg'], (display_width * 0.85, display_height * 0.13 + (40 * human.cardIndex)))
    human.cardIndex += 1


def cityNameDisplay(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x), (y))
    screen.blit(TextSurf, TextRect)


WA = City(int(display_width * 0.1), int(display_height * 0.15))
CO = City(int(display_width * 0.3), int(display_height * 0.35))
MT = City(int(display_width * 0.35), int(display_height * 0.1))
TX = City(int(display_width * 0.4), int(display_height * 0.7))
OK = City(int(display_width * 0.475), int(display_height * 0.45))
KS = City(int(display_width * 0.5), int(display_height * 0.25))
NY = City(int(display_width * 0.75), int(display_height * 0.2))

stateArray = [WA, MT, NY, TX, CO, KS, OK]


def drawDecks(color):
    return {
        'white': lambda: screen.blit(whiteDeckImg, (display_width * 0.017, display_height * 0.75)),
        'pink': lambda: screen.blit(pinkDeckImg, (display_width * 0.117, display_height * 0.75)),
        'red': lambda: screen.blit(redDeckImg, (display_width * 0.217, display_height * 0.75)),
        'orange': lambda: screen.blit(orangeDeckImg, (display_width * 0.317, display_height * 0.75)),
        'yellow': lambda: screen.blit(yellowDeckImg, (display_width * 0.417, display_height * 0.75)),
        'green': lambda: screen.blit(greenDeckImg, (display_width * 0.517, display_height * 0.75)),
        'blue': lambda: screen.blit(blueDeckImg, (display_width * 0.617, display_height * 0.75)),
        'black': lambda: screen.blit(blackDeckImg, (display_width * 0.717, display_height * 0.75)),

    }.get(color, lambda: None)()


def drawGameBoard():
    pygame.draw.line(screen, black, (WA.getX(), WA.getY()), (CO.getX(), CO.getY()))
    pygame.draw.line(screen, black, (WA.getX(), WA.getY()), (TX.getX(), TX.getY()))
    pygame.draw.line(screen, black, (WA.getX(), WA.getY()), (MT.getX(), MT.getY()))
    pygame.draw.line(screen, black, (TX.getX(), TX.getY()), (NY.getX(), NY.getY()))
    pygame.draw.line(screen, black, (NY.getX(), NY.getY()), (MT.getX(), MT.getY()))
    pygame.draw.line(screen, black, (NY.getX(), NY.getY()), (KS.getX(), KS.getY()))
    pygame.draw.line(screen, black, (TX.getX(), TX.getY()), (OK.getX(), OK.getY()))
    pygame.draw.line(screen, black, (OK.getX(), OK.getY()), (CO.getX(), CO.getY()))
    pygame.draw.line(screen, black, (KS.getX(), KS.getY()), (CO.getX(), CO.getY()))
    pygame.draw.line(screen, black, (OK.getX(), OK.getY()), (KS.getX(), KS.getY()))

    # draws the black and white train card on the card piles over the hit boxes
    for x in range(0, len(chosenColors), 1):
        drawDecks(chosenColors[x])

    pygame.draw.rect(screen, darkGreen,
                     (display_width * 0.83, display_height * 0.125, display_width * 0.15, display_height * 0.66))
    cityNameDisplay("HAND", display_width * 0.95, display_height * 0.14)

    drawCities()


def drawCities():
    pygame.draw.circle(screen, white, [WA.getX(), WA.getY()], 50, 50)
    pygame.draw.circle(screen, white, [CO.getX(), CO.getY()], 50, 50)
    pygame.draw.circle(screen, white, [MT.getX(), MT.getY()], 50, 50)
    pygame.draw.circle(screen, white, [TX.getX(), TX.getY()], 50, 50)
    pygame.draw.circle(screen, white, [OK.getX(), OK.getY()], 50, 50)
    pygame.draw.circle(screen, white, [KS.getX(), KS.getY()], 50, 50)
    pygame.draw.circle(screen, white, [NY.getX(), NY.getY()], 50, 50)

    cityNameDisplay("WA", WA.getX(), WA.getY())
    cityNameDisplay("CO", CO.getX(), CO.getY())
    cityNameDisplay("MT", MT.getX(), MT.getY())
    cityNameDisplay("TX", TX.getX(), TX.getY())
    cityNameDisplay("OK", OK.getX(), OK.getY())
    cityNameDisplay("KS", KS.getX(), KS.getY())
    cityNameDisplay("NY", NY.getX(), NY.getY())


trackDataArray = [[-1 for x in range(20)] for y in range(11)]


# draws the tracks
def drawTracks():
    row = 0
    for i in range(0, len(cityConnection), 1):
        for j in range(i, len(cityConnection[i]), 1):
            if cityConnection[i][j] != -1:
                length = cityConnection[i][j].getLength()
                testLength = length
                color = cityConnection[i][j].getColor()
                x1 = stateArray[i].getX()
                y1 = stateArray[i].getY()
                x2 = stateArray[j].getX()
                y2 = stateArray[j].getY()
                difx = x2 - x1
                dify = y2 - y1
                radians = math.atan2(dify, difx)
                rot = math.degrees(radians)

                perLenX = difx / length
                perLenY = dify / length

                trackImg = pygame.transform.scale(strToObj(color + "Track"), (100, 50))
                trackImgFin = pygame.transform.rotate(trackImg, -rot)

                for pri in range(1, length + 1):
                    if testLength >= 0:
                        left = x1 + (perLenX * pri * .8) - 50
                        top = y1 + (perLenY * pri * .8) - 50
                        screen.blit(trackImgFin, (left, top))

                        trackDataArray[row][pri - 1] = Track(top, left, color, trackImgFin, length, rot, perLenX,
                                                             perLenY, False)
                        testLength -= 1
                        if testLength == 0:
                            row += 1


def claimTrack(track, row):
    color = track.getColor()
    trackImg = pygame.transform.scale(strToObj(color + "TrackOcc"), (100, 50))
    trackImgFin = pygame.transform.rotate(trackImg, -track.getRot())
    testLength = track.getLength()
    for pri in range(0, track.getLength()):
        trackDataArray[row][pri].setOccupied(True)
        if testLength >= 0:
            left = track.getLeft() + (track.getPerX() * pri * .8)
            top = track.getTop() + (track.getPerY() * pri * .8)
            screen.blit(trackImgFin, (left, top))

    print("claimed")


def removeCardsFromHand(color, numRemove):
    for k in range(human.handCards.__len__() - 1, -1, -1):
        if human.handCards[k].getColor() == color and numRemove > 0:
            human.handCards.remove(human.handCards[k])
            human.cardIndex -= 1
            numRemove -= 1;
    pygame.draw.rect(screen, darkGreen,
                     (display_width * 0.83, display_height * 0.125, display_width * 0.15, display_height * 0.66))
    cityNameDisplay("HAND", display_width * 0.95, display_height * 0.14)
    for k in range(0, human.handCards.__len__(), 1):
        color = human.handCards[k].getColor()
        screen.blit(globals()[color + 'TrainImg'], (display_width * 0.85, display_height * 0.13 + (40 * k)))


firstTrack = None


def testHitboxes(color):
    return {
        'white': lambda: drawHand("white"),
        'pink': lambda: drawHand("pink"),
        'red': lambda: drawHand("red"),
        'orange': lambda: drawHand("orange"),
        'yellow': lambda: drawHand("yellow"),
        'green': lambda: drawHand("green"),
        'blue': lambda: drawHand("blue"),
        'black': lambda: drawHand("black"),

    }.get(color, lambda: None)()



def createBoard():
    global cityConnection
    cityConnection = ([[-1, Edge(3, chosenColors[randrange(0, len(chosenColors))]), -1,
                        Edge(5, chosenColors[randrange(0, len(chosenColors))]),
                        Edge(2, chosenColors[randrange(0, len(chosenColors))]), -1, -1],
                       [Edge(3, chosenColors[randrange(0, len(chosenColors))]), -1,
                        Edge(4, chosenColors[randrange(0, len(chosenColors))]), -1, -1, -1, -1],
                       [-1, Edge(4, chosenColors[randrange(0, len(chosenColors))]), -1,
                        Edge(6, chosenColors[randrange(0, len(chosenColors))]), -1,
                        Edge(4, chosenColors[randrange(0, len(chosenColors))]), -1],
                       [Edge(5, chosenColors[randrange(0, len(chosenColors))]), -1,
                        Edge(6, chosenColors[randrange(0, len(chosenColors))]), -1, -1, -1,
                        Edge(3, chosenColors[randrange(0, len(chosenColors))])],
                       [Edge(2, chosenColors[randrange(0, len(chosenColors))]), -1, -1, -1, -1,
                        Edge(3, chosenColors[randrange(0, len(chosenColors))]),
                        Edge(3, chosenColors[randrange(0, len(chosenColors))])],
                       [-1, -1, Edge(4, chosenColors[randrange(0, len(chosenColors))]), -1,
                        Edge(3, chosenColors[randrange(0, len(chosenColors))]), -1,
                        Edge(2, chosenColors[randrange(0, len(chosenColors))])],
                       [-1, -1, -1, Edge(3, chosenColors[randrange(0, len(chosenColors))]),
                        Edge(3, chosenColors[randrange(0, len(chosenColors))]),
                        Edge(2, chosenColors[randrange(0, len(chosenColors))]), -1]])

# draws the hit boxes for the white and black card draw piles
whiteDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.03, display_height * 0.77, 100, 100), 1)
pinkDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.13, display_height * 0.77, 100, 100), 1)
redDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.23, display_height * 0.77, 100, 100), 1)
orangeDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.33, display_height * 0.77, 100, 100), 1)
yellowDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.43, display_height * 0.77, 100, 100), 1)
greenDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.53, display_height * 0.77, 100, 100), 1)
blueDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.63, display_height * 0.77, 100, 100), 1)
blackDeck = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.73, display_height * 0.77, 100, 100), 1)


def gameLoop():

    for x in range(len(chosenColors)):
        print("here:")
        print(chosenColors[x])

    human.handCards = []
    human.cardIndex = 0
    bot.handCards = []
    bot.cardIndex = 0
    playerTurn = True
    numCards = 0
    screen.fill(white)

    screen.blit(BackGround.image, BackGround.rect)

    passTurn = pygame.draw.rect(screen, (255, 255, 255), (display_width * 0.75, display_height * 0.5, 100, 75), 1)
    createBoard()
    drawTracks()
    drawGameBoard()

    running = True

    while running:
        drawCities()
        button("Title Screen", 17, display_width * 0.85, display_height * 0.05, 100, 75, blue, darkBlue, titleScreen)
        button("Quit", 20, display_width * 0.85, display_height * 0.8, 100, 75, red, darkRed, quitGame)
        button("Pass Turn", 17, display_width * 0.75, display_height * 0.5, 100, 75, white, grey)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if playerTurn:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    for i in range(0, len(trackDataArray), 1):
                        for j in range(0, len(trackDataArray[i]), 1):
                            data = trackDataArray[i][j]

                            if data != -1:
                                # pygame.draw.circle(screen, black, (int(data.getLeft()), int(data.getTop())), 10)
                                if data.getImg().get_rect().move(data.getLeft(), data.getTop()).collidepoint(
                                        pos) and data.getOccupied() == False:
                                    sameColor = 0
                                    for k in range(0, human.handCards.__len__(), 1):
                                        if human.handCards[k].getColor() == data.getColor():
                                            sameColor += 1
                                        if sameColor == data.getLength():
                                            firstTrack = trackDataArray[i][0]
                                            claimTrack(firstTrack, i)
                                            removeCardsFromHand(data.getColor(), data.getLength())
                                            break

                    if len(human.handCards) >= 14:
                        print('There are 14 cards in your hand, you can not draw any more!')

                    elif passTurn.collidepoint(pos):
                        playerTurn = False
                    else:
                        for x in range(0, len(chosenColors), 1):
                            if strToObj(chosenColors[x] + "Deck").collidepoint(pos):
                                testHitboxes(chosenColors[x])

            ##ai decision
            if playerTurn == False:
                ##Call ai desision method/class here
                print("ai played its turn")
                playerTurn = True

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


titleScreen()
settings()
gameLoop()
