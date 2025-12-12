#      #  #####  #     ####  #####  #   #  #####
#      #  #      #    #     #   #  ## ##  #    
#      #  #      #    #     #   #  # # #  #    
#   #  #  #####  #    #     #   #  #   #  #####
# #  # #  #      #    #     #   #  #   #  #    
##    ##  #      #    #     #   #  #   #  #    
#      #  #####  ##### ####  #####  #   #  #####

# you may scroll around the code and see the progress

#Warning: DO NOT CHANGE THE CODE (IT WILL BREAK)
# & dont forget to try out the actual game from VERY obvious arrow
#Fill the form after you done ye

import pygame
import button
import math
import sys

pygame.init()



screen_h = 750
screen_w = 1000

screen = pygame.display.set_mode((screen_w,screen_h))

#button
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
back_img = pygame.image.load('back_btn.png').convert_alpha()

#create button instances (said the video)
start_button = button.Button(screen_w//2, 500, start_img, 1)
start_button.rect.center = (screen_w//2, 500)
exit_button = button.Button(screen_w,700, exit_img, 0.75)
exit_button.rect.center = (screen_w//2, 700)
back_button = button.Button(screen_w,700, back_img, 0.75)
back_button.rect.center = (screen_w//2, 700)


#font
font = pygame.font.SysFont (None, 20)
title = pygame.font.SysFont (None,100)

#load image
bg = pygame.image.load("bg.png").convert()
bg_width = bg.get_width()

tittle_img = pygame.image.load("title.png").convert_alpha()
tittle = button.Button(screen_w//2, 300, tittle_img, 1)
tittle.rect.center = (screen_w//2, 300)

# subject object/image
math_button = pygame.image.load("MATH_btn.png").convert_alpha()
math_btn = button.Button(200,screen_h//2 +100,math_button,1)
math_btn.rect.center = (200,screen_h//2 +100)

science_button = pygame.image.load("SCI_btn.png").convert_alpha()
sci_btn = button.Button(800, screen_h//2 +100,science_button,1)
sci_btn.rect.center = (800, screen_h//2 +100)

spacelobby = pygame.Surface((300,50))
spacelobby.fill((128,128,128,128))
spacelobby_rect = spacelobby.get_rect(center=(screen_w//2, screen_h//2 +100))


#TRANSPARENT IMG (for subjects aka math & sci)
transparent = pygame.image.load("TRANSPARENT.png").convert_alpha()
transparent.set_alpha(180)
transparent_1 = button.Button(50,40,transparent,0.9)
transparent_1.image.set_alpha(50)

    #Spaceship inside

Space_In = pygame.Surface((screen_w, screen_h))
Space_In.fill((128, 128, 128))  
# erase the center (hole) — match transparent_1's size/position
hole_rect = pygame.Rect(
    screen_w // 2 - transparent_1.rect.width // 2,
    screen_h // 2 - transparent_1.rect.height // 2,
    transparent_1.rect.width,
    transparent_1.rect.height
)
Space_In.fill((0, 0, 0, 0), hole_rect)  


#Math page & Sci page
mathematics = pygame.image.load('Math_UI.png').convert_alpha()
mathematics_UI = button.Button(screen_w//2, screen_h//2 -265 ,mathematics,1)
mathematics_UI.rect.center = (screen_w//2, screen_h//2 -265)

Science = pygame.image.load('Science_UI.png').convert_alpha()
Science_UI = button.Button(screen_w//2, screen_h//2 -265 ,Science,1)
Science_UI.rect.center = (screen_w//2, screen_h//2 -265)

    #Select subject
Select = pygame.image.load('SELECT_UI.png')
Select_UI = button.Button(screen_w//2, screen_h//2 -130 ,Select,1)
Select_UI.rect.center = (screen_w//2, screen_h//2 -130)

    #Math topics
Linear = pygame.image.load('LER_btn.png').convert_alpha()
Linear_btn = button.Button(screen_w//2*1.45, screen_h//1.5 ,Linear,1)
Linear_btn.rect.center = (screen_w//2*1.45, screen_h//1.5)

Sequence = pygame.image.load('SECS_btnx.png').convert_alpha()
Sequence_btn = button.Button(screen_w//3.75, screen_h//1.5, Sequence, 1)
Sequence_btn.rect.center = (screen_w//3.75, screen_h//1.5)

    #Mathematics
Linear1 = pygame.image.load('LIEAEQ.png').convert_alpha()
Linear1_UI = button.Button(screen_w//2, screen_h//2 -130 ,Linear1,1)
Linear1_UI.rect.center = (screen_w//2, screen_h//2 -130)

Sequence1 = pygame.image.load('SEQANB.png').convert_alpha()
Sequence1_UI = button.Button(screen_w//2, screen_h//2 -130 ,Sequence1,1)
Sequence1_UI.rect.center = (screen_w//2, screen_h//2 -130)

    #Science topic
Climate = pygame.image.load('CBIO_btn.png').convert_alpha()
Climate_btn = button.Button(screen_w//2*1.45, screen_h//1.5, Climate, 1)
Climate_btn.rect.center = (screen_w//2*1.45, screen_h//1.5)

ChemReact = pygame.image.load('CR(NF)_btn.png').convert_alpha()
ChemReact_btn = button.Button(screen_w//3.75, screen_h//1.5, ChemReact, 1)
ChemReact_btn.rect.center = (screen_w//3.75, screen_h//1.5)

    #Science 
ChemReact1 = pygame.image.load('CHEMREACT.png').convert_alpha()
ChemReact1_UI = button.Button(screen_w//2, screen_h//2 -130, ChemReact1,1)
ChemReact1_UI.rect.center = (screen_w//2, screen_h//2 -130)

Climate1 = pygame.image.load('CLIMATEBIOME.png').convert_alpha()
Climate1_UI = button.Button(screen_w//2, screen_h//2 -130, Climate1, 1)
Climate1_UI.rect.center = (screen_w//2, screen_h//2 -130)

    #Practice buttons

Pract_Math = pygame.image.load('PRACT_MATH_btn.png').convert_alpha()
Pract_Math_btn = button.Button(screen_w//2, screen_h//2 +100, Pract_Math, 1)
Pract_Math_btn.rect.center = (screen_w//2, screen_h//2 +100)

Pract_Sci = pygame.image.load('PRACT_SCI_btn.png').convert_alpha()
Pract_Sci_btn = button.Button(screen_w//2, screen_h//2 +100, Pract_Sci, 1)
Pract_Sci_btn.rect.center = (screen_w//2, screen_h//2 +100)

# True and falase

True_img = pygame.image.load('TRUE_btn.png').convert_alpha()
True_btn = button.Button(screen_w//2 -200, screen_h//2 +200, True_img, 1)
True_btn.rect.center = (screen_w//2 -200, screen_h//2 +200)

False_img = pygame.image.load('FALSE_btn.png').convert_alpha()
False_btn = button.Button(screen_w//2 +200, screen_h//2 +200, False_img, 1)
False_btn.rect.center = (screen_w//2 +200, screen_h//2 +200)

#Lesson materials

    # Chemical Reaction

Lesson_ChemReact_lesson1 = pygame.image.load('CHEMREACT_LESSON1.png').convert_alpha()
Lesson_ChemReact_lesson1_ui  = button.Button(screen_w//2 -250, screen_h//2 +50, Lesson_ChemReact_lesson1, 0.975)
Lesson_ChemReact_lesson1_ui.rect.center = (screen_w//2 -250, screen_h//2 +50)

Lesson_ChemReact_lesson2 = pygame.image.load('CHEMREACT_LESSON2.png').convert_alpha()
Lesson_ChemReact_lesson2_ui  = button.Button(screen_w//2 +250, screen_h//2 +50, Lesson_ChemReact_lesson2,0.975)
Lesson_ChemReact_lesson2_ui.rect.center = (screen_w//2 +250, screen_h//2 +50)

    #Chemical Reaction questions

Q1_ChemReact_img = pygame.image.load('Q1 CHEMREACT.png').convert_alpha()
Q1_ChemReact_ui  = button.Button(screen_w//2, screen_h//2 -100, Q1_ChemReact_img,1.25)
Q1_ChemReact_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q2_ChemReact_img = pygame.image.load('Q2 CHEMREACT.png').convert_alpha()
Q2_ChemReact_ui  = button.Button(screen_w//2, screen_h//2 -100, Q2_ChemReact_img,1.25)
Q2_ChemReact_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q3_ChemReact_img = pygame.image.load('Q3 CHEMREACT.png').convert_alpha()
Q3_ChemReact_ui  = button.Button(screen_w//2, screen_h//2 -100, Q3_ChemReact_img,1.25)
Q3_ChemReact_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q4_ChemReact_img = pygame.image.load('Q4 CHEMREACT.png').convert_alpha()
Q4_ChemReact_ui  = button.Button(screen_w//2, screen_h//2 -100, Q4_ChemReact_img,1.25)
Q4_ChemReact_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q5_ChemReact_img = pygame.image.load('Q5 CHEMREACT.png').convert_alpha()
Q5_ChemReact_ui  = button.Button(screen_w//2, screen_h//2 -100, Q5_ChemReact_img,1.25)
Q5_ChemReact_ui.rect.center = (screen_w//2, screen_h//2 -100)

    # Biomes and climate

Lesson_CLIBIO_lesson1 = pygame.image.load('CLIBIO_LESSON1.png').convert_alpha()
Lesson_CLIBIO_lesson1_ui  = button.Button(screen_w//2 -250, screen_h//2 +50, Lesson_CLIBIO_lesson1,0.975)
Lesson_CLIBIO_lesson1_ui.rect.center = (screen_w//2 -250, screen_h//2 +50)

Lesson_CLIBIO_lesson2 = pygame.image.load('CLIBIO_LESSON2.png').convert_alpha()
Lesson_CLIBIO_lesson2_ui  = button.Button(screen_w//2 +250, screen_h//2 +50, Lesson_CLIBIO_lesson2,0.975)
Lesson_CLIBIO_lesson2_ui.rect.center = (screen_w//2 +250, screen_h//2 +50)
    #Biome and climate questions

Q1_CLIBIO_img = pygame.image.load('Q1 CLIBIO.png').convert_alpha()
Q1_CLIBIO_ui  = button.Button(screen_w//2, screen_h//2 -100, Q1_CLIBIO_img,1.25)
Q1_CLIBIO_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q2_CLIBIO_img = pygame.image.load('Q2 CLIBIO.png').convert_alpha()
Q2_CLIBIO_ui  = button.Button(screen_w//2, screen_h//2 -100, Q2_CLIBIO_img,1.25)
Q2_CLIBIO_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q3_CLIBIO_img = pygame.image.load('Q3 CLIBIO.png').convert_alpha()
Q3_CLIBIO_ui  = button.Button(screen_w//2, screen_h//2 -100, Q3_CLIBIO_img,1.25)
Q3_CLIBIO_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q4_CLIBIO_img = pygame.image.load('Q4 CLIBIO.png').convert_alpha()
Q4_CLIBIO_ui  = button.Button(screen_w//2, screen_h//2 -100, Q4_CLIBIO_img,1.25)
Q4_CLIBIO_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q5_CLIBIO_img = pygame.image.load('Q5 CLIBIO.png').convert_alpha()
Q5_CLIBIO_ui  = button.Button(screen_w//2, screen_h//2 -100, Q5_CLIBIO_img,1.25)
Q5_CLIBIO_ui.rect.center = (screen_w//2, screen_h//2 -100)

    # Sequences

Lesson_SEquenceAR_img = pygame.image.load('SEQ_AR_LESSON.png')
Lesson_SEquenceAR_UI = button.Button(screen_w//2 -250, screen_h//2 +50, Lesson_SEquenceAR_img,1)
Lesson_SEquenceAR_UI.rect.center = (screen_w//2 -250, screen_h//2 +50)

Lesson_SEquenceGEO_img = pygame.image.load('SEQ_GEO_LESSON.png')
Lesson_SEquenceGEO_UI = button.Button(screen_w//2 +250, screen_h//2 +50, Lesson_SEquenceGEO_img,1)
Lesson_SEquenceGEO_UI.rect.center = (screen_w//2 +250, screen_h//2 +50)

    # Sequence questions

Q1_Sequence_img = pygame.image.load('Q1_SEQUENCE.png').convert_alpha()
Q1_Sequence_ui  = button.Button(screen_w//2, screen_h//2 -100, Q1_Sequence_img,1.25)
Q1_Sequence_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q2_Sequence_img = pygame.image.load('Q2_SEQUENCE.png').convert_alpha()
Q2_Sequence_ui  = button.Button(screen_w//2, screen_h//2 -100, Q2_Sequence_img,1.25)
Q2_Sequence_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q3_Sequence_img = pygame.image.load('Q3_SEQUENCE.png').convert_alpha()
Q3_Sequence_ui  = button.Button(screen_w//2, screen_h//2 -100, Q3_Sequence_img,1.25)
Q3_Sequence_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q4_Sequence_img = pygame.image.load('Q4_SEQUENCE.png').convert_alpha()
Q4_Sequence_ui  = button.Button(screen_w//2, screen_h//2 -100, Q4_Sequence_img,1.25)
Q4_Sequence_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q5_Sequence_img = pygame.image.load('Q5_SEQUENCE.png').convert_alpha()
Q5_Sequence_ui  = button.Button(screen_w//2, screen_h//2 -100, Q5_Sequence_img,1.25)
Q5_Sequence_ui.rect.center = (screen_w//2, screen_h//2 -100)


    # Linear
Lesson_LEquations_img = pygame.image.load('Lesson_LEquation.png').convert_alpha()
Lesson_LEquations_UI = button.Button(screen_w//2 -250, screen_h//2 +50, Lesson_LEquations_img,0.95)
Lesson_LEquations_UI.rect.center = (screen_w//2 -250, screen_h//2 +50)

HowToLinear_img = pygame.image.load('How To.png').convert_alpha()
HowToLinear  = button.Button(screen_w//2 +250, screen_h//2 +25, HowToLinear_img,0.95)
HowToLinear.rect.center = (screen_w//2 +250, screen_h//2 +25)
        # Linear questions
Q1_LINEAR_img = pygame.image.load('Q1_LINEAR.png').convert_alpha()
Q1_LINEAR_ui  = button.Button(screen_w//2, screen_h//2 -100, Q1_LINEAR_img,1.25)
Q1_LINEAR_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q2_LINEAR_img = pygame.image.load('Q2_LINEAR.png').convert_alpha()
Q2_LINEAR_ui  = button.Button(screen_w//2, screen_h//2 -100, Q2_LINEAR_img,1.25)
Q2_LINEAR_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q3_LINEAR_img = pygame.image.load('Q3_LINEAR.png').convert_alpha()
Q3_LINEAR_ui  = button.Button(screen_w//2, screen_h//2 -100, Q3_LINEAR_img,1.25)
Q3_LINEAR_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q4_LINEAR_img = pygame.image.load('Q4_LINEAR.png').convert_alpha()
Q4_LINEAR_ui  = button.Button(screen_w//2, screen_h//2 -100, Q4_LINEAR_img,1.25)
Q4_LINEAR_ui.rect.center = (screen_w//2, screen_h//2 -100)

Q5_LINEAR_img = pygame.image.load('Q5_LINEAR.png').convert_alpha()
Q5_LINEAR_ui  = button.Button(screen_w//2, screen_h//2 -100, Q5_LINEAR_img,1.25)
Q5_LINEAR_ui.rect.center = (screen_w//2, screen_h//2 -100)

#--------------------------------------

Clear_Game = pygame.image.load('CLEAR.png').convert_alpha()
Clear_Game_btn  = button.Button(screen_w//2, screen_h//2 -100, Clear_Game,1.25)
Clear_Game_btn.rect.center = (screen_w//2, screen_h//2 -100)

#define game variables
scroll = 0
tiles = math.ceil(screen_w  / bg_width) + 1

# Some shortcuts for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#-------------------------------------------------------
#Quiz for

#-------------------------------------------------------
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)



#Opening menu, 
def main_menu():

    """Draw the menu and return which page should be active next:
       'menu' (stay), 'game' (start), or 'quit' (exit)."""
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5

    #screen.blit(surface_start, surface_start_rect)

    #tittle
    tittle.rect.center = (screen_w//2,300)
    tittle.draw(screen)

    #reset scroll (said the video, or like repeat)
    if abs(scroll) > bg_width:
        scroll = 0


    # buttons
    if start_button.draw(screen):
        return 'subject'   # switch to the gamepage thingy
    if exit_button.draw(screen):
        return 'quit'   # so it quit
    
    #this one
    draw_text('Adryano presents', font, (255,255,255), screen, 450, 150)
    return 'menu'
   


def subject_page():
    # simple example game page
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   
    #spaceship 0.5
    screen.blit(spacelobby,spacelobby_rect)  

    #subject
    clicked_math = math_btn.draw(screen)
    clicked_sci  = sci_btn.draw(screen)
    if clicked_math:
        return 'math'
    if clicked_sci:
        return 'sci'

    tittle.rect.center = (screen_w//2, 250)
    tittle.draw(screen)


   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   

    # draw a random spaceship, heck yea

    pygame.draw.circle(screen, (161, 161, 161), (screen_w//2, screen_h//2 +100), 55)
    pygame.draw.circle(screen, (120,255,255), (screen_w//2, screen_h//2 +100), 20)
 


    if exit_button.draw(screen):
        return 'menu'
    
    return 'subject'  # remain on game unless an event requests change


# ----------------------------------------------

def math_page():
        # simple example game page
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    # draw_text('Math Page', title, (255,255,255), screen, 75, 60)
     
    mathematics_UI.rect.center = (screen_w//2 ,screen_h//2 -265)
    mathematics_UI.draw(screen)

    Select_UI.rect.center = (screen_w//2 ,screen_h//2 -130)
    Select_UI.draw(screen)

    clicked_Linear = Linear_btn.draw(screen)
    clicked_Sequence  = Sequence_btn.draw(screen)
    if clicked_Linear:
        return 'math_2'
    if clicked_Sequence:
        return 'math_1'

    if exit_button.draw(screen):
        return 'subject'
    return 'math'




def sci_page():
        # simple example game page
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   

    #    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    # draw_text('Science Page', title, (255,255,255), screen, 40, 40)

    Science_UI.rect.center = (screen_w//2 ,screen_h//2 -265)
    Science_UI.draw(screen)

    Select_UI.rect.center = (screen_w//2 ,screen_h//2 -130)
    Select_UI.draw(screen)

    clicked_ChemReact = ChemReact_btn.draw(screen)
    clicked_CBIO  = Climate_btn.draw(screen)
    if clicked_ChemReact:
        return 'sci_1'
    if clicked_CBIO:
        return 'sci_2'

    if exit_button.draw(screen):
        return 'subject'
    return 'sci'



# ----------------------------------------------


#Chemical reaction
def sci_1_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    # UI THINGY
    Science_UI.rect.center = (screen_w//2 ,screen_h//2 -265)
    Science_UI.draw(screen)
    ChemReact1_UI.rect.center = (screen_w//2, screen_h//2 -130)
    ChemReact1_UI.draw(screen)

    clicked_pract_sci = Pract_Sci_btn.draw(screen)
    if clicked_pract_sci:
        return 'sci_pract1'
    


    if back_button.draw(screen):
        return 'sci'
    return 'sci_1'



#Climate and biomes
def sci_2_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    # UI THINGY
    Science_UI.rect.center = (screen_w//2 ,screen_h//2 -265)
    Science_UI.draw(screen)
    Climate1_UI.rect.center = (screen_w//2, screen_h//2 -130)
    Climate1_UI.draw(screen)

    clicked_pract_sci = Pract_Sci_btn.draw(screen)
    if clicked_pract_sci:
        return 'sci_pract2'


    if back_button.draw(screen):
        return 'sci'
    return 'sci_2'



#Sequences
def math_1_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #UI THINGY
    mathematics_UI.rect.center = (screen_w//2 ,screen_h//2 -265)
    mathematics_UI.draw(screen)
    Sequence1_UI.rect.center = (screen_w//2, screen_h//2 -130)
    Sequence1_UI.draw(screen)
    clicked_pract_math = Pract_Math_btn.draw(screen )
    if clicked_pract_math:
        return 'math_pract1'

    if back_button.draw(screen):
        return 'math'
    return 'math_1'



#Linear Equations
def math_2_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #UI THINGY
    mathematics_UI.rect.center = (screen_w//2 ,screen_h//2 -265)
    mathematics_UI.draw(screen)
    Linear1_UI.rect.center = (screen_w//2, screen_h//2 -130)
    Linear1_UI.draw(screen)

    clicked_pract_math = Pract_Math_btn.draw(screen)
    if clicked_pract_math:
        return 'math_pract2'

    if back_button.draw(screen):
        return 'math'
    return 'math_2'


#-----------------------------------------------


#CHEMICAL REACTIONS (EVIDENCE)
def sci_pract1_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #UI THINGY
    
    ChemReact1_UI.rect.center = (screen_w//2 ,screen_h//2 -265)    
    ChemReact1_UI.draw(screen)
    Lesson_ChemReact_lesson1_ui.draw(screen)
    Lesson_ChemReact_lesson2_ui.draw(screen)

    # Start the practice
    start_button = button.Button(screen_w//2 +300, screen_h//2 +250, start_img, 0.75)
    start_button.rect.center = (screen_w//2 + 300, screen_h//2 +250)
    clicked_start_button = start_button.draw(screen)
    if clicked_start_button:
        return 'sci_pract1x1'

    if back_button.draw(screen):
        return 'sci_1'
    return 'sci_pract1'



def sci_pract1x_page1():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q1_ChemReact_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'sci_pract1x2'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'


    if back_button.draw(screen):
        return 'sci_1'
    return 'sci_pract1x1'


def sci_pract1x_page2():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q2_ChemReact_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'sci_pract1x3'


    if back_button.draw(screen):
        return 'sci_1'
    return 'sci_pract1x2'


def sci_pract1x_page3():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q3_ChemReact_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'sci_pract1x4'


    if back_button.draw(screen):
        return 'sci_1'
    return 'sci_pract1x3'


def sci_pract1x_page4():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q4_ChemReact_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'sci_pract1x5'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'


    if back_button.draw(screen):
        return 'sci_1'
    return 'sci_pract1x4'


def sci_pract1x_page5():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q5_ChemReact_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'CLEAR_GAME'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'


    if back_button.draw(screen):
        return 'sci_1'
    return 'sci_pract1x5'

#CLIMATE & BIOMES
def sci_pract2_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #UI THINGY
    
    Climate1_UI.rect.center = (screen_w//2 ,screen_h//2 -265)    
    Climate1_UI.draw(screen)

    Lesson_CLIBIO_lesson1_ui.draw(screen)
    Lesson_CLIBIO_lesson2_ui.draw(screen)

    # Start the practice
    start_button = button.Button(screen_w//2 +300, screen_h//2 +250, start_img, 0.75)
    start_button.rect.center = (screen_w//2 + 300, screen_h//2 +250)
    clicked_start_button = start_button.draw(screen)
    if clicked_start_button:
        return 'sci_pract2x1'

    if back_button.draw(screen):
        return 'sci_2'
    return 'sci_pract2'


def sci_pract2x_page1():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q1_CLIBIO_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'sci_pract2x2'

    if back_button.draw(screen):
        return 'sci_pract2'
    return 'sci_pract2x1'

def sci_pract2x_page2():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q3_CLIBIO_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'sci_pract2x3'

    if back_button.draw(screen):
        return 'sci_pract2'
    return 'sci_pract2x2'


def sci_pract2x_page3():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q2_CLIBIO_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'sci_pract2x4'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'

    if back_button.draw(screen):
        return 'sci_pract2'
    return 'sci_pract2x3'

def sci_pract2x_page4():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q4_CLIBIO_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'sci_pract2x5'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'

    if back_button.draw(screen):
        return 'sci_pract2'
    return 'sci_pract2x4'


def sci_pract2x_page5():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q5_CLIBIO_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'CLEAR_GAME'

    if back_button.draw(screen):
        return 'sci_pract2'
    return 'sci_pract2x5'

#SEQUENCE PRACTICE
def math_pract1_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #UI THINGY
    
    Sequence1_UI.rect.center = (screen_w//2 ,screen_h//2 -265)    
    Sequence1_UI.draw(screen)

    #Lesson

    Lesson_SEquenceAR_UI.draw(screen)
    Lesson_SEquenceGEO_UI.draw(screen)



    # Start the practice
    start_button = button.Button(screen_w//2 +300, screen_h//2 +250, start_img, 0.75)
    start_button.rect.center = (screen_w//2 + 300, screen_h//2 +250)
    
    clicked_start_button = start_button.draw(screen)
    if clicked_start_button:
        return 'math_pract1x1'
    
    if back_button.draw(screen):
        return 'math_1'
    return 'math_pract1'

def math_pract1x_page1():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q1_Sequence_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'math_pract1x2'


    if back_button.draw(screen):
        return 'math_1'
    return 'math_pract1x1'


def math_pract1x_page2():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q2_Sequence_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'math_pract1x3'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'


    if back_button.draw(screen):
        return 'math_1'
    return 'math_pract1x2'


def math_pract1x_page3():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q3_Sequence_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'math_pract1x4'


    if back_button.draw(screen):
        return 'math_1'
    return 'math_pract1x3'


def math_pract1x_page4():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q4_Sequence_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'math_pract1x5'


    if back_button.draw(screen):
        return 'math_1'
    return 'math_pract1x4'



def math_pract1x_page5():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q5_Sequence_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'CLEAR_GAME'


    if back_button.draw(screen):
        return 'math_1'
    return 'math_pract1x5'

#--------------------------------------
#LINEAR PRACTICE
def math_pract2_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #UI THINGY
    
    Linear1_UI.rect.center = (screen_w//2 ,screen_h//2 -265)    
    Linear1_UI.draw(screen)

    #Lesson
    Lesson_LEquations_UI.draw(screen)
    HowToLinear.draw(screen)

    # Start the practice
    start_button = button.Button(screen_w//2 +300, screen_h//2 +250, start_img, 0.75)
    start_button.rect.center = (screen_w//2 + 300, screen_h//2 +250)
    
    clicked_start_button = start_button.draw(screen)
    if clicked_start_button:
        return 'math_pract2x1'

    if back_button.draw(screen):
        return 'math_2'
    return 'math_pract2'



def math_pract2x_page1():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q1_LINEAR_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'math_pract2x2'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'

    if back_button.draw(screen):
        return 'math_pract2'
    return 'math_pract2x1'


def math_pract2x_page2():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q2_LINEAR_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'math_pract2x3'

    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'WRONGPAGE'

    if back_button.draw(screen):
        return 'math_pract2'
    return 'math_pract2x2'


def math_pract2x_page3():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q3_LINEAR_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'
    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'math_pract2x4'

    if back_button.draw(screen):
        return 'math_pract2'
    return 'math_pract2x3'


def math_pract2x_page4():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q4_LINEAR_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'
    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'math_pract2x5'

    if back_button.draw(screen):
        return 'math_pract2'
    return 'math_pract2x4'


def math_pract2x_page5():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #Question THINGY
    Q5_LINEAR_ui.draw(screen)

    # TRUE & FALSE
    clicked_true = True_btn.draw(screen)
    if clicked_true:
        return 'WRONGPAGE'
    clicked_false = False_btn.draw(screen)
    if clicked_false:
        return 'CLEAR_GAME'


    if back_button.draw(screen):
        return 'math_pract2'
    return 'math_pract2x5'


#--------------------------------------
#Wrong ANsar / multiversal

def WRONG_ANSWER_page():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)


    draw_text("YOU ARE WRONG", title, (255,255,255), screen, screen_w//2-300, screen_h//2 -40)
    draw_text("click back to restart", title, (255,255,255), screen, screen_w//2-325, screen_h//2 +100,)


    if back_button.draw(screen):
        return 'subject'
    return 'WRONGPAGE'

def CLEAR_GAME_YAY():
    global scroll
    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 5
   #loop 
    if abs(scroll) > bg_width:
        scroll = 0   
    
#    Background design
    overlay_dynamic = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
    overlay_dynamic.fill((128, 128, 128))  
    hole_rect = transparent_1.rect.copy()
    overlay_dynamic.fill((0, 0, 0,125), hole_rect) 
    screen.blit(overlay_dynamic, (0, 0))
    transparent_1.draw(screen)

    #this THINGY
    Clear_Game_btn.draw(screen)

    if back_button.draw(screen):
        return 'subject'
    return 'CLEAR_GAME'

#--------------------------------------

def main():
    pygame.time.delay(100)
    current_page = 'menu'
    running = True

    while running:
        
        screen.fill((202,228,241))
        # per-frame update/draw depending on current page
        if current_page == 'menu':
            next_page = main_menu()
            if next_page == 'quit':
                running = False
            else:
                current_page = next_page
                while pygame.mouse.get_pressed()[0]:
                    for _ev in pygame.event.get():
                        if _ev.type == pygame.QUIT:
                            running = False
                            break
                    clock.tick(60)
         # handle menu separately (returns next_page)
        if current_page == 'menu':
            next_page = main_menu()
            if next_page == 'quit':
                running = False
            elif next_page != current_page:
                current_page = next_page
                # wait until left mouse released so the click that opened the page
                # can't immediately trigger buttons on the new page
                while pygame.mouse.get_pressed()[0]:
                    for _ev in pygame.event.get():
                        if _ev.type == pygame.QUIT:
                            running = False
                            break
                    clock.tick(60)
        else:
            # call current page function, get a next_page string and apply same wait when it changes
            if current_page == 'subject':
                next_page = subject_page()
            elif current_page == 'math':
                next_page = math_page()
            elif current_page == 'sci':
                next_page = sci_page()

            elif current_page == 'sci_1':
                next_page = sci_1_page()
            elif current_page == 'sci_2':
                next_page = sci_2_page()
            elif current_page == 'math_1':
                next_page = math_1_page()
            elif current_page == 'math_2':
                next_page = math_2_page()


            elif current_page == 'sci_pract1':
                next_page = sci_pract1_page()   
            elif current_page == 'sci_pract1x1':
                next_page = sci_pract1x_page1()  
            elif current_page == 'sci_pract1x2':
                next_page = sci_pract1x_page2()  
            elif current_page == 'sci_pract1x3':
                next_page = sci_pract1x_page3()  
            elif current_page == 'sci_pract1x4':
                next_page = sci_pract1x_page4()  
            elif current_page == 'sci_pract1x5':
                next_page = sci_pract1x_page5()



            elif current_page == 'sci_pract2':
                next_page = sci_pract2_page()   
            elif current_page == 'sci_pract2x1':
                next_page = sci_pract2x_page1()  
            elif current_page == 'sci_pract2x2':
                next_page = sci_pract2x_page2()  
            elif current_page == 'sci_pract2x3':
                next_page = sci_pract2x_page3()  
            elif current_page == 'sci_pract2x4':
                next_page = sci_pract2x_page4()  
            elif current_page == 'sci_pract2x5':
                next_page = sci_pract2x_page5()



            elif current_page == 'math_pract1':
                next_page = math_pract1_page()   
            elif current_page == 'math_pract1x1':
                next_page = math_pract1x_page1()  
            elif current_page == 'math_pract1x2':
                next_page = math_pract1x_page2()  
            elif current_page == 'math_pract1x3':
                next_page = math_pract1x_page3()  
            elif current_page == 'math_pract1x4':
                next_page = math_pract1x_page4()  
            elif current_page == 'math_pract1x5':
                next_page = math_pract1x_page5()



            elif current_page == 'math_pract2':
                next_page = math_pract2_page()
            elif current_page == 'math_pract2x1':
                next_page = math_pract2x_page1()  
            elif current_page == 'math_pract2x2':
                next_page = math_pract2x_page2()  
            elif current_page == 'math_pract2x3':
                next_page = math_pract2x_page3() 
            elif current_page == 'math_pract2x4':
                next_page = math_pract2x_page4()
            elif current_page == 'math_pract2x5':
                next_page = math_pract2x_page5() 


            elif current_page == 'sci_pract1':
                next_page = sci_pract1_page()
            elif current_page == 'sci_pract2':
                next_page = sci_pract2_page()

             
            elif current_page == 'WRONGPAGE':
                next_page = WRONG_ANSWER_page()  
            elif current_page == 'CLEAR_GAME':
                next_page = CLEAR_GAME_YAY()    
            else:
                next_page = current_page

            if next_page != current_page:
                current_page = next_page
                # wait for mouse release to avoid bleed-through clicks
                while pygame.mouse.get_pressed()[0]:
                    for _ev in pygame.event.get():
                        if _ev.type == pygame.QUIT:
                            running = False
                            break
                    clock.tick(60)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 0:
                    start_button.clicked = False
                    exit_button.clicked = False
                    back_button.clicked = False
                    True_btn.clicked = False
                    False_btn.clicked = False


                   
                    

        pygame.display.update() 
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()



    











