                              # bibliotecas tkinter
from tkinter    import *
from time       import sleep

import tkinter  as tk
import sqlite3


                                 # diretorio do app
from janela.principal.composicao_principal import (
    TAMANHO_WIDTH_JANELA, MENUS_WIDTH, MENU_Y, MENU_HEIGHT, 
    COR_FUNDO_JANELA, COR_FUNDO_BOTAO_MENU_BAR, COR_ESCRITA_MENU_BAR,
    NOME_NOVA_ALIANCA, COR_BOTAO_FUNDO, CONFIGURACAO_BOTAO_INSTITUICAO_X,
    CONFIGURACAO_BOTAO_INSTITUICAO_Y, CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH,
    CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT
)

################################################### função principal
                          # função de inicialização
def main():
    root = tk.Tk() # create a Tk root window
    
                                   # função chamada
    centralizador_janela (root)
    menu_bar = MenuWidget()

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

    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
###################################################
class BarraMenuInicializacao():
        
    def funcao_class_barra_menus(self):            # funcao inicializacao

        ###########################################            label fixa
                                        
        self.MENU_PROCESSOS_BARRA_FIXO = Label ( 
                                                # cor Aqua / Cyan
                                                bg     = "#00FFFF", 
                                                # formato da borda
                                                relief = "groove"  
        )

        self.MENU_PROCESSOS_BARRA_FIXO.place(x = 2, y = 5, width = (
                                            TAMANHO_WIDTH_JANELA - 4),
                                        height = 30
        )

        ###########################################        variavel movel
        self.botao_1home = Button (
                                    # cor botao
                                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                                    text    = "HOME",
                                    # negrito
                                    font    ='Helvetica 10 bold', 
                                    # cor escrita
                                    fg      = COR_ESCRITA_MENU_BAR, 
                                    # chamada         
                                    command = self.funcao_class_menu_home           

        )

        self.botao_1home. place(x=30, y = MENU_Y, width=MENUS_WIDTH, 
                                height=MENU_HEIGHT
        )

        self.botao_2configuracao = Button (
                                            # cor botao
                                            bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                                            text    = "CONFIGURAÇÕES",
                                            # negrito
                                            font    ='Helvetica 10 bold', 
                                            # cor escrita
                                            fg      = COR_ESCRITA_MENU_BAR,    
                                            # chamada       
                                            command = self.funcao_class_menu_configuracao  

        )

        self.botao_2configuracao. place(x=190, y = MENU_Y, width=MENUS_WIDTH, 
                                         height=MENU_HEIGHT
        )


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class ClassBanco():
    
    ############################################### conectar
    def funcao_classdb_conectar(self):

        self.sql_connect = sqlite3.connect("banco_de_dados/sistema_financeiro.db")
        self.sql_cursorr = self.sql_connect.cursor()
    
    ############################################### criar tabela
    def funcao_classdb_criar_tabela(self):

        self.sql_cursorr.execute("""
            CREATE TABLE IF NOT EXISTS Instituicao ( cod INTEGER PRIMARY KEY,
                                                    nome_igreja TEXT

            )
             """)

    def funcao_classdb_commit(self):
        self.sql_connect.commit()

    ############################################### deconectar
    def funcao_classdb_desconectar(self):

        self.sql_connect.close()

    ############################################### inserir dados
    def funcao_classdb_inserir_nova_alianca(self):
                           
            
        self.sql_cursorr.execute( "INSERT INTO Instituicao VALUES (1, '"+NOME_NOVA_ALIANCA+"')")
        self.funcao_classdb_commit()

    def funcao_classdb_atalizar_igreja_configuracoes(self):

        
        self.funcao_classdb_conectar()

        get_entrada_instituicao = self.entry_banco_instituicao.get()
        maiuscula_instituicao = str(get_entrada_instituicao.upper())
        
        if maiuscula_instituicao == "":

            self.funcao_label_fixa_erro_instituicao()
            
            self.LABEL_INSTITUICAO_FIXA_ERRO.after(7000, self.funcao_destruir_erro)

        else:
        
            self.sql_cursorr.execute("UPDATE Instituicao SET nome_igreja ='"+maiuscula_instituicao+"' WHERE cod = 1")
            self.funcao_classdb_commit()

        self. funcao_classdb_desconectar( )

        self.funcao_destruir_configuracao_entry_instituicao()
        self.funcao_destruir_configuracao_botao_salvar_igreja() 
        
        self.funcao_class_visualdb_leitura_alianca()

    ############################################### visualizar dados
    def funcao_classdb_visualizar_1 (self):

        self.sql_cursorr.execute( "SELECT nome_igreja FROM Instituicao WHERE cod = 1")
        self.visualiza = self.sql_cursorr.fetchone()

        if self.visualiza == None:

            self.funcao_classdb_inserir_nova_alianca()

    def funcao_class_visualdb_instituicao (self):

        for visual_nome in self.visualiza:
                            
            self.label_nome_instituicao_class.configure(text=visual_nome)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class barraVisualizarNomeInstituicao():

    def funcao_class_barra_instituicao(self):      # funcao inicializacao

        #visual
        self.funcao_class_visual_instituicao()

        # banco
        self.funcao_classdb_conectar()
        self.funcao_classdb_criar_tabela()                   
        self.funcao_classdb_visualizar_1() 
        self.funcao_classdb_desconectar()

        self.funcao_nome_instituicao_db()

    def funcao_class_visual_instituicao(self):     # funcao inicializacao

        self.label_nome_instituicao_class = Label (
                                        # cor de fundo -DeepSkyBlue
                                        bg   = "#00BFFF",  

                                        # negrito
                                        font ='Helvetica 20 bold', 

                                        # formato da borda
                                        relief      ="ridge", 
                                        # tamanho da borda
                                        borderwidth = 5       
        )      
                                
        self.label_nome_instituicao_class.place(x = 0, y = 758, 
                                        width = TAMANHO_WIDTH_JANELA,
                                        height = 40
        )
    
    def funcao_nome_instituicao_db(self):

        self.funcao_classdb_conectar()
        self.funcao_classdb_visualizar_1() 
        self.funcao_class_visualdb_instituicao()
        self.funcao_classdb_desconectar()

    def funcao_class_visualdb_barra_intituicao(self):

        self.funcao_classdb_conectar()
        self.funcao_classdb_visualizar_1()
        self.funcao_class_visualdb_instituicao()
        self.funcao_classdb_desconectar()

        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BarraMenuHome():                             

    def funcao_class_menu_home(self):              #  inicializacao botao

        ###########################################
                                  # destruir widget
        self.funcao_class_destruir_conguracao_instituicao()

        ###########################################
                                    # ativar widget
        self.funcao_class_visual_instituicao()
        
        # ativar configurações barra
        self.funcao_class_ativar_botao_barra_configurações()

        # funcao barra inferior visualizar
        self.funcao_class_visualdb_barra_intituicao()

    ################################################ chamar botao
    #configuracao
    def funcao_class_destruir_home(self):          

        self.label_nome_instituicao_class.destroy()

    def funcao_class_destruir_conguracao_instituicao(self):
        
        self.LABEL_BANCO_INSTITUICAO_FIXA.destroy()
         
        #função
        self.funcao_class_if_destruir_widget()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class ConfiguracaoWidgetDaBarra():

    def funcao_label_fixa_erro_instituicao(self):

        self.LABEL_INSTITUICAO_FIXA_ERRO = Label (
                                                    # cor botao
                                                    bg      = COR_FUNDO_JANELA,
                                                    text    = "DIGITE O NOME DE SEU TEMPLO",
                                                    # negrito
                                                    font    ='Helvetica 11 bold', 

        )

        self.LABEL_INSTITUICAO_FIXA_ERRO.place(x= 20, y=120, width= 250, 
                                                height= 20

        )

        #sleep(5)

        #self.LABEL_INSTITUICAO_FIXA_ERRO.destroy( )
    def funcao_label_fixa_configuracao(self):

        self.LABEL_BANCO_INSTITUICAO_FIXA = Label (
                                                    # cor botao
                                                    bg      = COR_FUNDO_JANELA,
                                                    text    = "NOME DO TEMPLO:",
                                                    # negrito
                                                    font    ='Helvetica 10 bold', 

        )

        self.LABEL_BANCO_INSTITUICAO_FIXA.place(x= 20, y=60, width=140, 
                                                height= 20

        )

          

    def funcao_salvar_instituicao_widget(self):

        self.entry_banco_instituicao = Entry(
                                            
                                            font    ='Helvetica 10', 
        )

        self.entry_banco_instituicao.place(
                                            x=20, y= 85, width= 200, height= 25
        )

        self.botao_salvar_instituicao = Button ( 
                                                # cor botao 
                                                bg      = COR_BOTAO_FUNDO,          
                                                text    = "SALVAR",
                                                # negrito
                                                font    ='Helvetica 20 bold', 
                                                # cor escrita - Yellow
                                                fg      = COR_ESCRITA_MENU_BAR,        
                                                # chamada  
                                                command = self.funcao_classdb_atalizar_igreja_configuracoes

        )

        self.botao_salvar_instituicao. place(x=CONFIGURACAO_BOTAO_INSTITUICAO_X, 
                                            y = CONFIGURACAO_BOTAO_INSTITUICAO_Y,
                                            width= CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH, 
                                            height= CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT
        )

    def funcao_class_institucao_atualizar_widget(self):

        self.label_nome_instituicao = Label (
                                            text= self.transfomar_str_nome,
                                            font= 'Helvetica 11 bold'
        )
            
        self.label_nome_instituicao.place( x=20, y= 85, width= 200, height= 25)

        self.botao_atualizar_instituicao = Button ( 
                                                # cor botao - 
                                                bg      = COR_BOTAO_FUNDO,          
                                                text    = "ATUALIZAR",
                                                # negrito
                                                font    ='Helvetica 15 bold', 
                                                # cor escrita - Yellow
                                                fg      = COR_ESCRITA_MENU_BAR,        
                                                # chamada  
                                                #command = self.salvar_nome_instituicao

        )

        self.botao_atualizar_instituicao. place(x=CONFIGURACAO_BOTAO_INSTITUICAO_X, 
                                            y = CONFIGURACAO_BOTAO_INSTITUICAO_Y, 
                                            width=CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH, 
                                            height=CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT
        )


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BarraMenuConfiguracoes():

    def funcao_class_menu_configuracao(self):       #funcao inicializacao

        ###########################################
                                  # destruir widget
        self.funcao_class_destruir_home()

        ###########################################
                                    # ativar widget
        self.funcao_class_visualdb_leitura_alianca()
        self.funcao_label_fixa_configuracao()
        
        self.funcao_class_desativar_botao_barra_configuracoes()
        
    
    def funcao_class_visualdb_leitura_alianca(self):

        self.funcao_classdb_conectar()
        self.funcao_classdb_visualizar_1()
        self.funcao_class_if_ativar_widget()   
        self.funcao_classdb_desconectar()

    ############################################### ativado e desativado
    def funcao_class_desativar_botao_barra_configuracoes(self):
        
        # desativa botao
        self.botao_2configuracao["state"] = "disabled"

    def funcao_class_ativar_botao_barra_configurações(self):

        self.botao_2configuracao["state"] ="normal"

    ###############################################  processo verificacao
    def funcao_class_if_ativar_widget(self):

        self.transfomar_str_nome = self.visualiza[0]
        
        if self.transfomar_str_nome != NOME_NOVA_ALIANCA:
            
            self.funcao_class_institucao_atualizar_widget()
        
        elif self.transfomar_str_nome == NOME_NOVA_ALIANCA:
           
            self.funcao_salvar_instituicao_widget()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class DestruirWidgetConfiguracao():

    def funcao_destruir_configuracao_entry_instituicao(self):

        self.entry_banco_instituicao.destroy()

    def funcao_destruir_configuracao_botao_salvar_igreja(self):

        self.botao_salvar_instituicao.destroy()

