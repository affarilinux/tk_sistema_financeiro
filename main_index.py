
                              # bibliotecas tkinter
from tkinter    import *

import tkinter  as tk
import sqlite3


                                 # diretorio do app
from janela.principal.composicao_principal import (
    CADASTRO_FRAME1HEIGHT, CADASTRO_FRAME1WIGHT, CADASTRO_FRAME1X, CADASTRO_FRAME2Y, TAMANHO_WIDTH_JANELA, TAMANHO_HEIGHT_JANELA,

    MENUS_WIDTH, MENU_Y, MENU_HEIGHT, 

    COR_FUNDO_JANELA, COR_FUNDO_BOTAO_MENU_BAR, COR_BOTAO_FUNDO, COR_FUNDO_1,
    COR_FUNDO_2,

    COR_ESCRITA_MENU_BAR, COR_ESCRITA1,

    NOME_NOVA_ALIANCA, 

    CONFIGURACAO_BOTAO_INSTITUICAO_X, CONFIGURACAO_BOTAO_INSTITUICAO_Y, 
    CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH, CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT,

    CONFIGURACAO_ENTRYX, CONFIGURACAO_ENTRYY, CONFIGURACAO_ENTRYWIDGET, 
    CONFIGURACAO_ENTRYHEIGHT,

    DB_THUE, DB_FALSE,DB_SALVAR, DB_ATUALIZAR,

    DB_0, DB_1, DB_2, DB_3, DB_4, DB_5, DB_6, 

    WIDGET_2, WIDGET_4,

    CADASTRO_FRAME1X, CADASTRO_FRAME1WIGHT, CADASTRO_FRAME1HEIGHT,

    CADASTRO_FRAME2Y, CADASTRO_FRAME2W, CADASTRO_FRAME2H
     
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
    HEIGHT = TAMANHO_HEIGHT_JANELA # height for the Tk root

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

        """fixo"""
        ###########################################            label fixa
                                        
        self.MENU_PROCESSOS_BARRA_FIXO = Label ( 
                    # cor Aqua / Cyan
                    bg     = "#00FFFF", 
                    # formato da borda
                    relief = "groove"  
        )

        self.MENU_PROCESSOS_BARRA_FIXO.place(
                    x = WIDGET_2, y = 5, 

                    width = TAMANHO_WIDTH_JANELA - WIDGET_4,
                    height = 35
        )

        """botoes chamada da estrutura"""
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
                    command = self.funcao_command_menu_home           

        )

        self.botao_1home. place(
                    x=100, y = MENU_Y, 

                    width=MENUS_WIDTH, height=MENU_HEIGHT
        )

        self.botao_2projetos = Button(
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "PROJETOS",
                    # negrito
                    font    ='Helvetica 10 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR,
                    command = self.funcao_command_projeto
        )

        self.botao_2projetos.place(
                    x=290, y = MENU_Y, 

                    width=MENUS_WIDTH, height=MENU_HEIGHT
        )

        self.botao_3recursos = Button(
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "RECURSOS",
                    # negrito
                    font    ='Helvetica 10 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR,
                    command= self.funcao_command_recurso
        )

        self.botao_3recursos.place(
                    x=490, y = MENU_Y, 
                        
                    width=MENUS_WIDTH, height=MENU_HEIGHT
        )

        self.botao_4cadastro = Button(
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "CADASTRO",
                    # negrito
                    font    ='Helvetica 10 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR,
                    command= self.funcao_command_cadastro
        )

        self.botao_4cadastro.place(
                    x=690, y = MENU_Y, 

                    width=MENUS_WIDTH, height=MENU_HEIGHT
        )

        self.botao_5configuracao = Button (
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "CONFIGURAÇÕES",
                    # negrito
                    font    ='Helvetica 10 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR,    
                    # chamada       
                    command = self.funcao_command_menu_configuracao  

        )

        self.botao_5configuracao.place(
                    x=890, y = MENU_Y, 

                    width=MENUS_WIDTH, height=MENU_HEIGHT
        )

        self.botao_6APP = Button(
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "INFORMAÇÕES",
                    # negrito
                    font    ='Helvetica 10 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR,
                    command = self.funcao_command_informacao
        )

        self.botao_6APP.place(
                    x=1080, y = MENU_Y, 
                    
                    width=MENUS_WIDTH, height=MENU_HEIGHT

        )


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BarraMenusState():

    #1
    def funcao_desativar_botao_barra_home(self):

        self.botao_1home["state"] = "disabled"

    def funcao_ativar_botao_barra_home(self):

        self.botao_1home["state"] ="normal"

    #2
    def funcao_desativar_botao_barra_projetos(self):

        self.botao_2projetos["state"] = "disabled"

    def funcao_ativar_botao_barra_projetos(self):

        self.botao_2projetos["state"] ="normal"

    #3
    def funcao_desativar_botao_barra_recursos(self):

        self.botao_3recursos["state"] = "disabled"

    def funcao_ativar_botao_barra_recursos(self):

        self.botao_3recursos["state"] ="normal"

    #4
    def funcao_desativar_botao_barra_cadastro(self):

        self.botao_4cadastro["state"] = "disabled"

    def funcao_ativar_botao_barra_cadastro(self):

        self.botao_4cadastro["state"] ="normal"

    #5
    def funcao_class_desativar_botao_barra_configuracoes(self):
        
        self.botao_5configuracao["state"] = "disabled"

    def funcao_class_ativar_botao_barra_configurações(self):

        self.botao_5configuracao["state"] ="normal"

    #6
    def funcao_desativar_botao_barra_informacoes(self):
        
        self.botao_6APP["state"] = "disabled"

    def funcao_ativar_botao_barra_informacoes(self):

        self.botao_6APP["state"] ="normal"


