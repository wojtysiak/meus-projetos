from conexão_banco import cursor,conexao
import flet as ft
import funções
import sys
import time
from datetime import datetime

class Usuario_no_Banco():
    def __init__(self, Usuario_do_banco):
        self.id = Usuario_do_banco[0]
        self.nome = Usuario_do_banco[1]
        self.Cpf = Usuario_do_banco[2]
        self.login = Usuario_do_banco[3]
        self.status = Usuario_do_banco[5]
        self.funcao = Usuario_do_banco[6]
        self.nivel_de_acesso = Usuario_do_banco[7]
        




class Tela_de_login(ft.Column):
    def __init__(self, page, callback):
        super().__init__()
        self.mensagem_de_erro = ft.Text(value=None)
        self.main_page = page
        self.callback_sucesso = callback
        self.login = ft.TextField(label="usuario")
        self.senha = ft.TextField(label="senha", password=True, can_reveal_password=True, on_submit=self.checar_login)
        self.horizontal_alignment = ft.VerticalAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.sair = ft.FloatingActionButton(content='ENCERRAR APLICAÇÃO',on_click=sys.exit,width=300)


        self.controls=[
                        self.login,
                        self.senha,
                        ft.FloatingActionButton(
                        icon=ft.Icons.LOGIN, 
                        on_click=self.checar_login,width=300),
                        self.sair,
                        self.mensagem_de_erro,]
    def checar_login(self,e):
        
        self.mensagem_de_erro.value = None
        
        usuario = self.login.value.strip()
        senha = self.senha.value.strip()

        if not self.login.value or not self.senha.value:
            self.login.helper = None
            self.senha.helper = None
            self.main_page.update()
            
            if not self.login.value and not self.senha.value:
                self.mensagem_de_erro.value = 'Verifique os campos obrigatórios'
                self.main_page.update()
                return
            elif not self.login.value:
             
             self.login.helper ="usuário obrigatório" 
            elif not self.senha.value:
                self.senha.helper = "Senha obrigatória" 

            self.main_page.update()
            return
        

        

        status, resultado = funções.checar_senha(Tentativa_de_senha=senha,login=usuario)
        

        if status == False:
            self.login.helper = None
            self.senha.helper = None
            self.mensagem_de_erro.value = "Usuário ou senha inválidos"
            self.main_page.update()
            return
        
    
        Login = Usuario_no_Banco(resultado)
        
            
        if resultado[5] == "INATIVO":
            self.login.helper = None
            self.senha.helper = None
            self.mensagem_de_erro.value = 'Esse usuário está inativo'
            self.main_page.update()
            print(self.mensagem_de_erro.value)
        else:
            self.login.helper = None
            self.senha.helper = None
            
            self.mensagem_de_erro.visible=False
            self.nome = resultado[1]
            self.cpf = resultado[2]
            self.cargo = resultado[6]
            self.nivel_de_acesso = resultado[7]
            self.callback_sucesso(Login)
            self.main_page.update()

            
            

class Botoes(ft.Column):
    def __init__(self, nivel_usuario, callback):
        super().__init__()
        self.nivel = nivel_usuario
        self.callback = callback
        self.sair = ft.FloatingActionButton(content='ENCERRAR APLICAÇÃO',on_click=sys.exit,width=300)

        self.configurar_botoes = {
            'INICIAR VENDA': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'CADASTRAR NOVO COLABORADOR': ['GERENTE'],
            'CONSULTAR CADASTRO DE COLABORADOR': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'RELATÓRIO DE VENDAS MENSAIS': ['SUPERVISOR','GERENTE'],
            'RELATÓRIO DE VENDAS PERSONALIZADAS': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'CONSULTAR SERVIÇOS': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'CONSULTAR CLIENTES': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'CANCELAR VENDA': ['GERENTE'],
            'CADASTRAR O.S': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'CONSULTAR ESTOQUE': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'ALTERAR SENHA': ['SUPERVISOR','VENDEDOR','GERENTE'],
            'SAIR': ['SUPERVISOR','VENDEDOR','GERENTE'],
    
        }

        self.controls=self.controles_gerados()
    def controles_gerados(self):
        Botoes_gerados = []



        for botao, nivel_de_acesso in self.configurar_botoes.items():
            if self.nivel in nivel_de_acesso:
                btn = ft.FloatingActionButton(content= botao,
                    on_click=lambda e, n=botao: self.callback(n),
                    width=300
                )
                Botoes_gerados.append(btn)
        Botoes_gerados.append(self.sair)
        return Botoes_gerados
    