################################################### if-else
    def funcao_class_if_destruir_widget(self):
        
        self.funcao_classdb_conectar()
        self.funcao_classdb_visualizar_1()

                
        destroir_banco_1 = self.visualiza[0]
        
        if destroir_banco_1 != NOME_NOVA_ALIANCA: 
                  
            self.label_nome_instituicao.destroy()
            self.botao_atualizar_instituicao.destroy()

        elif destroir_banco_1 == NOME_NOVA_ALIANCA:
            
            self.funcao_destruir_configuracao_entry_instituicao()
            self.funcao_destruir_configuracao_botao_salvar_igreja()          

        self.funcao_classdb_desconectar()

    def funcao_destruir_erro(self):
        self.LABEL_INSTITUICAO_FIXA_ERRO.destroy()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
############################################### menus da janela principal
class MenuWidget ( ClassBanco,barraVisualizarNomeInstituicao, BarraMenuHome,
                   BarraMenuInicializacao, BarraMenuConfiguracoes,
                   DestruirWidgetConfiguracao, ConfiguracaoWidgetDaBarra):

    #**********************************************
    ###############################################       função inicial
    def __init__(self):

        ########################################### classe externa
        self.funcao_class_barra_menus()
        self.funcao_class_barra_instituicao()   

    '''def a(self,):
        root.after(5000,self.pi)
    def pi():
        print('certo')'''

#**************************************************
###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()