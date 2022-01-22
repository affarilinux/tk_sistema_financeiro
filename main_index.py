
                              # bibliotecas tkinter
from tkinter    import *

import tkinter  as tk
import sqlite3


                                 # diretorio do app
from janela.principal.composicao_principal import (
    CADASTRO_FRAME1HEIGHT, CADASTRO_FRAME1WIGHT, CADASTRO_FRAME1X, 
    CADASTRO_FRAME2Y, TAMANHO_WIDTH_JANELA, TAMANHO_HEIGHT_JANELA,

    MENUS_WIDTH, MENU_Y, MENU_HEIGHT, 

    COR_FUNDO_JANELA, COR_FUNDO_BOTAO_MENU_BAR, COR_BOTAO_FUNDO, COR_FUNDO_1,
    COR_FUNDO_2, COR_FUNDO_3,

    COR_ESCRITA_MENU_BAR, COR_ESCRITA1,

    NOME_NOVA_ALIANCA, 

    CONFIGURACAO_BOTAO_INSTITUICAO_X, CONFIGURACAO_BOTAO_INSTITUICAO_Y, 
    CONFIGURACAO_BOTAO_INSTITUICAO_WIDTH, CONFIGURACAO_BOTAO_INSTITUICAO_HEIGHT,

    CONFIGURACAO_ENTRYX, CONFIGURACAO_ENTRYY, CONFIGURACAO_ENTRYWIDGET, 
    CONFIGURACAO_ENTRYHEIGHT,

    TEXT_THUE, TEXT_FALSE,TEXT_SALVAR, TEXT_ATUALIZAR,

    NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, 

    WIDGET_2, WIDGET_4,

    CADASTRO_FRAME1X, CADASTRO_FRAME1WIGHT, CADASTRO_FRAME1HEIGHT,

    CADASTRO_FRAME2Y, CADASTRO_FRAME2W, CADASTRO_FRAME2H,

    CADAST_BOTAO_INSTITUICAO_X, CADAST_BOTAO_INSTITUICAO_Y,
    CADAST_BOTAO_INSTITUICAO_W, CADAST_BOTAO_INSTITUICAO_H
     
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
        
    def WIDGET_barra_menus_principal(self):        # funcao inicializacao

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
                    command = self.COMMAND1_home           

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
                    command = self.COMMAND1_projeto
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
                    command= self.COMMAND1_recursos
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
                    command= self.COMMAND1_cadastro
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
                    command = self.COMMAND1_configuracoes

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
                    command = self.COMMAND1_informacao
        )

        self.botao_6APP.place(
                    x=1080, y = MENU_Y, 
                    
                    width=MENUS_WIDTH, height=MENU_HEIGHT

        )


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BarraMenusState():

    #1
    def STATE1_desativar_home(self):

        self.botao_1home["state"] = "disabled"

    def STATE1_ativar_home(self):

        self.botao_1home["state"] ="normal"

    #2
    def STATE1_desativar_projetos(self):

        self.botao_2projetos["state"] = "disabled"

    def STATE1_ativar_projetos(self):

        self.botao_2projetos["state"] ="normal"

    #3
    def STATE1_desativar_recursos(self):

        self.botao_3recursos["state"] = "disabled"

    def STATE1_ativar_recursos(self):

        self.botao_3recursos["state"] ="normal"

    #4
    def STATE1_desativar_cadastro(self):

        self.botao_4cadastro["state"] = "disabled"

    def STATE1_ativar_cadastro(self):

        self.botao_4cadastro["state"] ="normal"

    #5
    def STATE1_desativar_configuracoes(self):
        
        self.botao_5configuracao["state"] = "disabled"

    def STATE1_ativar_configuracoes(self):

        self.botao_5configuracao["state"] ="normal"

    #6
    def STATE1_desativar_informacoes(self):
        
        self.botao_6APP["state"] = "disabled"

    def STATE1_ativar_informacoes(self):

        self.botao_6APP["state"] ="normal"