class Alterar_Senha(ft.Column)      :
    def __init__(self, page, callback, Usuario):
        super().__init__()
        self.main_page = page
        self.callback = callback
        self.usr = Usuario
        
        
        

        self.usuario = ft.Text(f'*Usuario: {self.usr.nome}*')

        
        self.senha = ft.TextField(
            label='Nova Senha',
            password=True,
            can_reveal_password=True,
            width=300
        )
        self.Confirmar_senha = ft.TextField(
            label='Confirme sua senha',
            password=True,
            can_reveal_password=True,
            width=300,
            on_submit=self.valid
        
        )
        self.botao_de_confirmacao = ft.ElevatedButton(
            content="Confirmar Alteração",
            width=200,
            on_click=self.valid  
        )
        self.mensagem = ft.Text(
            value="",
            color="red",
            visible=False,
            size=16,
            weight='bold'
        )

        
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Text("Alterar Senha do Sistema", size=20, weight="bold"),
            self.usuario,
            self.senha,
            self.Confirmar_senha,
            self.mensagem,
            self.botao_de_confirmacao
        ]

    
    def valid(self, e):
        
        if not self.senha.value or not self.Confirmar_senha.value:
            self.mensagem.value = "Preencha todos os campos!"
            self.mensagem.visible = True
            self.update()
            return

       
        if self.senha.value != self.Confirmar_senha.value:
            self.mensagem.value = "As senhas não conferem!"
            self.mensagem.visible = True
            self.update()
        else:
            self.mensagem.value = "Senha alterada Com sucesso, Você será redirecionado para pagina principal"
            self.mensagem.color = 'Green'
            self.mensagem.visible = True
            self.update()
            print("Senhas conferem! Enviando para o banco...")
            self.callback(self.senha.value)
            

       

class New_User(ft.Column):
    def  __init__(self, page,):
        super().__init__()
       
        self.main_page = page
        self.Nome = ft.TextField(label='Nome', width=600)
        self.Cpf = ft.TextField(label='Cpf',width=600,hint_text='00000000000',max_length=11, helper="Digite sem sinalização",input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9]*$",replacement_string=""))
        self.login = ft.TextField(label='login',width=600)
        self.senha = ft.TextField(label='Senha', password=True,can_reveal_password=True,width=600)
        self.status = ft.Dropdown(width=220,hint_text="Situação ",options=[ft.DropdownOption(key="ATIVO", text="ATIVO"),ft.DropdownOption(key="INATIVO", text="INATIVO")])
        self.funcao = ft.Dropdown(width=220,hint_text="Função",options=[ft.DropdownOption(key="GERENTE", text="GERENTE"),ft.DropdownOption(key="VENDEDOR", text="VENDEDOR"),ft.DropdownOption(key="TECNICO", text="TECNICO")])
        self.Nivel_de_acesso = ft.Dropdown(width=220,hint_text="Função",options=[ft.DropdownOption(key="GERENTE", text="GERENTE"),ft.DropdownOption(key="VENDEDOR", text="VENDEDOR"),ft.DropdownOption(key="SUPERVISOR", text="SUPERVISOR")])
        self.mensagem = ft.Text(visible=False,value='Verifique os campos inválidos e tente novamente',color="red")
        self.botao = ft.FloatingActionButton(icon=ft.Icons.SEND,on_click=self.Validar,width=600,content='Cadastrar Usuário')
        
        
        self.controls = [
                self.Nome,self.Cpf,self.login,self.senha,
                self.status,self.funcao,self.Nivel_de_acesso,
                self.mensagem,self.botao
        ]

    def Validar(self,e):


        if not self.Nome.value:
            self.Nome.error = 'Este campo é obrigatório'
            self.mensagem.visible = True
            self.update()
            return
        else:
            self.Nome.error = None
            self.update()
        if len(self.Cpf.value) < 11:
            self.Cpf.error = 'Cpf invalido, verifique e tente novamente'
            self.mensagem.visible = True
            self.update()
            return
        else:
            self.Cpf.error = None
            self.update()   
        if not self.login.value:
            self.login.error = 'Este campo é obrigatório'
            self.mensagem.visible = True
            self.update()
            return
        else:
            self.login.error = None
            self.update()    
        if not self.senha.value:
            self.senha.error = 'Este campo é obrigatório'
            self.mensagem.visible = True
            self.update()
            return
        else:
            self.senha.error = None
            self.update()

        if not self.status.value:
            self.status.error_text='*CAMPO OBRIGATÓRIO*'
            self.mensagem.visible = True
            self.update()
            return
        else:
            self.status.error_text=None
            self.update()

        if not self.funcao.value:
            self.funcao.error_text='*CAMPO OBRIGATÓRIO*'
            self.mensagem.visible = True
            self.update()
            return  
        else:
            self.funcao.error_text=None
            self.update()


        if not self.Nivel_de_acesso.value:
            self.Nivel_de_acesso.error_text ='*CAMPO OBRIGATÓRIO*'
            self.mensagem.visible = True
            self.update()
        else:
            self.Nivel_de_acesso.error_text = None
            self.update()


        

        self.mensagem.visible = False
        self.update()


        dados, retorno = funções.cadastrar_novo_usuario(Nome_Completo=self.Nome.value.strip(),
                                       Cpf=self.Cpf.value.strip(),
                                       Login=self.login.value.strip(),
                                       Senha=self.senha.value.strip(),
                                       Status_do_usuario=self.status.value.strip(),
                                       Funcao=self.funcao.value.strip(),
                                       Nivel_De_Acesso=self.Nivel_de_acesso.value.strip())
        
        if dados:
            self.mensagem.value = f'{retorno} Você será redirecionado para pagina principal'
            self.mensagem.color = "Green"
            self.mensagem.visible = True
            
            self.callback(e)
            
            

            self.update()
        elif retorno != 'Cpf ou usuário já cadastrado':
            print(retorno)
            self.mensagem.value = "Verifique os campos obrigatórios e tente novamente"
            self.mensagem.color = "red"
            self.mensagem.visible = True
            
            self.update()
        else:
            self.mensagem.value = f'*{retorno}*'
            self.mensagem.color = "yellow"
            self.mensagem.visible = True
            self.update()