"""BANCO"""
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

        self.sql_cursorr.execute("""
            CREATE TABLE IF NOT EXISTS MEMBROS ( ID_cod INTEGER PRIMARY KEY AUTOINCREMENT,
                                                Nome TEXT NOT NULL UNIQUE)
        """)

        self.sql_cursorr.execute("""
            CREATE TABLE IF NOT EXISTS ESTADO_CIVIL( 
                        ID_COD_ESTADO INTEGER PRIMARY KEY AUTOINCREMENT,
                        ID_casal1 INTEGER,
                        ID_casal2 INTEGER,
                        ID_solteiro INTEGER,
                        FOREIGN KEY (ID_casal1) REFERENCES MEMBROS (ID_cod),
                        FOREIGN KEY (ID_casal2) REFERENCES MEMBROS (ID_cod),
                        FOREIGN KEY (ID_solteiro) REFERENCES MEMBROS (ID_cod)
            )
        """)
    def funcao_classdb_commit(self):
        self.sql_connect.commit()

    ############################################### deconectar
    def funcao_classdb_desconectar(self):

        self.sql_connect.close()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BancoExecucaoConfiguracoes():

    ############################################### inserir if none
    """instituicao"""
    def funcao_classdb_inserir_nova_alianca(self):
            
        self.sql_cursorr.execute( "INSERT INTO Instituicao VALUES (1, '"+NOME_NOVA_ALIANCA+"')")
        self.funcao_classdb_commit()

    """processos"""
    def funcao_cursorrdb_inserir_thue(self):

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (1, '"+DB_THUE+"')")
        self.funcao_classdb_commit()

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (2, '"+DB_SALVAR+"')")
        self.funcao_classdb_commit()

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (3, '"+str(DB_1)+"')")
        self.funcao_classdb_commit()

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (4, '"+str(DB_0)+"')")
        self.funcao_classdb_commit()     

    ############################################### visualizar dados None
    """instituicao"""
    def funcao_classdb_visualizar_1 (self):
        
        self.sql_cursorr.execute( "SELECT nome_igreja FROM Instituicao WHERE cod = 1")
        self.visualiza = self.sql_cursorr.fetchone()

        if self.visualiza == None:

            self.funcao_classdb_inserir_nova_alianca()

    """processos"""
    def funcao_db_visualizar_tbprocesso(self, id_boleano):
        
        self.sql_cursorr.execute("SELECT boleano FROM Processos WHERE ID_processos = ?", (id_boleano,) )
        self.visualiza_processo = self.sql_cursorr.fetchone()
        
    def funcao_db_update_tbprocessos_linhaid(self,up_processo):

        self.funcao_classdb_conectar()
        
        sql_update_tbprocessos = """UPDATE Processos SET boleano = ? WHERE ID_processos = ?"""
        self.sql_cursorr.execute(sql_update_tbprocessos, up_processo)
        self.funcao_classdb_commit()
        
        self.funcao_classdb_desconectar()

    def funcao_db_conectar_e_visualizar_1(self):

        self.funcao_classdb_conectar()
        self.funcao_classdb_visualizar_1()

    ############################################### upgrade
    def funcao_db_update_tbprocessos_linha1(self):

        self.funcao_destruir_erro_bd()

        self.funcao_db_update_tbprocessos_linhaid((DB_THUE,DB_1))


