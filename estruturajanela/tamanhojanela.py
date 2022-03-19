from janela.principal import TAMANHO_WIDTH_JANELA
from janela.principal import TAMANHO_HEIGHT_JANELA

#from main_index import root

def centralizador_janela(root):

    WIDTH = TAMANHO_WIDTH_JANELA # width for the Tk root
    HEIGHT = TAMANHO_HEIGHT_JANELA # height for the Tk root

# get screen width and height
    WS = root.winfo_screenwidth() # width of the screen
    HS = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
    CALCULO_X = (WS/2) - (WIDTH/2)
    CALCULO_Y = (HS/2) - (HEIGHT/2)

    root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, CALCULO_X, CALCULO_Y))

    acf = root
    # set the dimensions of the screen 
    # and where it is placed
    
    