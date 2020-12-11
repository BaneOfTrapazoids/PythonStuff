import pygame
import sys
import keyboard
from string import digits
digits += " "

#reads all the lines
def reader():
    with open("turing.txt", "r") as turingtext:
        lines = turingtext.readlines()
        #returns all the lines
        return lines

#takes in what cell you want to go to and what you want to change it to
def writer(cellnum, newcellvalue):
    lines = reader()
    with open("turing.txt", "w") as turingtext:
        lines[cellnum-1] = f"{newcellvalue}\n"
        turingtext.writelines(lines)

#loads up all of pygame's stuff
pygame.init()

#creates the window with a variable and sets the width and height
screen = pygame.display.set_mode((500, 400))

#sets the name for the window
pygame.display.set_caption("Turing Machine")

#sets what fonts to use
font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 50)
small_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)

#assigns the clock (which is a tool to help track time in the game) to a variable for easy use
clock = pygame.time.Clock()

#loads a picture in and converts it to a format easier for pygame to work with
background = pygame.image.load("turingpics/mainhead.png").convert()

#used to track where in the text file pygame should be rendering
text_render_num = 0

#text that will be rendered onto the writer text box
writer_box_text = ""

#text that will be rendered onto the mover text box
mover_box_text = ""

#is changed to true after a button is clicked once, once the mouse is unclicked then it gets set back to false
#allowing the buttons to be clicked again
mouseisbeingheld = False

#checks if the writer text box has been clicked
writer_text_box_active = False

#checks if the mover text box has been clicked
mover_text_box_active = False

#checks if a key is being held down
key_is_held = False
#runs all the code needed for buttons
def buttons():
    global text_render_num
    global mouse_pos
    global mouse_pressed
    global mouse_is_being_held
    global writer_text_box_active
    global mover_text_box_active

    #moves the tape left, showing the numbers further left
    def left_button_clicked():
        global text_render_num
        text_render_num -= 1

    #same as above, but in the opposite direction
    def right_button_clicked():
        global text_render_num
        text_render_num += 1

    #starts reading for numbers and spaces
    def writer_text_box_clicked():
        global digits
        global writer_box_text
        global key_is_held
        def key_is_held_changer(argument):
            global key_is_held
            key_is_held = False
        for number in digits:
            if keyboard.is_pressed(number) and key_is_held == False:
                writer_box_text += number
                key_is_held = True
            keyboard.on_release_key(number, key_is_held_changer)
        if keyboard.is_pressed("backspace") and key_is_held == False:
            writer_box_text = writer_box_text[0:len(writer_box_text)-1]
            key_is_held = True
        if keyboard.is_pressed("enter"):
            writer_args = writer_box_text.split(" ")
            writer(int(writer_args[0]), int(writer_args[1]))
    
    def mover_text_box_clicked():
        global digits
        global key_is_held
        global mover_box_text
        global text_render_num

        def key_is_held_changer(argument):
            global key_is_held
            key_is_held = False
        
        for number in digits:
            if keyboard.is_pressed(number) and key_is_held == False:
                mover_box_text += number
                key_is_held = True
            keyboard.on_release_key(number, key_is_held_changer)
        
        if keyboard.is_pressed("backspace") and key_is_held == False:
            mover_box_text = mover_box_text[0:len(mover_box_text)-1]
            key_is_held = True
        if keyboard.is_pressed("enter"):
            text_render_num = int(mover_box_text)-3
    
    #checks if the mouse is within the border of the left button and if it is clicked
    if mouse_pressed[0] == True and 20+70 > mouse_pos[0] > 20 and 355+40 > mouse_pos[1] > 355 and mouse_is_being_held == False:
        left_button_clicked()
        mouse_is_being_held = True
    
    #checks if the mouse is within the border of the right button and if it is clicked
    if mouse_pressed[0] == True and 415+70 > mouse_pos[0] > 415 and 355+40 > mouse_pos[1] > 355 and mouse_is_being_held == False:
        right_button_clicked()
        mouse_is_being_held = True

    #checks if the writer text box has been clicked
    if mouse_pressed[0] == True and 410+70 > mouse_pos[0] > 410 and 40+35 > mouse_pos[1] > 40 or writer_text_box_active == True:
        writer_text_box_clicked()
        writer_text_box_active = True

    #checks if the mover text box has been clicked
    if mouse_pressed[0] == True and 20+70 > mouse_pos[0] > 20 and 40+35 > mouse_pos[1] > 40 or mover_text_box_active == True:       
        mover_text_box_clicked()
        mover_text_box_active = True
    
    #checks if the mouse has clicked off the writer text box
    if mouse_pressed[0] == True and not(410+70 > mouse_pos[0] > 410 and 40+35 > mouse_pos[1] > 40):
        writer_text_box_active = False

    #resets mouse_is_being_held if the mouse is not being held
    if mouse_pressed[0] == False:
        mouse_is_being_held = False