"""LABEL INSTITUICAO BARRA"""
class BarraVisualizarNomeInstituicao():

    def funcao_class_barra_instituicao(self):      # funcao inicializacao

        #visual
        self.funcao_class_visual_instituicao()

        self.funcao_class_visualdb_barra_intituicao()

    def funcao_class_visual_instituicao(self):     # funcao inicializacao

        self.label_nome_instituicao_class= Label (
                    # cor de fundo -DeepSkyBlue
                    bg   = "#00BFFF",  

                    # negrito
                    font ='Helvetica 20 bold', 

                    # formato da borda
                    relief      ="ridge", 
                    # tamanho da borda
                    borderwidth = 5       
        )      
                                
        self.label_nome_instituicao_class.place(
                    x = WIDGET_2, y = TAMANHO_HEIGHT_JANELA - 50, 

                    width = TAMANHO_WIDTH_JANELA - WIDGET_4, height = 40
        )

    def funcao_class_visualdb_barra_intituicao(self):

        self.funcao_db_conectar_e_visualizar_1()

        for visual_nome in self.visualiza:

            upper_label = visual_nome.upper()
                            
            self.label_nome_instituicao_class.configure(text=upper_label)
            
        self.funcao_classdb_desconectar()


"""HOME"""
class ProcessoHome():                             

    def funcao_command_menu_home(self):              #  inicializacao botao

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco processos l3
        self.funcao_db_update_tbprocessos_linhaid((str(DB_1),DB_3))
        
        # ativar widget
        self.funcao_class_visual_instituicao()

        # funcao barra inferior visualizar
        self.funcao_class_visualdb_barra_intituicao()

        #state desativar home
        self.funcao_desativar_botao_barra_home()# desativar home


class DestruirHomeExterno():

    ################################################### if-else  home
    def funcao_class_if_destruir_widget(self):

        self.LABEL_BANCO_INSTITUICAO_FIXA.destroy() #Varivel fixa

        self.funcao_classdb_conectar()

        self.funcao_db_visualizar_tbprocesso(DB_2)
        visualizar_s_f = self.visualiza_processo[0]

        if visualizar_s_f == DB_SALVAR:
            
           self.funcao_destruir_entry_btsalvar()
           self.funcao_db_update_tbprocessos_linha1()

        elif visualizar_s_f == DB_ATUALIZAR:
            
            self.funcao_destruir_atalizar_label()
                
        self.funcao_classdb_desconectar()


"""projetos"""
class ProcessoProjetos():

    def funcao_command_projeto(self):

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.funcao_db_update_tbprocessos_linhaid((str(DB_2),DB_3))

        #state desativar projetos
        self.funcao_desativar_botao_barra_projetos()


"""recursos"""
class WidgetRecursos():

    def funcao_frame_widget_recursos(self):

        "label fixa"
        self.MENU_RECURSOS_BARRA_FIXO = Label ( 
                    # ForestGreen
                    bg     = "#228B22", 
                    # formato da borda
                    relief = "groove"  
        )

        self.MENU_RECURSOS_BARRA_FIXO.place(
                    x = 2, y = 50, 
                    
                    width = TAMANHO_WIDTH_JANELA - 4, height= 40
        )

        """botoes chamada da estrutura"""
        
        self.botao_1entradas_recursos= Button (
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "ENTRADAS",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR
                    # chamada         
                    #command = self.funcao_command_menu_home           

        )

        self.botao_1entradas_recursos. place(
                    x=400, y = 55, 
                    width=150, height= 30
        )

        self.botao_2gastos_recursos= Button (
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "GASTOS",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR
                    # chamada         
                    #command = self.funcao_command_menu_home           

        )

        self.botao_2gastos_recursos. place(
                    x=100, y = 55, 
                    
                    width=150, height= 30
        )

        self.botao_3resultado_recursos= Button (
                    # cor botao
                    bg      = COR_FUNDO_BOTAO_MENU_BAR,          
                    text    = "RESULTADO",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA_MENU_BAR
                    # chamada         
                    #command = self.funcao_command_menu_home           

        )

        self.botao_3resultado_recursos. place(
                    x=700, y = 55, 
                    width=150, height= 30
        )
    
