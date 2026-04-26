from DATABASE.conexão_banco import conectar_banco
import flet as ft
import DATABASE.funções as funções
import ui.telas as telas
from datetime import datetime
import sys
import time
import threading




def main (page: ft.Page):
    # page.window.full_screen = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER   
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
    
    alterar_senha = None
    
    
    def login(Usuario):
      
       Usuario_Logado = Usuario

       def Timer_Para_retornar(tempo=0):
        time.sleep(tempo)
        Retornar()
        page.update()
      
       
       
       
       def Retornar(e=None):
        nonlocal Usuario_Logado
        Usuario_Logado = Usuario
        login(Usuario_Logado)
        page.update()
        
      
       page.clean()
       page.update()
       mensagem = ft.Text(f'Seja Bem vindo {Usuario.nome}')
       def menu(Botao):
          

           page.clean()
           page.update()
           match Botao:
            case 'ALTERAR SENHA' :
              
              def menu_de_alteracao_senha(senha):
                nova_senha = senha
                funções.alterar_senha(login=Usuario_Logado.login,senha_para_alterar=nova_senha)
                page.run_thread(Timer_Para_retornar, 2)
                page.update()
                


                
                return
              alterar_senha= telas.Alterar_Senha(page,callback=menu_de_alteracao_senha,Usuario=Usuario_Logado)
              page.add(alterar_senha,ft.ElevatedButton(content="Retornar ao menu",width=200, on_click=Retornar))
              page.update()
            case 'CADASTRAR NOVO COLABORADOR':
                 page.clean()
                 colaborador = telas.New_User(page)
                 page.add(colaborador,ft.FloatingActionButton(content="Retornar ao menu",width=600, on_click=Retornar))
                 page.update()
            case 'CONSULTAR CADASTRO DE COLABORADOR':
                 consulta_de_cadastro = 1
                 page.add(telas.Consulta_de_cadastro(page),ft.FloatingActionButton(content="Retornar ao menu",width=600, on_click=Retornar))
                 

            case 'INICIAR VENDA':
                 venda = telas.Tela_de_vendas(page)
                 page.add(venda)
            case 'CADASTRAR PRODUTO':
                 tela_produto = telas.Cadastrar_Produto(page)
                 page.add(tela_produto,ft.FloatingActionButton(content="Retornar ao menu",width=600, on_click=Retornar))
            case 'SAIR':
                page.clean()
                page.add(telas.Tela_de_login(page,callback=login))
                page.update()
                return


       botoes = telas.Botoes(nivel_usuario=Usuario_Logado.nivel_de_acesso,callback=menu)
       
       page.add(mensagem,botoes)
       



    
    
    page.add(telas.Tela_de_login(page,callback=login))
    page.update()



      
if __name__ == "__main__":
    ft.run(main)




    
