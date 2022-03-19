                 
from pacotes import *
#from estruturajanela.tamanhojanela import acf


################################################### função principal
                          # função de inicialização
def main():
    root = tk.Tk() # create a Tk root window
    
    WS = root.winfo_screenwidth() # width of the screen
    HS = root.winfo_screenheight() # height of the screen

    CALCULO_X = (WS/2) - (TAMANHO_WIDTH_JANELA/2)
    CALCULO_Y = (HS/2) - (TAMANHO_HEIGHT_JANELA/2)

    root.geometry('%dx%d+%d+%d' % (TAMANHO_WIDTH_JANELA, TAMANHO_HEIGHT_JANELA, CALCULO_X, CALCULO_Y))
                                   # função chamada
    

    menu_bar = MenuWidget()

                          # configurações da janela
    
    root.title      ("NOVA ALIANÇA")               # titulo da igreja
    root.iconbitmap ("imagem/ico.ico")             # ico
    root.configure(bg=COR_FUNDO_JANELA)                   # cor da fundo janela


    ###############################################
    root.mainloop() # starts the mainloop 


    
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
                    text    = INFORMACOES,
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
        
        #banco primarios
        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS Instituicao ( cod INTEGER PRIMARY KEY,
                                                    nome_igreja TEXT

            )
             """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS PROCESOSbarraapp(
                ID_barra INTERGER PRIMARY KEY,
                numero_barra INTEGER NOT NULL
                
            )
        """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS PROCESOSbarraapptext(
                ID_bar INTERGER PRIMARY KEY,
                text_barra text NOT NULL
                
            )
        """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS MEMBROS ( 
                ID_cod INTEGER  PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL UNIQUE)
                
                
        """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS ESTADOS ( 
                ID_EST INTEGER  PRIMARY KEY AUTOINCREMENT,
                Nome_EST TEXT NOT NULL UNIQUE)
                
                
        """)

        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS DATA_USUARIO ( 
                ID_data INTEGER  PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL UNIQUE)      
        """)

        #banco secundarios
        self.sql_cursor.execute("""
            CREATE TABLE IF NOT EXISTS ESTADO_CIVIL( 
                        ID_COD_ESTADO INTEGER PRIMARY KEY AUTOINCREMENT,
                        ID_casal_masculino INTEGER,
                        ID_casal_feminino INTEGER,
                        ID_solteiro INTEGER,
                        ID_aniversario INTEGER,
                        endereco TEXT,
                        informacao TEXT,
                        FOREIGN KEY (ID_casal_masculino) REFERENCES MEMBROS (ID_cod),
                        FOREIGN KEY (ID_casal_feminino) REFERENCES MEMBROS (ID_cod),
                        FOREIGN KEY (ID_solteiro) REFERENCES MEMBROS (ID_cod),
                        FOREIGN KEY (ID_aniversario) REFERENCES DATA_USUARIO (ID_data)
            )
        """)

        self.DB_desconectar()

    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################