class ProcessoRecurso():

    def funcao_command_recurso(self):

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.funcao_db_update_tbprocessos_linhaid((str(DB_3),DB_3))

        # frame widget
        self.funcao_frame_widget_recursos()

        #state desativar projetos
        self.funcao_desativar_botao_barra_recursos()


"""cadastro"""
class WidgetCadastro():

    def funcao_frame_widget_cadastro(self):

        "label fixa"
        self.MENU_CADASTRO_BARRA_FIXO = Label ( 
                    bg     = COR_FUNDO_2, 
                    # formato da borda
                    relief = "groove"  
        )

        self.MENU_CADASTRO_BARRA_FIXO.place(
                    x = 2, y = 50, 
                    
                    width = 180, height = TAMANHO_HEIGHT_JANELA- 60
        )

        self.MENU_CADASTRO_BARRA_FIXO_FRAME2 = Label ( 
                    bg     = COR_FUNDO_2, 
                    # formato da borda
                    relief = "groove"  
        )

        self.MENU_CADASTRO_BARRA_FIXO_FRAME2.place(
                    x = 190, y = 50, 
                    
                    width = TAMANHO_WIDTH_JANELA -200, height = 40
        )

        """botoes chamada da estrutura"""
        self.botao_1banco_cadastro= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "BANCO",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.funcao_command_bancocadastro     

        )

        self.botao_1banco_cadastro. place(
                    x=CADASTRO_FRAME1X, y = 60, 

                    width= CADASTRO_FRAME1WIGHT, height= CADASTRO_FRAME1HEIGHT
        )

        self.botao_2entradas_cadastros= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "ENTRADAS",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.funcao_command_entradascadastros          

        )

        self.botao_2entradas_cadastros. place(
                    x=CADASTRO_FRAME1X, y = 120, 

                    width=CADASTRO_FRAME1WIGHT, height= CADASTRO_FRAME1HEIGHT
        )

        self.botao_3gastos_cadastros= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "GASTOS",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.funcao_command_gastoscadastros_3          

        )

        self.botao_3gastos_cadastros. place(
                    x=CADASTRO_FRAME1X, y = 180, 
                    width=CADASTRO_FRAME1WIGHT, 
                    height= CADASTRO_FRAME1HEIGHT
        )

        self.botao_4membros_cadastros= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "MEMBROS",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.funcao_command_cadastromembros          

        )

        self.botao_4membros_cadastros. place(
                    x=CADASTRO_FRAME1X, y = 240, 

                    width=CADASTRO_FRAME1WIGHT, height= CADASTRO_FRAME1HEIGHT
        )

        self.funcao_framewidget_cadastrarbanco()


    #1
    def funcao_desativar_bancocadastro_1(self):

        self.botao_1banco_cadastro["state"] = "disabled"
        
    def funcao_ativar_bancocadastro_1(self):

        self.botao_1banco_cadastro["state"] = "normal"
    
    #2
    def funcao_desativar_entradascadastro_1(self):

        self.botao_2entradas_cadastros["state"] = "disabled"

    def funcao_ativar_entradascadastro_1(self):

        self.botao_2entradas_cadastros["state"] = "normal"

    #3
    def funcao_desativar_gastoscadastro_1(self):

        self.botao_3gastos_cadastros["state"] = "disabled"

    def funcao_ativar_gastoscadastro_1(self):

        self.botao_3gastos_cadastros["state"] = "normal"

    #4
    def funcao_desativar_membroscadastro_1(self):

        self.botao_4membros_cadastros["state"] = "disabled"

    def funcao_ativar_membroscadastro_1(self):

        self.botao_4membros_cadastros["state"] = "normal"

    def funcao_framewidget_cadastrarbanco(self):
        print(1)
        # update linha4 tbprocessos
        self.funcao_db_update_tbprocessos_linhaid((str(DB_1),DB_4))

        #state desativar
        self.funcao_desativar_bancocadastro_1()
        
    "membros parte 4"
    def funcao_frame_widget_cadastromembros(self):

        """botoes chamada da estrutura"""
        #barra principal

        self.botao_1cadastrar_cadastro_frame2= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "CADASTRAR",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.funcao_command_cadastrar_frame2_cadastro           

        )

        self.botao_1cadastrar_cadastro_frame2. place(
                    x=300, y = CADASTRO_FRAME2Y, 
                    
                    width=CADASTRO_FRAME2W, height= CADASTRO_FRAME2H
        )

        
        self.botao_2atualizar_cadastro_frame2= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = DB_ATUALIZAR,
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1
                    # chamada         
                    #command = self.funcao_command_      

        )

        self.botao_2atualizar_cadastro_frame2. place(
                    x=650, y = CADASTRO_FRAME2Y, 
                    
                    width=CADASTRO_FRAME2W, height= CADASTRO_FRAME2H
        )

        self.botao_3informacoes_cadastro_frame2= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "INFORMAÇÕES",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1
                    # chamada         
                    #command = self.funcao_command_menu_home           

        )

        self.botao_3informacoes_cadastro_frame2. place(
                    x=980, y = CADASTRO_FRAME2Y, 
                    
                    width=CADASTRO_FRAME2W, height= CADASTRO_FRAME2H
        )
    
    #1
    def funcao_desativar_btmembros_cadastrar_cadastro_2(self):

        self.botao_1cadastrar_cadastro_frame2["state"] = "disabled"

    def funcao_ativar_btmembros_cadastrar_cadastro_2(self):

        self.botao_1cadastrar_cadastro_frame2["state"] = "normal"

    #2
    def funcao_desativar_btmembros_atualizar_cadastro_2(self):

        self.botao_2atualizar_cadastro_frame2["state"] = "disabled"

    def funcao_ativar_btmembros_atualizar_cadastro_2(self):

        self.botao_2atualizar_cadastro_frame2["state"] = "normal"

    #3
    def funcao_desativar_btmembros_informacoes_cadastro_2(self):

        self.botao_3informacoes_cadastro_frame2["state"] = "disabled"

    def funcao_ativar_btmembros_informacoes_cadastro_2(self):

        self.botao_3informacoes_cadastro_frame2["state"] = "normal"

    "frame 2 cadastrar membros"
    def funcao_command_cadastrar_frame2_cadastro(self):

        "label fixa"
        self.LABEL_NOME_1 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "NOME DO MEMBRO",
                    # negrito
                    font    ='Helvetica 11 bold', 

        )

        self.LABEL_NOME_1.place(
                    x= 250, y=120, 
                    
                    width= 160, height= 25

        )

        self.LABEL_NOME_2 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "* escreva nome completo.",
                    # negrito
                    font    ='Helvetica 11 bold',

                    fg = "#FF0000"

        )

        self.LABEL_NOME_2.place(
                    x= 650, y=120, 
                    
                    width= 200, height= 25

        )

        "variaveis"
        self.entry_nome1 = Entry(
                                            
                    font    ='Helvetica 15', 
        )

        self.entry_nome1.place(
                    x=250, y= 150, 
                    width= 600, 
                    height= 30
        )

        self.botao_salvar_instituicao = Button ( 
                    # cor botao 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = DB_SALVAR,
                    # negrito
                    font    ='Helvetica 20 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
                    # chamada  
                    command = self.funcao_command_salvarnome

        )

        self.botao_salvar_instituicao. place(
                    x=900, 
                    y = 145,

                    width= 150, 
                    height= 40
        )


