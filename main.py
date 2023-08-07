import pygame
from Imagehandler import Imageclass

# Initiate pygame
pygame.init()

# Check for dimension of user display and put values in a list
monitorWindowWidth, monitorWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
gameWindowSize = []

# Create the screen that the image will be drawn on with the dimensions of the chosen image
screen = pygame.display.set_mode((monitorWindowWidth, monitorWindowHeight))

# Create however many instances of the Imageclass as you want and put them into the imageList
imageONE = Imageclass(screen, "Billeder/frædert.png", False)
imageTWO = Imageclass(screen, "Billeder/elon-musk.jpg", False)
imageList = [imageONE, imageTWO]


# Function for checking if the user typed number is out of the imageList's range
def list_out_of_range(userselectedimage):
    if userselectedimage > len(imageList) - 1:
        return True
    else:
        return False


# Basic font for user typed
baseFont = pygame.font.Font(None, 32)
# Empty string used for holding text typed by the user
userText = ''
# Variable for storing the user typed text an an integer
userTextAsInt = 0

# Textbox passive color
color_passive = (128, 154, 226)
# Textbox active color
color_active = (67, 104, 220)
# Default color is pasive
color = color_passive

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            # Quit game
            if event.key == pygame.K_ESCAPE:
                running = False

            # Change flip variable of the shown picture to flip it
            elif event.key == pygame.K_k:
                imageList[userTextAsInt].flip = True
            elif event.key == pygame.K_l:
                imageList[userTextAsInt].flip = False

            # Check for backspace
            elif event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                userText = userText[:-1]

            # Unicode standard is used for string formation
            else:
                userText += event.unicode

        # Quit game
        elif event.type == pygame.QUIT:
            running = False

        # Change color of textbox if it's been clicked on
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect.collidepoint(event.pos):
                color = color_active
            else:
                color = color_passive

    try:
        userTextAsInt = int(userText) - 1
        if list_out_of_range(userTextAsInt):
            screen.fill((0, 0, 0))
        else:
            imageList[userTextAsInt].draw()
    except ValueError:
        pass

    # Variable holding rendered version of what the user has typed
    text_surface = baseFont.render(userText, True, (255, 255, 255))
    # Input rect behind the user text
    inputRect = pygame.Rect((monitorWindowWidth - 140) / 2, 200, 140, 32)
    # Draw rectangle and argument passed which should be on screen
    pygame.draw.rect(screen, color, inputRect)
    # Set width of textfield so that text cannot get outside of user's text input
    inputRect.w = max(100, text_surface.get_width() + 10)
    # Blit what the user has typed to the screen
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))

    pygame.display.flip()
pygame.quit()