class BancoExecucaoConfiguracoes():

    ############################################### inserir if none
    """instituicao"""
    def DBinserir_PROCESOSbarraapp(self):

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapp  VALUES (1, '"+str(NUM_1)+"')")
        self.DB_commit()

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapp  VALUES (2, '"+str(NUM_0)+"')")
        self.DB_commit()  

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapp  VALUES (3, '"+str(NUM_0)+"')")
        self.DB_commit() 

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapp  VALUES (4, '"+str(NUM_0)+"')")
        self.DB_commit() 

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapp  VALUES (4, '"+str(NUM_0)+"')")
        self.DB_commit() 

    "PROCESOSbarraapptext"
    def DB_inserir_PROCESOSbarraapptext(self):

        self.sql_cursor.execute("INSERT INTO PROCESOSbarraapptext  VALUES (1, '"+str(TEXT_THUE)+"')")
        self.DB_commit() 

    "Instituicao"
    def DB_inserir_N_AInstituicao(self):
            
        self.sql_cursor.execute( "INSERT INTO Instituicao VALUES (1, '"+NOME_NOVA_ALIANCA+"')")
        self.DB_commit()

    "membros"
    def inserir_membros(self,ins_1a):
              
        self.sql_cursor.execute( "INSERT INTO MEMBROS VALUES (NULL,'"+ins_1a+"')")
        self.DB_commit()

    "DATA_USUARIO"
    def inserir_datau(self,ins_data):
              
        self.sql_cursor.execute( "INSERT INTO DATA_USUARIO VALUES (NULL,'"+ins_data+"')")
        self.DB_commit()

    ############################################### visualizar dados 
    """instituicao"""
    def DB_visualizar_instituicao (self):
        
        self.sql_cursor.execute( "SELECT nome_igreja FROM Instituicao WHERE cod = 1")
        self.visualiza = self.sql_cursor.fetchone()

        if self.visualiza == None:

            self.DB_inserir_N_AInstituicao()

    """processo barra"""
    def DB_visualizar_PROCESOSbarraapp(self, id_numero_barra):
        
        self.sql_cursor.execute("SELECT numero_barra FROM PROCESOSbarraapp WHERE ID_barra = ?", (id_numero_barra,) )
        self.visualiza_barraapp = self.sql_cursor.fetchone()
    
    """processo interno"""
    def DB_visualizar_PROCESOSbarraapptext(self, id_numero_barra_t):

        self.sql_cursor.execute("SELECT text_barra FROM PROCESOSbarraapptext WHERE ID_bar = ?", (id_numero_barra_t,) )
        self.visualiza_sistema_interno = self.sql_cursor.fetchone()
    
    """ESTADOS"""
    def DB_visualizar_estados(self):

        self.sql_cursor.execute( "SELECT Nome_EST FROM ESTADOS")
        self.fc_cad = self.sql_cursor.fetchall()

    "membros"
    def DB_vizualizar_membros(self,visu_mb):

        self.sql_cursor.execute( "SELECT  ID_cod FROM MEMBROS WHERE Nome = ?", (visu_mb,))
        visualiza_membros = self.sql_cursor.fetchone()

        if visualiza_membros == None:

            self.inserir_membros(visu_mb)

    def DB_vizualizar_membros1(self,visu_mb1):

        self.sql_cursor.execute( "SELECT  ID_cod FROM MEMBROS WHERE Nome = ?", (visu_mb1,))
        visualiza_membros1 = self.sql_cursor.fetchone()

        if visualiza_membros1 == None:

            self.v_m_1 = None

        else:

            for row_vm1 in visualiza_membros1:

                self.v_m_1 = row_vm1

    def DB_vizualizar_membrosid(self,visu_mbid):

        self.sql_cursor.execute( "SELECT  Nome FROM MEMBROS WHERE Nome = ?", (visu_mbid,))
        visualiza_membrosid = self.sql_cursor.fetchone()

        for row_m in visualiza_membrosid:

            self.an1 = row_m

    "estado_civil"
    def DB_vizualizar_estadocivil(self,vis):

        self.sql_cursor.execute( "SELECT  ID_casal_masculino FROM ESTADO_CIVIL WHERE ID_casal_masculino = ?", (vis,))
        self.vis_st_civ = self.sql_cursor.fetchall()

    def DB_vizualizar_estadocivil_1(self,vis_1):

        self.sql_cursor.execute( "SELECT  ID_casal_feminino FROM ESTADO_CIVIL WHERE ID_casal_feminino = ?", (vis_1,))
        self.vis_st_civ_1 = self.sql_cursor.fetchall()

    def DB_vizualizar_estadocivil_2(self,vis_a1,vis_a2):

        self.sql_cursor.execute( "SELECT  ID_casal_masculino,ID_casal_feminino FROM ESTADO_CIVIL WHERE ID_casal_masculino = ? and ID_casal_feminino = ?", (vis_a1,vis_a2))
        self.vis_st_civ_12 = self.sql_cursor.fetchall()

    def DB_vizualizar_estadocivil_2_1(self,vis_a11,vis_a22):

        print("ab", vis_a11)
        print("ab2", vis_a22)

        self.sql_cursor.execute( "SELECT  ID_casal_masculino,ID_casal_feminino FROM ESTADO_CIVIL WHERE  ID_casal_masculino = ? and ID_casal_feminino = ?", (vis_a22,vis_a11))
        self.vis_st_civ_122 = self.sql_cursor.fetchall()


    "DATA_USUARIO"
    
    def DB_vizualizar_datausuario(self,visu_dat):

        self.sql_cursor.execute( "SELECT  data FROM DATA_USUARIO WHERE data = ?", (visu_dat,))
        vis_data_data = self.sql_cursor.fetchone()

        if vis_data_data == None:

            self.inserir_datau(visu_dat)
    
    def DB_vizualizar_datausuario1(self,visu_dat1):

        self.sql_cursor.execute( "SELECT  ID_data FROM DATA_USUARIO WHERE data = ?", (visu_dat1,))
        vis_data_data1 = self.sql_cursor.fetchone()

        for row_dat in vis_data_data1:

            self.dataus = row_dat
    ############################################### update
    """update tabelas"""
    def DB_update_PROCESOSbarraapp(self,up_barra):

        self.DB_connectar()

        sql_update_PROCESSObarra = """UPDATE PROCESOSbarraapp SET numero_barra = ? WHERE ID_barra = ?"""
        self.sql_cursor.execute(sql_update_PROCESSObarra, up_barra)
        self.DB_commit()
        
        self.DB_desconectar()

    def DB_update_PROCESOSbarraapptext(self,up_barra_t):

        self.DB_connectar()

        sql_update_PROCESSObarra_t = """UPDATE PROCESOSbarraapptext SET text_barra = ? WHERE ID_bar = ?"""
        self.sql_cursor.execute(sql_update_PROCESSObarra_t, up_barra_t)
        self.DB_commit()

        self.DB_desconectar()
        
        ############################################### upgrade
    
    
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

        self.DB_connectar()
        self.DB_visualizar_instituicao()

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
    