class ProcessoCadastro():

    "cadastro barra"
    def funcao_command_cadastro(self):

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.funcao_db_update_tbprocessos_linhaid((str(DB_4),DB_3))

        # frame widget
        self.funcao_frame_widget_cadastro()
        #state desativar projetos
        self.funcao_desativar_botao_barra_cadastro()

    "frame 1"
    #1
    def funcao_command_bancocadastro(self):

        self.funcao_classdb_conectar()
        self.funcao_if_widget_cadastrar_processo()
        self.funcao_classdb_desconectar()
        #frame 2
        self.funcao_framewidget_cadastrarbanco()
    
    #2
    def funcao_command_entradascadastros(self):

        self.funcao_classdb_conectar()
        self.funcao_if_widget_cadastrar_processo()
        self.funcao_classdb_desconectar()
        #tb processos updatye linha 4
        self.funcao_db_update_tbprocessos_linhaid((str(DB_2),DB_4))

        #state desativar
        self.funcao_desativar_entradascadastro_1()

    #3
    def funcao_command_gastoscadastros_3(self):

        self.funcao_classdb_conectar()
        self.funcao_if_widget_cadastrar_processo()
        self.funcao_classdb_desconectar()
        #tb processos updatye linha 4
        self.funcao_db_update_tbprocessos_linhaid((str(DB_3),DB_4))

        #state desativar
        self.funcao_desativar_gastoscadastro_1()

    #4
    def funcao_command_cadastromembros (self):

        self.funcao_classdb_conectar()
        self.funcao_if_widget_cadastrar_processo()
        self.funcao_classdb_desconectar()
        #tb processos updatye linha 4
        self.funcao_db_update_tbprocessos_linhaid((str(DB_4),DB_4))
        
        #frame
        self.funcao_frame_widget_cadastromembros()

        #state desativar
        self.funcao_desativar_membroscadastro_1()

    "frame 2 membros cadastrar"
    def funcao_command_salvarnome(self):
            
        insertmembros = str(self.entry_nome1.get())
        self.funcao_classdb_conectar()
        self.sql_cursorr.execute( "INSERT INTO MEMBROS VALUES (NULL,'"+insertmembros+"')")
        self.funcao_classdb_commit()
        self.funcao_classdb_desconectar()