"""BANCO"""
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class ClassBanco():
    
    ############################################### conectar
    def DB_connectar(self):

        self.sql_connect = sqlite3.connect("banco_de_dados/sistema_financeiro.db")
        self.sql_cursor = self.sql_connect.cursor()

    def DB_commit(self):
        self.sql_connect.commit()

    ############################################### deconectar
    def DB_desconectar(self):

        self.sql_connect.close()
    
    ############################################### criar tabela
    def DB_criar_tabela(self):

        self.DB_connectar()

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS Instituicao ( cod INTEGER PRIMARY KEY,
                                                    nome_igreja TEXT

            )
             """)

        self.sql_cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Processos (ID_processos PRIMARY KEY,
                                                    boleano  BOOLEAN)
            """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS PROCESOSbarraapp(
                ID_barra INTERGER PRIMARY KEY,
                numero_barra INTEGER NOT NULL
                
            )
        """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS MEMBROS ( 
                ID_cod INTEGER  PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL UNIQUE)
                
                
        """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS ESTADO_CIVIL( 
                        ID_COD_ESTADO INTEGER PRIMARY KEY AUTOINCREMENT,
                        ID_casal1 INTEGER NOT NULL,
                        ID_casal2 INTEGER NOT NULL,
                        ID_solteiro INTEGER NOT NULL,
                        FOREIGN KEY (ID_casal1) REFERENCES MEMBROS (ID_cod),
                        FOREIGN KEY (ID_casal2) REFERENCES MEMBROS (ID_cod),
                        FOREIGN KEY (ID_solteiro) REFERENCES MEMBROS (ID_cod)
            )
        """)

        self.DB_desconectar()

    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BancoExecucaoConfiguracoes():

    ############################################### inserir if none
    """instituicao"""
    def funcao_classdb_inserir_nova_alianca(self):
            
        self.sql_cursor.execute( "INSERT INTO Instituicao VALUES (1, '"+NOME_NOVA_ALIANCA+"')")
        self.DB_commit()

    """processos"""
    def funcao_cursorrdb_inserir_thue(self):

        self.sql_cursor.execute("INSERT INTO Processos  VALUES (1, '"+TEXT_THUE+"')")
        self.DB_commit()

        self.sql_cursor.execute("INSERT INTO Processos  VALUES (2, '"+TEXT_SALVAR+"')")
        self.DB_commit() 

    def DBinserir_PROCESOSbarraapp(self):

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapp  VALUES (1, '"+str(NUM_1)+"')")
        self.DB_commit()

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapp  VALUES (2, '"+str(NUM_0)+"')")
        self.DB_commit()  


    ############################################### visualizar dados 
    """instituicao"""
    def funcao_classdb_visualizar_1 (self):
        
        self.sql_cursor.execute( "SELECT nome_igreja FROM Instituicao WHERE cod = 1")
        self.visualiza = self.sql_cursor.fetchone()

        if self.visualiza == None:

            self.funcao_classdb_inserir_nova_alianca()

    """processo barra"""
    def DB_visualizar_PROCESOSbarraapp(self, id_numero_barra):
        
        self.sql_cursor.execute("SELECT numero_barra FROM PROCESOSbarraapp WHERE ID_barra = ?", (id_numero_barra,) )
        self.visualiza_barraapp = self.sql_cursor.fetchone()
    
    """processos"""
    def funcao_db_visualizar_tbprocesso(self, id_boleano):
        
        self.sql_cursor.execute("SELECT boleano FROM Processos WHERE ID_processos = ?", (id_boleano,) )
        self.visualiza_processo = self.sql_cursor.fetchone()
        
    """update tabelas"""
    def DB_update_PROCESOSbarraapp(self,up_barra):

        self.DB_connectar()

        sql_update_PROCESSObarra = """UPDATE PROCESOSbarraapp SET numero_barra = ? WHERE ID_barra = ?"""
        self.sql_cursor.execute(sql_update_PROCESSObarra, up_barra)
        self.DB_commit()
        
        self.DB_desconectar()

    def funcao_db_update_tbprocessos_linhaid(self,up_processo):

        self.DB_connectar()
        
        sql_update_tbprocessos = """UPDATE Processos SET boleano = ? WHERE ID_processos = ?"""
        self.sql_cursor.execute(sql_update_tbprocessos, up_processo)
        self.DB_commit()
        
        self.DB_desconectar()

    def funcao_db_conectar_e_visualizar_1(self):

        self.DB_connectar()
        self.funcao_classdb_visualizar_1()

        ############################################### upgrade
    def funcao_db_update_tbprocessos_linha1(self):

        self.funcao_destruir_erro_bd()

        self.funcao_db_update_tbprocessos_linhaid((TEXT_THUE,NUM_1))

    
"""LABEL INSTITUICAO BARRA"""
class BarraVisualizarNomeInstituicao():

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
            
        self.DB_desconectar()


"""HOME"""
class ProcessoHome():                             

    def COMMAND1_home(self):              #  inicializacao botao

        # destruir externamente
        self.DESTROIR_externoif_widget_barra()

        # atualizar banco processos l3
        self.DB_update_PROCESOSbarraapp((NUM_1,NUM_1))
        
        # ativar widget
        self.funcao_class_visual_instituicao()

        # funcao barra inferior visualizar
        self.funcao_class_visualdb_barra_intituicao()

        #state desativar home
        self.STATE1_desativar_home()# desativar home


class DestruirHomeExterno():

    ################################################### if-else  home
    def funcao_class_if_destruir_widget(self):

        self.LABEL_BANCO_INSTITUICAO_FIXA.destroy() #Varivel fixa

        self.DB_connectar()

        self.funcao_db_visualizar_tbprocesso(NUM_2)
        visualizar_s_f = self.visualiza_processo[0]

        if visualizar_s_f == TEXT_SALVAR:
            
           self.funcao_destruir_entry_btsalvar()
           self.funcao_db_update_tbprocessos_linha1()

        elif visualizar_s_f == TEXT_ATUALIZAR:
            
            self.funcao_destruir_atalizar_label()
                
        self.DB_desconectar()


"""projetos"""
class ProcessoProjetos():

    def COMMAND1_projeto(self):

        # destruir externamente
        self.DESTROIR_externoif_widget_barra()

        # atualizar banco
        self.DB_update_PROCESOSbarraapp((NUM_2,NUM_1))

        #state desativar projetos
        self.STATE1_desativar_projetos()


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

    def COMMAND1_recursos(self):

        # destruir externamente
        self.DESTROIR_externoif_widget_barra()

        # atualizar banco
        self.DB_update_PROCESOSbarraapp((NUM_3,NUM_1))

        # frame widget
        self.funcao_frame_widget_recursos()

        #state desativar projetos
        self.STATE1_desativar_recursos()


"""cadastro"""
class WidgetCadastro():

    def WIDGETframe44_cadastro(self):

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
                    command = self.COMMANDframe44_bancocd     

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
                    command = self.COMMANDframe44_entradascd          

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
                    command = self.COMMANDframe44_gastoscd          

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
                    command = self.COMMANDframe44_membroscd          

        )

        self.botao_4membros_cadastros. place(
                    x=CADASTRO_FRAME1X, y = 240, 

                    width=CADASTRO_FRAME1WIGHT, 
                    height= CADASTRO_FRAME1HEIGHT
        )

        self.botao_4instituicao_cadastros= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "INSTITUIÇÃO",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.COMMANDframe44_instituicaocd          

        )

        self.botao_4instituicao_cadastros. place(
                    x=CADASTRO_FRAME1X, y = 300, 

                    width=CADASTRO_FRAME1WIGHT, 
                    height= CADASTRO_FRAME1HEIGHT
        )

        self.FC_WIDGETframe44_processo_banco()

    #1
    def STATE44_desativar_banco(self):

        self.botao_1banco_cadastro["state"] = "disabled"
        
    def STATE44_ativar_banco(self):

        self.botao_1banco_cadastro["state"] = "normal"
    
    #2
    def STATE44_desativar_entradas(self):

        self.botao_2entradas_cadastros["state"] = "disabled"

    def STATE44_ativar_entradas(self):

        self.botao_2entradas_cadastros["state"] = "normal"

    #3
    def STATE44_desativar_gastos(self):

        self.botao_3gastos_cadastros["state"] = "disabled"

    def STATE44_ativar_gastos(self):

        self.botao_3gastos_cadastros["state"] = "normal"

    #4
    def STATE44_desativar_membros(self):

        self.botao_4membros_cadastros["state"] = "disabled"

    def STATE44_ativar_membros(self):

        self.botao_4membros_cadastros["state"] = "normal"

    #5
    def STATE44_desativar_instituicao(self):

        self.botao_4instituicao_cadastros["state"] = "disabled"

    def STATE44_ativar_instituicao(self):

        self.botao_4instituicao_cadastros["state"] = "normal"

    "banco"
    def FC_WIDGETframe44_processo_banco(self):
        
        # update linha4 tbprocessos
        self.DB_update_PROCESOSbarraapp((NUM_1,NUM_2))

        #state desativar
        self.STATE44_desativar_banco()
        
    "membros parte 4"
    def WIDGETframe44_cadastromembros(self):

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
                    command = self.WIDGETframe44_COMMAND4_cadastrar_membros           

        )

        self.botao_1cadastrar_cadastro_frame2. place(
                    x=300, y = CADASTRO_FRAME2Y, 
                    
                    width=CADASTRO_FRAME2W, height= CADASTRO_FRAME2H
        )

        
        self.botao_2atualizar_cadastro_frame2= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = TEXT_ATUALIZAR,
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
                    
                    width=CADASTRO_FRAME2W, 
                    height= CADASTRO_FRAME2H
        )
    
    #1
    def STATE44_desativar_cadastrar_mb(self):

        self.botao_1cadastrar_cadastro_frame2["state"] = "disabled"

    def STATE44_ativar_cadastrar_mb(self):

        self.botao_1cadastrar_cadastro_frame2["state"] = "normal"

    #2
    def STATE44_desativar_atualizar_mb(self):

        self.botao_2atualizar_cadastro_frame2["state"] = "disabled"

    def STATE44_ativar_atualizar_mb(self):

        self.botao_2atualizar_cadastro_frame2["state"] = "normal"

    #3
    def STATE44_desativar_informacoes_mb(self):

        self.botao_3informacoes_cadastro_frame2["state"] = "disabled"

    def STATE44_ativar_informacoes_mb(self):

        self.botao_3informacoes_cadastro_frame2["state"] = "normal"

    "frame 2 cadastrar membros"
    def WIDGETframe44_COMMAND4_cadastrar_membros(self):

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
                    text    = TEXT_SALVAR,
                    # negrito
                    font    ='Helvetica 20 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
                    # chamada  
                    command = self.COMMAND4_db_membros_atsalvar

        )

        self.botao_salvar_instituicao. place(
                    x=900, 
                    y = 145,

                    width= 150, 
                    height= 40
        )

    "5 widget instituicao"
    def WIDGETframe44_sistemamembros(self):

        #sistema
        self.LABELfixo_sistema2 = Label (
                    # cor botao
                    bg      = COR_FUNDO_2,
                    text    = "INFORMAÇÕES INSTITUIÇÃO",
                    # negrito
                    font    ='Helvetica 20 bold',

                    fg = COR_ESCRITA1

        )

        self.LABELfixo_sistema2.place(
                    x= 500, y=55, 
                    
                    width= 400, height= 30

        )

        self.LABELfixo_sistema = Label ( 
                    bg     = COR_FUNDO_3, 
                    # formato da borda
                    relief = "groove"  
        )

        self.LABELfixo_sistema.place(
                    x = 190, y = 130, 
                    
                    width = TAMANHO_WIDTH_JANELA -200, height = 150
        )

        self.LABELfixo_sistema_nome = Label (
                    # cor botao
                    bg      = COR_FUNDO_3,
                    text    = "Nome da Instituição:",
                    # negrito
                    font    ='Helvetica 14 bold',

                    fg = COR_ESCRITA1
        )

        self.LABELfixo_sistema_nome.place(
                    x= 200, y=140, 
                    
                    width= 190, height= 25

        )

        #label varivel

        self.LABELvariavel_sistema_nome = Label (
                    # cor botao
                    bg      = COR_FUNDO_3,
                    
                    # negrito
                    font    ='Helvetica 13 bold',

                    fg      = COR_ESCRITA1
        )

        self.LABELvariavel_sistema_nome.place(
                    x= 400, y=140, 
                    
                    width= 250, height= 25
        )

        self.WIDGETfc_atualizar_instiruicao()

    def WIDGETfc_atualizar_instiruicao(self):

        self.BOTAOfcInstituicao = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = TEXT_ATUALIZAR,
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR        
                    # chamada  
                    #command = self.funcao_if_widget_intermediario_atualizar_salvar

        )

        self.BOTAOfcInstituicao. place(
                    x      =  CADAST_BOTAO_INSTITUICAO_X, 
                    y      = CADAST_BOTAO_INSTITUICAO_Y, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )

    def FC_dbvisualiar_instituicao(self):

        self.DB_connectar()

        self.DB_desconectar()

class ProcessoCadastro():

    "cadastro barra"
    def COMMAND1_cadastro(self):

        # destruir externamente
        self.DESTROIR_externoif_widget_barra()

        # atualizar banco
        self.DB_update_PROCESOSbarraapp((NUM_4,NUM_1))

        # frame widget
        self.WIDGETframe44_cadastro()
        #state desativar projetos
        self.STATE1_desativar_cadastro()

    "frame 1"
    #1
    def COMMANDframe44_bancocd(self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #frame 2
        self.FC_WIDGETframe44_processo_banco()
    
    #2
    def COMMANDframe44_entradascd(self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processo barra app updatye linha 2
        self.DB_update_PROCESOSbarraapp((NUM_2,NUM_2))

        #state desativar
        self.STATE44_desativar_entradas()

    #3
    def COMMANDframe44_gastoscd(self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processos updatye linha 4
        self.DB_update_PROCESOSbarraapp((NUM_3,NUM_2))
        #state desativar
        self.STATE44_desativar_gastos()

    #4
    def COMMANDframe44_membroscd (self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processos updatye linha 4
        self.DB_update_PROCESOSbarraapp((NUM_4,NUM_2))
        
        #frame
        self.WIDGETframe44_cadastromembros()

        #state desativar
        self.STATE44_desativar_membros()

    def COMMANDframe44_instituicaocd(self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processos updatye linha 4
        self.DB_update_PROCESOSbarraapp((NUM_5,NUM_2))

        # widget

        self.WIDGETframe44_sistemamembros()
        #state desabilitar
        self.STATE44_desativar_instituicao()

    "frame 2 membros cadastrar"
    def COMMAND4_db_membros_atsalvar(self):
            
        insertmembros = str(self.entry_nome1.get())

        '''self.DB_connectar()
        self.sql_cursor.execute( "INSERT INTO MEMBROS VALUES (NULL,'"+insertmembros+"')")
        self.DB_commit()
        self.DB_desconectar()'''
        
        try:
            self.DB_connectar()
            self.sql_cursor.execute( "INSERT INTO MEMBROS VALUES (NULL,'"+insertmembros+"')")
            self.DB_commit()
            self.DB_desconectar()
        except sqlite3.IntegrityError:
            print("erro")
        # Exception as Erro:
            #print(Erro.__class__)

    #def 
class CadastroDestroy():

    """frame2"""
    def DESTROIR4_internoif_widget_cadastro(self):

        self.DB_visualizar_PROCESOSbarraapp(NUM_2)
        db_if_viasualizar = self.visualiza_barraapp[0]

        if db_if_viasualizar == NUM_1:

            #ativar
            self.STATE44_ativar_banco()

        elif db_if_viasualizar == NUM_2:

            #ativar
            self.STATE44_ativar_entradas()

        elif db_if_viasualizar == NUM_3:

            #ativar
            self.STATE44_ativar_gastos()

        elif db_if_viasualizar == NUM_4:

            #ativar
            self.STATE44_ativar_membros()

            #destroy
            self.botao_1cadastrar_cadastro_frame2.destroy()
            self.botao_2atualizar_cadastro_frame2.destroy()
            self.botao_3informacoes_cadastro_frame2.destroy()

        elif db_if_viasualizar == NUM_5:

            #reativar
            self.STATE44_ativar_instituicao()

        
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
                    text    = TEXT_SALVAR,
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

        self.funcao_db_update_tbprocessos_linhaid((TEXT_SALVAR,NUM_2))

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
                    text    = TEXT_ATUALIZAR,
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

        self.DB_desconectar()

        self.funcao_db_update_tbprocessos_linhaid((TEXT_ATUALIZAR,NUM_2))
    

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

            self.DB_connectar()

            self.funcao_db_visualizar_tbprocesso(NUM_1)

            visualiza_V_F = self.visualiza_processo[NUM_0]
           
            if  visualiza_V_F == TEXT_THUE:

                self.funcao_label_fixa_erro_instituicao()
                self.LABEL_INSTITUICAO_FIXA_ERRO.after(4000, self.funcao_destruir_erro)

            self. DB_desconectar()

            self.funcao_db_update_tbprocessos_linhaid((TEXT_FALSE,NUM_1))

        else:
            
            self.DB_connectar()

            self.sql_cursor.execute("UPDATE Instituicao SET nome_igreja ='"+get_entrada_instituicao+"' WHERE cod = 1")
            self.DB_commit()

            self.funcao_db_update_tbprocessos_linha1()

            self.funcao_destruir_entry_btsalvar()
            self.funcao_class_institucao_atualizar_widget()

            self. DB_desconectar()

    def COMMAND1_configuracoes(self):       #funcao inicializacao configurações

        # destruir externamente
        self.DESTROIR_externoif_widget_barra()

        # atualizar banco
        self.DB_update_PROCESOSbarraapp((NUM_5,NUM_1))
        
        ###########################################
                                    # ativar widget
        self.funcao_if_widget_intermediario_salvar_atualizar()
        self.funcao_label_fixa_configuracao()
        
        #state desativar configuracao
        self.STATE1_desativar_configuracoes()

class ConfiguracaoDestruir():

    """salvar"""
    def funcao_destruir_erro(self):

        self.funcao_destruir_widget_erro()

        self.funcao_db_update_tbprocessos_linha1()

    def funcao_destruir_entry_btsalvar(self):

        self.entry_banco_instituicao.destroy()
        self.botao_salvar_instituicao.destroy()

    def funcao_destruir_erro_bd(self):

        self.DB_connectar()

        self.funcao_db_visualizar_tbprocesso(NUM_1)

        ad = self.visualiza_processo[NUM_0]
    
        if ad == TEXT_FALSE:
            
            self.funcao_destruir_widget_erro()
         
        self.DB_desconectar()

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

    def COMMAND1_informacao(self):

        # destruir externamente
        self.DESTROIR_externoif_widget_barra()

        # atualizar banco
        self.DB_update_PROCESOSbarraapp((NUM_6,NUM_1))

       #state desativar informacao
        self.STATE1_desativar_informacoes()


class Destruir_Widget_Barra():

    def DESTROIR_externoif_widget_barra(self):
       
        self.DB_connectar()

        self.DB_visualizar_PROCESOSbarraapp(NUM_1)

        db_if = self.visualiza_barraapp[0]

        if db_if   ==  NUM_1:
            
            # ativar botao
            self.STATE1_ativar_home()

            #destruir
            self.funcao_class_destruir_home()

        elif db_if == NUM_2:

            # ativar botao
            self.STATE1_ativar_projetos()

        elif db_if == NUM_3:
            
            # ativar botao
            self.STATE1_ativar_recursos()

            #destruir frame 1
            self.MENU_RECURSOS_BARRA_FIXO.destroy()

            self.botao_1entradas_recursos.destroy()
            self.botao_2gastos_recursos.destroy()
            self.botao_3resultado_recursos.destroy()

        elif db_if ==NUM_4:
            
            # ativar botao
            self.STATE1_ativar_cadastro()

            #frame 2
            self.DESTROIR4_internoif_widget_cadastro()

            #destruir frame 1
            self.MENU_CADASTRO_BARRA_FIXO.destroy()
            self.MENU_CADASTRO_BARRA_FIXO_FRAME2.destroy()

            self.botao_1banco_cadastro.destroy()
            self.botao_2entradas_cadastros.destroy()
            self.botao_3gastos_cadastros.destroy()
            self.botao_4membros_cadastros.destroy()
            self.botao_4instituicao_cadastros.destroy()

            # update tb processobarraapp lonha 4
            self.DB_update_PROCESOSbarraapp((NUM_0,NUM_2))

        elif db_if == NUM_5:
            
            # ativar botao
            self.STATE1_ativar_configuracoes()

            #destruir
            self.funcao_class_if_destruir_widget()
            

        elif db_if == NUM_6:
            
            # ativar botao
            self.STATE1_ativar_informacoes()
            
            #destruir
            self.funcao_class_destruir_home()

        self.DB_desconectar()


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

        "externas"
        "criar tabela"
        self.DB_criar_tabela()

        "funcoes intenas"
        "inserir banco"
        self.FCmi_seguranca_tbprocessos()
        self.fcmi_seguranca_PROCESOSbarraapp()

        self.FCmi_criar_tabela()

        ########################################### classe externa
        #menus fixos
        self.WIDGET_barra_menus_principal()
        
        #home
        self.funcao_class_visual_instituicao()

        self.funcao_class_visualdb_barra_intituicao()

        #state
        self.STATE1_desativar_home()  

    def FCmi_seguranca_tbprocessos(self):

        self.DB_connectar()
        self.sql_cursor.execute("SELECT boleano  FROM Processos ")
        visualizar_id = self.sql_cursor.fetchall()
        
        if len(visualizar_id) == NUM_0:
            self.funcao_cursorrdb_inserir_thue()

        elif len(visualizar_id) <NUM_4:
            
            self.sql_cursor.execute("DELETE FROM Processos ")
            self.DB_commit()

            self.funcao_cursorrdb_inserir_thue()

        self.DB_desconectar()

    def fcmi_seguranca_PROCESOSbarraapp(self):

        self.DB_connectar()
        self.sql_cursor.execute("SELECT numero_barra  FROM PROCESOSbarraapp ")
        visualizar_idbarra = self.sql_cursor.fetchall()
        
        if len(visualizar_idbarra) == NUM_0:
            self.DBinserir_PROCESOSbarraapp()

        elif len(visualizar_idbarra) <NUM_2:
            
            self.sql_cursor.execute("DELETE FROM Processos ")
            self.DB_commit()

            self.DBinserir_PROCESOSbarraapp()

        self.DB_desconectar()

    def FCmi_criar_tabela(self):
        
        
        self.DB_connectar()
         
        "visualizar"
        self.funcao_classdb_visualizar_1()  
        
        
        "update"
        self.funcao_db_update_tbprocessos_linhaid((TEXT_THUE,NUM_1))
        
        self.DB_desconectar()

        "update"
        #barra principal
        self.DB_update_PROCESOSbarraapp((NUM_1,NUM_1))

        #subbarra
        self.DB_update_PROCESOSbarraapp((NUM_0,NUM_2))
#**************************************************
###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()