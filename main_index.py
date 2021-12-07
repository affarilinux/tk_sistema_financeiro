                              # bibliotecas tkinter
import tkinter as tk
from tkinter import *

                                 # diretorio do app
from janela.principal.composicao_principal import (
    TAMANHO_WIDTH_JANELA, MENUS_WIDTH, MENU_Y, MENU_HEIGHT, 
    COR_FUNDO_JANELA, COR_FUNDO_BOTAO_MENU_BAR, COR_ESCRITA_MENU_BAR
)


################################################### função principal
                          # função de inicialização
def main():
    root = tk.Tk() # create a Tk root window
    
                                   # função chamada
    centralizador_janela (root)
    nome_igreja_fisica   (root)
    menu_bar = MenuWidget          (root)

                          # configurações da janela
    root.title      ("NOVA ALIANÇA")               # titulo da igreja
    root.iconbitmap ("imagem/ico.ico")             # ico
    root.configure(bg=COR_FUNDO_JANELA)                   # cor da fundo janela


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
                                bg   = "#00BFFF",  # cor de fundo -DeepSkyBlue

                                text = "ABBA PAI", 
                                font ='Helvetica 20 bold', # negrito

                                relief      ="ridge", # formato da borda
                                borderwidth = 5       # tamanho da borda
    )      
                                
    nome_instituicao.place(x = 0, y = 758, width = TAMANHO_WIDTH_JANELA,
                             height = 40
    )


############################################### menus da janela principal
class MenuWidget ():


    def __init__(self,root):
        
                                       # label fixa
        self.MENU_PROCESSOS = Label ( root,
                                        # cor Aqua / Cyan
                                        bg     = "#00FFFF", 
                                        # formato da borda
                                        relief = "groove"  
        )

        self.MENU_PROCESSOS.place(x = 2, y = 5, width = (
                                    TAMANHO_WIDTH_JANELA - 4),
                                    height = 30
        )

        self.botao_1home = Button ( root,
                                    # cor botao
                                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                                    text    = "HOME",
                                    # negrito
                                    font    ='Helvetica 10 bold', 
                                    # cor escrita
                                    fg      = COR_ESCRITA_MENU_BAR, 
                                    # chamada         
                                    command = self.botao_home           

        )

        self.botao_1home. place(x=30, y = MENU_Y, width=MENUS_WIDTH, 
                                height=MENU_HEIGHT
        )

        self.botao_2configuracao = Button ( root,
                                            # cor botao
                                            bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                                            text    = "CONFIGURAÇÕES",
                                            # negrito
                                            font    ='Helvetica 10 bold', 
                                            # cor escrita
                                            fg      = COR_ESCRITA_MENU_BAR,    
                                            # chamada       
                                            command = self.botao_configuracao   

        )

        self.botao_2configuracao. place(x=190, y = MENU_Y, width=MENUS_WIDTH, 
                                         height=MENU_HEIGHT
        )


    ###############################################
                                     # funções base
    def botao_home(self):
        self.destruir_configuracao()

    def botao_configuracao(self):
        
        self.LABEL_BANCO_INSTITUICAO_fixa = Label (
                                                    # cor botao
                                                    bg      = COR_FUNDO_JANELA,
                                                    text    = "NOME DO TEMPLO:",
                                                    # negrito
                                                    font    ='Helvetica 10 bold', 

        )

        self.LABEL_BANCO_INSTITUICAO_fixa.place(x= 20, y=60, width=140, 
                                                height= 20

        )

        self.entry_banco_instituicao = Entry(
                                            # negrito
                                            font    ='Helvetica 10', 
        )

        self.entry_banco_instituicao.place(
                                            x=20, y= 85, width= 200, height= 25
        )

        self.botao_salvar_instituicao = Button ( 
                                                # cor botao - SlateBlue
                                                bg      = "#6A5ACD",          
                                                text    = "SALVAR",
                                                # negrito
                                                font    ='Helvetica 20 bold', 
                                                # cor escrita - Yellow
                                                fg      = COR_ESCRITA_MENU_BAR          
                                                #command = botao_configuracao   # chamada

        )

        self.botao_salvar_instituicao. place(x=240, y = 80, width=150, 
                                            height=35
        )
    

    ###############################################
                        # funções destruição widget
    def destruir_configuracao(self):
           
            self.LABEL_BANCO_INSTITUICAO_fixa.destroy()
            self.entry_banco_instituicao.destroy()
            self.botao_salvar_instituicao.destroy()


###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()