class CadastroDestroy():

    """frame2"""
    def funcao_if_widget_cadastrar_processo(self):

        self.funcao_db_visualizar_tbprocesso(DB_4)
        db_if_viasualizar = self.visualiza_processo[0]

        if db_if_viasualizar == DB_1:

            #ativar
            self.funcao_ativar_bancocadastro_1()

        elif db_if_viasualizar == DB_2:

            #ativar
            self.funcao_ativar_entradascadastro_1()

        elif db_if_viasualizar == DB_3:

            #ativar
            self.funcao_ativar_gastoscadastro_1()

        elif db_if_viasualizar == DB_4:

            #ativar
            self.funcao_ativar_membroscadastro_1()

            #destroy
            self.botao_1cadastrar_cadastro_frame2.destroy()
            self.botao_2atualizar_cadastro_frame2.destroy()
            self.botao_3informacoes_cadastro_frame2.destroy()

        
"""CONFIGURAÇÕES"""
class WidgetConfiguracoes():

    """label fixas"""
    def funcao_label_fixa_erro_instituicao(self):

        self.LABEL_INSTITUICAO_FIXA_ERRO = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "DIGITE O NOME DO TEMPLO",
                    # negrito
                    font    ='Helvetica 11 bold', 

        )

        self.LABEL_INSTITUICAO_FIXA_ERRO.place(
                    x= 20, y=120, 
                    
                    width= 250, height= 20

        )

    def funcao_label_fixa_configuracao(self):

        self.LABEL_BANCO_INSTITUICAO_FIXA = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "NOME DO TEMPLO:",
                    # negrito
                    font    ='Helvetica 10 bold', 

        )

        self.LABEL_BANCO_INSTITUICAO_FIXA.place(
                    x= 20, y=60, 
                    
                    width=140, height= 20

        )

    """salvar instituicao"""
    def funcao_instituicao_entry_buton(self):

        self.entry_banco_instituicao = Entry(
                                            
                    font    ='Helvetica 10', 
        )

        self.entry_banco_instituicao.place(
                    x=CONFIGURACAO_ENTRYX, y= CONFIGURACAO_ENTRYY, 
                    width= CONFIGURACAO_ENTRYWIDGET, 
                    height= CONFIGURACAO_ENTRYHEIGHT
        )

        self.botao_salvar_instituicao = Button ( 
                    # cor botao 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = DB_SALVAR,
                    # negrito
                    font    ='Helvetica 20 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
                    # chamada  
                    command = self.funcao_classdb_atalizar_igreja_configuracoes

        )

        self.botao_salvar_instituicao. place(
                    x=CONFIGURACAO_BOTAO_INSTITUICAO_X, 
                    y = CONFIGURACAO_BOTAO_INSTITUICAO_Y,

                    width= CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH, 
                    height= CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT
        )

        self.funcao_db_update_tbprocessos_linhaid((DB_SALVAR,DB_2))

    """atualizar instituição"""
    def funcao_class_institucao_atualizar_widget(self):

        self.label_nome_instituicao_atualizar = Label ( 
                    bg = '#A9A9A9',
                    font= 'Helvetica 11 bold'
        )
            
        self.label_nome_instituicao_atualizar.place( 
                    x=CONFIGURACAO_ENTRYX, 
                    y= CONFIGURACAO_ENTRYY, 

                    width= CONFIGURACAO_ENTRYWIDGET, 
                    height= CONFIGURACAO_ENTRYHEIGHT)

        self.botao_atualizar_instituicao_atualizar = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = DB_ATUALIZAR,
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
                    # chamada  
                    command = self.funcao_if_widget_intermediario_atualizar_salvar

        )

        self.botao_atualizar_instituicao_atualizar. place(
                    x=CONFIGURACAO_BOTAO_INSTITUICAO_X, 
                    y = CONFIGURACAO_BOTAO_INSTITUICAO_Y, 
                    
                    width=CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH, 
                    height=CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT
        )

        self.funcao_db_conectar_e_visualizar_1()

        for label_nome in self.visualiza:
            self.label_nome_instituicao_atualizar.configure(text= label_nome)

        self.funcao_classdb_desconectar()

        self.funcao_db_update_tbprocessos_linhaid((DB_ATUALIZAR,DB_2))
    

