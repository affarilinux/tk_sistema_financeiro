
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

        """fixo"""
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

        self.botao_1home. place(x=30, y = MENU_Y, width=MENUS_WIDTH, 
                                height=MENU_HEIGHT
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

        self.botao_2projetos.place(x=190, y = MENU_Y, width=MENUS_WIDTH, 
                                height=MENU_HEIGHT
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

        self.botao_3recursos.place(x=350, y = MENU_Y, width=MENUS_WIDTH, 
                                height=MENU_HEIGHT
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

        self.botao_4cadastro.place(x=510, y = MENU_Y, width=MENUS_WIDTH, 
                                height=MENU_HEIGHT
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

        self.botao_5configuracao.place(x=670, y = MENU_Y, width=MENUS_WIDTH, 
                                         height=MENU_HEIGHT
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

        self.botao_6APP.place(x=830, y = MENU_Y, width=MENUS_WIDTH, 
                            height=MENU_HEIGHT

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

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (1, 'Thue')")
        self.funcao_classdb_commit()

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (2, '"+CONFIGURACOES_INSTITUICAO_L2_SALVAR+"')")
        self.funcao_classdb_commit()

        self.sql_cursorr.execute("INSERT INTO Processos  VALUES (3, '1')")
        self.funcao_classdb_commit()

    ############################################### visualizar dados None
    """instituicao"""
    def funcao_classdb_visualizar_1 (self):
        
        self.sql_cursorr.execute( "SELECT nome_igreja FROM Instituicao WHERE cod = 1")
        self.visualiza = self.sql_cursorr.fetchone()

        if self.visualiza == None:

            self.funcao_classdb_inserir_nova_alianca()

    """processos"""

    def funcao_db_visualizar_tbprocesso(self):
        
        self.sql_cursorr.execute("SELECT boleano FROM Processos WHERE ID_processos = '"+self.boleano_id+"' ")
        self.visualiza_processo = self.sql_cursorr.fetchone()
        print(self.boleano_id)
        print(self.visualiza_processo)

        if self.visualiza_processo == None:

            self.funcao_cursorrdb_inserir_thue()

    def funcao_db_visualiar_tbprocessos (self):

        self.sql_cursorr.execute("SELECT boleano FROM Processos WHERE ID_processos = 1 ")
        self.visualiza_processos = self.sql_cursorr.fetchone()

        if self.visualiza_processos == None:

            self.funcao_cursorrdb_inserir_thue()

    def funcao_db_visualiza_tbprocessos_linha2(self):

        self.sql_cursorr.execute("SELECT boleano FROM Processos WHERE ID_processos =2 ")
        self.visualiza_processos_L2 = self.sql_cursorr.fetchone()

    def funcao_db_visualiza_tbprocessos_linha3(self):

        self.sql_cursorr.execute("SELECT boleano FROM Processos WHERE ID_processos =3 ")
        self.visualiza_processos_L3 = self.sql_cursorr.fetchone()

    def funcao_db_conectar_e_visualizar_1(self):

        self.funcao_classdb_conectar()
        self.funcao_classdb_visualizar_1()

    ############################################### upgrade
    def funcao_db_update_tbprocessos_linha1(self):

        self.funcao_destruir_erro_bd()

        self.funcao_classdb_conectar()

        self.sql_cursorr.execute("UPDATE Processos SET boleano = 'Thue' WHERE ID_processos = 1 " )
        self.funcao_classdb_commit()

        self.funcao_classdb_desconectar()

    def funcao_db_update_tbinstituicao_linha2(self):

        self.sql_cursorr.execute("UPDATE Instituicao SET  nome_igreja = '"+self.destroir_banco_1+"' WHERE cod = 2 " )
        self.funcao_classdb_commit()

    def funcao_update_processo_home_l3(self):

        # atualizar banco
        self.funcao_classdb_conectar()

        self.sql_cursorr.execute("UPDATE Processos SET boleano = '"+self.up_processo_l3+"' WHERE ID_processos = 3 ")
        self.funcao_classdb_commit()

        self.funcao_classdb_desconectar()


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
                                
        self.label_nome_instituicao_class.place(x = 0, y = 758, 
                                        width = TAMANHO_WIDTH_JANELA,
                                        height = 40
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
        self.up_processo_l3 =str(1)
        self.funcao_update_processo_home_l3()
        
        # ativar widget
        self.funcao_class_visual_instituicao()

        # funcao barra inferior visualizar
        self.funcao_class_visualdb_barra_intituicao()

        #state desativar home
        self.funcao_desativar_botao_barra_home()# desativar home

        #state ativar
        #1
        self.funcao_ativar_botao_barra_projetos()
        self.funcao_ativar_botao_barra_recursos()
        self.funcao_ativar_botao_barra_cadastro()
        self.funcao_class_ativar_botao_barra_configurações()
        self.funcao_ativar_botao_barra_informacoes()


class DestruirHomeExterno():

    ################################################### if-else  home
    def funcao_class_if_destruir_widget(self):

        self.LABEL_BANCO_INSTITUICAO_FIXA.destroy() #Varivel fixa

        self.funcao_classdb_conectar()

        self.funcao_db_visualiza_tbprocessos_linha2()
        visualizar_s_f = self.visualiza_processos_L2[0]

        if visualizar_s_f == CONFIGURACOES_INSTITUICAO_L2_SALVAR:
            
           self.funcao_destruir_entry_btsalvar()
           self.funcao_db_update_tbprocessos_linha1()

        elif visualizar_s_f == "ATUALIZAR":
            
            self.funcao_destruir_atalizar_label()
                
        self.funcao_classdb_desconectar()


"""projetos"""
class ProcessoProjetos():

    def funcao_command_projeto(self):

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.up_processo_l3 =str(2)
        self.funcao_update_processo_home_l3()

        #state desativar projetos
        self.funcao_desativar_botao_barra_projetos()

        #state ativar
        self.funcao_ativar_botao_barra_home()
        #2
        self.funcao_ativar_botao_barra_recursos()
        self.funcao_ativar_botao_barra_cadastro()
        self.funcao_class_ativar_botao_barra_configurações()
        self.funcao_ativar_botao_barra_informacoes()


"""recursos"""
class ProcessoRecurso():

    def funcao_command_recurso(self):

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.up_processo_l3 =str(3)
        self.funcao_update_processo_home_l3()

        #state desativar projetos
        self.funcao_desativar_botao_barra_recursos()

        #state ativar
        self.funcao_ativar_botao_barra_home()
        self.funcao_ativar_botao_barra_projetos()
        #3
        self.funcao_ativar_botao_barra_cadastro()
        self.funcao_class_ativar_botao_barra_configurações()
        self.funcao_ativar_botao_barra_informacoes()


"""cadastro"""
class ProcessoCadastro():

    def funcao_command_cadastro(self):

        # destruir externamente
        self.funcao_analizar_processos_l3()

        # atualizar banco
        self.up_processo_l3 =str(4)
        self.funcao_update_processo_home_l3()

        self.funcao_classdb_desconectar()

        #state desativar projetos
        self.funcao_desativar_botao_barra_cadastro()

        #state ativar
        self.funcao_ativar_botao_barra_home()
        self.funcao_ativar_botao_barra_projetos()
        self.funcao_ativar_botao_barra_recursos()
        #4
        self.funcao_class_ativar_botao_barra_configurações()
        self.funcao_ativar_botao_barra_informacoes()


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

    """salvar instituicao"""
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
                                                text    = CONFIGURACOES_INSTITUICAO_L2_SALVAR,
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

    """atualizar instituição"""
    def funcao_class_institucao_atualizar_widget(self):

        self.label_nome_instituicao_atualizar = Label ( bg = '#A9A9A9',
    
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

        
        self.funcao_db_conectar_e_visualizar_1()

        for label_nome in self.visualiza:
            self.label_nome_instituicao_atualizar.configure(text= label_nome)

        self.sql_cursorr.execute("UPDATE Processos SET boleano = '"+CONFIGURACOES_INSTITUICAO_L2_ATUALIZAR+"' WHERE ID_processos = 2 " )
        self.funcao_classdb_commit()

        self.funcao_classdb_desconectar()
    

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

            self.boleano_id = 2
            self.funcao_db_visualizar_tbprocesso()

            visualiza_V_F = self.visualiza_processo[0]

            if  visualiza_V_F == 'Thue':

                self.funcao_label_fixa_erro_instituicao()
                self.LABEL_INSTITUICAO_FIXA_ERRO.after(4000, self.funcao_destruir_erro)

                self.sql_cursorr.execute("UPDATE Processos SET boleano = 'False' WHERE ID_processos = 1 " )
                self.funcao_classdb_commit()

            self. funcao_classdb_desconectar()

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

        self.up_processo_l3 =str(5)
        self.funcao_update_processo_home_l3()
        
        ###########################################
                                    # ativar widget
        self.funcao_if_widget_intermediario_salvar_atualizar()
        self.funcao_label_fixa_configuracao()
        
        #state desativar configuracao
        self.funcao_class_desativar_botao_barra_configuracoes()

        #state ativar
        self.funcao_ativar_botao_barra_home()
        self.funcao_ativar_botao_barra_projetos()
        self.funcao_ativar_botao_barra_recursos()
        self.funcao_ativar_botao_barra_cadastro()
        #5
        self.funcao_ativar_botao_barra_informacoes()


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

        self.funcao_db_visualiar_tbprocessos()

        ad = self.visualiza_processos[0]
    
        if ad == 'False':
            
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
        self.up_processo_l3 =str(6)
        self.funcao_update_processo_home_l3()

        #destruir widget externo
        self.funcao_class_destruir_home()

        #state desativar informacao
        self.funcao_desativar_botao_barra_informacoes()

        #state ativar
        self.funcao_ativar_botao_barra_home()
        self.funcao_ativar_botao_barra_projetos()
        self.funcao_ativar_botao_barra_recursos()
        self.funcao_ativar_botao_barra_cadastro()
        self.funcao_class_ativar_botao_barra_configurações()
        #6


class Destruir_Widget_Barra():

    def funcao_analizar_processos_l3(self):
       
        self.funcao_classdb_conectar()
        self.funcao_db_visualiza_tbprocessos_linha3()

        db_if = self.visualiza_processos_L3[0]

        if db_if == 1:

            self.funcao_class_destruir_home()

        elif db_if ==2:
            print(2)

        elif db_if ==3:
            print(3)

        elif db_if ==4:
            print(4)

        elif db_if == 5:

            self.funcao_class_if_destruir_widget()

        elif db_if == 6:

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
                ProcessoRecurso,
                # cadastro 4
                ProcessoCadastro,
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
        #self.funcao_db_visualiar_tbprocessos()
        self.boleano_id = str(1)
        self.funcao_db_visualizar_tbprocesso()
        "update"
        self.funcao_db_update_tbprocessos_linha1()
        
        self.funcao_classdb_desconectar()

        "update"
        self.up_processo_l3 =str(1)
        self.funcao_update_processo_home_l3()
        


#**************************************************
###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()