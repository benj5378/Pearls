import pygame
import cv2
import json
import math
import numpy

FPS = int(input("Type FPS: "))

pygame.init()
pygame.font.init()

fpsClock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, 32)
pygame.display.set_caption('Perls')
screen.fill((11, 162, 6))
splash = pygame.image.load("assets/splash.png")
screen.blit(splash, (int(screen.get_width() / 2 - splash.get_width() / 2), int(screen.get_height() / 2 - splash.get_height() / 2)))

# background.blit()
pygame.display.update()

quit = False


def defineVariables():
    global margin
    global width
    global radius
    global space
    global grid
    global push
    global zoom
    global xMove
    global yMove
    global mouseMove
    global oldPos
    global zoomOld
    global startAt
    global spaceI
    global typing
    global boxMargin
    global marked
    global updateFontSurf
    updateFontSurf = True
    margin = [30, 30]
    width = 3
    radius = 4
    space = 1
    spaceI = space
    space = 0
    grid = 0
    push = radius + grid + space
    push = 20
    zoom = 5
    perls = [
            [[255, 255, 255, 0], [0, 1, 50, 25], [0, 0, 0, 255]],
            [[255, 255, 255, 0], [0, 1, 50, 25], [0, 0, 0, 255]],
            [[255, 255, 255, 0], [0, 1, 50, 25], [0, 0, 0, 255]],
        ]
    xMove = 0
    yMove = 0
    mouseMove = False
    oldPos = []
    zoomOld = zoom
    startAt = [0, 0]
    typing = False
    boxMargin = [180, 20]
    marked = [0, 0]

perls = cv2.cvtColor(cv2.imread("assets/final 3 s.png"), cv2.COLOR_BGR2RGB)


def savePerlsArray(filename):
    f = open(filename, "w+")
    f.write(json.dumps(perls.tolist(), indent=2))
    f.close()


def replaceColor(image, find, replace):
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if numpy.array_equal(image[i][j], find):
                image[i][j] = replace
    #perls = cv2.cvtColor(perls, cv2.COLOR_BGR2RGB)


# Define colors
def c(colorCode):
    return {
        "[69 49 46]": "Hama midi 12 Mørkebrun",
        "[185 107  60]": "Hama midi Nougat mørk",
        "[232 175 100]": "Hama midi 61 Met.guld",
        "[233 138  51]": "Hama midi 21 Nougat lys",
        "[255 181  33]": "Hama midi 60 Bamsegul",
        "[57 96 84]": "Hama midi 28 Mørkegrøn",
        "[229 168 116]": "Hama midi Lysebrun",
        "[185 218 122]": "Hama midi 47 Pastelgrøn",
        "[241 234 202]": "Hama midi 02 Creme",
        "[255 215 158]": "Hama midi 27 Varmbeige",
        "[255 242  99]": "Hama midi 43 Pastelgul",
        "[255 225   0]": "Hama midi 03 Gul",
        "[255 255 255]": "Hama midi 01 Hvid",
        "[250 248 217]": "Hama midi Lysegul",
        "[0 0 0]": "Hama midi 18 Sort",
        "[203  62  16]": " Hama midi 20 Rødbrun",
        "[53 61 65]": "Hama midi 77 Mørkegrå",
        "[179 181 186]": "Hama midi 17 Grå",
        "[252 111  57]": "Hama midi 04 Orange",
        "[ 59 176 206]": "Hama midi 31 Turkis",
        "[  0 136  91]": "Hama midi 10 Grøn",
        "[244 124 104]": "Hama midi 33 Lyserød hudfarve",
        "[  0 101 184]": "Hama midi 09 Blå",
        "[183  35  48]": "Hama midi Mørkerød",
        "[ 19 185 223]": "Hama midi 49 Azurblå",
        "[ 53 178 125]": "Hama midi 11 Lysegrøn",
        "[173 132 184]": "Hama midi 45 Pastellilla",
        "[224  26  44]": "Hama midi 22 Julerød",
        "[186 190 196]": "Hama midi 70 Lysegrå",
        "[111 196 246]": "Hama midi 46 Pastelblå",
        "[  0  54 152]": "Hama midi 08 Klar blå",
        "[250 183 186]": "Hama midi 06 Rosa",
        "[145  83 161]": "Hama midi 07 Lilla"
    }.get(colorCode, "Unknown")