class ProcessoConfiguracoes():

    """processo intermediario widget"""
    ###############################################  processo verificacao
    def funcao_if_widget_intermediario_salvar_atualizar(self):

        self.funcao_db_conectar_e_visualizar_1()

        self.transfomar_str_nome = self.visualiza[0]
        
        if self.transfomar_str_nome != NOME_NOVA_ALIANCA:
            
            self.funcao_class_institucao_atualizar_widget()
        
        elif self.transfomar_str_nome == NOME_NOVA_ALIANCA:
           
            self.funcao_instituicao_entry_buton()

    def funcao_if_widget_intermediario_atualizar_salvar(self):

        self.funcao_destruir_atalizar_label()
        
        self.funcao_instituicao_entry_buton()

    """salvar"""
    def funcao_classdb_atalizar_igreja_configuracoes(self):  # botao salvar
        
        get_entrada_instituicao = str(self.entry_banco_instituicao.get())
       
        if get_entrada_instituicao == "":

            self.funcao_classdb_conectar()

            self.funcao_db_visualizar_tbprocesso(DB_1)

            visualiza_V_F = self.visualiza_processo[DB_0]
           
            if  visualiza_V_F == DB_THUE:

                self.funcao_label_fixa_erro_instituicao()
                self.LABEL_INSTITUICAO_FIXA_ERRO.after(4000, self.funcao_destruir_erro)

            self. funcao_classdb_desconectar()

            self.funcao_db_update_tbprocessos_linhaid((DB_FALSE,DB_1))

        else:
            
            self.funcao_classdb_conectar()

            self.sql_cursorr.execute("UPDATE Instituicao SET nome_igreja ='"+get_entrada_instituicao+"' WHERE cod = 1")
            self.funcao_classdb_commit()

            self.funcao_db_update_tbprocessos_linha1()

            self.funcao_destruir_entry_btsalvar()
            self.funcao_class_institucao_atualizar_widget()

            self. funcao_classdb_desconectar()

    def funcao_command_menu_configuracao(self):       #funcao inicializacao configurações

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.funcao_db_update_tbprocessos_linhaid((str(DB_5),DB_3))
        
        ###########################################
                                    # ativar widget
        self.funcao_if_widget_intermediario_salvar_atualizar()
        self.funcao_label_fixa_configuracao()
        
        #state desativar configuracao
        self.funcao_class_desativar_botao_barra_configuracoes()

class ConfiguracaoDestruir():

    """salvar"""
    def funcao_destruir_erro(self):

        self.funcao_destruir_widget_erro()

        self.funcao_db_update_tbprocessos_linha1()

    def funcao_destruir_entry_btsalvar(self):

        self.entry_banco_instituicao.destroy()
        self.botao_salvar_instituicao.destroy()

    def funcao_destruir_erro_bd(self):

        self.funcao_classdb_conectar()

        self.funcao_db_visualizar_tbprocesso(DB_1)

        ad = self.visualiza_processo[DB_0]
    
        if ad == DB_FALSE:
            
            self.funcao_destruir_widget_erro()
         
        self.funcao_classdb_desconectar()

    """atualizar"""
    def funcao_destruir_atalizar_label(self):

        self.label_nome_instituicao_atualizar.destroy()
        self.botao_atualizar_instituicao_atualizar.destroy()

    def funcao_destruir_widget_erro(self):

        self.LABEL_INSTITUICAO_FIXA_ERRO.destroy()


class DestruirconfiguracoesExterno():

    ################################################ chamar botao
    #configuracao
    def funcao_class_destruir_home(self):          

        self.label_nome_instituicao_class.destroy()


class ProcessoInformacao():

    def funcao_command_informacao(self):

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.funcao_db_update_tbprocessos_linhaid((str(DB_6),DB_3))

       #state desativar informacao
        self.funcao_desativar_botao_barra_informacoes()


