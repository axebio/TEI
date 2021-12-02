import psycopg2
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def connect_sql():
    connection = psycopg2.connect(
        host = "ec2-34-195-69-118.compute-1.amazonaws.com",
        database = "d9qjtrq9db67vk",
        user = "iptfnyypxsvbqc",
        password = "88feda52e1640bba0021fc5500804bcb42dd96aaa043229b980981623bff910f",
        port = "5432"
    )
    return connection

def create_tables():
    connection = connect_sql()

    tb_user = '''CREATE TABLE IF NOT EXISTS tb_user
                        (id_user      SERIAL,
                        usuario     VARCHAR(20),
                        senha       VARCHAR(12),
                        CONSTRAINT pk_tb_user PRIMARY KEY(usuario)
                        );
                        '''


    tb_clientes = '''CREATE TABLE IF NOT EXISTS tb_clientes
                        (id_clientes            SERIAL,
                        nome_cliente            VARCHAR(20),
                        tel_cliente             VARCHAR(11),
                        email_cliente           VARCHAR(30),
                        end_cliente             VARCHAR(50),
                        CONSTRAINT pk_tb_clientes PRIMARY KEY(id_clientes)
                        );
                        '''

    tb_produtos = '''CREATE TABLE IF NOT EXISTS tb_produtos
                        (id_produtos                     SERIAL,
                        nome_prod                        VARCHAR(30),
                        p_compra_prod                    VARCHAR(5),
                        p_venda_prod                     VARCHAR(5),
                        quant_prod                       VARCHAR(4),
                        CONSTRAINT pk_tb_produtos PRIMARY KEY(id_produtos)
                        );
                        '''

    tb_funcionarios = '''CREATE TABLE IF NOT EXISTS tb_funcionarios
                    (id_funcionarios                    SERIAL,
                    nome_func                           VARCHAR(30),
                    cpf                                 VARCHAR(11),
                    telefone                            VARCHAR(11),
                    funcao                              VARCHAR(20),
                    CONSTRAINT pk_tb_funcionarios PRIMARY KEY(id_funcionarios)
                    );
                    '''

    cur = connection.cursor()

    tables = [tb_user, tb_clientes, tb_produtos, tb_funcionarios]

    for i in tables:
        cur.execute(i)

    connection.commit()
    connection.close()

def insert_data(table, values):
    try:    
        connection = connect_sql()
        print(1)
        cur = connection.cursor()

        sql = ""
        sql = '''INSERT INTO {} VALUES (DEFAULT, '''.format(table)
        for i in range(len(values)):
            sql += ''' '{}', '''.format(values[i])
        sql = sql[:-2]
        sql += ");"

        cur.execute(sql)
        msg = "Os dados foram registrados com sucesso."
        messagebox.showinfo("Dados inseridos.", msg)
    except:
        msg = "Erro ao registrar os dados, por favor verifique e tente novamente."
        messagebox.showinfo("Impossivel cadastrar.", msg)


    connection.commit()
    connection.close()
    
def select_data(table, columns = "*"):
    connection = connect()
    create_tables()
    #baixar valores do banco de dados
    sql = '''SELECT {} FROM {} ;'''.format(columns, table)

    df = pd.read_sql_query(sql,connection)
    connection.commit()
    connection.close()

    return df

def delete_data(table, ID):
    connection = connect_sql()
    cur = connection.cursor()
    
    id = 'id_' + table.split("_")[1]
    sql = '''DELETE FROM {} WHERE {} = '{}' '''.format(table, id, ID)
    try:
        cur.execute(cur.mogrify(sql))
        msg = "Os dados foram apagados com sucesso."
        messagebox.showinfo("Dados apagados.", msg)
    except:
        msg = "Erro ao apagar os dados, por favor verifique e tente novamente."
        messagebox.showinfo("Impossivel apagar.", msg)
    
    connection.commit()
    connection.close()

def verificar(user):
    connection = connect_sql()
    create_tables()
    #baixar valores do banco de dados
    sql = '''SELECT senha FROM tb_user WHERE usuario = '{}';'''.format(user)

    cur = connection.cursor()
    cur.execute(sql)
    senha = cur.fetchone()
    senha = senha[0]
    connection.commit()
    connection.close()
    return senha

def prepara_import(table, df):
    try:
        id = 'id_' + table.split("_")[1]
        df.drop([id], axis=1)
        df = df.set_index(df.columns[0])
        print(df)
        for i in df.itertuples(index= False, name= None):
            insert_data(table, list(i))
    except:
        msg = "Erro ao registrar os dados, por favor verifique o formato do arquivo e tente novamente."
        messagebox.showinfo("Impossivel importar.", msg)



insert_data("tb_user", ['rafael', '1234'])