def numbersY(start, end, outerSize, shift):
    maxWidth = 0
    for i in range(start, end):
        if not i == marked[1]:
            textSurface = font.render(str(i), False, (0, 0, 0))
        else:
            # textSurface = font.render(str(i), False, (0, 0, 0), (255, 0, 0))
            textSurface = font.render(str(i), False, (0, 0, 0))
            #print("marked")
        if maxWidth < textSurface.get_width():
            maxWidth = textSurface.get_width()
        y = math.ceil(outerSize * i) + shift + margin[0]
        y = y - textSurface.get_height() / 2
        if y > SCREEN_HEIGHT:
            break
        elif y < 0 + margin[0]:
            continue
        screen.blit(textSurface, (0, y))  # Font-size = radius
    return maxWidth


def numbersX(start, end, outerSize, shift):
    maxHeight = 0
    for i in range(start, end):
        if not i == marked[0]:
            textSurface = font.render(str(i), False, (0, 0, 0))
        else:
            #textSurface = font.render(str(i), False, (0, 0, 0), (255, 0, 0))
            textSurface = font.render(str(i), False, (0, 0, 0))
            #print("marked")

        # If there isnt space for numbers, then rotate
        if textSurface.get_width() > perlSize:
            textSurface = pygame.transform.rotate(textSurface, -90)
        
        # Get the highest rect size
        if maxHeight < textSurface.get_height():
            maxHeight = textSurface.get_height()
        
        # Calculate center x coordinate for perl
        x = math.ceil(outerSize * i) + shift + margin[1]
        
        # Set to middle
        x = x - textSurface.get_width() / 2
        if x > SCREEN_WIDTH - margin[1] + perlSize:
            break
        elif x < 0 + margin[1] - perlSize:
            continue
        
        screen.blit(textSurface, (x, 0))
    return maxHeight


