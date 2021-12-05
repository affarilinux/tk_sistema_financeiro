                              # bibliotecas tkinter
import tkinter as tk
from tkinter import *

                          # função de inicialização
def main():
    root = tk.Tk() # create a Tk root window
    
                                   # função chamada
    centralizador_janela(root)
    nome_igreja_fisica(root)

                          # configurações da janela
    root.title("NOVA ALIANÇA")
    root.iconbitmap("ico.ico")


    ###############################################
    root.mainloop() # starts the mainloop

                               # centralizar janela
def centralizador_janela(root):

    WIDTH = 1000 # width for the Tk root
    HEIGHT = 800 # height for the Tk root

    # get screen width and height
    WS = root.winfo_screenwidth() # width of the screen
    HS = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    CALCULO_X = (WS/2) - (WIDTH/2)
    CALCULO_Y = (HS/2) - (HEIGHT/2)

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, CALCULO_X, CALCULO_Y))
               
                                   # nome da igreja
# base inferior do grafico
def nome_igreja_fisica(root):

    nome_instituicao = Label (root, 
                                bg = "#00008B")

    nome_instituicao.pack()

###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()