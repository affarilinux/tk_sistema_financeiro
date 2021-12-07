                              # bibliotecas tkinter
import tkinter as tk
from tkinter import *

                                 # diretorio do app
from janela.principal.composicao_principal import (
    TAMANHO_WIDTH_JANELA
)


################################################### função principal
                          # função de inicialização
def main():
    root = tk.Tk() # create a Tk root window
    
                                   # função chamada
    centralizador_janela (root)
    nome_igreja_fisica   (root)
    menu_widget          (root)

                          # configurações da janela
    root.title      ("NOVA ALIANÇA")               # titulo da igreja
    root.iconbitmap ("imagem/ico.ico")             # ico
    root.configure(bg='#C0C0C0')                   # cor da fundo janela


    ###############################################
    root.mainloop() # starts the mainloop


############################################## funções controle da janela
                               # centralizar janela
def centralizador_janela(root):

    WIDTH = TAMANHO_WIDTH_JANELA # width for the Tk root
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


################################################ base inferior do grafico    
                         # nome da igreja
def nome_igreja_fisica(root):

    nome_instituicao = Label (root, 
                                bg   = "#00BFFF",  # cor de fundo

                                text = "ABBA PAI", 
                                font ='Helvetica 20 bold', # negrito

                                relief      ="ridge", # formato da borda
                                borderwidth = 5       # tamanho da borda
    )      
                                
    nome_instituicao.place(x = 0, y = 758, width = TAMANHO_WIDTH_JANELA,
                             height = 40
    )


############################################### menus da janela principal
def menu_widget (root):

                                       # label fixa
    menu_processos = Label ( root,
                             bg = "#00FFFF",
                             relief = "groove"     # formato da borda
    )

    menu_processos.place(x = 2, y = 5, width = (TAMANHO_WIDTH_JANELA - 4),
                          height = 30
      )

def nome_da_instituicao():
    print("ola")
    
###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()