def getMousePos(size):
    x, y = pygame.mouse.get_pos()
    return x, y
    # Calculate perls x coordinate
    startAt[1]
    print((startAt[1] * perlSize + xMove + x))
    print(int((startAt[1] * perlSize + x + margin[1] + perlSize / 2) // perlSize))
    print(startAt[1] * perlSize + x + margin[1] + perlSize / 2)
    print(xMove)

    # Calculate perls y coordinate


def displayPerlInfo(perl):
    print(str(perl) + " = " + str(perls[perl[0]][perl[1]])  + " = " + c(str(perls[perl[0]][perl[1]])))
    print("---")


def countColors(image):
    count = {}
    for i in range(0, len(image)):
        unique, counts = numpy.unique(image[i], axis=0, return_counts=True)
        for j in range(0, len(unique)):
            if c(str(unique[j])) in count:
                count[c(str(unique[j]))] = count[c(str(unique[j]))] + counts[j]
            else:
                count[c(str(unique[j]))] = counts[j]
    return count


defineVariables()
print(countColors(perls))
while not quit:
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
    
    screen.fill((255, 255, 255))

    background = pygame.Surface(pygame.display.get_surface().get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    perlSize = (grid + radius + width) * zoom
    push = math.ceil(perlSize)

    # Check events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if typing:
                if event.key == pygame.K_RETURN:
                    typing = False
                    try:
                        temp = typed.split(', ')
                        x = int(temp[0])
                        y = int(temp[1])
                        displayPerlInfo([x, y])
                    except:
                        print("Error")
                elif event.unicode.isdigit() or event.unicode == "," or event.unicode == " ":
                    typed += event.unicode
            elif event.key == pygame.K_LEFT:
                xMove += push
            elif event.key == pygame.K_RIGHT:
                xMove -= push
            elif event.key == pygame.K_UP:
                yMove += push
            elif event.key == pygame.K_DOWN:
                yMove -= push
            elif event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                break
            elif event.unicode == "+":
                zoom += 1
            elif event.unicode == "-":
                zoom -= 1
            elif event.unicode == "s" and pygame.key.get_mods() & pygame.KMOD_CTRL:
                typed = ""
                typing = True
            elif event.unicode == "?":
                typed = ""
                typing = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseMove = True
                oldPos = pygame.mouse.get_pos()
            elif event.button == 2:
                print(xMove)
            elif event.button == 3:
                # displayPerlInfo(getMousePos(perlSize))
                typed = ""
                typing = True
            elif event.button == 4:
                zoom += 1
            elif event.button == 5:
                zoom -= 1
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseMove = False
        elif event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
            updateFontSurf = True
        elif event.type == pygame.QUIT:
            pygame.display.quit()
            break

    if mouseMove:
        pos = pygame.mouse.get_pos()
        xMove += pos[0] - oldPos[0]
        yMove += pos[1] - oldPos[1]
        oldPos = pos

    background.fill((255, 255, 255))

    if zoom == zoomOld:
        # Make space 0 if zoomed out so picture makes sense for eyes
        if zoom < 2:
            space = 0
        else:
            space = spaceI
        
        grid = space
        # Calculate where to start for y
        i = 0
        firstPerlPos = math.ceil((i * grid + i * radius + i * width) * zoom) + yMove

        result = math.ceil((-firstPerlPos) / perlSize)
        if result > 0:  # Result not less than 0
            startAt[0] = result - 1
        else:
            startAt[0] = 0
        # Calculate where to start for y
        i = 0
        firstPerlPos = math.ceil((i * grid + i * radius + i * width) * zoom) + xMove

        result = math.ceil((-firstPerlPos) / perlSize)
        if result > 0:  # Result not less than 0
            startAt[1] = result - 1
        else:
            startAt[1] = 0
    else:
        if zoom <= 0:
            zoom = zoomOld
        # Keep startAt[0] = 0
        i = startAt[0]
        perlSize = (grid + radius + width) * zoom
        yMove = math.ceil(-perlSize * startAt[0])

        i = startAt[1]
        perlSize = (grid + radius + width) * zoom
        xMove = math.ceil(-perlSize * startAt[1])
        zoomOld = zoom
    
    maxNumOfPerls = [math.ceil((SCREEN_HEIGHT - margin[0] * 2) / ((grid + radius + width) * zoom)), math.ceil((SCREEN_WIDTH - margin[1] * 2) / ((grid + radius + width) * zoom))]
    fontSize = (radius + width) * zoom
    grid = (space + width / 2)
    screen.fill((255, 255, 255))  # Do white background

    for i in range(startAt[0], len(perls)):
        y = math.ceil((i * grid + i * radius + i * width) * zoom) + yMove + margin[0]

        if y > SCREEN_HEIGHT + perlSize:
            break
        elif y < margin[0] - perlSize:
            continue

        for j in range(startAt[1], len(perls[i])):
            x = math.ceil(j * perlSize) + xMove + margin[1]
            if x > SCREEN_WIDTH + perlSize:
                break
            elif x < margin[1] - perlSize:
                continue
            # gridSet.append([i, j])
            if not numpy.array_equal(perls[i][j], [255, 255, 255]):
                pygame.draw.circle(background, perls[i][j], [x, y], radius * zoom, width * zoom)
            else:
                pygame.draw.circle(background, (0, 0, 0), [x, y], radius * zoom, width)
    

    # Do margins gray
    # For top side
    pygame.draw.rect(background, (150, 150, 150), (0, 0, SCREEN_WIDTH, margin[1]), 0)
    # For left side
    pygame.draw.rect(background, (150, 150, 150), (0, 0, margin[0], SCREEN_HEIGHT), 0)
    screen.blit(background, (0, 0))
    
    font = pygame.font.SysFont('Comic Sans MS', fontSize)

    
    # Draw numbers horizontally
    margin[0] = numbersY(startAt[0], startAt[0] + maxNumOfPerls[0], perlSize, yMove)
    # Draw numbers vertically
    margin[1] = numbersX(startAt[1], startAt[1] + maxNumOfPerls[1], perlSize, xMove)
    
    if typing:
        screen.blit(font.render(typed, False, (0, 0, 0), (255, 255, 255)), (SCREEN_WIDTH - boxMargin[0], SCREEN_HEIGHT - fontSize - boxMargin[1]))


    # pygame.draw.line(screen, (255, 0, 0), (radius * zoom, 20), (500, 20), 1)
    
    if updateFontSurf:
        # Update font surface
        temp = pygame.font.Font("Calibri", fontSize)
        creditSurf = temp.render("Copyright 2018 Benjamin Sayoc", False, (0, 0, 0), (255, 255, 255))
        updateFontSurf = False
    screen.blit(creditSurf, (margin[0] * 2, SCREEN_HEIGHT - fontSize - boxMargin[1]))


    pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(FPS)