class ProcessoRecurso():                           # class recursos

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
class WidgetCadastro():                            # class cadastros

    """funcao principal"""
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
                    relief = "flat"  
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

        self.botao_4instituicao_CAD_INFOR= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = "CADASTRAR \n INFORMAÇÕES",
                    # negrito
                    font    ='Helvetica 13 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.COMMANDframe44_CadInf         
        )

        self.botao_4instituicao_CAD_INFOR.place(
                    x=CADASTRO_FRAME1X, y = 750, 

                    width=CADASTRO_FRAME1WIGHT, 
                    height= 50
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

    #6
    def STATE44_desativar_cad_inf(self):

        self.botao_4instituicao_CAD_INFOR["state"] = "disabled"

    def STATE44_ativar_cad_inf(self):

        self.botao_4instituicao_CAD_INFOR["state"] = "normal"

    ###############################################
    #sistema 4
    """botao 4"""
    def WIDGETframe44_cadastromembros(self):

        """botoes chamada da estrutura"""
        #barra principal

        self.botao_1cadastrar_cadastro_frame2= Button (
                    # cor botao
                    bg      = COR_FUNDO_1,          
                    text    = CADASTRAR, # MEMBROS
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita
                    fg      = COR_ESCRITA1,
                    # chamada         
                    command = self.COMMAND_WIDGET_cadastro_membros           

        )

        self.botao_1cadastrar_cadastro_frame2. place(
                    x=400, y = CADASTRO_FRAME2Y, 
                    
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
                    x= 860, y = CADASTRO_FRAME2Y, 
                    
                    width=CADASTRO_FRAME2W, height= CADASTRO_FRAME2H
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

    ###############################################

    """subprocessos"""
    "frame 2 cadastrar membros"
    def COMMAND_WIDGET_cadastro_membros(self):

        "label fixa"
        self.LABEL_NOME_1 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "NOME DO MEMBRO:",
                    # negrito
                    font    ='Helvetica 11 bold'
        )

        self.LABEL_NOME_1.place(
                    x= 250, y=270, 
                    
                    width= 160, height= 25
        )


        

        

        self.LABEL_NOME_4_INF = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "INFORMAÇÕES:",
                    # negrito
                    font    ='Helvetica 11 bold' 
        )

        self.LABEL_NOME_4_INF.place(
                    x= 250, y=420, 
                    
                    width= 120, height= 25
        )

        self.LABEL_NOME_5 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "ANIVERSÁRIO:",
                    # negrito
                    font    ='Helvetica 11 bold' 
        )

        self.LABEL_NOME_5.place(
                    x= 870, y=300, 
                    
                    width= 120, height= 25
        )

        self.LABEL_NOME_6 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "ENDEREÇO:",
                    # negrito
                    font    ='Helvetica 11 bold' 
        )

        self.LABEL_NOME_6.place(
                    x= 870, y=420, 
                    
                    width= 120, height= 25
        )

        ###$ tipo 2
        self.LABEL_NOME_1_1 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "* Escreva nome completo.",
                    # negrito
                    font    ='Helvetica 11 bold',

                    fg = "#FF0000"
        )

        self.LABEL_NOME_1_1.place(
                    x= 600, y=300, 
                    
                    width= 200, height= 25
        )

        
        ####### variaveis externas fixas

        "variaveis"
        self.entry_nome1 = Entry( # masculino
                                            
                    font    ='Helvetica 15', 
                    # formato da borda
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 1  
        )

        self.entry_nome1.place(
                    x=250, y= 325, 
                    width= 600, 
                    height= 30
        )

        

        self.entry_nome3 = Text(   # informações
                                            
                    font    ='Helvetica 15', 
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 1 
        )

        self.entry_nome3.place(
                    x=250, y= 450, 
                    width= 600, 
                    height= 90
        )

        self.entry_nome4_1 = DateEntry( # data aniversario
                                            
                    font    ='Helvetica 15',
                    date_partter =  'dd/mm/y',
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 1 
        )

        self.entry_nome4_1.place(
                    x=880, y= 325, 
                    width= 130, 
                    height= 30
        )

        self.valor_check = IntVar()
        check = Checkbutton(
                    text    = "SALVAR ANIVERSÁRIO",
                    variable=  self.valor_check,
                    font    ='Helvetica 10',
                    bg= COR_FUNDO_JANELA
        )

        check.place(

                    x=880, y= 370, 
                    width= 165, 
                    height= 25
        )

        self.valor_check_sol = IntVar()
        check_sol = Checkbutton(
                    text    = SOLTEIRO, # CHECKBUTTON
                    variable=  self.valor_check_sol,
                    font    ='Helvetica 15',
                    bg= COR_FUNDO_JANELA,
                    command= self.COMMAND_check_cad
        )

        check_sol.place(

                    x=600, y= 220, 
                    width= 150, 
                    height= 25
        )

        self.entry_nome5 = Text( # endereço
                                            
                    font    ='Helvetica 15',
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 1 
        )

        self.entry_nome5.place(
                    x=880, y= 450, 
                    width= 300, height= 90
        )

        self.atualizar_processo = CADASTRAR
        self.fixo = 0

        self.WIDGET_SECUNDARIA()

    def WIDGET_SECUNDARIA(self):

        ## label fixas
        self.LABEL_NOME_3 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "MASCULINO:",
                    # negrito
                    font    ='Helvetica 11 bold' 
        )

        self.LABEL_NOME_3.place(
                    x= 250, y=300, 
                    
                    width= 100, height= 25
        )

        self.LABEL_NOME_4 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "FEMININO:",
                    # negrito
                    font    ='Helvetica 11 bold' 
        )

        self.LABEL_NOME_4.place(
                    x= 245, y=360, 
                    
                    width= 90, height= 25
        )

        ### processo
        self.entry_nome2 = Entry( # feminino
                                            
                    font    ='Helvetica 15', 
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 1 
        )

        self.entry_nome2.place(
                    x=250, y= 385, 
                    width= 600, 
                    height= 30
        )

    def WIDGETfc_treeview(self):

        tv = ttk.Treeview(
                    columns = ("COD", "masc","fem","ani","end","inf"),
                    show= "headings"
        )

        tv.column("COD", minwidth= 30, width=40)
        tv.heading("COD", text= "ID")

        tv.column("masc", minwidth= 90, width=100)
        tv.heading("masc", text= "MASCULINO")

        tv.column("fem", minwidth= 90, width=100)
        tv.heading("fem", text= "FEMININO")

        tv.column("ani", minwidth= 90, width=100)
        tv.heading("ani", text= "ANIVERSÁRIO")

        tv.column("end", minwidth= 90, width=100)
        tv.heading("end", text= "ENDEREÇO")

        tv.column("inf", minwidth= 90, width=100)
        tv.heading("inf", text= "INFORMAÇÃO")

        tv.place(
                    x=220, y= 605, 
                    width= 1010, height= 185
        )

        self.scroll_tvv = ttk.Scrollbar(orient="vertical",command=tv.yview)
        tv.configure(yscrollcommand=self.scroll_tvv.set)
        self.scroll_tvv.place(x=1209, y= 606,width=20,height= 183)

        self.scroll_tvh = ttk.Scrollbar(orient="horizontal",command=tv.yview)
        tv.configure(yscrollcommand=self.scroll_tvh.set)
        self.scroll_tvh.place(x=221, y= 769,width=986,height= 20)

    def WIDGET_spinbox_cadastro_membros(self):

        self.DB_connectar()

        self.DB_visualizar_estados()

        if len(self.fc_cad) == NUM_0:

            self.LABELfcnomeInstituicao = Label ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = "SEM INFORMAÇÃO",
                    # negrito
                    font    ='Helvetica 10 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
            )

            self.LABELfcnomeInstituicao. place(
                    x      = 250, y      = 430, 
                    
                    width  = 130, height = 25
            )

        elif len(self.fc_cad) > NUM_0:
            
            lista_fc_sp = []

            for row in self.fc_cad:
                lista_fc_sp.append(row[0])

            spb_1 = Spinbox(
                    values = (lista_fc_sp),
                    font   = 'Helvetica 15'
            )

            spb_1.place(
                    x= 250, y=430, 
                    
                    width= 100, height= 30
            )
            
        self.DB_desconectar()

    def WIDGET_salvar_cadastro_menbros(self):

        self.botao_salvar_instituicao = Button ( 
                    # cor botao 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = TEXT_SALVAR, # MEMBROS-btn
                    # negrito
                    font    ='Helvetica 20 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
                    # chamada  
                    command = self.COMMAND4_db_membros_atsalvar

        )
        self.botao_salvar_instituicao. place(
                    x      = CADASTRO_SALVARX, y = CADASTRO_SALVARY, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )
        

    ###############################################
    #sistema5
    """botao 5"""
    def WIDGETframe44_sistemamembros(self):

        "fixo"
        #sistema
        #1
        self.LABELfixo_sistema2 = Label (
                    # cor botao
                    bg      = COR_FUNDO_2,
                    text    = "INFORMAÇÕES INSTITUIÇÃO",
                    # negrito
                    font    ='Helvetica 20 bold',

                    fg = COR_ESCRITA1

        )

        self.LABELfixo_sistema2.place(
                    x= FRAME2_500, y=FRAME2_55, 
                    
                    width= FRAME2_400, height= FRAME2_30
        )

        #2
        self.LABELfixo_sistema = Label ( 
                    bg     = COR_FUNDO_3, 
                    # formato da borda
                    relief = "flat"  
        )

        self.LABELfixo_sistema.place(
                    x = 190, y = 130, 
                    
                    width = TAMANHO_WIDTH_JANELA -200, height = 150
        )

        #3
        self.LABELfixo_sistema_nome = Label (
                    # cor botao
                    bg      = COR_FUNDO_3,
                    text    = CADAST_TEXT_NOME,
                    # negrito
                    font    ='Helvetica 13 bold',

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

        self.WIDGETfc_atualizar_instituicao()

        self.DB_connectar()
        # atualizar escrita label
        self.FC_dbvisualiar_instituicao()
        self.DB_desconectar()

        self.DB_update_PROCESOSbarraapp((NUM_1,NUM_4))
    """subprocesso"""

    def WIDGETfc_atualizar_instituicao(self):

        self.BOTAOfcInstituicao = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = TEXT_ATUALIZAR,
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
                    # chamada  
                    command = self.COMMAND_4instituicao_atualizar

        )

        self.BOTAOfcInstituicao. place(
                    x      = CADAST_BOTAO_INSTITUICAO_X, 
                    y      = CADAST_BOTAO_INSTITUICAO_Y, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )

    def WIDGETfc_salvar_instiuicao(self):

        "label fixo"
        self.LABELfixo_salvar = Label ( 
                    bg     = "#A9A9A9", 
                    # formato da borda
                    relief = "flat"  
        )

        self.LABELfixo_salvar.place(
                    x = 190, y = 350, 
                    
                    width = TAMANHO_WIDTH_JANELA -200, height = 150
        )

        self.LABELfcnomeInstituicao = Label ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = CADAST_TEXT_NOME,
                    # negrito
                    font    ='Helvetica 10 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
        )

        self.LABELfcnomeInstituicao. place(
                    x      = 200, y = 360, 
                    
                    width  = 190, height = 25
        )
        "botao"
        self.BOTAOfcvoltar = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = "VOLTAR",
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,     
                    # chamada  
                    command = self.COMMAND_4instituicao_voltar

        )

        self.BOTAOfcvoltar. place(
                    x      = CADAST_BOTAO_INSTITUICAO_X, 
                    y      = CADAST_BOTAO_INSTITUICAO_Y, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )

        self.BOTAOfcsalvar = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = TEXT_SALVAR, # instituicao-btn
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,    
                    # chamada  
                    command = self.COMMAND_4instituicao_salvar

        )

        self.BOTAOfcsalvar. place(
                    x      = 400, 
                    y      = CADAST_BOTAO_INSTITUICAO_Y, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )

        "entry"

        self.entry_banco_instituicao_cadastro = Entry(
                                            
                    font    ='Helvetica 11', 
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 1 

        )

        self.entry_banco_instituicao_cadastro.place(
                    x=200, y= 400,
                    width= 200, height= 30
        )

        self.DB_update_PROCESOSbarraapp((NUM_2,NUM_4))

    def WIDGETfc_salvar_aspasentry(self):

        self.LABELfcsalvar_entryaspas = Label ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = "INSIRA AS INFORMAÇÕES",
                    # negrito
                    font    ='Helvetica 11 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR   
        )

        self.LABELfcsalvar_entryaspas. place(
                    x      = 200, 
                    y      = 510, 
                    
                    width  = 200, 
                    height = 25
        )
    
    ###############################################
    #botao6
    def WIDGETframe44_cad_inf(self):

        "fixo"
        self.LABELfixo_cad_inf = Label (
                    # cor botao
                    bg      = COR_FUNDO_2,
                    text    = "CADASTRO GERAIS",
                    # negrito
                    font    ='Helvetica 20 bold',

                    fg = COR_ESCRITA1
        )

        self.LABELfixo_cad_inf.place(
                    x= FRAME2_500, y=FRAME2_55, 
                    
                    width= FRAME2_400, height= FRAME2_30
        )

        self.LABEL_banco1 = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = "BANCO:",
                    # negrito
                    font    ='Helvetica 13 bold', 
        )

        self.LABEL_banco1.place(
                    x= 235, y=130, 
                    
                    width= 100, height= 25
        )

        self.FCwidget_var_fixa_sist_cadastro()

        "variaveis"
        "processo 1"
        
        self.spb1_db = Spinbox(
                    values = ("ESTADOS"),
                    font   = 'Helvetica 15'
        )

        self.spb1_db.place(
                    x= 250, y=160, 
                    
                    width= 120, height= 30
        )

        self.BOTAO2_ci_gerais = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = CADASTRAR,  # CADASTRAR INFORMAÇÕES
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,        
                    # chamada  
                    command = self.COMMAND_IFfc_processo_estados_cadastrar

        )

        self.BOTAO2_ci_gerais. place(
                    x      = 500, y = 160, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )

        self.BOTAO3_ci_gerais = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = TEXT_ATUALIZAR,
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR        
                    # chamada  
                    #command = self.COMMAND_4instituicao_atualizar

        )

        self.BOTAO3_ci_gerais. place(
                    x      = 750, y = 160, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )

        self.BOTAO4_ci_gerais = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = 'EXCLUIR',
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR        
                    # chamada  
                    #command = self.COMMAND_4instituicao_atualizar

        )

        self.BOTAO4_ci_gerais. place(
                    x      = 1000, y = 160, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )

        self.BOTAO5_ci_geraissl = Button ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = TEXT_SALVAR,
                    # negrito
                    font    ='Helvetica 15 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR,       
                    # chamada  
                    command = self.COMMAND_4_iffc_salvar_lista

        )

        self.BOTAO5_ci_geraissl. place(
                    x      = CADASTRO_SALVARX, y = CADASTRO_SALVARY, 
                    
                    width  = CADAST_BOTAO_INSTITUICAO_W, 
                    height = CADAST_BOTAO_INSTITUICAO_H
        )
        
        self.WIDGETfc_listabox_cad_inf()
        self.STATE1_desativar_2_ci_gerais()
        self.WIDGETfc_cadastrar_exe()

    def STATE1_desativar_2_ci_gerais(self):

        self.BOTAO2_ci_gerais["state"] = "disabled"

    def STATE1_ativar_2_ci_gerais(self):

        self.BOTAO2_ci_gerais["state"] ="normal"

    def WIDGETfc_listabox_cad_inf(self):

        self.DB_connectar()
        
        self.DB_visualizar_estados()

        self.LB_1 = Listbox(
                    bg = COR_FUNDO_1,
                    font    ='Helvetica 15 bold',
                    # formato da borda
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 3      
        )

        self.LB_1.place(
                    x = 600, y = 600, 
                    
                    width  = 300, height = 193
        )

        lista_fc_cad = []
        if len(self.fc_cad) == NUM_0:


            self.LB_1.insert(END, "SEM INFORMAÇÕES","       NO BANCO" )

        elif len(self.fc_cad) > NUM_0:

            for row in self.fc_cad:
                lista_fc_cad.append(row[0])

            for lis in lista_fc_cad:
                self.LB_1.insert(END, lis)        

        self.DB_desconectar()
        
        self.scroll = ttk.Scrollbar(orient="vertical",command=self.LB_1.yview)
        self.LB_1.configure(yscrollcommand=self.scroll.set)
        self.scroll.place(x=875, y= 605,width=20,height= 183)

    def WIDGETfc_cadastrar_exe(self):

        "fixo"
        self.LABELfixo_cad_inf_sr = Label (
                    bg      = COR_FUNDO_JANELA,
                    text    = "SIGLA DA REGIÃO:",
                    # negrito
                    font    ='Helvetica 11 bold'
        )

        self.LABELfixo_cad_inf_sr.place(
                    x= 250, y=300, 
                    
                    width= 135, height= 20
        )

        "varivaeis"
        self.entry_exe_part1 = Entry(
                                            
                    font    ='Helvetica 15', 
        )

        self.entry_exe_part1.place(
                    x=250, y= 330, 
                    width= 200, height= 25
        )


    #### variaveis entre sistemas
    def FCwidget_var_fixa_sist_cadastro(self):

        self.LABEL_fixo_processo= Label (
                    # cor de fundo -DeepSkyBlue
                    bg = COR_FUNDO_JANELA,  

                    # formato da borda
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 10       
        )      
                                
        self.LABEL_fixo_processo.place(
                    x = 200,  y= 250, 

                    width = TAMANHO_WIDTH_JANELA- 250, 
                    height = TAMANHO_HEIGHT_JANELA - 290
        )

        self.LABEL_fixo_processo_1= Label (
                    # cor de fundo -DeepSkyBlue
                    bg = COR_FUNDO_JANELA,  

                    # formato da borda
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 4       
        )      
                                
        self.LABEL_fixo_processo_1.place(
                    x = 210,  y= 595, 

                    width = 1030, 
                    height = 205
        )

        self.LABEL_fixo_processo_2= Label (
                    # cor de fundo -DeepSkyBlue
                    bg = COR_FUNDO_JANELA,  

                    # formato da borda
                    relief      ="solid", 
                    # tamanho da borda
                    borderwidth = 4       
        )      
                                
        self.LABEL_fixo_processo_2.place(
                    x = 210,  y= 550, 

                    width = 1030, 
                    height = 50
        )

    def WIDGET_fc_processo_salvar(self):

            self.LABELfcsal_1_entryaspas = Label ( 
                    # cor botao - 
                    bg      = COR_BOTAO_FUNDO,          
                    text    = "INSIRA O NOME DOS USUÁRIOS",
                    # negrito
                    font    ='Helvetica 11 bold', 
                    # cor escrita - Yellow
                    fg      = COR_ESCRITA_MENU_BAR   
            )

            self.LABELfcsal_1_entryaspas. place(
                    x      = 430, 
                    y      = 560, 
                    
                    width  = 250, 
                    height = 25
            )


