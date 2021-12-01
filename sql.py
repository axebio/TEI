from pandas.io import sql
import psycopg2
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def connect():
    connection = psycopg2.connect(
        host = "ec2-3-221-24-14.compute-1.amazonaws.com",
        database = "dbcimbaajv8c3l",
        user = "cnucpvybbkkjsm",
        password = "d1a2f05ff9c28be1b7cc2321dc9bd6cfb4241ae1a1c9a903b59437f70083d7d3",
        port = "5432",
    )
    return connection

def create_tables():
    connection = connect()

    tb_user = '''CREATE TABLE IF NOT EXISTS tb_user
                        (index      SERIAL,
                        id_user     VARCHAR(20),
                        senha       VARCHAR(12),
                        CONSTRAINT pk_tb_user PRIMARY KEY(id_user)
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
                    CPF                                 VARCHAR(11),
                    dpto                                VARCHAR(5),
                    funcao                              VARCHAR(4),
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
    connection = connect()
    cur = connection.cursor()

    sql = ""
    sql = '''INSERT INTO {} VALUES (DEFAULT, '''.format(table)
    for i in range(len(values)):
        sql += ''' '{}', '''.format(values[i])
    sql = sql[:-2]
    sql += ");"
    try:
        cur.execute(sql)
        msg = "Os dados foram registrados com sucesso."
        messagebox.showinfo("Dados inseridos.", msg)
    except:
        msg = "Erro ao registrar os dados, por favor verifique e tente novamente."
        messagebox.showinfo("Impossivel cadastrar.", msg)


    connection.commit()
    connection.close()
    

	# Insert data into table

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
    connection = connect()
    cur = connection.cursor()
    
    id = 'id_' + table.split("_")[1]
    sql = '''DELETE FROM {} WHERE {} = '{}' '''.format(table, id, ID)

    cur.execute(cur.mogrify(sql))
    connection.commit()
    connection.close()

def verificar(user):
    connection = connect()
    create_tables()
    #baixar valores do banco de dados
    sql = '''SELECT senha FROM tb_user WHERE id_user = '{}';'''.format(user)

    cur = connection.cursor()
    cur.execute(sql)
    senha = cur.fetchone()
    senha = senha[0]
    connection.commit()
    connection.close()
    return senha

valor = select_data("tb_user")


def prepara_import(table, df):
    try:
        id = 'id_' + table.split("_")[1]
        df.drop([id], axis=1)
        df = df.set_index(df.columns[0])
        print(df)
        for i in df.itertuples(index= False, name= None):
            insert_data(table, list(i))
        msg = "Os dados foram registrados com sucesso."
        messagebox.showinfo("Dados inseridos.", msg)
    except:
        msg = "Erro ao registrar os dados, por favor verifique o formato do arquivo e tente novamente."
        messagebox.showinfo("Impossivel importar.", msg)