while True:
    #quit checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #checks if the text render num has gone below 0, if it has then sets it so that the furthest right cell is the last cell
    if text_render_num < 0:
        text_render_num = len(reader())-5
    
    #opposite of last part
    if text_render_num > 495:
        text_render_num = 0
    
    #removes the \n's from the result of the reader
    turing_machine_text = reader()
    new_text = []
    for i in turing_machine_text:
        newi = i.replace("\n", "")
        new_text += newi
    
    #Cell value says whether that cell is a 0 or a 1
    cell_value = [font.render(new_text[text_render_num+i], True, (0,0,0)) for i in range(5)]

    #cell num says what line number in the text file that cell is
    cell_num = [small_font.render(str(text_render_num+i), True, (0,0,0)) for i in range(1, 6)]

    #the text that will be rendered onto the writer text box
    writer_text = small_font.render(writer_box_text, True, (0,0,0))

    #the text that will be rendered onto the mover text box
    mover_text = small_font.render(mover_box_text, True, (0,0,0))

    #some extra text for the buttons
    left_button_arrow = small_font.render("<---", True, (0,0,0))
    right_button_arrow = small_font.render("--->", True, (0,0,0))

    #throws each surface onto the screen
    screen.blit(background, (0,0))
    screen.blit(cell_value[0], (35,220))
    screen.blit(cell_value[1], (135,220))
    screen.blit(cell_value[2], (235,220))
    screen.blit(cell_value[3], (335,220))
    screen.blit(cell_value[4], (435,220))
    screen.blit(cell_num[0], (40, 320))
    screen.blit(cell_num[1], (140, 320))
    screen.blit(cell_num[2], (240, 320))
    screen.blit(cell_num[3], (340, 320))
    screen.blit(cell_num[4], (440, 320))

    #gets the position of the mouse and what buttons are being pressed on the mouse
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    #left button outer border
    pygame.draw.rect(screen, (0,0,0), (20,355,70,40))

    #left button inner border
    pygame.draw.rect(screen, (255,255,255), (25,360,60,30))

    #right button outer border
    pygame.draw.rect(screen, (0,0,0), (415,355,70,40))

    #right button inner border
    pygame.draw.rect(screen, (255,255,255), (420,360,60,30))

    #writer text box outer border
    pygame.draw.rect(screen, (0,0,0), (410,40,70,35))

    #writer text box inner border
    pygame.draw.rect(screen, (255,255,255), (415,45,60,25))

    #mover text box outer border
    pygame.draw.rect(screen, (0,0,0), (20,40,70,35))

    #mover text box inner border
    pygame.draw.rect(screen, (255,255,255), (25,45,60,25))

    #arrows for the left and right buttons
    screen.blit(left_button_arrow, (35, 362))
    screen.blit(right_button_arrow, (430, 362))

    #all the code for the buttons
    buttons()
    screen.blit(writer_text, (415,47))
    screen.blit(mover_text, (25,47))
    pygame.display.update()
    clock.tick(60)