class BancoCadastro():                             # class cadastro

    def FC_WIDGETframe44_processo_banco(self):
        
        # update linha4 tbprocessos
        self.DB_update_PROCESOSbarraapp((NUM_1,NUM_2))

        #state desativar
        self.STATE44_desativar_banco()

    def COMMAND_4_iffc_salvar_lista(self):

        list_salvar = self.spb1_db.get()

        if list_salvar == "ESTADOS":

            try:
                entry_ver_for_1 = str(self.entry_exe_part1.get())

                if entry_ver_for_1 == "":

                    print(1504)

                else:
                    self.DB_connectar()
            
                    entry_ins_1 = str(self.entry_exe_part1.get())

                    self.sql_cursor.execute("INSERT INTO  ESTADOS VALUES (NULL,'"+entry_ins_1+"')")
                    self.DB_commit()
           
                    self.DB_desconectar()
                    self.WIDGETfc_listabox_cad_inf()
            
            except sqlite3.IntegrityError:
                print(1504.1)

    
class ProcessoCadastro():                          #class cadastro

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

        #tb processo barra app update linha 2
        self.DB_update_PROCESOSbarraapp((NUM_2,NUM_2))

        #state desativar
        self.STATE44_desativar_entradas()

    #3
    def COMMANDframe44_gastoscd(self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processos update linha 2
        self.DB_update_PROCESOSbarraapp((NUM_3,NUM_2))
        #state desativar
        self.STATE44_desativar_gastos()

    #4
    def COMMANDframe44_membroscd (self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processos update linha 2
        self.DB_update_PROCESOSbarraapp((NUM_4,NUM_2))
        
        #frame
        self.WIDGETframe44_cadastromembros()

        #widget externa fixas
        self.FCwidget_var_fixa_sist_cadastro()

        #widget
        self.COMMAND_WIDGET_cadastro_membros()
        #self.WIDGET_spinbox_cadastro_membros()
        self.WIDGET_salvar_cadastro_menbros()
        self.WIDGETfc_treeview()

        #state desativar
        self.STATE44_desativar_membros()

    #5
    def COMMANDframe44_instituicaocd(self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processos update linha 2
        self.DB_update_PROCESOSbarraapp((NUM_5,NUM_2))

        # widget
        self.WIDGETframe44_sistemamembros()

        #state desabilitar
        self.STATE44_desativar_instituicao()

    #6
    def COMMANDframe44_CadInf(self):

        self.DB_connectar()
        self.DESTROIR4_internoif_widget_cadastro()
        self.DB_desconectar()

        #tb processos update linha 4
        self.DB_update_PROCESOSbarraapp((NUM_6,NUM_2))

        #widget
        self.WIDGETframe44_cad_inf()

        #state desabilitar
        self.STATE44_desativar_cad_inf()

    "frame 2 membros cadastrar"
    def COMMAND4_db_membros_atsalvar(self):
            
        insertmembros  = str(self.entry_nome1.get())
        #insertmembros2 = str(self.entry_nome2.get())
        insertend      = str(self.entry_nome5.get("1.0",END))
        insertdatau    = str(self.entry_nome4_1.get())
        insertinf      = str(self.entry_nome3.get("1.0",END))
        insertcheck    = self.valor_check.get()
        bool_check     = self.valor_check_sol.get()

        if bool_check == 0:
            print("as1")

        elif bool_check == 1:

            print("as2")

        
        
        '''if insertmembros == "" and insertmembros2 == "":

            self.DB_connectar()

            self.DB_visualizar_PROCESOSbarraapptext(NUM_1)
            v_db_1 = self.visualiza_sistema_interno[0]

            if v_db_1 == TEXT_THUE:

                #label temporaria
                self.WIDGET_fc_processo_salvar()

                self.LABELfcsal_1_entryaspas.after(4000, self.FC_destruir_tp)

                #update
                self.DB_update_PROCESOSbarraapptext((TEXT_FALSE,NUM_1))

            self.DB_desconectar()
        
        elif insertmembros == insertmembros2:

            print("nao auotizado palavras nomes repetidos")
        else:
                        
            self.DB_connectar()

            self.DB_vizualizar_membros1(insertmembros)
            vis_mem_var = self.v_m_1

            self.DB_vizualizar_membros1(insertmembros2)
            vis_mem_var1 = self.v_m_1

            self.DB_desconectar()

            if vis_mem_var == None and vis_mem_var1 == None:

                print("ativado")

            else:
                
                self.DB_connectar()
                


                self.DB_vizualizar_estadocivil_2(vis_mem_var, vis_mem_var1)
                print("f",len(self.vis_st_civ_12))
                #print(self.vis_st_civ_12)

                asd = len(self.vis_st_civ_12)
                print("lem",asd)

                self.DB_desconectar()

                self.DB_connectar()

                self.DB_vizualizar_membros1(insertmembros)
                vis_mem_var_elm = self.v_m_1

                self.DB_vizualizar_membros1(insertmembros2)
                vis_mem_var1_elf = self.v_m_1

                self.DB_vizualizar_estadocivil_2_1(vis_mem_var_elm, vis_mem_var1_elf)
                print(vis_mem_var_elm)
                print(vis_mem_var1_elf)
                print(len(self.vis_st_civ_122))
                #print(self.vis_st_civ_12)

                asd1 = len(self.vis_st_civ_122)
                print(asd1) '''

        '''self.DB_vizualizar_estadocivil(vis_mem_var)
                print("estado",len(self.vis_st_civ))'''

        '''self.DB_desconectar()

                if asd == 0 and asd1 == 0 :

                    print("ativado1")
                
                else:
                    print("nao ativado")

            

                #if insertmembros != "" and insertmembros2 != "":'''

        '''self.DB_vizualizar_estadocivil(vis_mem_var)
                    print("estado",len(self.vis_st_civ))

                    self.DB_vizualizar_estadocivil_1(vis_mem_var1)
                    print("estados",len(self.vis_st_civ_1))
                    self.DB_vizualizar_membros1("")
                    vis_a = self.v_m_1'''

        '''print(len((self.vis_st_civ or self.vis_st_civ_1) != vis_a ))
                
                    print((self.vis_st_civ or self.vis_st_civ_1) != vis_a)'''

                


        '''self.DB_vizualizar_membros1("")
                vis_a = self.v_m_1
                print("vis",vis_a)
                self.DB_vizualizar_estadocivil(vis_a)
                print("teste",len(self.vis_st_civ))
                for row in self.vis_st_civ:
                    #print(row)
                    print("p1",row[0],"p2",row[1])
                    #print("p2",row[1])

                if len(self.vis_st_civ) != 0 and len(self.vis_st_civ_1) != 0:

                    print("ok")'''

    '''self.DB_vizualizar_membros(insertmembros)
            self.DB_vizualizar_membros(insertmembros2)

            self.DB_vizualizar_membrosid(insertmembros)
            vis_an1_1 = self.an1
            
            self.DB_vizualizar_membrosid(insertmembros2)
            vis_an1_2 = self.an1

            if insertcheck == 0:

                db_3est1 = ""

            elif insertcheck == 1:
                self.DB_vizualizar_datausuario(insertdatau)

                self.DB_vizualizar_datausuario1(insertdatau)
                db_3est1 = self.dataus

            

            self.sql_cursor.execute( "INSERT INTO ESTADO_CIVIL VALUES (NULL,'"+str(vis_an1_1)+"','"+str(vis_an1_2)+"','"+str(db_3est1)+"','"+insertend+"','"+insertinf+"')")
            self.DB_commit()

            
            

            #elif insertmembros == "" and insertmembros2 != "":
                #print(1)

            #elif insertmembros != "" and insertmembros2 == "":
                #print(2)'''
        # Exception as Erro:
            #print(Erro.__class__)

    def FC_dbvisualiar_instituicao(self):

        self.DB_visualizar_instituicao()
        var_db_visual_instituicao = self.visualiza[0]

        self.LABELvariavel_sistema_nome.configure(text=var_db_visual_instituicao)

    def COMMAND_4instituicao_atualizar(self):

        #destruir botao atualizar
        self.BOTAOfcInstituicao.destroy()

        self.WIDGETfc_salvar_instiuicao()
    
    def COMMAND_4instituicao_voltar(self):

        "destroy"
        self.DESTROY_cadastro_parte2_intituicao()
        
        "chamar botao atualizar de volta"
        self. WIDGETfc_atualizar_instituicao()

        " update banco linha 4"
        self.DB_update_PROCESOSbarraapp((NUM_1,NUM_4))

        self.FC_destruir_aspas()

    def COMMAND_4instituicao_salvar(self):

        up_banco_instituicao = str(self.entry_banco_instituicao_cadastro.get())

        if up_banco_instituicao == "":

            self.DB_connectar()

            self.DB_visualizar_PROCESOSbarraapptext(NUM_1)
            visual_processos_t = self.visualiza_sistema_interno[0]

            if visual_processos_t == TEXT_THUE:

                #label temporaria
                self.WIDGETfc_salvar_aspasentry()

                self.LABELfcsalvar_entryaspas.after(4000, self.FC_destruir_aspas)

                #update
                self.DB_update_PROCESOSbarraapptext((TEXT_FALSE,NUM_1))
            self.DB_desconectar()

        else:

            self.DB_connectar()

            self.sql_cursor.execute("UPDATE Instituicao SET nome_igreja ='"+up_banco_instituicao+"' WHERE cod = 1")
            self.DB_commit()

            # atualizar escrita label
            self.FC_dbvisualiar_instituicao()

            # atualizar banco PROCESOSbarraapptext
            self.FC_destruir_aspas()

            self.DB_desconectar()

    def COMMAND_IFfc_processo_estados_cadastrar(self):

        spb1_db_get = self.spb1_db.get()

        if spb1_db_get == "ESTADOS":

            self.WIDGETfc_listabox_cad_inf()
            self.WIDGETfc_cadastrar_exe()

    def COMMAND_check_cad(self):
        
        if self.atualizar_processo == CADASTRAR:
            
            if self.fixo == 0:
                self.fixo = 1
            
                self.DESTROY_widget_casados()

                self.LABEL_sol_if = Label (
                    # cor botao
                    bg      = COR_FUNDO_JANELA,
                    text    = SOLTEIRO, # LABEL
                    # negrito
                    font    ='Helvetica 11 bold' 
                )

                self.LABEL_sol_if.place(
                    x= 245, y=300, 
                    
                    width= 100, height= 25
                )

            elif self.fixo == 1:

                self.fixo = 0

                self.LABEL_sol_if.destroy()

                self.WIDGET_SECUNDARIA()

                
                
        
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

        elif db_if_viasualizar == NUM_4: # membros

            #ativar
            self.STATE44_ativar_membros()

            #destroy
            self.botao_1cadastrar_cadastro_frame2.destroy()
            self.botao_2atualizar_cadastro_frame2.destroy()
            self.botao_3informacoes_cadastro_frame2.destroy()

        elif db_if_viasualizar == NUM_5: # Instituicao

            #reativar
            self.STATE44_ativar_instituicao()

            #destroy parte 1

            self.LABELfixo_sistema2.destroy()
            self.LABELfixo_sistema.destroy()
            self.LABELfixo_sistema_nome.destroy()

            self.LABELvariavel_sistema_nome.destroy()

            self.DB_connectar()

            self.DB_visualizar_PROCESOSbarraapp(NUM_4)
            db_if_viasualizar_1 = self.visualiza_barraapp[0]

            if db_if_viasualizar_1 == 1:

                self.BOTAOfcInstituicao.destroy()

            elif db_if_viasualizar_1 == 2:

                self.FC_destruir_aspas()
                self.DESTROY_cadastro_parte2_intituicao()
        
        elif db_if_viasualizar == NUM_6: # cadastro informação

            #reativar
            self.STATE44_ativar_cad_inf()

            #destroy parte 1
            self.LABELfixo_cad_inf.destroy()
            self.LABEL_fixo_processo.destroy()
            self.LABEL_fixo_processo_1.destroy()
            self.LABEL_fixo_processo_2.destroy()
            self.LABEL_banco1.destroy()
            self.spb1_db.destroy()
            self.BOTAO2_ci_gerais.destroy()
            self.BOTAO3_ci_gerais.destroy()
            self.BOTAO4_ci_gerais.destroy()
            self.BOTAO5_ci_geraissl.destroy()

            self.DESTROY_cadastro_par2_processo_interno()

    def DESTROY_cadastro_par2_processo_interno(self):

        self.LABELfixo_cad_inf_sr.destroy()
        self.entry_exe_part1.destroy()
        self.LB_1.destroy()
        self.scroll.destroy()

    def DESTROY_cadastro_parte2_intituicao(self):

        "destroy"
        self.LABELfixo_salvar.destroy()
        self.LABELfcnomeInstituicao.destroy()

        self.BOTAOfcInstituicao.destroy()
        self.BOTAOfcvoltar.destroy()
        self.BOTAOfcsalvar.destroy()
        
        self.entry_banco_instituicao_cadastro.destroy()

    def FC_destruir_aspas(self):

        self.FC_if_dbprocessotext_destroy()

        self.DB_update_PROCESOSbarraapptext((TEXT_THUE,NUM_1))
        

    def FC_if_dbprocessotext_destroy(self):

        self.DB_connectar()
        
        self.DB_visualizar_PROCESOSbarraapptext(NUM_1)
        visual_processos_td2 = self.visualiza_sistema_interno[0]

        if visual_processos_td2 == TEXT_FALSE:

            self.LABELfcsalvar_entryaspas.destroy()

        self.DB_desconectar()

    def FC_destruir_tp(self):

        self.FC_if_dbprocessotext_destroy_1()

        self.DB_update_PROCESOSbarraapptext((TEXT_THUE,NUM_1))

    def FC_if_dbprocessotext_destroy_1(self):

        self.DB_connectar()
        
        self.DB_visualizar_PROCESOSbarraapptext(NUM_1)
        v_0tp = self.visualiza_sistema_interno[0]

        if v_0tp == TEXT_FALSE:

            self.LABELfcsal_1_entryaspas.destroy()

        self.DB_desconectar()

    def DESTROY_widget_casados(self):

        self.LABEL_NOME_3.destroy()
        self.LABEL_NOME_4.destroy()
        self.entry_nome2.destroy()

class ProcessoConfiguracoes():

    def COMMAND1_configuracoes(self):       #funcao inicializacao configurações

        # destruir externamente
        self.DESTROIR_externoif_widget_barra()

        # atualizar banco
        self.DB_update_PROCESOSbarraapp((NUM_5,NUM_1))
             
        #state desativar configuracao
        self.STATE1_desativar_configuracoes()

    
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

        elif db_if ==NUM_4: # cadastro
            
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
            self.botao_4instituicao_CAD_INFOR.destroy()

            # update tb processobarraapp lonha 4
            self.DB_update_PROCESOSbarraapp((NUM_0,NUM_2))

        elif db_if == NUM_5: #configurações
            
            # ativar botao
            self.STATE1_ativar_configuracoes()
            

        elif db_if == NUM_6: # informações
            
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
                #DestruirHomeExterno,
                #projetos 2
                ProcessoProjetos,
                # recursos 3
                WidgetRecursos,
                ProcessoRecurso,
                # cadastro 4
                WidgetCadastro,
                BancoCadastro,
                ProcessoCadastro,
                CadastroDestroy,
                #configurações 5
                #WidgetConfiguracoes, #widget
                ProcessoConfiguracoes,
                #ConfiguracaoDestruir,
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
        self.fcmi_seguranca_PROCESOSbarraapp()
        self.fcmi_seguranca_PROCESOSbarraapptext()

        self.fCmi_visualizar_instituicao()

        ########################################### classe externa
        #menus fixos
        self.WIDGET_barra_menus_principal()
        
        #home
        self.funcao_class_visual_instituicao()

        self.funcao_class_visualdb_barra_intituicao()

        #state
        self.STATE1_desativar_home()  

    def fcmi_seguranca_PROCESOSbarraapp(self):

        self.DB_connectar()
        self.sql_cursor.execute("SELECT numero_barra  FROM PROCESOSbarraapp ")
        visualizar_idbarra = self.sql_cursor.fetchall()

        if len(visualizar_idbarra) == NUM_0:
            self.DBinserir_PROCESOSbarraapp()

        elif len(visualizar_idbarra) <NUM_4:
            
            self.sql_cursor.execute("DELETE FROM PROCESOSbarraapp")
            self.DB_commit()

            self.DBinserir_PROCESOSbarraapp()

        self.DB_desconectar()

        "update"
        #barra principal
        self.DB_update_PROCESOSbarraapp((NUM_1,NUM_1))
        #subbarra
        self.DB_update_PROCESOSbarraapp((NUM_0,NUM_2))

        self.DB_update_PROCESOSbarraapp((NUM_0,NUM_4))

    def fcmi_seguranca_PROCESOSbarraapptext(self):

        self.DB_connectar()
        self.sql_cursor.execute("SELECT text_barra  FROM PROCESOSbarraapptext ")
        visualizar_idtext = self.sql_cursor.fetchall()

               
        if len(visualizar_idtext) == NUM_0:
            self.DB_inserir_PROCESOSbarraapptext()

        # novo processo
        self.DB_desconectar()

        # update
        self.DB_update_PROCESOSbarraapptext((TEXT_THUE,NUM_1))

    def fCmi_visualizar_instituicao(self):
        
        self.DB_connectar()
         
        "visualizar"
        self.DB_visualizar_instituicao()  
        
        self.DB_desconectar()

        
#**************************************************
###################################################
                              # somente uma entrada
if __name__ == '__main__':
    main()