class Destruir_Widget_Barra():

    def funcao_analizar_processos_l3(self):
       
        self.funcao_classdb_conectar()

        self.funcao_db_visualizar_tbprocesso(DB_3)

        db_if = self.visualiza_processo[DB_0]

        if db_if   ==  DB_1:
            
            # ativar botao
            self.funcao_ativar_botao_barra_home()

            #destruir
            self.funcao_class_destruir_home()

        elif db_if == DB_2:

            # ativar botao
            self.funcao_ativar_botao_barra_projetos()
            print(2)

        elif db_if == DB_3:
            
            # ativar botao
            self.funcao_ativar_botao_barra_recursos()

            #destruir frame 1
            self.MENU_RECURSOS_BARRA_FIXO.destroy()

            self.botao_1entradas_recursos.destroy()
            self.botao_2gastos_recursos.destroy()
            self.botao_3resultado_recursos.destroy()

        elif db_if ==DB_4:
            
            # ativar botao
            self.funcao_ativar_botao_barra_cadastro()

            #frame 2
            self.funcao_if_widget_cadastrar_processo()

            #destruir frame 1
            self.MENU_CADASTRO_BARRA_FIXO.destroy()
            self.MENU_CADASTRO_BARRA_FIXO_FRAME2.destroy()

            self.botao_1banco_cadastro.destroy()
            self.botao_2entradas_cadastros.destroy()
            self.botao_3gastos_cadastros.destroy()
            self.botao_4membros_cadastros.destroy()

            # update tb processo lonha 4
            self.funcao_db_update_tbprocessos_linhaid((str(DB_0),DB_4))

        elif db_if == DB_5:
            
            # ativar botao
            self.funcao_class_ativar_botao_barra_configurações()

            #destruir
            self.funcao_class_if_destruir_widget()
            

        elif db_if == DB_6:
            
            # ativar botao
            self.funcao_ativar_botao_barra_informacoes()
            
            #destruir
            self.funcao_class_destruir_home()

        self.funcao_classdb_desconectar()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
############################################### menus da janela principal
class MenuWidget ( BarraMenuInicializacao, # barra
                BarraMenusState, #state
                #banco
                ClassBanco, BancoExecucaoConfiguracoes,
                #barra instituicao
                BarraVisualizarNomeInstituicao,
                #home 1
                ProcessoHome,
                DestruirHomeExterno,
                #projetos 2
                ProcessoProjetos,
                # recursos 3
                WidgetRecursos,
                ProcessoRecurso,
                # cadastro 4
                WidgetCadastro,
                ProcessoCadastro,
                CadastroDestroy,
                #configurações 5
                WidgetConfiguracoes, #widget
                ProcessoConfiguracoes,
                ConfiguracaoDestruir,
                DestruirconfiguracoesExterno,
                #informacao 6
                ProcessoInformacao,
                #sistema destruir
                Destruir_Widget_Barra
    ):

    #**********************************************
    ###############################################       função inicial
    def __init__(self):

        self.funcao_criar_tabela()
        ########################################### classe externa
        self.funcao_class_barra_menus()
        self.funcao_class_barra_instituicao() 

        #state
        self.funcao_desativar_botao_barra_home()  

    def funcao_criar_tabela(self):
        
        self.funcao_classdb_conectar()
        "criar"
        self.funcao_classdb_criar_tabela()   
        "visualizar"
        self.funcao_classdb_visualizar_1()  
        self.funcao_for_seguranca_tbprocessos()
        
        "update"
        self.funcao_db_update_tbprocessos_linhaid((DB_THUE,DB_1))
        
        self.funcao_classdb_desconectar()

        "update"
        self.funcao_db_update_tbprocessos_linhaid((str(DB_1),DB_3))
        self.funcao_db_update_tbprocessos_linhaid((str(DB_0),DB_4))

    def funcao_for_seguranca_tbprocessos(self):

        #self.funcao_cursorrdb_inserir_thue()
        self.funcao_classdb_conectar()
        self.sql_cursorr.execute("SELECT boleano  FROM Processos ")
        visualizar_id = self.sql_cursorr.fetchall()
        
        if len(visualizar_id) == DB_0:
            self.funcao_cursorrdb_inserir_thue()

        elif len(visualizar_id) <DB_4:
            
            self.sql_cursorr.execute("DELETE FROM Processos ")
            self.funcao_classdb_commit()

            self.funcao_cursorrdb_inserir_thue()

        self.funcao_classdb_desconectar()

#**************************************************
###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()