class Consulta_de_cadastro(ft.Column):
    def __init__(self,page):
        super().__init__()
        
        mensagem = ft.Text()
        self.Nome = ft.TextField(label='NOME')
        self.Cpf = ft.TextField(label='CPF',width=600,hint_text='00000000000',max_length=11, helper="Digite sem sinalização",input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",replacement_string=""))
        self.login = ft.TextField(label='LOGIN')
        self.status = ft.Dropdown(width=220,hint_text="Situação ",options=[ft.DropdownOption(key="ATIVO", text="ATIVO"),ft.DropdownOption(key="INATIVO", text="INATIVO")])
        self.funcao = ft.Dropdown(width=220,hint_text="Função",options=[ft.DropdownOption(key="GERENTE", text="GERENTE"),ft.DropdownOption(key="VENDEDOR", text="VENDEDOR"),ft.DropdownOption(key="TECNICO", text="TECNICO")])
        self.Nivel_de_acesso = ft.Dropdown(width=220,hint_text="Função",options=[ft.DropdownOption(key="GERENTE", text="GERENTE"),ft.DropdownOption(key="VENDEDOR", text="VENDEDOR"),ft.DropdownOption(key="SUPERVISOR", text="SUPERVISOR")])
        self.Botao = ft.FloatingActionButton(icon=ft.Icons.SEND,content="CONSULTAR",on_click=self.consultar)
    
        self.controls = [
            self.Cpf,
            self.Botao
        ]
        


        
    def consultar(self):
        if self.Cpf.value:
            retorno = funções.consultar_cadastro(self.Cpf.value)
            print(retorno[1])
            # self.Nome.value = retorno[1]
            # self.Cpf.value = retorno[2]
            # self.login = retorno[3]
            # self.status.hint_text=retorno[5]
            # self.funcao.hint_text=retorno[6]
            # self.Nivel_de_acesso.hint_text = retorno[7]
            self.page.clean()
    

    
class Tela_de_vendas(ft.Column):
    def __init__(self,page):
        super().__init__()   
        def nascimento(e: ft.Event[ft.DatePicker]):
            return  
        self.nome_cliente = ft.TextField(label='Nome', width=600)
        self.Cpf =ft.TextField(label='CPF',width=600,hint_text='00000000000',max_length=11, helper="Digite sem sinalização",input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9]*$",replacement_string=""))
        self.Cnpj = ft.TextField(label='CNPJ',width=600,hint_text='000000000000000',max_length=15, helper="Digite sem sinalização",input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9]*$",replacement_string=""))
        self.email = ft.TextField(label='EMAIL', width=600)
        self.Botão = ft.FloatingActionButton(content="Cadastrar",icon=ft.Icons.SEND, on_click=self.Cadastrar)
        self.mensagem = ft.Text(visible=False)
        self.Data_De_Nascimento = ft.DatePicker(
        date_picker_mode = datetime.now(),
        on_change=nascimento 
    )
        self.email = None
        self.Telefone = None
        # self.controls = ft.SafeArea(content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Button(icon=ft.Icons.CALENDAR_MONTH,on_click=lambda _: page.show_dialog(self.Data_De_Nascimento),content="Pick date")])),self.Cpf_ou_Cnpj
        # self.page.overlay.append(self.Data_De_Nascimento)
        
        #ft.SafeArea(ft.FloatingActionButton(content='data', on_click= lambda _:page.show_dialog(self.Data_De_Nascimento))),self.Cpf_ou_Cnpj
        self.controls = [
            self.nome_cliente,
            self.Cpf,
            self.Cnpj,
            self.Botão,
            self.mensagem
        ]
        
    def Cadastrar(self,e):
        if not self.nome_cliente.value:
            self.nome_cliente.error = 'Campo obrigatório'
            self.page.update()
        elif not self.Cpf.value and not self.Cnpj.value:
            self.mensagem.value = '*Selecione um CNPJ ou CPF*'
            self.mensagem.color = "yellow"
            self.mensagem.visible = True
            self.page.update()
            return
        elif self.Cpf.value and not self.Cnpj.value:
            self.Cnpj.value = None
            print('entrei cnpj null')
        elif self.Cnpj.value and not self.Cpf.value:
            self.Cpf.value = None
            print("entrei cpf null")



class Cadastrar_Produto(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.marca = ft.TextField(label="Marca")
        self.modelo = ft.TextField(label="Modelo")
        self.preco_custo = ft.TextField(label="Preço de custo",on_change=self.Fomatar_decimal)
        self.preco_venda = ft.TextField(label="Preço de Venda", on_change=self.Fomatar_decimal)
        self.Botao = ft.FloatingActionButton(content="CADASTRAR PRODUTo", icon=ft.Icons.SEND,on_click=self.cadastrar_produto)
        self.mensagem = ft.Text(visible=False)

        self.controls = [
            self.marca,
            self.modelo,
            self.preco_custo,
            self.preco_venda,
            self.Botao,
            self.mensagem
        ]
    def Fomatar_decimal(self,e):
        if ',' in e.control.value:
            e.control.value = e.control.value.replace(",", ".")
            e.control.update()
            
        

    def cadastrar_produto(self,e):
        if not self.marca.value:
            self.marca.error = "*CAMPO OBRIGATÓRIO*"
            self.page.update()
            return
        else:
            self.marca.error = None
            self.page.update()
        if not self.modelo.value:
            self.modelo.error = "*CAMPO OBRIGATÓRIO*"
            self.page.update()
            return
        else:
            self.modelo.error = None
            self.page.update()

        if not self.preco_custo.value:
            self.preco_custo.error = "*CAMPO OBRIGATÓRIO*"
            self.page.update()
            return
        else:
            self.preco_custo.error = None
            self.page.update()

        if not self.preco_venda.value:
            self.preco_venda.error = "*CAMPO OBRIGATÓRIO*"
            self.page.update()
            return
        else:
            self.preco_venda.error = None
            self.page.update()
        if self.marca.value and self.modelo.value and self.preco_custo.value and self.preco_venda.value:
            situação, status = funções.cadastrar_produto(Marca=self.marca.value,Modelo=self.modelo.value,Preco_custo=self.preco_custo.value,Preco_venda=self.preco_venda.value)
            if situação:
                self.mensagem.value = status
                self.mensagem.visible =True
                self.mensagem.color = "GREEN"
                self.page.update()
            elif status == "Modelo já cadastrado":
                self.mensagem.value = status
                self.mensagem.visible =True
                self.mensagem.color = "RED"
                self.page.update()
            else:
                self.mensagem.value = 'Problema no banco de dados, Consulte o responsavel pelo sistema'
                self.mensagem.visible =True
                self.mensagem.color = "RED"
                self.page.update()

            
    

        
    

        
        
        
        
        
        






    
            











