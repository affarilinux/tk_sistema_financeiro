
                              # bibliotecas tkinter
from tkinter    import *

import tkinter  as tk
import sqlite3


                                 # diretorio do app
from janela.principal.composicao_principal import (
    TAMANHO_WIDTH_JANELA, MENUS_WIDTH, MENU_Y, MENU_HEIGHT, 
    COR_FUNDO_JANELA, COR_FUNDO_BOTAO_MENU_BAR, COR_ESCRITA_MENU_BAR,
    NOME_NOVA_ALIANCA, COR_BOTAO_FUNDO, CONFIGURACAO_BOTAO_INSTITUICAO_X,
    CONFIGURACAO_BOTAO_INSTITUICAO_Y, CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH,
    CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT, CONFIGURACOES_INSTITUICAO_L2_SALVAR,
    CONFIGURACOES_INSTITUICAO_L2_ATUALIZAR
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
        
    def funcao_class_barra_menus(self):        # funcao inicializacao

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
class BarraMenusState():

    #configurações
    def funcao_class_desativar_botao_barra_configuracoes(self):
        
        # desativa botao
        self.botao_2configuracao["state"] = "disabled"

    def funcao_class_ativar_botao_barra_configurações(self):

        self.botao_2configuracao["state"] ="normal"


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

        self.sql_cursorr.execute(""" 
            CREATE TABLE IF NOT EXISTS Processos (ID_processos PRIMARY KEY,
                                                    boleano  BOOLEAN)
            """)

    def funcao_classdb_commit(self):
        self.sql_connect.commit()

    ############################################### deconectar
    def funcao_classdb_desconectar(self):

        self.sql_connect.close()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BancoExecucao():

    ############################################### inserir if none
    def funcao_classdb_inserir_nova_alianca(self):
                           
        self.sql_cursorr.execute( "INSERT INTO Instituicao VALUES (1, '"+NOME_NOVA_ALIANCA+"')")
        self.funcao_classdb_commit()
    
    def funcao_db_inserir_instituicao_linha2_none (self):
        
        self.sql_cursorr.execute( "INSERT INTO Instituicao VALUES (2, '"+NOME_NOVA_ALIANCA+"')")
        self.funcao_classdb_commit()

    def funcao_cursorrdb_inserir_thue(self):

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (1, 'Thue')")
        self.funcao_classdb_commit()

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (2, '"+CONFIGURACOES_INSTITUICAO_L2_SALVAR+"')")
        self.funcao_classdb_commit()

    ############################################### visualizar dados None
    def funcao_classdb_visualizar_1 (self):

        self.sql_cursorr.execute( "SELECT nome_igreja FROM Instituicao WHERE cod = 1")
        self.visualiza = self.sql_cursorr.fetchone()

        if self.visualiza == None:

            self.funcao_classdb_inserir_nova_alianca()

    def funcao_db_visualiza_instituicao_linha2(self):

        self.sql_cursorr.execute( "SELECT nome_igreja FROM Instituicao WHERE cod = 2")
        self.visualiza_L2 = self.sql_cursorr.fetchone()

        if self.visualiza == None:

            self.funcao_db_inserir_instituicao_linha2_none ()

    def funcao_db_visualiar_tbprocessos (self):

        self.sql_cursorr.execute("SELECT boleano FROM Processos WHERE ID_processos = 1 ")
        self.visualiza_processos = self.sql_cursorr.fetchone()

        if self.visualiza_processos == None:

            self.funcao_cursorrdb_inserir_thue()

    def funcao_db_visualiza_tbprocessos_linha2(self):

        self.sql_cursorr.execute("SELECT boleano FROM Processos WHERE ID_processos =2 ")
        self.visualiza_processos_L2 = self.sql_cursorr.fetchone()

    ############################################### processos
    def funcao_class_visualdb_instituicao (self):

        for visual_nome in self.visualiza:
                            
            self.label_nome_instituicao_class.configure(text=visual_nome)

    def funcao_db_conectar_e_visualizar_1(self):

        self.funcao_classdb_conectar()
        self.funcao_classdb_visualizar_1()

    
    ############################################### upgrade
    def funcao_db_update_tbprocessos_linha1(self):

        self.funcao_classdb_conectar()
        self.sql_cursorr.execute("UPDATE Processos SET boleano = 'Thue' WHERE ID_processos = 1 " )
        self.funcao_classdb_commit()
        self.funcao_classdb_desconectar()

    def funcao_db_update_tbinstituicao_linha2(self):

        self.sql_cursorr.execute("UPDATE Instituicao SET  nome_igreja = '"+self.destroir_banco_1+"' WHERE cod = 2 " )
        self.funcao_classdb_commit()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class barraVisualizarNomeInstituicao():

    def funcao_class_barra_instituicao(self):      # funcao inicializacao

        #visual
        self.funcao_class_visual_instituicao()

        self.funcao_class_visualdb_barra_intituicao()

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

    def funcao_class_visualdb_barra_intituicao(self):

        self.funcao_db_conectar_e_visualizar_1()
        self.funcao_class_visualdb_instituicao()
        self.funcao_classdb_desconectar()

        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BarraMenuHome():                             

    def funcao_class_menu_home(self):              #  inicializacao botao

        ###########################################
                                  # destruir widget
        self.funcao_class_if_destruir_widget()

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


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class ConfiguracaoWidgetDaBarraSSalvar():

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

          

    def funcao_instituicao_entry_buton(self):

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

        self.funcao_classdb_conectar()
        
        self.sql_cursorr.execute("UPDATE Processos SET boleano = '"+CONFIGURACOES_INSTITUICAO_L2_SALVAR+"' WHERE ID_processos = 2 " )
        self.funcao_classdb_commit()
        
        self. funcao_classdb_desconectar()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class ConfiguracoesBancoSSalvar():                 

    def funcao_classdb_atalizar_igreja_configuracoes(self):  # botao salvar
        
        self.funcao_classdb_conectar()

        get_entrada_instituicao = str(self.entry_banco_instituicao.get())
       
        
        if get_entrada_instituicao == "":
            
            self.funcao_db_visualiar_tbprocessos()

            visualiza_V_F = self.visualiza_processos[0]

            if  visualiza_V_F == 'Thue':

                self.funcao_label_fixa_erro_instituicao()
                self.LABEL_INSTITUICAO_FIXA_ERRO.after(4000, self.funcao_destruir_erro)

                self.sql_cursorr.execute("UPDATE Processos SET boleano = 'False' WHERE ID_processos = 1 " )
                self.funcao_classdb_commit()

        else:
        
            self.sql_cursorr.execute("UPDATE Instituicao SET nome_igreja ='"+get_entrada_instituicao+"' WHERE cod = 1")
            self.funcao_classdb_commit()

            self.funcao_db_update_tbprocessos_linha1()

        self. funcao_classdb_desconectar()

        #self.funcao_destruir_configuracao_entry_salvar()
       
        self.funcao_class_visualdb_leitura_alianca()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class ConfiguracoesProcessosBarraSSalvar():

    def funcao_class_menu_configuracao(self):       #funcao inicializacao configurações

        ###########################################
                                  # destruir widget
        self.funcao_class_destruir_home()

        ###########################################
                                    # ativar widget
        self.funcao_class_visualdb_leitura_alianca()
        self.funcao_label_fixa_configuracao()
        
        self.funcao_class_desativar_botao_barra_configuracoes()
        

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class ConfiguracaoDestruirWidgetSSalvar():

    #def funcao_destruir_configuracao_entry_salvar(self):

        #self.entry_banco_instituicao.destroy()

        #self.botao_salvar_instituicao.destroy()

################################################### if-else  home
    def funcao_class_if_destruir_widget(self):

        self.LABEL_BANCO_INSTITUICAO_FIXA.destroy() #Varivel fixa

        self.funcao_db_conectar_e_visualizar_1()
        self.destroir_banco_1 = self.visualiza [0]

        self.funcao_db_visualiza_instituicao_linha2()
        destruir_banco_2 = self.visualiza_L2 [0]
        
        
        if self.destroir_banco_1 != destruir_banco_2: 
            print(2)
            
            self.funcao_db_update_tbinstituicao_linha2()
            self.funcao_destruir_atalizar_label()

        elif self.destroir_banco_1 == destruir_banco_2: 
            print(1)
            
            #self.funcao_destruir_configuracao_entry_salvar()
                    
        self.funcao_classdb_desconectar()

    def funcao_destruir_erro(self):

        self.LABEL_INSTITUICAO_FIXA_ERRO.destroy()

        self.funcao_db_update_tbprocessos_linha1()


class ConfiguracoesWidgetIntermediario():

    ###############################################  processo verificacao
    def funcao_if_widget_intermediario_salvar_atualizar(self):

        self.transfomar_str_nome = self.visualiza[0]
        
        if self.transfomar_str_nome != NOME_NOVA_ALIANCA:
            
            self.funcao_class_institucao_atualizar_widget()
        
        elif self.transfomar_str_nome == NOME_NOVA_ALIANCA:
           
            self.funcao_instituicao_entry_buton()

    def funcao_if_widget_intermediario_atualizar_salvar(self):

        self.funcao_destruir_atalizar_label()
        
        self.funcao_instituicao_entry_buton()


class ConfiguracoesBancoIntermediario():

    def funcao_class_visualdb_leitura_alianca(self):

        self.funcao_db_conectar_e_visualizar_1()
        self.funcao_if_widget_intermediario_salvar_atualizar()   
        self.funcao_classdb_desconectar()


class ConfiguracaoWidgetDaBarraAAtualizar():

    def funcao_class_institucao_atualizar_widget(self):

        self.label_nome_instituicao_atualizar = Label ( bg = '#A9A9A9',
                                            text= self.transfomar_str_nome,
                                            font= 'Helvetica 11 bold'
        )
            
        self.label_nome_instituicao_atualizar.place( x=20, y= 85, width= 200, height= 25)

        self.botao_atualizar_instituicao_atualizar = Button ( 
                                                # cor botao - 
                                                bg      = COR_BOTAO_FUNDO,          
                                                text    = "ATUALIZAR",
                                                # negrito
                                                font    ='Helvetica 15 bold', 
                                                # cor escrita - Yellow
                                                fg      = COR_ESCRITA_MENU_BAR,        
                                                # chamada  
                                                command = self.funcao_if_widget_intermediario_atualizar_salvar

        )

        self.botao_atualizar_instituicao_atualizar. place(x=CONFIGURACAO_BOTAO_INSTITUICAO_X, 
                                            y = CONFIGURACAO_BOTAO_INSTITUICAO_Y, 
                                            width=CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH, 
                                            height=CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT
        )

        self.funcao_classdb_conectar()

        self.sql_cursorr.execute("UPDATE Processos SET boleano = '"+CONFIGURACOES_INSTITUICAO_L2_ATUALIZAR+"' WHERE ID_processos = 2 " )
        self.funcao_classdb_commit()

        self.funcao_classdb_desconectar()
class ConfiguracaoDestruirWidgetAAtualizar():
    
    def funcao_destruir_atalizar_label(self):

        self.label_nome_instituicao_atualizar.destroy()
        self.botao_atualizar_instituicao_atualizar.destroy()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
############################################### menus da janela principal
class MenuWidget ( ClassBanco,barraVisualizarNomeInstituicao, BarraMenuHome,
                   BarraMenuInicializacao, ConfiguracoesProcessosBarraSSalvar,
                   ConfiguracaoDestruirWidgetSSalvar, ConfiguracaoWidgetDaBarraSSalvar,
                   ConfiguracoesBancoSSalvar, BarraMenusState,BancoExecucao,
                   ConfiguracaoWidgetDaBarraAAtualizar, ConfiguracoesWidgetIntermediario,
                   ConfiguracoesBancoIntermediario, ConfiguracaoDestruirWidgetAAtualizar
                   ):

    #**********************************************
    ###############################################       função inicial
    def __init__(self):

        self.funcao_criar_tabela()
        ########################################### classe externa
        self.funcao_class_barra_menus()
        self.funcao_class_barra_instituicao()   

    def funcao_criar_tabela(self):
        
        self.funcao_classdb_conectar()
        self.funcao_classdb_criar_tabela()   
        self.funcao_classdb_visualizar_1()  
        self.funcao_db_visualiza_instituicao_linha2()
        self.funcao_db_visualiar_tbprocessos()
        self.funcao_db_update_tbprocessos_linha1()
        self.funcao_classdb_desconectar()


#**************************************************
###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()