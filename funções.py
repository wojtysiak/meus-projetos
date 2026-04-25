import bcrypt
from conexão_banco import conexao, cursor
import mysql.connector
import flet as ft




def criptografar_senha(senha_Digitada):

    senha = f"{senha_Digitada}".encode("utf-8")
    salt = bcrypt.gensalt()
    hash_da_senha = bcrypt.hashpw(senha,salt)
    return hash_da_senha




def checar_senha (Tentativa_de_senha, login):

    comando = "SELECT * FROM colaboradores WHERE BINARY Login = %s"
    cursor.execute(comando,(login,))
    busca = cursor.fetchone()
    if busca:
        senha_digitada = f"{Tentativa_de_senha}".encode("Utf-8")
        hash_da_senha = str(busca[4]).encode("utf-8")
        if bcrypt.checkpw(senha_digitada, hash_da_senha):
            return True, busca
        else:
            return False,"senha"

    else:
        return False, 'Usuário'




def cadastrar_novo_usuario(Nome_Completo, Cpf, Login, Senha, Status_do_usuario, Funcao, Nivel_De_Acesso):

    comando = 'Insert into Colaboradores (Nome_Completo, Cpf, Login, Senha, Status_do_usuario, Funcao, Nivel_De_Acesso) values (%s,%s,%s,%s,%s,%s,%s)'
    senha_criptografada = criptografar_senha(Senha)
    try:
        cursor.execute(comando,(Nome_Completo, Cpf, Login, senha_criptografada, Status_do_usuario, Funcao, Nivel_De_Acesso))
        conexao.commit()
        return True, "Usuário Cadastrado"
    except mysql.connector.Error as err:
        if err.errno == 1062:
            return False,'Cpf ou usuário já cadastrado'
        else:
            return False, f'erro no Banco{err}' 



def alterar_senha(login,senha_para_alterar):
        
        comando = 'select * from colaboradores where Login = %s'
        try:
            cursor.execute(comando,(login,))
            retorno = cursor.fetchone()
            if retorno == None:
                return False, "Usuario não encontrado"
            else:
                comando = 'update colaboradores set senha = %s where Login = %s'
                cursor.execute(comando,(criptografar_senha(senha_para_alterar),login))
                conexao.commit()
                return True, "Senha alterada Com sucesso"
        except mysql.connector.Error as err:
                return False, f'erro no Banco{err}' 


def cadastrar_cliente(Nome,Data_De_Nascimento,Email,Telefone, Cpf=None, Cnpj=None, ):
    comando = 'insert into clientes (Nome, Cpf, Cnpj, Data_De_Nascimento, Email, Telefone) values (%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(comando,(Nome,
                                Cpf,
                                Cnpj,
                                Data_De_Nascimento,
                                Email,
                                Telefone))
        conexao.commit()
        return True, 'Usuário cadastrado'
    except mysql.connector.Error as err:
        if err.errno == 1062:
            return False, 'Cpf, Cnpj ou email já cadastrado na base de dados'
        else:
           return False,f'Erro no banco{err}'

       

def Cadastrar_serviço(Tipo_de_serviço, Custo_do_servico, Preco_do_servico):
    comando = 'insert into servicos (Tipo_de_serviço, Custo_do_servico, Preco_do_servico) values (%s,%s,%s)'  

    try:  
        cursor.execute(comando,(Tipo_de_serviço,Custo_do_servico,Preco_do_servico))
        conexao.commit() 
        return True,'Serviço cadastrado'   
    except mysql.connector.Error as err:
         if err.errno == 1265:
             return False,'Tipo incorreto'
         return False,f'erro no banco {err}'
    

def cadastrar_produto (Marca, Modelo, Preco_custo, Preco_venda):
    comando = 'insert into produto (Marca, Modelo, Preco_custo, Preco_venda) values (%s,%s,%s,%s)'
    try:
        cursor.execute(comando,(Marca, Modelo, Preco_custo, Preco_venda))
        conexao.commit()
        
        return True, 'produto cadastrado'
    except mysql.connector.Error as err:
        if err.errno == 1062:
            
            return False,"Modelo já cadastrado"
        else:
            
            return False, f'Erro no banco {err}'
    
def cadastrar_fornecedor(Razao_social, Cnpj, Nome_Fantasia, Telefone, Email):
    comando = 'insert into fornecedor (Razao_social, Cnpj, Nome_Fantasia, Telefone, Email) values (%s,%s,%s,%s,%s)'  

    try:  
        cursor.execute(comando,(Razao_social, Cnpj, Nome_Fantasia, Telefone, Email))
        conexao.commit() 
        
        return True,'Fonecedor cadastrado'   
    except mysql.connector.Error as err:
         if err.errno == 1062:
             
             return False,'Fornecedor já cadastrado'
         
         return False,f'erro no banco {err}'
    


def fazer_login():
    page = ft.Page
    login = ft.TextField(label="usuario")
    senha = ft.TextField(label="senha")
    
    page.add(ft.Row(controls=[
                    login,senha]))

def consultar_cadastro(cpf):
    comando = "Select * from colaboradores where cpf = %s"
    
    try:
        cursor.execute(comando,(cpf,))
        resultado = cursor.fetchone()
        return resultado
    except mysql.connector.errors as err:
        if err:
            return err


    
consultar_cadastro('074.883.995-01')
